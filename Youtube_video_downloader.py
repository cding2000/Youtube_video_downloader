from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path, resolution_choice=None):
    try:
        yt = YouTube(url)
        
        # Display available resolutions
        print("Available Resolutions:")
        for stream in yt.streams.filter(progressive=True, file_extension="mp4"):
            print(f"{stream.resolution} - {stream.mime_type}")

        if resolution_choice:
            # Download the specified resolution
            selected_stream = yt.streams.filter(res=resolution_choice).first()
            selected_stream.download(output_path=save_path)
            print(f"Video downloaded successfully in {resolution_choice} resolution!")
        else:
            # Let the user choose resolution
            resolution_choice = input("Enter the desired resolution (e.g., '720p'): ")
            selected_stream = yt.streams.filter(res=resolution_choice).first()
            selected_stream.download(output_path=save_path)
            print(f"Video downloaded successfully in {resolution_choice} resolution!")

    except Exception as e:
        print(e)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please enter a YouTube url: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Started download...")
        download_video(video_url, save_dir)
    else:
        print("Invalid save location.")
