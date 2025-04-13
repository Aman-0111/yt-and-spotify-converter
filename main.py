
import darkdetect
import os
import pywinstyles
import subprocess
import sv_ttk
import sys
import tkinter
from tkinter import ttk
from pytubefix import YouTube



class GUI:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("400x280")
        self.tab_parent = ttk.Notebook(self.root)

        self.tab1 = ttk.Frame(self.tab_parent)
        self.tab2 = ttk.Frame(self.tab_parent)
        self.tab3 = ttk.Frame(self.tab_parent)

        label1 = ttk.Label(self.tab1, text = "Youtube Video URL:")
        self.entry1 = ttk.Entry(self.tab1)
        button1 = ttk.Button(self.tab1, text="Convert", command=self.yt_to_mp4)
        
        label1.grid(row=0, column=1, padx=15, pady=15)
        self.entry1.grid(row=1, column=1, padx=15, pady=15)
        button1.grid(row=2, column=1, padx=15, pady=15)

        label2 = ttk.Label(self.tab2, text = "Youtube Video URL:")
        self.entry2 = ttk.Entry(self.tab2)
        button2 = ttk.Button(self.tab2, text="Convert", command=self.yt_to_mp3)
        
        label2.grid(row=0, column=1, padx=15, pady=15)
        self.entry2.grid(row=1, column=1, padx=15, pady=15)
        button2.grid(row=2, column=1, padx=15, pady=15)

        label3 = ttk.Label(self.tab3, text = "Spotify URL:")
        self.entry3 = ttk.Entry(self.tab3)
        button3 = ttk.Button(self.tab3, text="Convert", command=self.spotify_to_mp3)
        
        label3.grid(row=0, column=1, padx=15, pady=15)
        self.entry3.grid(row=1, column=1, padx=15, pady=15)
        button3.grid(row=2, column=1, padx=15, pady=15)

        self.tab_parent.add(self.tab1, text = "Youtube to MP4")
        self.tab_parent.add(self.tab2, text = "Youtube to MP3")
        self.tab_parent.add(self.tab3, text = "Spotify to MP3")
        self.tab_parent.pack( expand = 1, fill ="both")

    def set_theme(self):
        version = sys.getwindowsversion()

        sv_ttk.set_theme(darkdetect.theme())

        if version.major == 10 and version.build >= 22000:
            pywinstyles.change_header_color(self.root, "#1c1c1c" if sv_ttk.get_theme() == "dark" else "#fafafa")
        elif version.major == 10:
            pywinstyles.apply_style(self.root, "dark" if sv_ttk.get_theme() == "dark" else "normal")

            self.root.wm_attributes("-alpha", 0.99)
            self.root.wm_attributes("-alpha", 1)

    def yt_to_mp4(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        video = YouTube(self.entry1.get())
        stream = video.streams.filter(adaptive=True).order_by("resolution").last()
        stream.download(filename=f"{video.title}.mp4", output_path=f"{dir_path}/yt-mp4")

    def yt_to_mp3(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        video = YouTube(self.entry2.get())
        stream = video.streams.get_audio_only()
        stream.download(filename=f"{video.title}.mp3", output_path=f"{dir_path}/yt-mp3")

    def spotify_to_mp3(self):
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