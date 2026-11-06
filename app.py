import os
import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(
    page_title="AI Content Generator",
    page_icon="✍️",
    layout="centered"
)

st.title("✍️ AI Content Generator")
st.caption("Create blog posts and social media content using Generative AI.")

# Read API key from Streamlit secrets or environment variable.
saved_api_key = ""
try:
    saved_api_key = st.secrets.get("GEMINI_API_KEY", "")
except Exception:
    saved_api_key = ""
saved_api_key = saved_api_key or os.getenv("GEMINI_API_KEY", "")

with st.sidebar:
    st.header("Settings")
    api_key = st.text_input(
        "Gemini API key",
        value=saved_api_key,
        type="password",
        help="Get a key from https://aistudio.google.com/app/apikey"
    )
    st.caption("Your API key is used for the current session. Do not share it or upload it to GitHub.")
    st.divider()
    st.markdown("**Project:** AI Content Generator")
    st.markdown("**Built with:** Python · Streamlit · Gemini")

st.subheader("Create your content")

topic = st.text_area(
    "What should the content be about?",
    placeholder="Example: Benefits of learning artificial intelligence",
    height=100
)

col1, col2 = st.columns(2)
with col1:
    content_type = st.selectbox(
        "Content type",
        ["Blog post", "Instagram caption", "LinkedIn post", "Facebook post"]
    )
    tone = st.selectbox(
        "Writing tone",
        ["Professional", "Friendly", "Creative", "Informative", "Persuasive"]
    )
with col2:
    length = st.selectbox("Content length", ["Short", "Medium", "Long"])
    audience = st.text_input("Target audience", placeholder="Example: College students")

keywords = st.text_input(
    "Keywords (optional)",
    placeholder="Example: AI, learning, technology"
)

if st.button("✨ Generate Content", type="primary", use_container_width=True):
    if not topic.strip():
        st.warning("Please enter a topic first.")
    elif not api_key.strip():
        st.error("Please enter your Gemini API key in the Settings section.")
    else:
        prompt = f"""
You are a helpful professional content writer.
Create a {content_type.lower()} about: {topic.strip()}.

Requirements:
- Tone: {tone}
- Length: {length}
- Target audience: {audience.strip() if audience.strip() else "General audience"}
- Keywords to naturally include: {keywords.strip() if keywords.strip() else "No specific keywords"}
- Use clear, natural language.
- Make the content original, useful, and well structured.
- Do not invent statistics, facts, or references.
- For social media content, include suitable hashtags where appropriate.
- Return only the finished content, with a suitable title if relevant.
"""
        try:
            with st.spinner("Generating content with Gemini..."):
                client = genai.Client(api_key=api_key.strip())
                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        temperature=0.7,
                        max_output_tokens=1800
                    )
                )
                generated_text = response.text
                if not generated_text:
                    st.error("The model returned an empty response. Please try again.")
                else:
                    st.session_state["generated_content"] = generated_text
                    st.success("Content generated successfully!")
        except Exception as exc:
            st.error("Content generation failed. Check your API key and internet connection, then try again.")
            with st.expander("Technical error details"):
                st.code(str(exc))

if st.session_state.get("generated_content"):
    st.divider()
    st.subheader("Generated Content")
    st.text_area(
        "Your generated content",
        value=st.session_state["generated_content"],
        height=350
    )
    st.download_button(
        "⬇️ Download content as TXT",
        data=st.session_state["generated_content"],
        file_name="generated_content.txt",
        mime="text/plain",
        use_container_width=True
    )
    st.caption("Review AI-generated content for accuracy and originality before publishing.")

st.divider()
st.caption("Academic mini-project demonstration. Requires a Gemini API key and an internet connection.")
