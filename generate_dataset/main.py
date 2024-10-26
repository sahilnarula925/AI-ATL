import pandas as pd

# from dotenv import load_dotenv
# import google.generativeai as genai
# import os

# load_dotenv()  # take environment variables


# genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content("Write a story about a magic backpack.")
# print(response.text)


# df = pd.read_json("hf://datasets/greengerong/leetcode/leetcode-train.jsonl", lines=True)
# df = df[["Difficulty", "Python"]]
# df.to_csv("test.csv")

# df = pd.read_csv("test.csv")
# print(df.columns)
# df = df[["difficulty", "content", "python"]]
# df.to_csv("test2.csv")

df = pd.read_csv("test2.csv")

code = df.pop("python")[0].split("```python")[1].split("```")
f = code[0].strip()
l, t = code[1].strip().split("\n\n")
df[["code", "explanation", "complexity"]] = f, l, t
df["problem"] = df.pop("content")
df = df.drop("Unnamed: 0", axis=1)

df.to_csv("test4.csv")
