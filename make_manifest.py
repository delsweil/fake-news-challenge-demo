import json
import os

# Files live here in the repo:
STIM_FS_DIR = "public/stimuli"

# But in the browser they are served from:
STIM_URL_PREFIX = "stimuli"

OUTFILE = "stimuli_manifest.json"
EXTS = (".png", ".jpg", ".jpeg", ".webp")

def main():
    files = []
    for name in sorted(os.listdir(STIM_FS_DIR)):
        if name.lower().endswith(EXTS):
            files.append(f"{STIM_URL_PREFIX}/{name}")
    with open(OUTFILE, "w", encoding="utf-8") as f:
        json.dump(files, f, indent=2)
    print(f"Wrote {OUTFILE} with {len(files)} files.")

if __name__ == "__main__":
    main()
