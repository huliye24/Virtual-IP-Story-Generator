import json
from datetime import datetime
import os

def load_characters(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_history(character, history_folder):
    file_path = os.path.join(history_folder, f"{character['name'].lower()}.json")
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            histories = json.load(f)
    else:
        histories = []

    histories.append(character['history'][-1])
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(histories, f, ensure_ascii=False, indent=2)

def get_today_date():
    return datetime.now().strftime("%Y-%m-%d")

# TODO: 根据性格 traits 生成随机情绪
def generate_mood(traits):
    return "平静"  # 先写默认值

# TODO: 根据性格 traits 生成当日状态短句
def generate_status(traits):
    return "今天过得平凡而充实。"  # 默认占位