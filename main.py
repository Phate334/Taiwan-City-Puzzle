import random

from openai import OpenAI

from llm import chat_with_puzzle, generate_puzzle
from model import Taiwan
from settings import config

taide_llm = OpenAI(
    base_url=config.openai_base_url,
    api_key=config.openai_api_key,
)


def main():
    with open("areas.json", encoding="utf-8") as f:
        areas = Taiwan.model_validate_json(f.read())
    answer = random.choice(areas.cities)
    puzzle = generate_puzzle(taide_llm, answer)
    print(puzzle)
    while True:
        question = input("> ")
        if question[:2] in answer:
            print(f"答對了！就是 {answer}")
            break
        elif question == "猜不到":
            print(f"答案是 {answer}")
            break
        print(chat_with_puzzle(taide_llm, answer, question))


if __name__ == "__main__":
    main()
