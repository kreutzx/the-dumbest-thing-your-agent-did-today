import os

# The dumbest thing your agent did today — one-line entry.
ENTRY_TEXT = "Mine looped 11,000 times asking itself 'are you sure?' — then answered 'no' and deleted the backup to be safe."


def main():
    # Write the entry to the required output location.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
