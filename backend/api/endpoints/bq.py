from oauth import load_creds

import google.generativeai as genai
import os

creds = load_creds()

genai.configure(credentials=creds)

def generate_problem(question_number):

    question_topics = ["", "tell me about yourself", "failure and improvement", "teamwork", "leadership", "problem solving", "adaptability and time management"]

    model = genai.GenerativeModel("tunedModels/behavioral-interview--dbnow66ey5gn")
    response = model.generate_content("Give me 1 behavioral interview question with ", question_topics[question_number], " as the main topic.")

    return response
