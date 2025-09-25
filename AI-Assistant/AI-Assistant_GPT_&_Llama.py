import os
import ollama
import gradio as gr

from openai import OpenAI
from IPython.display import Markdown, display, update_display
from dotenv import load_dotenv

MODEL_GPT = "gpt-4o-mini"
MODEL_LLAMA = "llama3.2"

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

system_prompt = "You are a technical assistant who answers questions about LLMs and provides information about these models."



def function(question, model_choice):
    if not model_choice:
        return "Please select a model first."

    user_prompt = "Please give a detailed explanation to the following question: " + question
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    
    if model_choice == "GPT":
        stream = openai.chat.completions.create(model=MODEL_GPT, messages=messages, stream=True)
        response_text = ""
        for chunk in stream:
            response_text += chunk.choices[0].delta.content or ''
        response_text = response_text.replace("```", "").replace("markdown", "")
        return response_text
    
    elif model_choice == "Llama":
        response = ollama.chat(model=MODEL_LLAMA, messages=messages)
        return response['message']['content']
    
    else:
        return "Invalid model selected."





with gr.Blocks() as interface:
    gr.Markdown("## AI Assistant\nAsk a technical question and choose a model to get a detailed explanation.")
    
    with gr.Row():
        question_input = gr.Textbox(label="Your Question", placeholder="Type your question here...")
        model_choice = gr.Radio(
            ["GPT", "Llama"], 
            label="Select model",
            value=None
        )
    
    output_box = gr.Textbox(label="Answer", placeholder="The model's answer will appear here:")
    
    submit_btn = gr.Button("Submit")
    submit_btn.click(fn=function, inputs=[question_input, model_choice], outputs=output_box)

interface.launch()