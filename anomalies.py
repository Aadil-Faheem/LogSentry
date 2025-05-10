
from collections import Counter

def detect_anomalies(log_entries):
    messages = [entry['message'] for entry in log_entries]
    counts = Counter(messages)
    threshold = 1

    anomalies = [msg for msg, count in counts.items() if count <= threshold]
    return anomalies
