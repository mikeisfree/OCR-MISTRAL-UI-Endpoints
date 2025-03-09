# PDF-OCR-MISTRAL API TOOL TO CRUSH YOUR ENEMIES

A Flask-based web application and API that performs OCR on PDF documents using Mistral AI's OCR service.

## Absurdly Overpovered Project Structure

```
ROOT/
  ├── templates/
  │   └── index.html
  ├── app.py
  ├── requirements.txt
  └── readme.md
```

## Features that will involve you into a state of nirvana

- Modern black & white web interface for PDF OCR processing
- REST API endpoints for JSON and Markdown output
- Support for remote PDF URLs
- Automatic retry mechanism with exponential backoff
- Comprehensive error handling and logging
- Direct result display in UI with download option

## Prerequisites which will make you feel like a real hacker

- Python 3.x
- Mistral AI API key

## Installation as enjoyable as trip to the dentist

1. Clone the repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up your Mistral AI API key as an environment variable:

```bash
# Windows PowerShell
$env:MISTRAL_API_KEY="your_api_key_here"

# Linux/macOS/hipsterXOS - Temporary (forever because 5minutes feels sometimes like an eternity)
export MISTRAL_API_KEY="your_api_key_here"

# Linux/macOS - Permanent (might last longer than Ozzy Osbourne. Future generations will name schools after you)

echo 'export MISTRAL_API_KEY="your_api_key_here"' >> ~/.bashrc
source ~/.bashrc

# For Bash'ers (add to ~/.bashrc or ~/.bash_profile or do wtatever you want tough guy - YoloForLife! ):
```

## Usage sharp as volwerine claws

### Running so fast it got Forrest Gump nickname

1. Start the Flask application:

```bash
python app_new.py
```

2. Access the web interface at: http://127.0.0.1:5000

### API Endpoints (startpoints are paid feature...call me...)

1. JASON (crazy stuff.No limits.Loves his mother):

```plaintext
GET /api/json?url=https://example.com/document.pdf
```

2. Markdown (Tango down with a twist):

```plaintext
GET /api/markdown?url=https://example.com/document.pdf
```

## How It Works (pass on this one. No human can posses force so strong)

1. Web InYourface:

   - Input PDF URL (or else I don't know what You are doing here)
   - Choose output format (JSON/Markdown) - ahhhh Democracy
   - Results displayed brightly inYourface through the interface
   - Option to download results (what more a man can ask for?)

2. API Endpoints (cherry on top):

   - Direct access to OCR functionality
   - JSON endpoint returns full OCR data
   - Markdown endpoint returns clean markdown text
   - Includes error handling and retry mechanism
   - Full DVR over intergalactic CTE and 7Ghz of mortadelas

3. OCR Processing( last one is a fake. Added for fame and woman attention ):
   - Uses Mistral AI's OCR service
   - Supports multiple page documents
   - Handles image extraction and text recognition (girls...call me...)

## Deployment (depyl...deplu...just dump it somewhere)

### Option 1: Selfhost on Mighty Raspberry Pi (Wordclass solution but not for the faint-hearted)

1. if You dont know how than watch Youtube or don't touch it at all unnless you got spare time to waste and VIP health insurance

### Option 2: PythonAnywhere.com (Free.Works everywhere and nowhere.Nice UI. Looks somwhere between Marty Mcfly and Honey I shrinked the kids)

1. Create a Python Anywhere account
2. Upload your code
3. Create a new web app:
   - Choose Flask framework
   - Point path to app.py
4. Set up WSGI + Mistral API key:

   - Example WSGI config:

   ```python
   import sys
   import os
   import logging
   ```

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(**name**)

logger.debug(f"Python path: {sys.path}")

path = '/home/username/app folder'
if path not in sys.path:
sys.path.insert(0, path)
logger.debug(f"Added {path} to Python path")

os.environ['MISTRAL_API_KEY'] = 'Your_API_Key_Here'

logger.debug(f"Contents of {path}: {os.listdir(path)}")

try:
from app import app as application
logger.debug("Successfully imported app")
except Exception as e:
logger.error(f"Failed to import app: {str(e)}")
raise``` 5. Reload your web app

### Option 2: Render (easy-peasy just don't push it...)

1. Connect your GitHub repository
2. Create new Web Service
3. Build Command
   - pip install -r requirements.txt
4. Start Command
   - python app.py
5. Set environment variables:
   - MISTRAL_API_KEY
6. Deploy

## Some Features ( World Class not seen anywhere else )

- Automatic retry on failed OCR attempts
- Exponential backoff between retries
- Detailed error logging
- User-friendly error messages in UI

**especially the last one blasts the competion out of the water**

## Limitations ( if below 21...else...put on rocket shoes search Youtube for "2 Unlimited")

- Requires valid PDF URL (blablabla)
- Processing time depends on PDF size and complexity (the more complexion the higher risk of exploexion)
- Mistral rate limits ( "2 Unlimited" is the answer again... or some bucks )

## Security Considerations ( God have mercy on us at the time of need )

- API key must be kept safely (outside of darknet and other spots with frightening names)
- Input validation for URLs so you will never f^\*k it up
- HTTPS recommended over HTTP because more letters is always better + sounds real deep, smart and secure

Future upgrades of this project are planned after Melania will return to the White House.
