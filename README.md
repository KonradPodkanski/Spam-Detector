# Spam Detector (Python + PyQt6)

An application with a graphical interface. The model is trained on data and automatically classifies messages as SPAM or NOT SPAM.

---

## Technologies used:
- Python 3.x  
- PyQt6 (GUI)  
- scikit-learn (classification model)  
- pandas & numpy (data processing)

---

## Interface:
GUI built with Qt Designer, includes:
- Input field for the message  
- **"Check"** button  
- Information whether the message is SPAM  
- **"Reset"** button to clear the input

---

### Requirements:
- Python 3.12  
- PyQt6 6.9.1  
- scikit-learn 1.7.0  
- pandas 2.3.1  
- numpy 2.3.1
- langdetect 1.0.9
---

### Installation:

1. Download the project

2. Install required libraries:
```bash
pip install -r requirements.txt
```

---

### How to run?

**Option 1** – using the graphical launcher:  
Run the file **`spam_detector_run.bat`**

![run_presentation](img/run_presentation.png)

**Option 2** – via terminal:
```bash
python main.py
```

---

## Requirements analysis:

### 1. Functional requirements:

- The application allows the user to enter a text message  
- The user can check whether the message is spam  
- The system warns if the message is not in English

### 2. Non-functional requirements:

- Fast operation (real-time response)  
- Intuitive interface  
- Portability between systems (Windows, macOS – with proper configuration)
