# Real-Time Face Recognition Attendance System

A Flask-based web application that uses face recognition for real-time attendance tracking via webcam. The system logs attendance, displays a dashboard, allows CSV download, and sends filtered PDF reports via email.

## 🔧 Features

- 🎥 Real-time face detection and recognition using webcam
- 📋 Attendance logging based on selected period
- 📊 Interactive dashboard with filters (Name, Date, Period)
- 📤 Download attendance records as CSV
- 📧 Send filtered records as PDF via email
- 🧠 Face recognition powered by deep learning (FaceNet or similar)

---

## 🛠️ Tech Stack

- Python (Flask, OpenCV, threading)
- HTML5/CSS3 (Frontend adapted from Celebrity Face Recognition UI)
- JavaScript (Optional: For frontend enhancements)
- ReportLab (for PDF generation)
- Google Sheets (via SheetBest API) for attendance storage

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/bhuvan-7/major_project.git
cd face-attendance-system
```
### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Make sure you have:

Python 3.7+
OpenCV
Flask
reportlib
requests
numpy, etc.

### 3. Run Application
```bash
python app.py
```

It will automatically open in your browser:

📸 Webcam Page: http://127.0.0.1:5000/
📊 Dashboard: http://127.0.0.1:5000/dashboard

### 4.✨ Future Improvements

-Student registration via UI

-Face recognition with liveness detection

-Admin login and user roles

-Enhanced UI with Bootstrap or Tailwind

-QR or RFID backup attendance
