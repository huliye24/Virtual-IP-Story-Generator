from scripts.generate_daily import generate_daily
from scripts.utils import load_characters
import os

DATA_FILE = "data/characters.json"
HISTORY_FOLDER = "history"

if not os.path.exists(HISTORY_FOLDER):
    os.makedirs(HISTORY_FOLDER)

def main():
    characters = load_characters(DATA_FILE)
    for char in characters:
        record = generate_daily(char, HISTORY_FOLDER)
        print(f"生成 {char['name']} 的今日记录：")
        print(f"情绪: {record['mood']}")
        print(f"状态: {record['status']}")
        print(f"故事: {record['story']}\n")

if __name__ == "__main__":
    main()