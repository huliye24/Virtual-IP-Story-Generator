# Virtual IP Story Generator

这是一个虚拟人物（IP）故事生成项目，用于管理和生成人物每日动态、情绪和故事内容。  
项目核心思想是把 **192 个虚拟人物** 的性格、星座、16 型人格等作为底层设定，通过 Python 框架每日生成他们的文字动态，就像写一本持续更新的小说。

---

## 项目目标

- 为每个虚拟人物生成每日：
  - 情绪（Mood）
  - 当日状态（Status）
  - 小故事（Story）
- 记录历史，形成完整的成长轨迹
- 提供可持续迭代的 IP 系统
- 支持未来扩展：
  - 人物数量增加到 192 个
  - AI 生成故事和互动事件
  - 可接入图像、音频或视频生成

---

## 核心特点

- **纯文字 MVP**：初始阶段只生成文本，不涉及图像或视频
- **Python 项目管理**：JSON 存储人物档案和历史
- **AI 协作**：可通过 GitHub 仓库链接或文件上传，让 AI 扫描整个项目生成内容
- **历史记录**：每日生成的故事会自动保存，方便长期迭代和分析

---

## 项目结构
virtual_ip_mvp/
│
├─ data/
│ └─ characters.json # 虚拟人物档案
├─ history/
│ └─ alice.json # 历史记录
│ └─ bob.json
│ └─ cathy.json
├─ scripts/
│ ├─ generate_daily.py # 核心逻辑：生成每日动态、故事
│ ├─ utils.py # 工具函数：日期、历史、情绪生成
│ └─ prompt_builder.py # 构建 AI prompt 模板
├─ main.py # 项目入口
└─ requirements.txt # Python 依赖


---

## 使用方式

1. 克隆仓库：

```bash
git clone <你的GitHub仓库链接>
cd virtual_ip_mvp

安装依赖（MVP 阶段可忽略，因为只用标准库）：

pip install -r requirements.txt

运行项目生成每日故事：

python -m main

输出每个人物的今日情绪、状态、故事占位文本

history/ 文件夹中保存每日历史记录

长期工作流建议

每次修改人物档案或故事逻辑 → 提交到 GitHub

提供仓库链接给 AI → AI 扫描整个项目 → 生成每日故事或优化代码

迭代扩展人物数量，丰富故事内容和事件

可以未来接入图像、音频、社群互动，形成完整 IP 生态

贡献与交流

欢迎提出建议、参与故事创作或扩展功能！
