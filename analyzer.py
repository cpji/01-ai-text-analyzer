from openai import OpenAI
from pydantic import BaseModel
import time


MODEL = "gpt-5.6"


class TextAnalysis(BaseModel):
    sentiment: str
    topic: str
    summary: str


def analyze_text(text):
    client = OpenAI()

    start_time = time.time()

    response = client.responses.parse(
    model=MODEL,
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

    analysis = response.output_parsed
    response_time = end_time - start_time

    return analysis, response_time


def main():
    text = input("Enter some text to analyze: ")

    analysis, response_time = analyze_text(text)

    print("\nAnalysis:")
    print("Sentiment:", analysis.sentiment)
    print("Topic:", analysis.topic)
    print("Summary:", analysis.summary)

    print(f"\nAPI response time: {response_time:.2f} seconds")


if __name__ == "__main__":
    main()
