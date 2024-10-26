from backend.api.utils.oauth import load_creds
import google.generativeai as genai
import os

creds = load_creds("bq")
genai.configure(credentials=creds)


def generate_problem(question_number):

    question_topics = [
        "tell me about yourself",
        "failure and improvement",
        "teamwork",
        "leadership",
        "problem solving",
        "adaptability and time management",
    ]

    model = genai.GenerativeModel("tunedModels/behavioral-interview--dbnow66ey5gn")

    prompt = (
        "Give me 1 behavioral interview question with "
        + question_topics[question_number]
        + " as the main topic."
    )
    response = model.generate_content(prompt)

    return response.text


# return score, explanation
def evaluate_user_response(user_response, ideal_response):

    model = genai.GenerativeModel("tunedModels/behavioral-interview--dbnow66ey5gn")

    prompt = (
        "Give me one number - a score out of 100 for how similar "
        + user_response
        + " is to "
        + ideal_response
    )
    response = model.generate_content(prompt)

    return response
