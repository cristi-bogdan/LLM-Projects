import os
import requests
import gradio as gr

from dotenv import load_dotenv
from bs4 import BeautifulSoup
from IPython.display import Markdown, display
from openai import OpenAI


load_dotenv(override=True)
openai_api_key = os.getenv("OPENAI_API_KEY")


#-------------------------Method 1 (Useful for quick testing, not recommended for production):---------------------------------------------------

#openai_api_key = "YOUR_OPENAI_API_KEY"

#-------------------------Method 2 - RECOMMENDED (Load API key from .env file, keeps your keys private and safe):--------------------------------
load_dotenv(override=True)
openai_api_key = os.getenv("OPENAI_API_KEY")

if openai_api_key:
    print(f"OpenAI API Key (GPT) exists and begin with {openai_api_key[:7]}")
else:
    print("OpenAI API Key not found. Please add your key in the .env file in the root directory.")


openai = OpenAI()



class FinvizWebsite(): 
    def __init__(self, ticker):
        self.ticker = ticker.upper()
        self.url = f"https://finviz.com/quote.ashx?t={self.ticker}&p=d&ty=ea"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}
        response = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(response.content, "html.parser")
        self.title = soup.title.string if soup.title else "No title found"
        self.table = soup.find("table", class_="snapshot-table2")


def messages_for(website):
    system_prompt = """
    You are a financial analysis assistant that analyzes the contents of HTML formatted table and provides a summary of the stock's analysis with clear and 
    professional language appropriate for financial research, including bulleted **advantages** and **disadvantages**, and a recommendation to buy, sell, or hold. 
    Ignore navigation-related text. Respond in markdown.
    """
    user_prompt = f"""
    You are looking at a website titled {website.title}.
    The contents of this website are as follows; please provide a summary of the stock's analysis from this website in markdown.
    
    {website.table}
    """
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]


def display_summary(ticker):
    website = FinvizWebsite(ticker)
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages_for(website)
    )
    summary = response.choices[0].message.content
    return summary

interface = gr.Interface(
    fn=display_summary,
    inputs=gr.Textbox(label="Symbol", placeholder="Enter stock symbol:"),
    outputs=gr.Markdown(label="Stock Analysis Summary"),
    title="Stock Analysis-GPT",
    description="Enter a stock symbol to get a professional summary of its financials."
)

interface.launch()
