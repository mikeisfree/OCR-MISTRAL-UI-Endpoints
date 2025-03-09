# PDF OCR API

A Flask-based web application and API that performs OCR on PDF documents using Mistral AI's OCR service.

## Project Structure

```
ROOT/
  ├── templates/
  │   └── index.html
  ├── app.py
  ├── requirements.txt
  └── readme.md
```

## Features

- Modern black & white web interface for PDF OCR processing
- REST API endpoints for JSON and Markdown output
- Support for remote PDF URLs
- Automatic retry mechanism with exponential backoff
- Comprehensive error handling and logging
- Direct result display in UI with download option

## Prerequisites

- Python 3.x
- Mistral AI API key

## Installation

1. Clone the repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up your Mistral AI API key as an environment variable:

```bash
# Windows Command Prompt
set MISTRAL_API_KEY=your_api_key_here

# Windows PowerShell
$env:MISTRAL_API_KEY="your_api_key_here"

# Linux/macOS - Temporary (current terminal session)
export MISTRAL_API_KEY="your_api_key_here"

# Linux/macOS - Permanent (add to shell configuration)
# For Bash users (add to ~/.bashrc or ~/.bash_profile):
echo 'export MISTRAL_API_KEY="your_api_key_here"' >> ~/.bashrc
source ~/.bashrc
```

## Usage

### Running Locally

1. Start the Flask application:

```bash
python app_new.py
```

2. Access the web interface at: http://127.0.0.1:5000

### API Endpoints

1. JSON Output:

```plaintext
GET /api/json?url=https://example.com/document.pdf
```

2. Markdown Output:

```plaintext
GET /api/markdown?url=https://example.com/document.pdf
```

## How It Works

1. Web Interface:

   - Input PDF URL
   - Choose output format (JSON/Markdown)
   - Results displayed directly in the interface
   - Option to download results

2. API Endpoints:

   - Direct access to OCR functionality
   - JSON endpoint returns full OCR data
   - Markdown endpoint returns clean markdown text
   - Includes error handling and retry mechanism

3. OCR Processing:
   - Uses Mistral AI's OCR service
   - Supports multiple page documents
   - Handles image extraction and text recognition

## Deployment

### Option 1: Python Anywhere

1. Create a Python Anywhere account
2. Upload your code
3. Create a new web app:
   - Choose Flask framework
   - Set working directory to your app folder
   - Point to app_new.py
4. Set up your environment variable:
   - Add MISTRAL_API_KEY to your .env file
5. Configure your virtual environment
6. Reload your web app

### Option 2: Render

1. Connect your GitHub repository
2. Create new Web Service
3. Set environment variables:
   - MISTRAL_API_KEY
4. Deploy

## Error Handling

- Automatic retry on failed OCR attempts
- Exponential backoff between retries
- Detailed error logging
- User-friendly error messages in UI

## Limitations

- Requires valid PDF URL
- Processing time depends on PDF size and complexity
- Rate limits based on Mistral AI API plan

## Security Considerations

- API key must be kept secure
- Debug mode disabled in production
- Input validation for URLs
- HTTPS recommended for production deployment
