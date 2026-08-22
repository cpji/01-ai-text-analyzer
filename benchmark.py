# Model performance experiments
from openai import OpenAI, APIConnectionError, RateLimitError, APIStatusError
from pydantic import BaseModel
from enum import Enum
import time


class Sentiment(str, Enum):
    POSITIVE = "positive"
    NEGATIVE = "negative"
    NEUTRAL = "neutral"


class TextAnalysis(BaseModel):
    sentiment: Sentiment
    topic: str
    summary: str

client = OpenAI()

text = input("Enter some text to analyze: ")

if not text.strip():
    print("Please enter some text to analyze.")
    exit()

def analyze(model):
    start_time = time.time()

    try:
        response = client.responses.parse(
            model=model,
            input=[
                {
                    "role": "user",
                    "content": f"""
Analyze the following text.

Determine:
- sentiment: positive, negative, or neutral
- main topic
- short summary

Text:
{text}
"""
                }
            ],
            text_format=TextAnalysis,
        )

        end_time = time.time()

        return response.output_parsed, end_time - start_time

    except RateLimitError:
        print("API rate limit or quota exceeded.")
        return None, None

    except APIConnectionError:
        print("Could not connect to the OpenAI API.")
        return None, None

    except APIStatusError as e:
        print(f"OpenAI API error: {e.status_code}")
        return None, None
    
times = []

print("\n===== GPT-5.6 Luna: 5 Runs =====")

for i in range(2):
    analysis, response_time = analyze("gpt-5.6-luna")

if analysis is not None:
    print("\nSentiment:", analysis.sentiment.value)
    print("Topic:", analysis.topic)
    print("Summary:", analysis.summary)
    print(f"Response time: {response_time:.2f} seconds")
    times.append(response_time)

average = sum(times) / len(times)

print("\n===== Statistics =====")
print(f"Average: {average:.2f} seconds")
print(f"Fastest: {min(times):.2f} seconds")
print(f"Slowest: {max(times):.2f} seconds")
