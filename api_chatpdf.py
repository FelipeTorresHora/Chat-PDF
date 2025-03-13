import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("CHATPDF_API_KEY")
BASE_URL = "https://api.chatpdf.com/v1"

def upload_pdf(file):
    headers = {"x-api-key": API_KEY}
    response = requests.post(
        f"{BASE_URL}/sources/add-file",
        headers=headers,
        files={"file": file}
    )
    return response.json()["sourceId"]

def ask_question(source_id, question):
    headers = {"x-api-key": API_KEY, "Content-Type": "application/json"}
    data = {
        "sourceId": source_id,
        "messages": [{"role": "user", "content": question}]
    }
    response = requests.post(f"{BASE_URL}/chats/message", headers=headers, json=data)
    return response.json()["content"]