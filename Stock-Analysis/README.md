# AI Assistant with GPT (Stock Analysis)

## Overview

This project is a stock analysis assistant that fetches financial data from Finviz and generates professional summaries using OpenAI's GPT-4o-mini model.
 
It provides:
- analysis of stock financials in a clear and professional format.
- bulleted advantages and disadvantages for each stock.
- buy, sell, or hold recommendations.

## Setup Instructions 

You can run the project in **two ways**: 

**1 – Running the Notebook** - make sure to activate your virtual environment from root directory (if applicable), install dependencies, open `Stock-Analysis_GPT.ipynb` file and run each cell sequentially using `Shift + Enter` in **Jupyter Lab** or **VS Code** (please check setup file from root directory). 

You can test GPT directly in the notebook. You will receive a professional analysis summary with advantages, disadvantages, and recommendations.

**2 – Gradio Web Interface** - make sure to activate your virtual environment from root directory (if applicable), install dependencies and run the Python script `Stock-Analysis_GPT.py`. 

A Gradio web interface will open in your browser. Enter a stock symbol (e.g., AAPL, TSLA), and click **Submit** to get a detailed answer.

## Notes

Don't forget to add your OpenAI API key in the code OR create a `.env` file in the project root (see setup file for details). 

Do not commit your `.env` file; it is ignored by `.gitignore`.  

The tool scrapes Finviz, so ensure your network allows access.

## Resources

- [OpenAI API Docs](https://platform.openai.com/docs/)
- [Gradio Docs](https://gradio.app/docs/)
- [Finviz](https://finviz.com/)
- [BeautifulSoup Docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)