```python
import requests

url = "http://localhost:11434/api/chat"

messages = []

while True:
    user_input = input("You: ")
    messages.append({"role": "user", "content": user_input})

    response = requests.post(url, json={
        "model": "qwen2.5:0.5b",
        "messages": messages,
        "stream": False
    })

    reply = response.json()["message"]["content"]
    print("AI:", reply)

    messages.append({"role": "assistant", "content": reply})

    # clear context
    # messages = []

```
