import re

def analyze_logs(log_file):
    failed_logins = {}
    with open(log_file, 'r') as file:
        for line in file:
            if "Failed password" in line:
                ip = re.search(r'\d+\.\d+\.\d+\.\d+', line)
                if ip:
                    ip_address = ip.group()
                    failed_logins[ip_address] = failed_logins.get(ip_address, 0) + 1

    print("=== Security Alert: Failed Login Attempts ===")
    for ip, count in failed_logins.items():
        if count >= 3:
            print(f"[ALERT] Suspicious activity from {ip}: {count} failed attempts")

if __name__ == "__main__":
    # Example log testing
    analyze_logs("sample_auth.log")
