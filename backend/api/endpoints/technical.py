import google.generativeai as genai
import json
from backend.api.utils.oauth import load_creds

creds = load_creds("technical")
genai.configure(credentials=creds)

"""
dict = {question = str, solution = str, complexity = {time = str space = str test_cases = [{input = obj, output = obj}], code_explanation = str}
"""


def generate_problem(difficulty):
    # difficuly - pre-internship(easy, easy), internship(med / medium, medium / medium, hard)
    prompt = (
        "Generate only one software engineering LeetCode style question. The difficulty should be "
        + difficulty
        + ". Generate 10 test cases. Generate 3 hints. Respond with a JSON compliant object"
        + " in format {question=..., solution=..., complexity=..., test_cases=..., code_explanation=..., hints=...}`. Only generate one question. Only return one object."
    )

    model = genai.GenerativeModel("tunedModels/test4-p3xuftrlivrt")
    response = model.generate_content(prompt)
    txt = response.text.replace("```", "").replace("json", "").strip()
    print(txt)
    res = json.loads(txt)

    return res


def generate_user(level):
    if level == "pre_internship":
        return [generate_problem("easy"), generate_problem("easy")]
    elif level == "internship":
        return [generate_problem("easy"), generate_problem("medium")]
    else:
        return [generate_problem("medium"), generate_problem("hard")]



def evaluate(problem: dict, user_input: str, is_code: bool):
    prompt = "Evaluate the user's solution given a problem. "
    if is_code:
        prompt += "The user provided a coding solution. "
    else:
        prompt += "The user explained their solution in words. "

    prompt += "The problem is defined as follows:\n" + problem.question

    prompt += "The user's solution is as follows:\n" + user_input

    prompt += 
