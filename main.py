
import darkdetect
import pywinstyles
import sys
import sv_ttk
import tkinter
from tkinter import ttk

class GUI:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("500x280")
        self.tab_parent = ttk.Notebook(self.root)

        self.tab1 = ttk.Frame(self.tab_parent)
        self.tab2 = ttk.Frame(self.tab_parent)
        self.tab3 = ttk.Frame(self.tab_parent)
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


if __name__ == "__main__":
    
    window = GUI()

    if "win" in sys.platform:
        window.set_theme()

    window.root.mainloop()