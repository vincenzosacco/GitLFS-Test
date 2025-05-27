"""
Display a simple video player interface, just a demo to check if large media files can be played 
using GitLFS tracking.
"""

import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

class SimpleVideoPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Video Player - Git LFS Demo")
        self.root.geometry("800x600")
        
        # Create a frame for the video display area (placeholder)
        self.video_frame = tk.Frame(self.root, bg="black", width=780, height=440)
        self.video_frame.pack(pady=10, padx=10)
        self.video_frame.pack_propagate(False)
        
        # Display placeholder text
        self.placeholder = tk.Label(self.video_frame, text="Select a video file to play", 
                                    fg="white", bg="black", font=("Arial", 14))
        self.placeholder.pack(expand=True)
        
        # Create control buttons
        self.control_frame = tk.Frame(self.root)
        self.control_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.open_btn = tk.Button(self.control_frame, text="Open Video File", 
                                  command=self.open_file, height=2, width=15)
        self.open_btn.pack(side=tk.LEFT, padx=5)
        
        self.play_btn = tk.Button(self.control_frame, text="Play", 
                                 command=self.play_video, height=2, width=10)
        self.play_btn.pack(side=tk.LEFT, padx=5)
        
        self.exit_btn = tk.Button(self.control_frame, text="Exit", 
                                 command=self.root.destroy, height=2, width=10)
        self.exit_btn.pack(side=tk.RIGHT, padx=5)
        
        # Status bar
        self.status = tk.Label(self.root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Current video path
        self.video_path = None
        self.process = None
        
        # Check for command line arguments (video file path)
        if len(sys.argv) > 1 and os.path.isfile(sys.argv[1]):
            self.video_path = sys.argv[1]
            self.play_video()

    def open_file(self):
        """Open a file dialog to select a video file"""
        filetypes = [
            ("Video files", "*.mp4 *.avi *.mov *.mkv *.wmv"),
            ("All files", "*.*")
        ]
        
        filepath = filedialog.askopenfilename(
            title="Select a video file",
            filetypes=filetypes
        )
        
        if filepath:
            self.video_path = filepath
            self.status.config(text=f"Selected: {os.path.basename(filepath)}")
            self.placeholder.config(text=f"Ready to play:\n{os.path.basename(filepath)}")

    def play_video(self):
        """Play the selected video file using the system's default player"""
        if not self.video_path:
            messagebox.showinfo("No File Selected", "Please select a video file first.")
            return
            
        try:
            # Display information in our window
            self.placeholder.config(text=f"Playing: {os.path.basename(self.video_path)}")
            self.status.config(text=f"Playing: {os.path.basename(self.video_path)}")
            
            # Use the system's default video player to play the file
            if sys.platform.startswith('win'):
                os.startfile(self.video_path)
            elif sys.platform.startswith('darwin'):  # macOS
                self.process = subprocess.Popen(['open', self.video_path])
            else:  # Linux and other Unix-like
                self.process = subprocess.Popen(['xdg-open', self.video_path])
                
            messagebox.showinfo("Playing Video", 
                               f"Now playing {os.path.basename(self.video_path)} in your default video player.\n\n"
                               f"This demonstrates that Git LFS is correctly tracking and retrieving the large video file.")
                
        except Exception as e:
            messagebox.showerror("Error", f"Could not play the video: {str(e)}")
            self.status.config(text="Error playing video")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleVideoPlayer(root)
    root.mainloop()