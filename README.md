# Text-Translator-app
A simple and interactive **Language Translator Web Application** built using Python and Streamlit.  
The application translates text from one language to another in real-time using a reliable translation API.


## Live Demo
https://text-translator-app-6ftemuak8w4fqfpkmy4ymx.streamlit.app/

# Features

-  Translate text into multiple languages  
-  Real-time translation  
-  Simple and user-friendly interface  
-  Supports a wide range of languages
-  Dropdown-based language selection  

# Tech Stack

- Python  
- Streamlit  
- deep-translator 

# Project Structure

language-translator/  
│  
├── Translator.py  
├── requirements.txt  
├── README.md  

## Installation & Setup

# 1. Open Project Folder
Open the folder in terminal or VS Code

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install streamlit googletrans==4.0.0-rc1

# 4.Run the Application
streamlit run Translator.py

Open your browser at:
http://localhost:8501

## How It Works
1.Enter text to translate
2.Select target language from dropdown
3.Click "Translate"
4.Output is displayed instantly

# Example
Input: Hello
Output (Hindi): नमस्ते

# Future Improvements
-Voice input support
-Text-to-speech output
-Improved UI
-Translation history


