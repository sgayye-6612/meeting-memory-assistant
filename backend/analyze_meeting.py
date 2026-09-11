import json

from backend.services.meeting_ai import MeetingAI


TRANSCRIPT_FILE = "data/transcripts/ES2002a.txt"
OUTPUT_FILE = "data/analyses/ES2002a_analysis.json"


def main():
    with open(TRANSCRIPT_FILE, "r", encoding="utf-8") as file:
        transcript = file.read()

    print("Loaded transcript.")
    print(f"Characters: {len(transcript)}")

    print("\nAnalyzing meeting with Ollama...")

    meeting_ai = MeetingAI()
    analysis = meeting_ai.analyze(transcript)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        json.dump(
            analysis,
            file,
            indent=2,
            ensure_ascii=False
        )

    print("\n" + "=" * 60)
    print("MEETING ANALYSIS")
    print("=" * 60)

    print(json.dumps(
        analysis,
        indent=2,
        ensure_ascii=False
    ))

    print("\nAnalysis saved to:")
    print(OUTPUT_FILE)


if __name__ == "__main__":
    main()