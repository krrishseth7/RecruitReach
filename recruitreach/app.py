from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend is running successfully!"

if __name__ == "__main__":
    app.run()





# import os
# import requests
# from dotenv import load_dotenv
# from bs4 import BeautifulSoup
# from openai import OpenAI
# import msoffcrypto
# import io
# import openpyxl
# from flask import Flask,render_template, request
# app=Flask(__name__)
# #@app.route("/generate", methods=["POST"])

# load_dotenv(dotenv_path="C:\Users\Krrish Seth\projects\llm_engineering\.env",override=True) #API KEY error
# try:
#     api_key=os.getenv('OPENAI_API_KEY')
#     if not api_key:
#         print("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
#     elif not api_key.startswith("sk-proj-"):
#         print("An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook")
#     elif api_key.strip() != api_key:
#         print("An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them - see troubleshooting notebook")
#     else:
#         print("API key found and looks good so far!")
# except:
#     print("API error")
# openai=OpenAI()
# def message_creater(name):
#     message=[{"role":"system","content":f"You are a very professional candidate, writing from my POV, my name is {name}"},{"role":"user","content":"Write an email as a cold email, you have access to the name, email, company,  position etc of the person, I am internship less so need an internship, make perzonalized email for each person"}]
#     return message
# def generate_email(name):
#     response=openai.chat.completions.create(model="gpt-4o-mini",messages=message_creater(name))
#     return response.choices[0].message.content
# inp=input("Enter your name: ")
# message=generate_email(inp)