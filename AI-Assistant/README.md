# AI Assistant with GPT & Llama (open-source)

## Overview

This project is an AI Assistant that answers technical questions about large language models (LLMs).  
It supports **GPT (OpenAI)** and **Llama (Ollama)**, allowing you to explore and compare responses from different models.  

You can interact with the assistant either directly in a **Jupyter notebook** or through a **Gradio web interface**, making it easy to experiment and get detailed explanations.

It’s a hands-on demonstration of combining Python, OpenAI’s API, and Llama with an optional interactive UI using Gradio.  

## Setup Instructions 

You can run the project in **two ways**: 

**1 – Running the Notebook** - make sure to activate your virtual environment from root directory (if applicable), install dependencies, open `AI-Assistant_GPT_&_Llama.ipynb` file and run each cell sequentially using `Shift + Enter` in **Jupyter Lab** or **VS Code** (please check setup file from root directory). 

You can test GPT and Llama responses directly in the notebook.

**2 – Gradio Web Interface** - make sure to activate your virtual environment from root directory (if applicable), install dependencies and run the Python script `AI-Assistant_GPT_&_Llama.py`. 

A Gradio web interface will open in your browser. Type a technical question, select a model (GPT or LLaMA), and click **Submit** to get a detailed answer.

## Notes

Don't forget to add your OpenAI API key in the code OR create a `.env` file in the project root (see setup file for details). 

Do not commit your `.env` file; it is ignored by `.gitignore`.  

FOR OLLAMA: ensure Ollama is installed and the model (llama3.2) is pulled:

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
- [Ollama Docs](https://ollama.com/docs/)  
- [Gradio Docs](https://gradio.app/docs/)
