# 🔫 Weapon Detection System 

![Project Banner](docs/banner.png) <!-- Optional banner image -->

---

## 🌟 Project Overview
This project implements an **AI-powered weapon detection system** using **YOLOv8**.  
It can automatically detect:  

- **Firearms** (pistols, rifles, guns)  
- **Improvised Weapons** (metal rods, broken glass, sharp objects)  

The system processes **videos or images** to identify and highlight weapons, and includes a **Streamlit web interface** for easy interaction.

---

## ⚡ Core Features
- ✅ Detect firearms and improvised weapons in images/videos  
- ✅ Output videos/images with **bounding boxes** around detected weapons  
- ✅ Firearm alert system (shows if a weapon is detected)  
- ✅ Streamlit app for **uploading media** and viewing results instantly  

---

## 🗂️ Dataset
- **Classes:** `Firearm`, `Improvised Weapons`, `No Weapon`  
- **Size:** ~1,500+ labeled images  
- **Annotations:** YOLO `.txt` files for bounding boxes  
- **Notes:** Custom dataset collected and labeled manually  

---

## 🏋️ Model & Training
- **Architecture:** YOLOv8n (fine-tuned)  
- **Framework:** Ultralytics YOLOv8 + PyTorch  
- **Training Details:**  
  - Epochs: 50  
  - Image Size: 640x640  
  - Batch Size: depends on system  
- **Metrics:** Precision, Recall, mAP (see results folder)  

---

## 🎬 Video Analysis Pipeline
1. **Video Input** → Extract frames  
2. **YOLO Detection** → Detect weapons per frame  
3. **Output Generation** → Annotated video with bounding boxes + alerts  

---

## 🖥️ Streamlit Interface
- Upload a **video** or **image**  
- Run detection on uploaded media  
- Display **annotated video or image** with bounding boxes  
- Show **alert** if a firearm or improvised weapon is detected  


---

## 📈 Results
- Firearms and improvised weapons successfully detected in test videos/images  

---

## ⚠️ Limitations
- Detection depends on dataset size & diversity  
- Rare or unusual improvised weapons may be missed  
- Live real-time stream detection not implemented (future scope)  

---

## 🚀 Future Scope
- Real-time detection from webcam streams  
- Expand dataset with more diverse improvised weapons  
- Multi-camera monitoring system  
- Automated alert notifications (SMS/email)  

---

## 💻 How to Run

```bash
# Clone repo
git clone <YOUR_REPO_URL>
cd weapon_detection_machine

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run interface.py
