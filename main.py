from backend.api.endpoints.technical import generate_user

u = generate_user("internship")
for i in u:
    print(i)
    print("--------")
