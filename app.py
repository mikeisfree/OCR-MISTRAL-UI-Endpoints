from flask import Flask, render_template, request, jsonify, Response
from mistralai import Mistral
import os
import json
import time
import traceback
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Configuration
MAX_RETRIES = 3

def process_ocr_with_retry(url, include_image_base64=True):
    """Process OCR with retry logic for reliability"""
    retries = 0
    last_exception = None
    
    while retries < MAX_RETRIES:
        try:
            api_key = os.environ.get("MISTRAL_API_KEY")
            if not api_key:
                raise ValueError("MISTRAL_API_KEY environment variable not set")
                
            with Mistral(api_key=api_key) as client:
                logger.debug(f"Sending OCR request for URL: {url}")
                
                # Process OCR request using the correct model name
                ocr_response = client.ocr.process(
                    model="mistral-ocr-latest",  # Changed from "Focus" to "mistral-ocr-latest"
                    document={
                        "type": "document_url",
                        "document_url": url
                    },
                    include_image_base64=include_image_base64
                )
                
                logger.debug("OCR request successful")
                return ocr_response
            
        except Exception as e:
            last_exception = e
            retries += 1
            logger.error(f"OCR attempt {retries} failed: {str(e)}")
            time.sleep(2 ** retries)
    
    logger.error(f"All OCR attempts failed: {str(last_exception)}")
    raise last_exception

# Main UI route
@app.route('/')
def index():
    return render_template('index.html')

# Unified Process OCR route
@app.route('/process_ocr', methods=['POST'])
def process_ocr():
    try:
        url = request.form['url']
        output_format = request.form['format']
        
        logger.info(f"Processing OCR for URL: {url}, format: {output_format}")
        ocr_response = process_ocr_with_retry(url)
        
        if output_format == 'json':
            ocr_data = ocr_response.model_dump()
            return jsonify({
                "status": "success",
                "data": ocr_data,
                "format": "json"
            })
        else:
            # Extract markdown content
            markdown_content = ""
            for page in ocr_response.pages:
                markdown_content += page.markdown + "\n\n"
            
            return jsonify({
                "status": "success",
                "data": markdown_content,
                "format": "markdown"
            })

    except Exception as e:
        logger.error(f"Error in process_ocr: {str(e)}")
        logger.error(traceback.format_exc())
        return jsonify({"status": "error", "message": str(e)}), 500

# API endpoint for Markdown output
@app.route('/api/markdown', methods=['GET'])
def api_markdown():
    try:
        url = request.args.get('url')
        if not url:
            return jsonify({"status": "error", "message": "URL parameter is required"}), 400
            
        logger.info(f"Processing OCR for URL: {url} (Markdown API)")
        ocr_response = process_ocr_with_retry(url)
        
        # Extract markdown content
        markdown_content = ""
        for page in ocr_response.pages:
            markdown_content += page.markdown + "\n\n"
        
        # Return plain markdown with proper content type
        return Response(
            markdown_content,
            mimetype='text/markdown',
            headers={'Content-Type': 'text/markdown; charset=utf-8'}
        )
    except Exception as e:
        logger.error(f"Error in api_markdown: {str(e)}")
        logger.error(traceback.format_exc())
        return jsonify({"status": "error", "message": str(e)}), 500
# API endpoint for JSON output
@app.route('/api/json', methods=['GET'])
def api_json():
    try:
        url = request.args.get('url')
        if not url:
            return jsonify({"status": "error", "message": "URL parameter is required"}), 400
            
        logger.info(f"Processing OCR for URL: {url} (JSON API)")
        ocr_response = process_ocr_with_retry(url)
        ocr_data = ocr_response.model_dump()
        
        return jsonify({
            "status": "success",
            "data": ocr_data,
            "format": "json"
        })
    except Exception as e:
        logger.error(f"Error in api_json: {str(e)}")
        logger.error(traceback.format_exc())
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # Print all registered routes for debugging
    print("Registered routes:")
    for rule in app.url_map.iter_rules():
        print(f"{rule.endpoint}: {rule.rule}")
    
    # Run the app - configure for both local development and production
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)