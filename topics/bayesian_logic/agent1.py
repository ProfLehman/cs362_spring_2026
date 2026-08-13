import json
import os
import shutil
from pathlib import Path
from ollama import chat

# ---------------------------
# Configuration
# ---------------------------
MODEL = "qwen3:4b"
DRY_RUN = True   # Change to False after you trust it

ALLOWED_FOLDERS = {
    "Documents",
    "Images",
    "Audio",
    "Video",
    "Code",
    "Archives",
    "Spreadsheets",
    "Presentations",
    "PDFs",
    "Other",
}

SYSTEM_PROMPT = """
You are a careful file-organizing assistant.

Your job:
- Read a list of filenames from the current directory.
- For each file, choose exactly one destination folder from this allowed list:
  Documents, Images, Audio, Video, Code, Archives, Spreadsheets, Presentations, PDFs, Other

Rules:
- Return ONLY valid JSON.
- Return a JSON array.
- Each item must have:
  - "file": original filename
  - "folder": destination folder
- Do not include explanations.
- Do not invent files.
- Ignore folders; only classify files given to you.
- Use these guidelines:
  - .pdf -> PDFs
  - .doc, .docx, .txt, .md -> Documents
  - .xls, .xlsx, .csv -> Spreadsheets
  - .ppt, .pptx -> Presentations
  - .py, .java, .js, .html, .css, .cpp, .c -> Code
  - .zip, .rar, .7z, .tar, .gz -> Archives
  - .jpg, .jpeg, .png, .gif, .webp -> Images
  - .mp3, .wav, .m4a -> Audio
  - .mp4, .mov, .mkv -> Video
  - anything unclear -> Other
"""

def get_files_in_current_directory() -> list[str]:
    """Return file names only, excluding directories and this script."""
    current = Path(".")
    files = []
    for item in current.iterdir():
        if item.is_file() and item.name != Path(__file__).name:
            files.append(item.name)
    return sorted(files)

def ask_model_for_plan(files: list[str]) -> list[dict]:
    """Send filenames to Ollama and ask for a JSON sorting plan."""
    user_prompt = (
        "Classify these files into folders.\n\n"
        f"Files:\n{json.dumps(files, indent=2)}\n\n"
        "Return ONLY JSON."
    )

    response = chat(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        format={
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "file": {"type": "string"},
                    "folder": {"type": "string"},
                },
                "required": ["file", "folder"],
            },
        },
    )

    content = response.message.content
    return json.loads(content)

def validate_plan(plan: list[dict], actual_files: list[str]) -> list[dict]:
    """Keep only safe, valid moves."""
    actual_set = set(actual_files)
    validated = []

    seen = set()

    for item in plan:
        file_name = item.get("file", "").strip()
        folder = item.get("folder", "").strip()

        if file_name not in actual_set:
            continue
        if folder not in ALLOWED_FOLDERS:
            continue
        if file_name in seen:
            continue

        validated.append({"file": file_name, "folder": folder})
        seen.add(file_name)

    # Any files the model missed go to Other
    for file_name in actual_files:
        if file_name not in seen:
            validated.append({"file": file_name, "folder": "Other"})

    return validated

def execute_plan(plan: list[dict], dry_run: bool = True) -> None:
    """Create folders and move files."""
    for item in plan:
        src = Path(item["file"])
        dst_folder = Path(item["folder"])
        dst = dst_folder / src.name

        print(f"{'[DRY RUN]' if dry_run else '[MOVE]   '} {src} -> {dst}")

        if not dry_run:
            dst_folder.mkdir(exist_ok=True)
            shutil.move(str(src), str(dst))

def main():
    files = get_files_in_current_directory()

    if not files:
        print("No files found in the current directory.")
        return

    print("Files found:")
    for f in files:
        print(" -", f)

    print("\nAsking model for plan...")
    raw_plan = ask_model_for_plan(files)
    safe_plan = validate_plan(raw_plan, files)

    print("\nPlanned actions:")
    execute_plan(safe_plan, dry_run=DRY_RUN)

    if DRY_RUN:
        print("\nDry run only. Set DRY_RUN = False to actually move files.")

if __name__ == "__main__":
    main()