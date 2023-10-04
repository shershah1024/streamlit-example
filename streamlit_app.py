import streamlit as st

# Title of the page
st.title("Quiz")

# Hardcoded YouTube and Quizizz embeds
video_id = "6v0Q-2IhqrE&t"
quiz_id = "651d53d3981f921f5ce77a40"

# YouTube Embed
video_url = f"https://www.youtube.com/embed/{video_id}"
st.markdown(f'<iframe width="100%" height="315" src="{video_url}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

# Spacer
st.write(" ")

# Quizizz Embed
quiz_url = f"https://quizizz.com/join/quiz/{quiz_id}/start"
st.markdown(f'<iframe src="{quiz_url}" width="100%" height="600px" frameborder="0"></iframe>', unsafe_allow_html=True)


