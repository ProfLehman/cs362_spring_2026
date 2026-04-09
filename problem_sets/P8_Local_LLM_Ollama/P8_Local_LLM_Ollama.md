# CS 362 Artificial Intelligence and Machine Learning  
**Spring 2026**  
**60 points**  
**Due: April 23, 2026**

## P8 Local LLMs with Ollama

---

## Overview

In this assignment, you will install and run a **local large language model (LLM)** using **[Ollama](https://ollama.com/)**. You will interact with the model both through the command line and through a Python program.

You will also compare two different models and reflect on their capabilities, performance, and potential use cases.

This assignment demonstrates how modern AI systems can run **locally without cloud access or API keys**, while still exposing a programmable interface.

---

## Learning Objectives

- Install and run a local LLM using Ollama  
- Interact with an LLM through both terminal and Python  
- Understand how a local AI server is accessed via HTTP  
- Use structured messages to provide context to a model  
- Compare different LLMs (size, speed, quality, use cases)  
- Reflect on the strengths and limitations of local AI systems  

---

## Setup

You may complete this assignment using:

- Your own **Windows or Mac computer**, or  
- A **Raspberry Pi** in the lab  

### Install Ollama

Follow the official instructions:

```bash
curl -fsSL https://ollama.com/install.sh | sh
````

Verify installation:

```bash
ollama -v
```

---

## A. Run Local Models (20 points)

### Step 1 — Run your first model

Run:

```bash
ollama run qwen2.5:0.5b
```

Ask at least **two questions**.

---

### Step 2 — Run a second model

Choose a different model, for example:

```bash
ollama run smollm2:135m
```

or another small model available in Ollama.

Ask the **same two questions** as above.

---

### Step 3 — Compare the models

Consider:

* Response quality
* Speed
* Detail of answers
* Accuracy

---

### Deliverable

Provide **screenshots** showing:

* Model 1 running in chat
* Model 2 running in chat

---

## B. Python Access to Local Model (20 points)

Write a Python program that sends a request to your local Ollama server.

### Example starter code

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

print(response.json()["message"]["content"])
```

---

### Requirements

Your program must:

1. Send at least one question to the model
2. Print the model’s response
3. Use a `messages` list structure
4. (Optional challenge) Maintain a multi-turn conversation

---

### Deliverable

Provide a **screenshot showing**:

* Your Python code running
* A question and response from the model

---

## C. Model Research and Comparison (20 points)

For each of the **two models you used**, write **one paragraph** that includes:

### Required elements (1 paragraph for each model)

* Model name
* Company
* Approximate size (e.g., 135M, 0.5B, etc.)
* General purpose or design goal
* Typical use cases
* Strengths and limitations

---

### Comparison (1 or 2 paragraphs)

Write a short comparison discussing:

* Which model performed better and why
* Tradeoffs between size and performance
* When you would choose each model

---

## Reflection (1 paragraph)

* One advantage of running AI locally
* One limitation compared to cloud-based models
  
---

## Submission

Submit a single document (PDF or Markdown) that includes:

### 1. Screenshots

* Two models running in the terminal
* Python program output

### 2. Python Code

* Your complete script

### 3. Written Responses

* Two model research paragraphs
* One comparison paragraph

---

## Key Concepts

* Local vs cloud-based AI
* Client-server architecture (`localhost`)
* JSON-based APIs
* Context using message history
* Model size vs performance tradeoffs

---

## Grading Summary

| Component                       | Points |
| ------------------------------- | ------ |
| A. Running and comparing models | 20     |
| B. Python access                        | 20     |
| C. Research, comparison, and reflection | 20     |
| **Total**                       | **60** |



---

## Notes

* The first model run may take time due to the download time
* Smaller models are recommended for Raspberry Pi
* Ollama runs locally — no API key required
* Responses may be slower on lower-powered devices

---

