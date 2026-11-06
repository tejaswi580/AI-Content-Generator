# AI Content Generator for Blogs and Social Media

A beginner-friendly Generative AI mini-project built with **Python**, **Streamlit**, and the **Google Gemini API**. It generates blog posts and social media content based on a topic, content type, tone, length, audience, and optional keywords.

## Features

- Generate blog posts, Instagram captions, LinkedIn posts, and Facebook posts.
- Choose a writing tone: Professional, Friendly, Creative, Informative, or Persuasive.
- Choose Short, Medium, or Long content.
- Add a target audience and optional keywords.
- View generated content in the web app.
- Download generated content as a `.txt` file.

## Technology used

- Python
- Streamlit
- Google Gemini API (`gemini-2.5-flash`)
- Git and GitHub

## Requirements

- Python 3.10 or later
- Internet connection
- Gemini API key

## Setup on Windows (VS Code)

### 1. Extract the ZIP

Extract the project folder to a convenient location, for example:

`D:\AI_Content_Generator`

Open this folder in VS Code.

### 2. Open the terminal

In VS Code, select **Terminal → New Terminal**.

### 3. Create a virtual environment

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt in VS Code and run:

```cmd
venv\Scripts\activate
```

### 4. Install the packages

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Get a Gemini API key

1. Open https://aistudio.google.com/app/apikey
2. Sign in with your Google account.
3. Create an API key.
4. Copy the key. Do not share it publicly.

### 6. Run the project

```powershell
streamlit run app.py
```

The app will open in your browser. Paste your Gemini API key into the **Settings** section in the left sidebar, enter a topic, choose the options, and click **Generate Content**.

## How to use

1. Enter a topic in the topic box.
2. Select a content type.
3. Select a writing tone and content length.
4. Optionally enter the target audience and keywords.
5. Enter your Gemini API key in the sidebar if it is not already configured.
6. Click **Generate Content**.
7. Read the result and download it as a text file.

## Project workflow

```text
User Input
   |
   v
Select Content Type, Tone, Length and Audience
   |
   v
Build Prompt
   |
   v
Send Prompt to Gemini API
   |
   v
Gemini Large Language Model
   |
   v
Receive Generated Text
   |
   v
Display and Download Content
```

## Project folder structure

```text
AI_Content_Generator/
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
└── assets/
```

## GitHub upload instructions

Create a new **Public** repository on GitHub named `AI-Content-Generator`.

In the VS Code terminal, from inside the project folder, run:

```powershell
git init
git add .
git commit -m "Initial commit - AI Content Generator"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/AI-Content-Generator.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. If Git asks you to sign in, complete the GitHub sign-in flow.

### Important GitHub security note

- Never add your real API key to `app.py`, `.env`, README, screenshots, or GitHub.
- `.gitignore` excludes `.env` and Streamlit secrets.
- The app asks for the API key in the sidebar, so you do not need to save it in the project.
- If a key is accidentally pushed, revoke it and create a new one.

## Suggested project description for GitHub

An AI-powered content generation web application built using Python, Streamlit, and Google Gemini API. It creates blog posts and social media content based on user-selected topics, tone, length, audience, and keywords.

## Limitations

- A working Gemini API key and internet connection are required to generate content.
- API access, quotas, and charges (if any) depend on Google's current account and service terms.
- AI output may contain mistakes. Verify important information before using or publishing it.

## Future enhancements

- Add more languages.
- Add downloadable PDF and DOCX formats.
- Save previous generations.
- Add content templates for different industries.
- Add an option to generate multiple versions.

## Academic note

This is a practical demonstration of prompt construction, API integration, and Large Language Model-based text generation. Mention only the features and tasks you actually implement and test in your internship report.
