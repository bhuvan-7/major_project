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
git clone https://github.com/yourusername/face-attendance-system.git
cd face-attendance-system
```
