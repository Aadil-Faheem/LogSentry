# 🔍 LogSentry

**LogSentry** is a lightweight Python-based anomaly detection tool for log files. It provides a simple GUI interface to scan and analyze logs from:

- 🪟 **Windows Event Logs**
- 🌐 **Apache Access Logs**
- 📡 **Syslog**

Built for security analysts, developers, and sysadmins looking for a quick and intuitive way to detect unusual events in log data.

<br>

---

<br>

## 📦 Features

- 🧠 **Anomaly Detection** (basic keyword + pattern-based detection)
- 🖼️ **GUI Interface** (built with Tkinter for ease of use)
- 📁 Drag-and-drop or select log files manually
- 🚨 Instant view of suspicious entries
- 🪶 Lightweight and easy to modify or extend

<br>

---

<br>

## 🛠 Installation

### ✅ Requirements
- Python 3.8+
- Works on Windows, macOS, and Linux

<br>

### 📥 Clone or Download

```
git clone https://github.com/Aadil-Faheem/LogSentry.git
cd LogSentry
```

<br>

📦 Install dependencies (optional)
```
pip install -r requirements.txt
```
Note: LogSentry uses mostly built-in modules.

<br>

🚀 Usage
Run the main script:

```
python logsentry/LogSentry_GUI.py
```
Then:

Click Browse Log to open a file

Select log type (Apache, Syslog, Windows Events)

Click Scan to analyze the file

⚠️ Note on Anomaly Detection
This version uses basic heuristics such as:
- Excessive HTTP error codes
- Failed logins or suspicious keywords (e.g., unauthorized, root, failed)
- Repeated access from the same IP

<br>

📦 Packaging to EXE (Optional)
If you want a standalone .exe:

```
pip install pyinstaller
pyinstaller --onefile logsentry/LogSentry_GUI.py
```
Output will be found in the /dist folder.

<br>



🧑‍💻 Author <br>
Aadil Faheem <br> 
🔗 https://aadilfaheem.framer.website  <br>
🐙 @Aadil-Faheem <br>

<br> 

📜 License
MIT License – use it freely and safely.
