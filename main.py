from pathlib import Path


TRAINING_FILE = Path("training.txt")


def load_training_data(path: Path):
    if not path.exists():
        raise FileNotFoundError(f"File tidak ditemukan: {path}")

    lines = path.read_text(encoding="utf-8").splitlines()

    conversations = []
    current_user = None

    for line in lines:
        line = line.strip()

        if not line:
            continue

        if line.startswith("User:"):
            current_user = line[5:].strip()

        elif line.startswith("AI:") and current_user is not None:
            assistant = line[3:].strip()

            conversations.append({
                "user": current_user,
                "assistant": assistant
            })

            current_user = None

    return conversations


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
