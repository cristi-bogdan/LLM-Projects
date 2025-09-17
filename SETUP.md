## SETUP INSTRUCTIONS
 
### Part 1: Clone the Repo

This gets you a local copy of the code on your box.

1. **Install Git** (if not already installed):

- Download Git from https://git-scm.com/download/win
- Run the installer and follow the prompts, using default options
- After the installation, you may need to open a new Powershell window to use it (or you might even need to restart)

2. **Open Command Prompt:**

- Press Win + R, type `cmd`, and press Enter

3. **Navigate to your projects folder:**

If you have a specific folder for projects, navigate to it using the cd command. For example:  
`cd C:\Users\YourUsername\Documents\Projects`  
Replacing YourUsername with your actual Windows user

If you don't have a projects folder, you can create one:
```
mkdir C:\Users\YourUsername\Documents\Projects
cd C:\Users\YourUsername\Documents\Projects
```

4. **Clone the repository:**

Enter this in the command prompt in the Projects folder:

`git clone https://github.com/cristi-bogdan/LLM-Projects.git`

This creates a new directory `LLM-Projects` within your Projects folder and downloads the code for the class. Do `cd LLM-Projects` to go into it. This `LLM-Projects` directory is known as the "project root directory".

### Part 2: Install Anaconda environment

1. **Install Anaconda:**

- Download Anaconda from https://docs.anaconda.com/anaconda/install/windows/
- Run the installer and follow the prompts. Note that it takes up several GB and take a while to install, but it will be a powerful platform for you to use in the future.

2. **Set up the environment:**

- Open **Anaconda Prompt** (search for it in the Start menu)
- Navigate to the "project root directory" by entering something like `cd C:\Users\YourUsername\Documents\Projects\LLM-Projects` using the actual path to your LLM-Projects project root directory. Do a `dir` and check you can see subdirectories.
- Create the environment: `conda env create -f environment.yml`
- Wait for a few minutes for all packages to be installed - in some cases, this can literally take 30 minutes if you've not used Anaconda before, and even longer depending on your internet connection. 
- You have now built an isolated, dedicated AI environment for engineering LLMs, running vector datastores, and so much more. You now need to **activate** it using this command: `conda activate llms`  

You should see `(llms)` in your prompt, which indicates you've activated your new environment.

3. **Start Jupyter Lab:**

- In the Anaconda Prompt, from within the `LLM-Projects` folder, type: `jupyter lab` and Jupyter Lab should open up in a browser. 

### Part 3 - OpenAI key (OPTIONAL but recommended)

1. Create an OpenAI account if you don't have one by visiting:  
https://platform.openai.com/

2. OpenAI asks for a minimum credit to use the API (around $5). But if you'd prefer not to pay for the API, I give you an alternative using Ollama.

You can add your credit balance to OpenAI at Settings > Billing:  
https://platform.openai.com/settings/organization/billing/overview

I recommend you disable the automatic recharge!

3. Create your API key

The webpage where you set up your OpenAI key is at https://platform.openai.com/api-keys - press the green 'Create new secret key' button and press 'Create secret key'. Keep a record of the API key somewhere private; you won't be able to retrieve it from the OpenAI screens in the future. It should start `sk-proj-`.

Set up keys for Anthropic, Google and HuggingFace:  
- Claude API at https://console.anthropic.com/ from Anthropic
- Gemini API at https://ai.google.dev/gemini-api from Google
- Deepseek API at https://platform.deepseek.com/
- HuggingFace API at https://huggingface.com

### PART 4 - .env file

1. Open the Notepad (Windows + R to open the Run box, enter `notepad`)

2. In the Notepad, type this, replacing xxxx with your API key (starting `sk-proj-`).

```
OPENAI_API_KEY=xxxx
```

If you have other keys, you can add them too: 

```
GOOGLE_API_KEY=xxxx
ANTHROPIC_API_KEY=xxxx
DEEPSEEK_API_KEY=xxxx
HF_TOKEN=xxxx
```

Double check there are no spaces before or after the `=` sign, and no spaces at the end of the key.

3. Go to File > Save As. In the "Save as type" dropdown, select All Files. In the "File name" field, type exactly **.env** as the filename. Choose to save this in the project root directory (the folder called `LLM-Projects`) and click Save.

4. Navigate to the folder where you saved the file in Explorer and ensure it was saved as ".env" not ".env.txt" - if necessary rename it to ".env" -  you might need to ensure that "Show file extensions" is set to "On" so that you see the file extensions.

This file won't appear in Jupyter Lab because jupyter hides files starting with a dot. This file is listed in the `.gitignore` file, so it won't get checked in and your keys stay safe.

### Part 5 - Start

- Open **Anaconda Prompt** (search for it in the Start menu)
  
- Navigate to the "project root directory" by entering something like `cd C:\Users\YourUsername\Documents\Projects\LLM-Projects` using the actual path to your LLM-Projects project root directory. Do a `dir` and check you can see subdirectories for each week of the course.

- Activate your environment with `conda activate llms` 

- You should see (llms) in your prompt which is your sign that all is well. And now, type: `jupyter lab` and Jupyter Lab should open up, ready for you to get started. 

For those new to Jupyter Lab / Jupyter Notebook, it's a Data Science environment where you can simply hit shift+return in any cell to run it.



