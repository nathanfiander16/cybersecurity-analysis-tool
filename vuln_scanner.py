import os

def check_file_permissions(filepath):
    """Checks if sensitive files are world-writable."""
    if os.path.exists(filepath):
        mode = os.stat(filepath).st_mode
        if mode & 0o002:
            print(f"[VULNERABILITY DETECTED] {filepath} is world-writable!")
        else:
            print(f"[OK] {filepath} permissions are secure.")
    else:
        print(f"[INFO] File {filepath} not found.")

if __name__ == "__main__":
    check_file_permissions("/etc/passwd")
