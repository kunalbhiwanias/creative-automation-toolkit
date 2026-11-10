
from pathlib import Path
from PIL import Image

INPUT_FOLDER = Path("input")
OUTPUT_FOLDER = Path("output")

MAX_WIDTH = 1080
MAX_HEIGHT = 1080
QUALITY = 90

INPUT_FOLDER.mkdir(exist_ok=True)
OUTPUT_FOLDER.mkdir(exist_ok=True)

SUPPORTED = {".jpg", ".jpeg", ".png", ".webp"}

for file in INPUT_FOLDER.iterdir():
    if file.suffix.lower() not in SUPPORTED:
        continue

    try:
        with Image.open(file) as image:
            image.thumbnail((MAX_WIDTH, MAX_HEIGHT))

            if image.mode not in ("RGB", "L"):
                image = image.convert("RGB")

            output = OUTPUT_FOLDER / f"{file.stem}.jpg"
            image.save(output, "JPEG", quality=QUALITY)

            print(f"Processed: {file.name}")

    except Exception as error:
        print(f"Error: {file.name}: {error}")

print("Batch resizing completed!")
