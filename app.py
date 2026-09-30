import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

client = InferenceClient(
   token=os.getenv("HF_TOKEN")
)

MODEL = "meta-llama/Llama-3.1-8B-Instruct"

prompt = """
Create 5 flashcards about Machine Learning.

For each flashcard, provide:
Question:
Answer:

Keep the answers clear and useful for a beginner.
"""

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "user", "content": prompt}
    ],
    max_tokens=1000
)

print(response.choices[0].message.content)