import requests

API_KEY = "YOUR API KEY"

PROXIES = {
    "http": "http://127.0.0.1:4780",
    "https": "http://127.0.0.1:4780"
}

MODEL = "gpt-3.5-turbo"

history = [{"role": "system", "content": "你好"}]

def chat():
    data = {
        "messages": history,
        "model": MODEL
    }

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json=data,
        proxies=PROXIES
    )

    message = response.json()["choices"][0]["message"]["content"].strip()
    history.append(response.json()["choices"][0]["message"])

    return message

while True:
    message = chat()
    print("Bot:", message)
    msg = input("You: ")
    history.append({"role": "user", "content": msg})
