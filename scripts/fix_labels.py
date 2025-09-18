import os
from pathlib import Path

def fix_labels(base_dir):
    """
    Ensures every image has a matching .txt label file.
    If missing, creates an empty .txt file.
    """
    image_exts = [".jpg", ".jpeg", ".png"]

    for split in ["train", "val", "test"]:
        img_dir = Path(base_dir) / "images" / split
        lbl_dir = Path(base_dir) / "labels" / split
        lbl_dir.mkdir(parents=True, exist_ok=True)

        for img_file in img_dir.glob("*"):
            if img_file.suffix.lower() in image_exts:
                label_file = lbl_dir / f"{img_file.stem}.txt"
                if not label_file.exists():
                    print(f"⚠️ Creating empty label for {img_file.name}")
                    label_file.touch()  # creates empty file

if __name__ == "__main__":
    fix_labels("data")  # path to your YOLO-ready dataset folder
