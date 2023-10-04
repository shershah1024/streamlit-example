import streamlit as st

# Title of the page
st.title("YouTube and Quizizz Embed Page")

# YouTube Embed
st.header("Embed a YouTube Video")
video_id = st.text_input("Enter the YouTube video ID (e.g., dQw4w9WgXcQ):")
if video_id:
    video_url = f"https://www.youtube.com/embed/{video_id}"
    st.markdown(f'<iframe width="560" height="315" src="{video_url}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

# Quizizz Embed
st.header("Embed a Quiz from Quizizz")
quiz_id = st.text_input("Enter the Quizizz quiz ID:")
if quiz_id:
    quiz_url = f"https://quizizz.com/join/quiz/{quiz_id}/start"
    st.markdown(f'<iframe src="{quiz_url}" width="100%" height="600px" frameborder="0"></iframe>', unsafe_allow_html=True)

st.sidebar.text("Made with Streamlit")
