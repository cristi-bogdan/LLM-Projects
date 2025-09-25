# Website Summarizer (OpenAI & Ollama)

## Overview

This project demonstrates two simple workflows to summarize the contents of any website:
- using OpenAI GPT via the chat.completions API (requires an API key)
- using Ollama to run models locally (e.g., llama3.2) without requiring an internet connection to OpenAI.

It’s a hands-on demonstration of combining Python, LLMs (GPT or Ollama), web scraping, and Gradio to create a reproducible environment.

## Setup Instructions 

You can run the project in **two ways**: 

**1 – Running the Notebook** - make sure to activate your virtual environment from root directory (if applicable), install dependencies, open `Website-Summarizer_GPT.ipynb` or `Website-Summarizer_LLAMA(open-source).ipynb` file and run each cell sequentially using `Shift + Enter` in **Jupyter Lab** or **VS Code** (please check setup file from root directory).

The final summary will be displayed in the notebook as Markdown.

**2 – Gradio Web Interface** - make sure to activate your virtual environment from root directory (if applicable), install dependencies and run the Python script `Website-Summarizer_GPT.py` or `Website-Summarizer_LLAMA(open-source).py`.

A Gradio web interface will open in your browser. Enter a URL, and click 'Submit' to get the summary.

## Notes

For GPT version: Don't forget to add your OpenAI API key in the code OR create a `.env` file in the project root (see setup file for details). 

Do not commit your `.env` file; it is ignored by `.gitignore`.  

FOR OLLAMA VERSION: ensure Ollama is installed and the model (llama3.2) is pulled:

1. Install Ollama on your system from `https://ollama.com/` 
2. Download a model:
```
ollama pull llama3.2
```
3. Install Python dependencies:
```
pip install gradio requests beautifulsoup4 ollama
```

## Resources

- [OpenAI API Docs](https://platform.openai.com/docs/) 
- [Ollama Docs](https://www.llama.com/docs/overview/) 
- [Gradio Docs](https://gradio.app/docs/)  
- [BeautifulSoup Docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)