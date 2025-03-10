# PDF-OCR-MISTRAL API TOOL TO CRUSH YOUR ENEMIES

A Flask-based web application for OCR PDF documents.
Brought to You by: Mistral AI: OCR.

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

- Modern black & white design **-...will make you feel like watching sunset through brick wall in a dark tunnel**
- REST API endpoints for JSON and Markdown output **-...you dont want to miss out on this one!**
- Support for remote PDF URLs **-...very powerfull support**
- Automatic retry mechanism with exponential backoff **- so back off!**
- Comprehensive error handling and logging **-...whatever that means**

## Prerequisites which will make you feel like a real hacker

- Python 3.x **(but install once)**
- Mistral AI API key **(found somewhere in France)**

## Installation **-...as enjoyable as trip to the dentist**

1. Clone the repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up your Mistral AI API key as an environment variable:

```bash
# Windows PowerShell
$env:MISTRAL_API_KEY="your_api_key_here"

# Linux/macOS/hipsterXOS - Temporary (extandable to eternity while listening to a 5 minute dad joke)
export MISTRAL_API_KEY="your_api_key_here"

# Linux/macOS - Permanent (lasts longer than Ozzy Osbourne career)

echo 'export MISTRAL_API_KEY="your_api_key_here"' >> ~/.bashrc
source ~/.bashrc

# For Bash'ers (add to ~/.bashrc or ~/.bash_profile or do wtatever you want tough guy - YoloForLife! ):

4. Smash that "python app.py"
4. Allow mayor to name schools after You
```

## Usage **-...sharp as Volverine claws**

### Running **(so fast it got nickname after "Forrest Gump")**

1. Start the Flask application:

```bash
python app_new.py
```

2. Unleash the fury at: http://127.0.0.1:5000

### API Endpoints **(startpoints are paid feature...call me...)**

1. JASON **(Crazy stuff. Vorhees has No limits but Loves his mother)**:

```plaintext
GET /api/json?url=https://example.com/document.pdf
```

2. Markdown **(same as Tangodown but with a twist)**:

```plaintext
GET /api/markdown?url=https://example.com/document.pdf
```

## How It Works **Pass on this one. No human can posses force so strong**

1. Web InYourface:

   - Input PDF URLn **-...or else I don't know what You are doing here**
   - Choose output format (JSON/Markdown) **-...ahhhh Democracy**
   - Results displayed brightly inYourface through the interface
   - Option to download results **-...what more a man can ask for?**

2. API Endpoints **(cherry on top)**:

   - Direct access to OCR functionality
   - JSON endpoint returns full OCR data
   - Markdown endpoint returns clean markdown text
   - Includes error handling and retry mechanism
   - Full DVR over intergalactic CTE and 7Ghz of mortadelas

3. OCR Processing: **-... last item added for fame and to grasp womans attention**
   - Uses Mistral new OCR model **- ....Vive La France!**
   - Supports multiple page documents **-...most probably.**
   - Handles image extraction and text recognition **-...girls...call me...**

## Deployment **(depyl...deplu...just dump it somewhere)**

### Option 1: Selfhost on Mighty Raspberry Pi**(Wordclass solution but not for faint-hearted)**

1. if You dont know how - watch Youtube or don't touch it at all unnless you got spare time to waste and VIP health insurance

### Option 2: PythonAnywhere.com **(Free plan. Works everywhere and nowhere. Nice user UI - Retro style brings back to somwhere in between Marty Mcfly and "Honey I shrinked the kids")**

1. Create a PythonAnywhere account
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

### Option 2: Render **(easy-peasy and free ...just don't push it)**

1. Connect your GitHub nerdsitory
2. Create new Web Service **-...or find yourself a hobby**
3. Build Command
   - pip install -r requirements.txt
4. Start Command
   - python app.py
5. Set environment variables:
   - MISTRAL_API_KEY
6. Deploy, **Command&Conquer**

## Some Features **(World Class. Not seen anywhere else. Last one blasts the competion out of the water)**

- Automatic retry on failed OCR attempts - shame I havent had this before in my life
- Base64 image extraction from PDFs and viewing in .md preview mode
- Detailed error logging **-...you will get 1000 lines of logs from which important are: "1:error" and "1000:kill process" - rest is plain gibberish.**
- User friendly error messages in UI -**...so user friendly you will beg the script notify crash**

## Limitations **(if below 21... else ...put on rocket shoes search Youtube for "2 Unlimited")**

- Requires valid PDF URL **(blablabla)**
- Processing time depends on PDF size **-... and complexity (the more complexion the higher risk of exploexion)**
- Mistral rate limits-... **( "2 Unlimited" again... or few bucks )**

## Security Considerations-... **( God have mercy on us at the time of need )**

- API key must be kept safely **(outside of darknet and other spots with frightening names)**
- Input validation for URLs **-... so you will never f^\*k it up**
- HTTPS recommended over HTTP **-...because more letters is always better + sounds real deep, smart and secure**

Future upgrades of this project are planned once Melania will return to the White House.
