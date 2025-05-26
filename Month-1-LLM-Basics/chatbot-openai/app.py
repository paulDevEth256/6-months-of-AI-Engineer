from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()


# Request model
class ChatRequest(BaseModel):
    message: str


# Response model
class ChatResponse(BaseModel):
    reply: str


# Simple rule-based response logic
def generate_reply(message: str) -> str:
    message = message.lower()
    if "hello" in message or "hi" in message:
        return "Hello! How can I help you today?"
    elif "your name" in message:
        return "I'm your friendly chatbot!"
    elif "bye" in message:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I didn't understand that. Can you try again?"


# Chat en
