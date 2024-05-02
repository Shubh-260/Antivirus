import fnmatch
import os
import shutil
import ctypes
import win32con
import win32file
import win32api

blacklist = [
    "malicious.exe", "virus.txt", "virus.scr", "virus.vbs", "virus.exe", "Worm.pif", "Worm.hta", "Worm.cpl", "trojan.txt", "trojan.exe", ".adware", ".adware.exe", ".spy", ".spy.exe", ".rar", ".zip", ".crypt"]


def is_blacklisted(file_name):
    for pattern in blacklist:
        if fnmatch.fnmatch(file_name, pattern):
            return True
    return False

def file_operation_callback(operation, src_path, dst_path):
    if operation in (win32file.FILE_ACTION_ADDED, win32file.FILE_ACTION_RENAMED_NEW_NAME):
        if is_blacklisted(os.path.basename(src_path)):
            print(f"Blocked access to blacklisted file: {src_path}")
            try:
                os.remove(src_path)
                print("File deleted.")
            except Exception as e:
                print(f"Error deleting file: {e}")

def register_file_operation_callback():
    pid = os.getpid()

    handle = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, False, pid)

    win32file.ReadDirectoryChangesW(
        handle,
        os.getcwd(),
        True,
        win32con.FILE_NOTIFY_CHANGE_FILE_NAME,
        file_operation_callback,
    )

def main():
    print("Antivirus program started.")
    print("Monitoring file operations...")
    register_file_operation_callback()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Antivirus program stopped.")

if __name__ == "__main__":
    main()
