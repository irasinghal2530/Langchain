from typing import TypedDict
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI()

# schema

class Review(TypedDict):
    rating: int
    summary: str
    is_positive: bool

# prompt

prompt = """You are a helpful assistant that analyzes product reviews.

Review: {review}

Extract the following information:
- rating: The rating given in the review (1-5)
- summary: A brief summary of the review
- is_positive: Whether the review is positive (True/False)

Return the information in the following format:
{{
    "rating": <rating>,
    "summary": "<summary>",
    "is_positive": <is_positive>
}}
"""
print(rating)