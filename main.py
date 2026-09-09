from pathlib import Path
import random

TRAINING_FILE = Path("training.txt")


def load_training_data():
    if not TRAINING_FILE.exists():
        print("training.txt tidak ditemukan.")
        return []

    lines = TRAINING_FILE.read_text(encoding="utf-8").splitlines()

    data = []
    user = None

    for line in lines:
        line = line.strip()

        if line.startswith("User:"):
            user = line[5:].strip()

        elif line.startswith("AI:") and user:
            ai = line[3:].strip()

            data.append({
                "user": user,
                "ai": ai
            })

            user = None

    return data


def find_response(question, data):
    question = question.lower().strip()

    if not question:
        return "Coba tulis pertanyaan."

    # Exact match
    for item in data:
        if item["user"].lower() == question:
            return item["ai"]

    # Keyword match sederhana
    words = question.split()

    best = []
    best_score = 0

    for item in data:
        text = item["user"].lower()

        score = sum(1 for word in words if word in text)

        if score > best_score:
            best_score = score
            best = [item["ai"]]
        elif score == best_score and score > 0:
            best.append(item["ai"])

    if best:
        return random.choice(best)

    return "Maaf, aku belum tahu cara menjawab pertanyaan itu."


def main():
    data = load_training_data()

    print("=" * 50)
    print("AI CLI")
    print("=" * 50)
    print(f"Dataset: {len(data)} percakapan")
    print("Ketik 'exit' untuk keluar.")
    print()

    while True:
        try:
            question = input("You: ").strip()

            if question.lower() in ["exit", "quit", "bye"]:
                print("AI: Sampai jumpa! 👋")
                break

            answer = find_response(question, data)

            print(f"AI: {answer}")
            print()

        except KeyboardInterrupt:
            print("\nAI: Sampai jumpa! 👋")
            break


if __name__ == "__main__":
    main()
def main():
    try:
        data = load_training_data(TRAINING_FILE)

        print(f"Training data loaded: {len(data)} conversations")

        for i, item in enumerate(data[:5], start=1):
            print(f"\nExample {i}")
            print(f"User: {item['user']}")
            print(f"AI: {item['assistant']}")

    except FileNotFoundError as error:
        print(f"Error: {error}")

    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
