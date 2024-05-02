import tkinter as tk
from tkinter import filedialog
import os
import events
import hash
import signature
import name
import monitor_process

class AntivirusUI:
    def __init__(self, master):
        self.master = master
        master.title("Antivirus Program")

        self.directory_label = tk.Label(master, text="Select Directory:")
        self.directory_label.grid(row=0, column=0)

        self.directory_entry = tk.Entry(master, width=50)
        self.directory_entry.grid(row=0, column=1)

        self.browse_button = tk.Button(master, text="Browse", command=self.browse_directory)
        self.browse_button.grid(row=0, column=2)

        self.scan_button = tk.Button(master, text="Scan", command=self.scan_directory)
        self.scan_button.grid(row=1, column=1)

        self.result_text = tk.Text(master, height=10, width=50)
        self.result_text.grid(row=2, columnspan=3)

    def browse_directory(self):
        directory = filedialog.askdirectory()
        self.directory_entry.delete(0, tk.END)
        self.directory_entry.insert(tk.END, directory)

    def scan_directory(self):
        directory = self.directory_entry.get()
        if directory:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Scanning directory...\n")
            self.scan(directory)

    def scan(self, directory):
        self.scan_events(directory)
        self.scan_hash(directory)
        self.scan_signature(directory)
        self.scan_name(directory)
        self.scan_process()

    def scan_events(self, directory):
        self.result_text.insert(tk.END, "Scanning events...\n")
        events.monitor_directory(directory)

    def scan_hash(self, directory):
        self.result_text.insert(tk.END, "Scanning hash...\n")
        file_hashes = hash.traverse_filesystem(directory)
        known_hashes = {'c4ca4238a0b923820dcc509a6f75849b', '72fe869aa394ef0a62bb8324857770dd', ...}  # Add your known hashes here
        hash.compare_hashes(file_hashes, known_hashes)

    def scan_signature(self, directory):
        self.result_text.insert(tk.END, "Scanning signature...\n")
        signature.scan_directory(directory)

    def scan_name(self, directory):
        self.result_text.insert(tk.END, "Scanning names...\n")
        name.scan_directory(directory)

    def scan_process(self):
        self.result_text.insert(tk.END, "Scanning processes...\n")
        monitor_process.monitor_processes()

root = tk.Tk()
antivirus_ui = AntivirusUI(root)
root.mainloop()
