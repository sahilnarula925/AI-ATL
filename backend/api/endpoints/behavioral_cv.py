import google.generativeai as genai
import time
from backend.api.utils.oauth import load_creds


creds = load_creds("cv")
genai.configure(credentials=creds)
model = genai.GenerativeModel('tunedModels/avbehavorialapi-rh48ho8em5cf')


def process_video(path: str, questions: str):
    video = genai.upload_file(path=path)

    while video_file.state.name == "PROCESSING":
        print('.', end='')
        time.sleep(10)
        video_file = genai.get_file(video_file.name)


    response = model.generate_content("Positive Cues in AUDIO response to interview questions voice/speech patterns: 25/25 - Clear and Concise Communication25/25 - Professionalism in Speaking20/25 - Engaging & Enthusiastic25/25 - Confidence in KnowledgeNegative Cues in AUDIO response to interview questions (voice/speech patterns):Minus 5 Points - HesitationMinus 0 Points - NervousnessMinus 0 Points - Uncertainty")
    print(response.text)

