# Image-to-Image editing with OpenAI

## Overview

This project demonstrates a simple workflow to edit images using OpenAI’s `images.edit` API. The notebook takes an existing image and transforms it according to a prompt. In this example, the glass is turned into a realistic cocktail with ice on a bar counter. The program handles loading your API key from a `.env` file, sending the image and prompt to the API, and saving the generated result.

It’s a hands-on demonstration of combining Python, OpenAI’s API, and image editing in a reproducible environment. 

## Usage

You can run the project in **two ways**:

**Method 1 – Gradio Web Interface**  

1. Open `Image-to-Image_GPT.py` and add your OpenAI API key in the code OR create a `.env` file in the project root (see setup file for details).
2. Run the Python script `Image-to-Image_GPT.py`: 
```
python Image-to-Image_GPT.py
```
3. A Gradio web interface will open in your browser.  
4. Upload an image, enter a prompt, and click "Generate" to see and download the edited result.

**Method 2 – Jupyter Notebook**  

1. After completing the steps in the setup file, activate your environment from root directory (C:\Users\YourUsername\Documents\Projects\LLM-Projects):
```
conda activate llms
```
2. Start Jupyter Lab:
```
jupyter lab
```
3. Open `Image-to-Image_GPT.ipynb` in Jupyter Lab. 
4. Run each cell sequentially using `Shift + Enter`.  

The final edited image will be saved as `result_image.png`.

## Notes

Do not commit your `.env` file; it is ignored by `.gitignore`.  

Ensure your images are in the project folder when using the notebook or Gradio interface.

## Resources

- [OpenAI API Docs](https://platform.openai.com/docs/)  
- [Gradio Docs](https://gradio.app/docs/)  

