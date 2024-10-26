import google.generativeai as genai
from backend.api.utils.oauth import load_creds
import json

creds = load_creds()
genai.configure(credentials=creds)

"""
dict = {question = str, solution = str, complexity = {time = str space = str test_cases = [{input = obj, output = obj}], code_explanation = str}
"""


def generate_problem(difficulty):
    # difficuly - pre-internship(easy, easy), internship(med / medium, medium / medium, hard)
    prompt = (
        "Generate a software engineering LeetCode style question. The difficulty should be "
        + difficulty
        + ". Generate 10 test cases. Return as a JSON."
        + " in format {question=..., solution=..., complexity=..., test_cases=..., code_explanation=...}`"
    )

    model = genai.GenerativeModel("tunedModels/test4-p3xuftrlivrt")
    response = model.generate_content(prompt)
    txt = response.text.replace("```", "").replace("json", "")
    print(txt)
    res = json.loads(txt)

    return res


print(generate_problem("easy"))
