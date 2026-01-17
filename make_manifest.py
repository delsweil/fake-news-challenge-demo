import os, json

STIM_DIR = "stimuli"
OUT_FILE = "stimuli_manifest.json"

def main():
    files = []
    for name in os.listdir(STIM_DIR):
        low = name.lower()
        if low.endswith((".png", ".jpg", ".jpeg", ".webp")):
            files.append(f"{STIM_DIR}/{name}")

    files.sort()
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(files, f, ensure_ascii=False, indent=2)

    print(f"Wrote {OUT_FILE} with {len(files)} files.")

if __name__ == "__main__":
    main()
