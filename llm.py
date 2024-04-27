from openai import OpenAI

from settings import config


def generate_puzzle(llm: OpenAI, answer: str) -> str:
    puzzle = (
        llm.chat.completions.create(
            model=config.model,
            max_tokens=4096,
            messages=[
                {
                    "role": "system",
                    "content": "一個熟悉台灣文化的助手，當收到一個台灣地名時請條列介紹當地著名特色，讓使用者猜測是在介紹甚麼地方。",
                },
                {"role": "user", "content": answer},
            ],
            temperature=0.8,
        )
        .choices[0]
        .message.content
    )
    return puzzle.replace(answer, "****").replace(answer[:2], "**")


def chat_with_puzzle(llm: OpenAI, answer: str, question: str) -> str:
    res = llm.chat.completions.create(
        model=config.model,
        max_tokens=4096,
        messages=[
            {
                "role": "system",
                "content": "一個熟悉台灣人文風景的助手，判斷使者的形容是否符合該地特色，最後要回答是否符合。不要自我介紹。不要提問。不要修正使用者說法。簡潔有力。",
            },
            {
                "role": "user",
                "content": f"形容:{question}\n地點:{answer}\n 這樣正確嗎？",
            },
        ],
    )
    return (
        res.choices[0].message.content.replace(answer, "****").replace(answer[:2], "**")
    )
