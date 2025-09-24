# Website Summarizer with OpenAI

## Overview

This project demonstrates a simple workflow to summarize the contents of any website using OpenAI’s chat.completions API. The script fetches a webpage, cleans it with BeautifulSoup, and then asks GPT to generate a concise summary in Markdown format.

It’s a hands-on demonstration of combining Python, OpenAI’s API, web scraping, and Gradio to create a reproducible environment.

## Usage

You can run the project in **two ways**:

**Method 1 – Gradio Web Interface**  

1. Open `Website_Summarizer.py` and add your OpenAI API key in the code OR create a `.env` file in the project root (see setup file for details).
2. Run the Python script `Website_Summarizer.py`: 
```
python Website_Summarizer.py
```
3. A Gradio web interface will open in your browser.  
4. Enter a website URL in the input box and click Submit to get the summary.

**Method 2 – Jupyter Notebook**  

1. After completing the steps in the setup file, activate your environment from root directory (C:\Users\YourUsername\Documents\Projects\LLM-Projects):
```
conda activate llms
```
2. Start Jupyter Lab:
```
jupyter lab
```
3. Open `Website_Summarizer.ipynb` in Jupyter Lab. 
4. Run each cell sequentially using `Shift + Enter`.  

The final summary will be displayed in the notebook as Markdown.

## Notes

Do not commit your `.env` file; it is ignored by `.gitignore`.  

## Resources

- [OpenAI API Docs](https://platform.openai.com/docs/)  
- [Gradio Docs](https://gradio.app/docs/)  
- [BeautifulSoup Docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
