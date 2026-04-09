```python
import requests

url = "http://localhost:11434/api/chat"

data = {
    "model": "qwen2.5:0.5b",
    "messages": [
        {"role": "user", "content": "Give one sentence definition of AI."}
    ],
    "stream": False
}

response = requests.post(url, json=data)

result = response.json()

print(result["message"]["content"])

```
