# Project report notes

Use these notes as a starting point for your own internship documentation. Update them after you run and test the project.

## Abstract
The AI Content Generator for Blogs and Social Media is a web-based application developed using Python and Streamlit. It connects to the Google Gemini API to generate text from user-provided topics and instructions. Users can select the content type, writing tone, length, target audience, and optional keywords. The generated output is displayed in the application and can be downloaded as a text file. This project demonstrates prompt engineering and the integration of a Large Language Model into a simple user-facing application.

## Problem statement
Writing suitable content for different digital platforms can take time. The wording, tone, and length often need to change depending on the platform and target audience. This project provides a simple interface that helps users generate a first draft from their requirements.

## Objectives
- Build a simple web application for AI-based text generation.
- Understand how prompts are prepared and sent to an LLM API.
- Generate content for blogs and social media platforms.
- Allow users to customize tone, length, audience, and keywords.
- Display and download the generated result.

## Modules
1. User input module
2. Content configuration module
3. Prompt construction module
4. Gemini API integration module
5. Output display and download module

## Testing checklist
- [ ] App starts successfully using `streamlit run app.py`.
- [ ] Empty topic shows a validation warning.
- [ ] Missing API key shows a clear error.
- [ ] Blog post generation works with a valid API key.
- [ ] Social media generation works with a valid API key.
- [ ] Download button saves a text file.
- [ ] Real API key is not committed to GitHub.

## Screenshots to capture
1. Main application page before generation.
2. Content options selected by the user.
3. Generated content displayed in the app.
4. Download option.
5. GitHub repository showing the uploaded source files.

Do not claim that tests passed until you have actually run them.
