# Image-to-Image Editing with OpenAI

This project demonstrates a simple workflow to edit images using OpenAI’s images.edit API. The notebook takes an existing image (e.g., a plain glass) and transforms it according to a prompt. In this example, the glass is turned into a realistic non-alcoholic cocktail with ice on a bar counter. The program handles loading your API key from a .env file, sending the image and prompt to the API, and saving the generated result.

It’s a hands-on demonstration of combining Python, OpenAI’s API, and image editing in a reproducible environment. 

## Setup
- Create `.env` in the project root with your OpenAI key: `OPENAI_API_KEY=your_key`    

## Usage
Run the script/notebook; output saved as `result_image.png`  