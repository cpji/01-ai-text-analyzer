# AI Text Analyzer

A Python application that uses the OpenAI API to analyze user-provided text.

This project is a hands-on exercise in building an AI-powered Python application. It explores API integration, structured AI responses, data validation, error handling, performance measurement, and model comparison.

## Project Started

August 21, 2026

---

## Project Goals

The goal of this project is to learn how to build a practical application that communicates with an AI model through an API.

1. Connect a Python application to an AI API.
2. Accept text from a user.
3. Send the text to an AI model.
4. Analyze sentiment.
5. Identify the main topic.
6. Generate a short summary.
7. Use structured AI output with Pydantic.
8. Validate AI-generated data.
9. Handle API errors gracefully.
10. Validate user input.
11. Measure API response time.
12. Compare AI models for response time and output quality.
13. Benchmark model performance.
14. Compare model quality and consistency.
15. Measure API usage and cost.
16. Separate application logic from benchmarking logic.
17. Build a clean, portfolio-ready Python project.

---

## Features

The application currently:

- Accepts text from the user.
- Analyzes sentiment.
- Identifies the main topic.
- Generates a short summary.
- Returns structured AI output.
- Uses Pydantic for data validation.
- Uses an Enum to validate sentiment values.
- Rejects blank or whitespace-only input.
- Handles common API errors.
- Measures API response time.
- Runs repeated model tests.
- Calculates benchmark statistics such as:
  - Average response time
  - Fastest response
  - Slowest response

---

## Example

### Input

```text
The restaurant was beautiful and the food was excellent, but the service was slow.

### Output

Sentiment: positive

Topic: Restaurant dining experience

Summary: The restaurant had an attractive setting and excellent food, though the service was slow.

Response time: 1.45 seconds

### Project Structure

01-ai-text-analyzer/
│
├── .gitignore
├── README.md
├── analyzer.py
├── benchmark.py
├── requirements.txt
└── .venv/

Files
analyzer.py

The main application.

It:

Gets text from the user.
Sends the text to the OpenAI API.
Requests structured output.
Validates the response.
Displays the analysis.
Measures response time.
benchmark.py

Used for experimenting with AI model performance.

It allows the project to:

Run the same analysis multiple times.
Measure response time.
Calculate average response time.
Identify fastest and slowest responses.
Compare model behavior and output quality.
requirements.txt

Contains the Python packages required by the project.

Current dependencies:

openai
pydantic
.gitignore

Prevents files such as the Python virtual environment, Python cache files, macOS system files, and environment files containing secrets from being committed to Git.

Technologies
Python
OpenAI API
OpenAI Python SDK
Pydantic
Git
GitHub
Concepts Learned

This project is being used to practice the following concepts:

Python
Virtual environments
Package management with pip
Functions
Loops
Conditional statements
Exception handling
Input validation
Enums
Timing and performance measurement
APIs
API authentication
API requests
API responses
HTTP/API errors
Rate limits and quotas
Structured API responses
AI Application Development
Prompt design
Structured AI output
Pydantic models
Model selection
Model benchmarking
Response-time measurement
Output quality comparison
Consistency testing
Software Development
Project organization
Separation of responsibilities
Dependency management
Git
Git commits
.gitignore
GitHub

Model Performance Experiment

One of the goals of this project is to determine whether a faster AI model can provide sufficiently good results for a simple text-analysis application.

Early tests showed that different models can produce similar results while having noticeably different response times.

For example, repeated tests of the same restaurant review produced response times ranging from approximately 1 to 4 seconds.

This led to an important observation:

The best model for an application is not necessarily the most capable model. It depends on the application's requirements for quality, speed, cost, and consistency.

The benchmark will be expanded as the project develops.

Error Handling

The application is designed to handle common API problems without exposing a large Python traceback to the user.

Examples include:

API rate limits
API quota problems
Connection errors
API status errors

The project also validates user input before making an API request.

For example, entering only spaces produces:

Please enter some text to analyze.

No API request is made in that situation.

Security

API keys should never be placed directly inside Python source code or committed to GitHub.

The application uses environment-based API authentication rather than hard-coding the API key.

The .gitignore file also prevents local environment files such as .env from being committed.

Future Improvements

Planned improvements include:

Separate the AI analysis logic from benchmarking logic.
Compare additional AI models.
Run larger benchmark samples.
Calculate statistical performance measures.
Measure token usage.
Estimate API cost.
Add automated quality evaluation.
Test consistency across repeated requests.
Add automated unit tests.
Improve error messages.
Add command-line options.
Add a simple graphical or web interface.
Improve documentation.
Publish the project on GitHub.
Learning Journey

This project is being developed incrementally.

Rather than building the entire application at once, each feature is being added to understand the underlying concept.

The development path so far has been:

Python environment
       ↓
Install OpenAI SDK
       ↓
Connect to OpenAI API
       ↓
Send first API request
       ↓
Accept user input
       ↓
Analyze text
       ↓
Create structured output
       ↓
Add Pydantic validation
       ↓
Add Enum validation
       ↓
Measure API response time
       ↓
Benchmark repeated requests
       ↓
Compare AI models
       ↓
Add input validation
       ↓
Add error handling
       ↓
Organize project with Git
       ↓
Publish project on GitHub
       ↓
Continue improving the application
Status

Current status: In development

The core text-analysis functionality is working.

The project is currently being expanded from a simple API experiment into a more complete and portfolio-ready AI application.

Author

Chet

This project is part of my ongoing practice in Python, APIs, AI application development, and modern IT skills.



### One small note


I deliberately wrote **"OpenAI API"**, not "GPT-5.6" throughout the README. That's better documentation because the project is becoming a **model-independent AI application**. We're already experimenting with different models, and later we may compare several models without having to rewrite the README.


Now save the file and run:


```bash
git status

You should see:

modified: README.md

Then we'll make your second meaningful commit:

git add README.md
git commit -m "Improve project documentation"

After that, your Git history will tell a nice little story:

068712e  Initial AI text analyzer project
         ↓
         Project documentation
         ↓
         More features
         ↓
         More commits
         ↓
         Final portfolio project
