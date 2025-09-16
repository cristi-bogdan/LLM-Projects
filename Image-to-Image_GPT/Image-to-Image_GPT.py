import os
import base64
import gradio as gr 

from dotenv import load_dotenv
from io import BytesIO
from PIL import Image
#from IPython.display import display
from openai import OpenAI

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

#------------------------------------------------------------------------------------------------------------------------------------------------

def edit_image(input_image, prompt):
    buffered = BytesIO()
    input_image.save(buffered, format="PNG")
    img_bytes = buffered.getvalue()

    result = openai.images.edit(
        model = "gpt-image-1",
        prompt = prompt,
        image = [("input.png", img_bytes)],
        size = "1024x1024"
    )

    image_base64 = result.data[0].b64_json
    image_data = base64.b64decode(image_base64)
    output_img = Image.open(BytesIO(image_data))

    return output_img


#------------------------------------------------------------------------------------------------------------------------------------------------

with gr.Blocks() as interface:
    gr.Markdown("Image-to-Image")
    with gr.Row():
        with gr.Column():
            input_img = gr.Image(type="pil", label="Upload an image")
            prompt = gr.Textbox(
                lines = 10,
                label = "Prompt",
                value = """ """
            )
            btn = gr.Button("Generate")
        with gr.Column():
            output_img = gr.Image(type="pil", label="Edited image")

    btn.click(fn = edit_image, inputs = [input_img, prompt], outputs = output_img)
            

if __name__ == "__main__":
    interface.launch()
