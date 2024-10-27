import google.generativeai as genai
import time
import os
from backend.api.endpoints.behavioral_bq import evaluate_user_response
import dotenv

dotenv.load_dotenv()
genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")


def get_behavioral_score(path: str, question: str):
    video_file = genai.upload_file(path)

    while video_file.state.name == "PROCESSING":
        time.sleep(2.5)
        video_file = genai.get_file(video_file.name)

    transcript = generate_transcript(video_file)

    behavioral_score = evaluate_user_response(transcript, question)
    visual_score = generate_visual_score(video_file)

    return behavioral_score, visual_score


def generate_transcript(video_file):
    prompt = (
        "You are a Recruiter for Software Engineering at a Top Company. You are analyzing a response from an prospective interviewer. "
        + "You must transcribe a full transcript of the users response in the inputted video file."
    )

    return model.generate_content([video_file, prompt])


def generate_visual_score(video_file):
    prompt = (
        "You are a Recruiter for Software Engineering at a Top Company. You are analyzing a response from an prospective interviewer. You must analyze their voiceand speech patterns. "
        + "You must give them a score out of 25 eachfor Clear and Concise Communication, Professionalism in Speaking, Engaging & Enthusiastic, Confidence in Knowledge. This should total to a number out of 100."
        + "Also ensure to account for Negative Cues in AUDIO response to interview questions (voice/speech patterns): Subtract 0-20 Points - Hesitation, Subtract 0-20 Points - Nervousness,Subtract 0-20 Points - Uncertainty"
        + "Note, negative cue minuses range from 0-20 points, with 0 being perfect question response and 20 being absolutely worst. In your response, output the final score that they get for their repsonse after adding up all of the positive cues and subtracting the negative ones."
    )

    return model.generate_content([video_file, prompt])
