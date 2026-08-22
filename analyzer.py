from openai import OpenAI
from pydantic import BaseModel
import time


class TextAnalysis(BaseModel):
    sentiment: str
    topic: str
    summary: str

start_time = time.time()
client = OpenAI()

text = input("Enter some text to analyze: ")

response = client.responses.parse(
    model="gpt-5.6",
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

print("\nAnalysis:")
print("Sentiment:", analysis.sentiment)
print("Topic:", analysis.topic)
print("Summary:", analysis.summary)
print(f"\nAPI response time: {end_time - start_time:.2f} seconds")