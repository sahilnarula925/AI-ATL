import google.generativeai as genai
import time
from backend.api.utils.oauth import load_creds
from backend.api.endpoints.behavorial_bq import evaluate_user_response

creds = load_creds("cv")
genai.configure(credentials=creds)
model = genai.GenerativeModel("tunedModels/avbehavorialapi-rh48ho8em5cf")


def process_video(path: str, question: str):
    video_file = genai.upload_file(path)

    while video_file.state.name == "PROCESSING":
        time.sleep(2.5)
        video_file = genai.get_file(video_file.name)

    prompt = "Positive Cues in AUDIO response to interview questions voice/speech patterns: 25/25 - Clear and Concise Communication25/25 - Professionalism in Speaking20/25 - Engaging & Enthusiastic25/25 - Confidence in KnowledgeNegative Cues in AUDIO response to interview questions (voice/speech patterns):Minus 5 Points - HesitationMinus 0 Points - NervousnessMinus 0 Points - Uncertainty"

    # response should contain evaluation of user video (scale 0 to 100) and speech to text
    response = model.generate_content(
        [video_file, prompt], request_options={"timeout": 600}
    )

    transcript = response["transcript"]  # do this

    score, explanation = evaluate_user_response(transcript, question)

    return score, explanation
