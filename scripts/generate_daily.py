from .utils import get_today_date, generate_mood, generate_status, save_history

def generate_daily(character, history_folder):
    today = get_today_date()
    mood = generate_mood(character['traits'])
    status = generate_status(character['traits'])

    # TODO: 调用 AI 生成故事，暂时填占位文本
    story = f"{character['name']} 的故事内容占位……"

    daily_record = {
        "date": today,
        "mood": mood,
        "status": status,
        "story": story
    }

    # 保存到人物历史
    character['history'].append(daily_record)
    save_history(character, history_folder)

    return daily_record
