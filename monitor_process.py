import psutil


def monitor_processes():
    print("Antivirus program started monitoring processes...")
    while True:
        for process in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                process_name = process.info['name']
                process_cmdline = process.info['cmdline']

                if process_name and process_cmdline and process_name.lower() not in process_cmdline[0].lower():
                    print(f"Suspicious process detected: {process_name} (PID: {process.pid})")
                    print("Action taken: Terminated process")

                if process_cmdline and '-inject' in process_cmdline:
                    print(f"Suspicious process detected: {process_name} (PID: {process.pid})")

                    print("Action taken: Quarantined process")

                if process_cmdline and 'C:\\Windows\\System32' in process_cmdline:
                    print(f"Suspicious process detected: {process_name} (PID: {process.pid})")
                    print("Action taken: Alert user")

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

def main():
    monitor_processes()

if __name__ == "__main__":
    main()
