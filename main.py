from backend.api.endpoints.technical import generate_user, evaluate

problem = generate_user("internship")
problem_one = problem[0]
print(problem_one)
print()

print(evaluate(problem_one, problem_one["solution"], True))
