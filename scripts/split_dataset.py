import os, random, shutil
from pathlib import Path

def split_dataset(base_dir, out_dir, val_ratio=0.2, test_ratio=0.1, seed=42):
    random.seed(seed)
    images_dir = Path(base_dir)/"images"
    labels_dir = Path(base_dir)/"labels"
    imgs = [p for p in images_dir.glob("*") if p.suffix.lower() in [".jpg",".png",".jpeg"]]
    random.shuffle(imgs)

    n = len(imgs)
    ntest = int(n * test_ratio)
    nval = int(n * val_ratio)

    sets = {
        "test": imgs[:ntest],
        "val": imgs[ntest:ntest+nval],
        "train": imgs[ntest+nval:]
    }

    for split, files in sets.items():
        out_img = Path(out_dir)/"images"/split
        out_lbl = Path(out_dir)/"labels"/split
        out_img.mkdir(parents=True, exist_ok=True)
        out_lbl.mkdir(parents=True, exist_ok=True)

        for imgp in files:
            shutil.copy(imgp, out_img/imgp.name)
            lbl = labels_dir/(imgp.stem + ".txt")
            if lbl.exists():
                shutil.copy(lbl, out_lbl/(lbl.name))

if __name__ == "__main__":
    split_dataset(
        "weapon-detection/train",  # your current dataset folder
        "data"                   # new YOLO-ready folder
    )
