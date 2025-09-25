# Image-to-Image editing with OpenAI

## Overview

This project demonstrates a simple workflow for editing images using OpenAI’s `images.edit` API. The notebook takes an existing image and transforms it according to a prompt. In this example, a glass is turned into a realistic cocktail with ice on a bar counter. The program handles loading your API key from a `.env` file, sending the image and prompt to the API, and saving the generated result.

It’s a hands-on demonstration of combining Python, OpenAI’s API, and image editing in a reproducible environment. 

## Setup Instructions 

You can run the project in **two ways**: 

**1 – Running the Notebook** - make sure to activate your virtual environment from root directory (if applicable), install dependencies, open `Image-to-Image_GPT.ipynb` file and run each cell sequentially using `Shift + Enter` in **Jupyter Lab** or **VS Code** (please check setup file from root directory). 

The final edited image will be saved as `result_image.png`.

**2 – Gradio Web Interface** - make sure to activate your virtual environment from root directory (if applicable), install dependencies and run the Python script `Image-to-Image_GPT.py`. 

A Gradio web interface will open in your browser. Upload an image, enter a prompt, and click "Generate" to see and download the edited result.

## Notes

Don't forget to add your OpenAI API key in the code OR create a `.env` file in the project root (see setup file for details). 

Do not commit your `.env` file; it is ignored by `.gitignore`.  

Ensure your images are in the project folder when using the notebook or Gradio interface.

## Resources

- [OpenAI API Docs](https://platform.openai.com/docs/)  
- [Gradio Docs](https://gradio.app/docs/)  

