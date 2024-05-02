import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

suspicious_extensions = ['.exe', '.dll', '.bat', '.ps1', '.exe', '.com''.dll','.scr','.pif','.sys','.ocx','.hlp','.cab','.chm','.ade','.adp','.tmp','.zip','.rar','.bat','.cmd','.vbs','.vbe','.js','.jse','.wsh','.msi','.cpl','.ins','.isp','.lib','.crt','.cer','.der','.p7b','.p7r','.p7s','.pem','.pfx','.p12','.p7c','.p7m','.p77','.p7x','.p10','.prf','.jks','.key','.pem','.pfx']

class FileEventHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            return

        if event.event_type in ['created', 'modified']:
            file_path = event.src_path

            _, file_extension = os.path.splitext(file_path)
            if file_extension.lower() in suspicious_extensions:
                print(f"Suspicious file event: {event.event_type} - {file_path}")
                print("Action taken: Alert user")

def monitor_directory(directory):
    event_handler = FileEventHandler()
    observer = Observer()
    observer.schedule(event_handler, directory, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

def main():
    directory_to_monitor = 'C:\\Users\\'
    print("Antivirus program started...")
    monitor_directory(directory_to_monitor)

if __name__ == "__main__":
    main()
