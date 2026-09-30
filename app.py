from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

print("API key loaded:", api_key is not None)

client = OpenAI(
    api_key=api_key
)

question = input("Enter your question: ")

response = client.responses.create(
    model="gpt-5.6-luna",
    input=question
)

print(response.output_text)