# 🎯 Real-Time Face Recognition Attendance System

A web-based system that leverages deep learning and computer vision for contactless and automated attendance logging using live webcam video. The project integrates real-time face recognition, attendance tracking, dashboard analytics, PDF and CSV generation, and email delivery, making it an ideal solution for classrooms or corporate environments.

---

## 🧠 What It Does

- Detects and recognizes faces using your webcam
- Logs attendance to Google Sheets via SheetBest API
- Allows you to select a class period before tracking
- Filters attendance records by Name, Date, or Period
- Displays stats for total logs, present, and absent counts
- Exports attendance reports as CSV and PDF
- Sends PDF reports via email directly from dashboard

---

## 💻 Tech Stack

| Technology     | Purpose                                |
|----------------|----------------------------------------|
| Python         | Core programming language              |
| Flask          | Web framework for backend and routing  |
| OpenCV         | Video processing and frame capture     |
| ReportLab      | Dynamic PDF generation                 |
| Google Sheets  | Cloud-based storage (via SheetBest)    |
| HTML/CSS       | Frontend interface (custom themed)     |
| JavaScript     | Optional UI enhancements               |
| Gmail SMTP     | Email delivery for reports             |

---

## 📂 Project Structure

```plaintext
face-attendance-system/
│
├── app.py                         # Main Flask app with all routes
├── models/                        # Trained face recognition models (.pkl/.npz)
├── recognition/
│   └── detector.py                # Face detection and recognition logic
├── attendance/
│   └── sheet_logger.py            # Logs absentees to Google Sheet
├── templates/
│   ├── index.html                 # Period selection + webcam feed
│   └── dashboard.html             # Dashboard with filters + analytics
├── static/
│   ├── css/                       # Custom styles (optional)
│   └── js/                        # JS scripts (optional)
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
```
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

### 3. Run Application
```bash
python app.py
```

It will automatically open in your browser:

-📸 Webcam Page: http://127.0.0.1:5000/

-📊 Dashboard: http://127.0.0.1:5000/dashboard

---
###  4. 🎥 How Attendance Works
You select a period (e.g., P1, P2, etc.) on the homepage.

The webcam starts detecting faces.

Face embeddings are compared to the stored models.

Recognized students are marked as "Present".

After the session, the unrecognized students are marked "Absent".

All logs are stored in Google Sheets.

---

### 5.📤 Email Functionality
Filter records in the dashboard and click "Send Email".

A PDF report is generated based on the filters.

The report is emailed to a predefined address using Gmail SMTP.

---

### 6. 📊 Dashboard Filters
Filter logs by:

👤 Student Name

📅 Date (YYYY-MM-DD)

⏰ Period (P1, P2, ...)

Displays:

✅ Present Count

❌ Absent Count

📄 Total Records

Download reports as:

📄 CSV

📄 PDF (via email)

---

### 7. 🔐 Security Notes
Do not hardcode production email credentials.

Use .env file or environment variables in future versions.

Enable liveness detection to prevent spoofing attacks.

Optional: Add admin authentication to restrict dashboard access.

---

### 8. 🎯 Future Scope
✨ User authentication for admin and students

📸 Student face registration via browser

📱 Mobile-friendly UI using Bootstrap/Tailwind

🔒 Secure face data storage using database

📆 Calendar heatmaps and charts for analytics

⌛ Attendance by time intervals (e.g., minutes late)

---

### 9. 📄 License
This project is licensed for educational and demonstration purposes only. For commercial usage, please contact the author.

---

### 10. Acknowledgements  

We would like to sincerely thank our project guide **Dr. Hemanth S R** for his valuable guidance, continuous support, and encouragement throughout the development of this project.  
We also extend our gratitude to our project co-ordinator **Dr. Victor A I** for his coordination, timely advice, and motivation that greatly contributed to this work.  


