from backend.api.endpoints.behavioral_cv import (
    get_behavioral_score
)

video = get_behavioral_score(
    "behavioral_interview.mp4",
    "Rate this interview out 100, include 3 key details said",
)

print(video)

""" from backend.api.endpoints.behavioral_bq import *
from 

question = generate_problem(2)
print(question) """
