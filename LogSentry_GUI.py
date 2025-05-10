
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk

def detect_anomalies(log_lines, log_type):
    alerts = []
    
    for line in log_lines:
        # Apache log pattern
        if log_type == "Apache":
            if " 401 " in line or " 403 " in line:
                alerts.append(f"[ALERT] Suspicious HTTP status in line:\n{line.strip()}")
        
        # Syslog pattern
        elif log_type == "Syslog":
            if "Failed password" in line or "error" in line.lower():
                alerts.append(f"[ALERT] Syslog authentication error:\n{line.strip()}")
        
        # Windows Event Log (very simplified)
        elif log_type == "Windows":
            if "EventID=4625" in line:
                alerts.append(f"[ALERT] Failed login detected:\n{line.strip()}")
            elif "EventID=1102" in line:
                alerts.append(f"[ALERT] Security log cleared!:\n{line.strip()}")

        # Fallback or unknown type
        else:
            if "error" in line.lower() or "failed" in line.lower():
                alerts.append(f"[ALERT] Possible issue:\n{line.strip()}")

    return alerts

class LogSentryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LogSentry - Log Anomaly Detector")

        self.log_type = tk.StringVar(value="Apache")

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Log Type:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        log_type_menu = ttk.OptionMenu(self.root, self.log_type, "Apache", "Apache", "Syslog", "Windows")
        log_type_menu.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        load_button = ttk.Button(self.root, text="Load Log File", command=self.load_log_file)
        load_button.grid(row=0, column=2, padx=5, pady=5)

        self.output_area = scrolledtext.ScrolledText(self.root, width=100, height=30)
        self.output_area.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    def load_log_file(self):
        filepath = filedialog.askopenfilename(title="Open Log File", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
        if not filepath:
            return

        try:
            with open(filepath, "r") as file:
                log_lines = file.readlines()
                results = detect_anomalies(log_lines, self.log_type.get())
                self.output_area.delete(1.0, tk.END)
                self.output_area.insert(tk.END, "\n\n".join(results) if results else "No anomalies detected.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read file: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LogSentryApp(root)
    root.mainloop()
