
import darkdetect
import pywinstyles
import sys
import sv_ttk
import tkinter
from tkinter import ttk
from pytube import YouTube

class GUI:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("400x280")
        self.tab_parent = ttk.Notebook(self.root)

        self.tab1 = ttk.Frame(self.tab_parent)
        self.tab2 = ttk.Frame(self.tab_parent)
        self.tab3 = ttk.Frame(self.tab_parent)

        label1 = ttk.Label(self.tab1, text = "Youtube Video URL:")
        entry1 = ttk.Entry(self.tab1)
        button1 = ttk.Button(self.tab1, text="Convert")
        
        label1.grid(row=0, column=1, padx=15, pady=15)
        entry1.grid(row=1, column=1, padx=15, pady=15)
        button1.grid(row=2, column=1, padx=15, pady=15)

        label2 = ttk.Label(self.tab2, text = "Youtube Video URL:")
        entry2 = ttk.Entry(self.tab2)
        button2 = ttk.Button(self.tab2, text="Convert")
        
        label2.grid(row=0, column=1, padx=15, pady=15)
        entry2.grid(row=1, column=1, padx=15, pady=15)
        button2.grid(row=2, column=1, padx=15, pady=15)

        label3 = ttk.Label(self.tab3, text = "Spotify URL:")
        entry3 = ttk.Entry(self.tab3)
        button3 = ttk.Button(self.tab3, text="Convert")
        
        label3.grid(row=0, column=1, padx=15, pady=15)
        entry3.grid(row=1, column=1, padx=15, pady=15)
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

    # def yt_to_mp4(self):
    #     yt = YouTube.


if __name__ == "__main__":
    
    window = GUI()

    if "win" in sys.platform:
        window.set_theme()

    window.root.mainloop()