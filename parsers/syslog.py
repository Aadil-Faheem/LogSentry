
def parse_syslog(filepath):
    logs = []
    with open(filepath, 'r') as f:
        for line in f:
            logs.append({
                "source": "syslog",
                "message": line.strip()
            })
    return logs
