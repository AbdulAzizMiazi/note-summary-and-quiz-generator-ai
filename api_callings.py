from google import genai
from PIL import Image
from dotenv import load_dotenv
from gtts import gTTS
import os
import io

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def generate_summary(images):

    piled_img = []
    for img in images:
        piled_img.append(Image.open(img))

    prompt = "Summarize these note images using appropriate Markdown syntax."

    # model="gemini-3.8-flash" # lates version of Gemini (but gets busy too quickly)
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents= [prompt, piled_img]
    )
    return response.text

def audio_transcription(text):
    audio = gTTS(text, lang="en", slow=False)
    buffer_space = io.BytesIO()
    audio.write_to_fp(buffer_space)
    return buffer_space

def generate_quiz(images, difficulty):
    piled_imgs = []
    for img in images:
        piled_imgs.append(Image.open(img))

    prompt = f"Please generate three quizzes from the images and the difficulty level should be {difficulty}. Reply with all the necessary markdown sytex."

    quiz_response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents= [piled_imgs, prompt]
    )
    return quiz_response.text