import json
from pathlib import Path
from ollama import chat

MODEL = "qwen3:4b"

SYSTEM_PROMPT = """
You are an assistant that organizes files into logical groups.

Your task:
- You will be given a list of file names (without extensions).
- Suggest 3 to 5 folder names that would best group these files.

Rules:
- Return ONLY valid JSON
- Return a JSON array of strings
- Folder names should be short and descriptive
- Use underscores instead of spaces
- Do NOT include explanations
- Do NOT include anything except the JSON list

Example output:
["New_York", "Texas", "California", "Midwest", "Travel_Guides"]
"""

def get_filenames_no_ext():
    files = []
    for p in Path(".").iterdir():
        if p.is_file():
            files.append(p.stem)  # removes extension
    return sorted(files)

def ask_model_for_folders(file_names):
    
    
    
    prompt = (
        "Here are file names:\n\n"
        f"{json.dumps(file_names, indent=2)}\n\n"
        "Suggest a folder name. Return only a JSON list of folder names."
    )

    response = chat(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
    )

    content = response.message.content.strip()

    try:
        folders = json.loads(content)
        return folders
    except json.JSONDecodeError:
        print("⚠️ Model did not return valid JSON:")
        print(content)
        return None

def main():
    file_names = get_filenames_no_ext()

    file_names = file_names[:10]

    print("Files (no extensions):")
    for f in file_names:
        print(" -", f)

    print("\nAsking model for folder suggestions...\n")

    folders = ask_model_for_folders(file_names)

    if folders:
        print("Suggested folders:")
        for f in folders:
            print(" -", f)

if __name__ == "__main__":
    main()