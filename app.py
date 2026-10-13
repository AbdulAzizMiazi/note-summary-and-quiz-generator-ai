import streamlit as st
from api_callings import generate_summary, audio_transcription, generate_quiz

with st.sidebar:
    st.header("Controls")
    images = st.file_uploader("Upload the photos of your notes",
                    type=["jpg", "jpeg", "png"],
                    accept_multiple_files=True)
   
    if images:
            cols = st.columns(len(images))
            for i, img in enumerate(images):
                with cols[i]:
                    st.image(img)

    difficulty = st.selectbox("Enter the difficulty of Quiz",
                ("Easy", "Medium", "Hard"),
                index=None)

    is_clicked = st.button("Click the button to initiate AI", type="primary")



# Main display is here
st.title("Note Summary and Quiz Generator", anchor=False)
st.markdown("Upload upto 3 images to generate note summary and quizzes")

# Genaration part
if is_clicked:
    num_img = len(images)
    is_conditions_matched = True

    if num_img < 1:
        st.error("Upload atleast 1 image")
        is_conditions_matched = False
    elif num_img > 3:
         st.error("Upload maximum 3 images")
         is_conditions_matched = False

    if difficulty is None:
        st.error("Select a difficulty")
        is_conditions_matched = False


    if is_conditions_matched: ## When all the condisions are met
        # Summary
            with st.container(border=True):
                st.subheader("Your note", anchor=False)
                with st.spinner("AI is writing the note for you...."):
                    summary = generate_summary(images)
                    st.markdown(summary)
                
            
        # Audio
            with st.container(border=True):
                st.subheader("Audio Transcription", anchor=False)
                with st.spinner("Loading your audio transcription..."):
                    summary = summary.translate(str.maketrans("", "", "#*`-_")) # removes markdowns syntex
                    audio_transcript = audio_transcription(summary)
                    st.audio(audio_transcript)
            
        # Quiz
            with st.container(border=True):
                st.subheader(f"Quiz: {difficulty} Level", anchor=False)
                with st.spinner("AI is preparing your quizzes..."):
                    quizzes = generate_quiz(images, difficulty)
                    st.markdown(quizzes)