
import darkdetect
import moviepy.editor as mpe
import os
import pywinstyles
import re
import subprocess
import sv_ttk
import sys
from tkinter import ttk, Tk
from pytubefix import YouTube


class GUI:
    def __init__(self):
        # Initialize main window and tabs
        self.root = Tk()
        self.root.geometry("400x280")
        self.root.title("Youtube And Spotify Converter")
        self.tab_parent = ttk.Notebook(self.root)

        self.tab1 = ttk.Frame(self.tab_parent)  # Youtube to MP4
        self.tab2 = ttk.Frame(self.tab_parent)  # Youtube to MP3
        self.tab3 = ttk.Frame(self.tab_parent)  # Spotify to MP3

        self.tab1.columnconfigure(0, weight=1)
        self.tab2.columnconfigure(0, weight=1)
        self.tab3.columnconfigure(0, weight=1)

        # Tab 1: Youtube to MP4
        label1 = ttk.Label(self.tab1, text="Youtube Video URL:")
        self.entry1 = ttk.Entry(self.tab1)
        self.combobox = ttk.Combobox(
            self.tab1,
            state="readonly",
            values=["2160p", "1440p", "1080p", "720p", "480p", "360p", "240p", "144p"]
        )
        button1 = ttk.Button(self.tab1, text="Convert", command=self.yt_to_mp4)

        label1.grid(row=0, column=0, padx=15, pady=10)
        self.entry1.grid(row=1, column=0, padx=15, pady=10)
        self.combobox.grid(row=2, column=0, padx=15, pady=10)
        button1.grid(row=3, column=0, padx=15, pady=10)

        self.progress_bar = ttk.Progressbar(self.tab1, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.grid(row=4, column=0, padx=15, pady=10)

        # Tab 2: Youtube to MP3
        label2 = ttk.Label(self.tab2, text="Youtube Video URL:")
        self.entry2 = ttk.Entry(self.tab2)
        button2 = ttk.Button(self.tab2, text="Convert", command=self.yt_to_mp3)

        label2.grid(row=0, column=0, padx=15, pady=10)
        self.entry2.grid(row=1, column=0, padx=15, pady=10)
        button2.grid(row=2, column=0, padx=15, pady=10)

        # Tab 3: Spotify to MP3
        label3 = ttk.Label(self.tab3, text="Spotify URL:")
        self.entry3 = ttk.Entry(self.tab3)
        button3 = ttk.Button(self.tab3, text="Convert", command=self.spotify_to_mp3)

        label3.grid(row=0, column=0, padx=15, pady=10)
        self.entry3.grid(row=1, column=0, padx=15, pady=10)
        button3.grid(row=2, column=0, padx=15, pady=10)

        self.tab_parent.add(self.tab1, text="Youtube to MP4")
        self.tab_parent.add(self.tab2, text="Youtube to MP3")
        self.tab_parent.add(self.tab3, text="Spotify to MP3")
        self.tab_parent.pack(expand=1, fill="both")

    def set_theme(self):
        # Set theme based on OS version and mode
        version = sys.getwindowsversion()
        sv_ttk.set_theme(darkdetect.theme())

        if version.major == 10 and version.build >= 22000:
            pywinstyles.change_header_color(
                self.root,
                "#1c1c1c" if sv_ttk.get_theme() == "dark" else "#fafafa"
            )
        elif version.major == 10:
            pywinstyles.apply_style(
                self.root,
                "dark" if sv_ttk.get_theme() == "dark" else "normal"
            )
            self.root.wm_attributes("-alpha", 0.99)
            self.root.wm_attributes("-alpha", 1)

    def sanitize_filename(self, title):
        # Remove illegal characters from filename
        return re.sub(r'[\\/*?:"<>|]', "", title)
    
    def progress_function(self, stream, chunk, bytes_remaining):
        # Sets progress bar to match progress of the pytube download
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage = (bytes_downloaded / total_size) * 100
        self.progress_bar["value"] = percentage
        self.root.update_idletasks()

    def yt_to_mp4(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))

        video = YouTube(self.entry1.get(), on_progress_callback=self.progress_function)
        video_title = self.sanitize_filename(video.title)

        # Try to get the matched resolution. If not available get the highest.
        try:
            stream = video.streams.filter(adaptive=True, res=self.combobox.get()).first()
        except:
            stream = video.streams.filter(adaptive=True).order_by("resolution").last()

        # # Download temporary audio and video files whilst updating the progress bar
        self.progress_bar["value"] = 0
        stream.download(filename=f"{video_title}-temp.mp4", output_path=f"{dir_path}/yt-mp4")
        self.progress_bar["value"] = 0
        stream_audio = video.streams.get_audio_only()
        stream_audio.download(filename=f"{video_title}-temp.mp3", output_path=f"{dir_path}/yt-mp3")

        # Use moviepy to combine the audio and video files.
        videoFile = mpe.VideoFileClip(f"{dir_path}/yt-mp4/{video_title}-temp.mp4")
        audio = mpe.AudioFileClip(f"{dir_path}/yt-mp3/{video_title}-temp.mp3")
        final_video = videoFile.set_audio(audio)
        final_video.write_videofile(f"{dir_path}/yt-mp4/{video_title}.mp4")

        # Remove temp files once complete
        os.remove(f"{dir_path}/yt-mp4/{video_title}-temp.mp4")
        os.remove(f"{dir_path}/yt-mp3/{video_title}-temp.mp3")

        self.progress_bar["value"] = 0

    def yt_to_mp3(self):
        # Download youtube video as mp3
        dir_path = os.path.dirname(os.path.realpath(__file__))
        video = YouTube(self.entry2.get())
        stream = video.streams.get_audio_only()
        stream.download(filename=f"{video.title}.mp3", output_path=f"{dir_path}/yt-mp3")

    def spotify_to_mp3(self):
        # Download spotify song via spotdl command line command
        try:
            os.makedirs("spot-mp3")
        except:
            pass

        command = ["spotdl", "download", self.entry3.get()]
        os.chdir("spot-mp3")
        p = subprocess.Popen(command)
        p.wait()



if __name__ == "__main__":
    
    window = GUI()

    if "win" in sys.platform:
        window.set_theme()

    window.root.mainloop()