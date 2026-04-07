from ollama import chat
import time
import os

# Show current working directory
cwd = os.getcwd()
print("Current directory:", cwd)

# Ask for just the file name
filename = input("Enter image file name (in this folder): ").strip()

# Build full path
image_path = os.path.join(cwd, filename)

# Check if file exists
if not os.path.exists(image_path):
    print("File not found:", image_path)
    quit()

question = input("Ask a question about the image: ").strip()

start = time.time()

response = chat(
    model="qwen2.5vl:3b",   # corrected model name
    messages=[
        {
            "role": "user",
            "content": question,
            "images": [image_path]
        }
    ]
)

end = time.time()

print("\nResponse:")
print(response.message.content)
print(f"\nTime: {end - start:.2f} seconds")