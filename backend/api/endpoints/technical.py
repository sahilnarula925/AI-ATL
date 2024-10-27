import google.generativeai as genai
import json
from backend.api.utils.oauth import load_creds
import time

"""
dict = {question = str, solution = str, complexity = {time = str space = str test_cases = [{input = obj, output = obj}], code_explanation = str}
"""


def generate_problem(difficulty):
    # difficuly - pre-internship(easy, easy), internship(med / medium, medium / medium, hard)

    creds = load_creds()
    genai.configure(credentials=creds)
    model = genai.GenerativeModel("tunedModels/aiatltechnical-g1tdmwqkmops")

    prompt = (
        "Generate only one software engineering LeetCode style question. The difficulty for this singular problem should be "
        + difficulty
        + ". Generate 10 test cases for this singular problem. Generate 3 hints for this singular problem. Respond with a JSON compliant object for this singular problem"
        + " in format {question=..., solution=..., complexity=..., test_cases=..., code_explanation=..., hints=...}`. Only generate one question. Only return one object."
    )

    response = model.generate_content(prompt)
    txt = response.text.replace("```", "").replace("json", "").strip()
    try:
        return json.loads(txt)
    except:
        time.sleep(0.2)
        return generate_problem(difficulty)


def generate_user(level):

    creds = load_creds()
    genai.configure(credentials=creds)
    model = genai.GenerativeModel("tunedModels/aiatltechnical-g1tdmwqkmops")

    if level == "1st/2nd Year Internship":
        return [generate_problem("easy"), generate_problem("easy")]
    elif level == "All Years Internship":
        return [generate_problem("easy"), generate_problem("medium")]
    else:
        return [generate_problem("medium"), generate_problem("hard")]


def evaluate(problem: dict, user_input: str, is_code: bool):

    creds = load_creds()
    genai.configure(credentials=creds)
    model = genai.GenerativeModel("tunedModels/aiatltechnical-g1tdmwqkmops")

    prompt = "Evaluate the user's solution given a problem. "
    if is_code:
        prompt += "The user provided a coding solution. "
    else:
        prompt += "The user explained their solution in words. "

    prompt += "The problem is defined as follows:\n" + problem["question"]

    prompt += "\nThe user's solution is as follows:\n" + user_input

    if is_code:
        prompt += "\nThe test cases are defined as follows:\n" + str(
            problem["test_cases"]
        )
        prompt += (
            "\nThe answer to the problem is defined as follows:\n" + problem["solution"]
        )
    else:
        prompt += (
            "\nThe answer to the problem is defined as follows:\n"
            + problem["code_explanation"]
        )

    prompt += "\nUsing the data provided, evaluate the user's solution. Rate the solution on score out of 1,000 where 0 is the worst and 1,000. Return the numerical score and a short explanation on how you came to the rating."

    response = model.generate_content(prompt)
    return response.text
