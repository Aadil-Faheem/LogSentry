
def parse_apache_logs(filepath):
    logs = []
    with open(filepath, 'r') as f:
        for line in f:
            parts = line.split()
            if len(parts) > 6:
                logs.append({
                    "source": "apache",
                    "message": " ".join(parts[6:]),
                })
    return logs
