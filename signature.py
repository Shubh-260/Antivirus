import os
import re
import time

malicious_signatures = [
    r"malware_signature1",
    r"malware_signature2",
    # I DON'T HAVE ANY SUCH FILE SO I AM NOT ABLE TO UPLAOD ANY DATA HERE
]

def scan_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
            for signature in malicious_signatures:
                if re.search(signature, content):
                    return True
    except Exception as e:
        print(f"Error scanning file {file_path}: {e}")
    return False

def monitor_file_system(directory):
    print("Antivirus program started...")
    while True:
        for root, _, files in os.walk(directory):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                if scan_file(file_path):
                    print(f"Malicious file detected: {file_path}")
                    print("Action taken: Alert user")
        time.sleep(1)


def main():
    directory_to_monitor = 'C:\\Users\\' 
    monitor_file_system(directory_to_monitor)

if __name__ == "__main__":
    main()
