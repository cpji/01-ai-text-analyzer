from analyzer import analyze_text
import statistics


def main():
    text = input("Enter some text to analyze: ")

    if not text.strip():
        print("Please enter some text to analyze.")
        return

    response_times = []

    for i in range(2):
        print(f"\n--- Run {i + 1} ---")

        analysis, response_time = analyze_text(text)

        print("Sentiment:", analysis.sentiment)
        print("Topic:", analysis.topic)
        print("Summary:", analysis.summary)
        print(f"Response time: {response_time:.2f} seconds")

        response_times.append(response_time)

    print("\n===== Statistics =====")

    print(f"Average: {statistics.mean(response_times):.2f} seconds")
    print(f"Fastest: {min(response_times):.2f} seconds")
    print(f"Slowest: {max(response_times):.2f} seconds")


if __name__ == "__main__":
    main()