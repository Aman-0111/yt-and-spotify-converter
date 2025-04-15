# Youtube and Spotify Converter

This is a simple desktop application that converts YouTube videos to either MP4 (with audio) or MP3 and also converts Spotify tracks to MP3 using the command-line tool [spotdl](https://github.com/spotDL/spotify-downloader). The program utilizes a simple Tkinter-based GUI to input URLs and select desired output options.

## Features

- **YouTube to MP4:**  
  Downloads a YouTube video’s selected resolution and its audio stream separately, then merges them into a final MP4 file.

- **YouTube to MP3:**  
  Downloads only the audio stream from a YouTube video and saves it as an MP3.

- **Spotify to MP3:**  
  Downloads audio from a Spotify URL using `spotdl`.

## Prerequisites

Make sure the following prerequisites are met before running the program:

- **Python 3.7+** – This program is written in Python.
- **FFmpeg** – Required by `moviepy` and `spotdl` for processing audio and video.  
  - **Windows:** Download from the [official website](https://ffmpeg.org/download.html), install via [Chocolatey](https://chocolatey.org/) with `choco install ffmpeg` or `spotdl --download-ffmpeg`.(Note, I am unsure if using spotDL will meet the requirements for moviepy, and this must be done after the requirements.txt is installed if spotDL is not already installed.)
  - **macOS:** Install using Homebrew: `brew install ffmpeg`.
  - **Linux:** Use your package manager, e.g., `sudo apt-get install ffmpeg`.

## Installation

1. **Clone the repository** (if applicable):

   ```bash
   git clone https://github.com/Aman-0111/yt-and-spotify-converter.git
   cd yt-and-spotify-converter
   ```

2. **Create a Virtual Environment (optional but recommended):**

   - **Using CMD on Windows:**
   
     ```cmd
     python -m venv venv
     venv\Scripts\activate.bat
     ```
   
   - **Using PowerShell on Windows:**
     
     If you encounter an execution policy error, run:
     
     ```powershell
     Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
     ```
     
     Then, create and activate the virtual environment:
     
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   
   - **On macOS or Linux:**
   
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install the Required Packages:**

   A minimal `requirements.txt` is provided containing only the dependencies needed to run the application:

   ```txt
   darkdetect==0.8.0
   moviepy==1.0.3
   pywinstyles==1.8
   sv-ttk==2.6.0
   pytubefix==8.12.3
   spotdl==4.2.11
   ```

   Install the dependencies with:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Application:**

   Open your terminal or command prompt and run:

   ```bash
   python main.py
   ```

2. **Using the GUI:**

   - **Youtube to MP4 Tab:**  
     Enter the YouTube video URL, select your desired resolution from the dropdown, and click **Convert**. The video and audio streams will be merged into a final MP4 file.

   - **Youtube to MP3 Tab:**  
     Enter the YouTube video URL and click **Convert** to download the audio as an MP3 file.

   - **Spotify to MP3 Tab:**  
     Enter the Spotify track URL and click **Convert**. The application will use `spotdl` to download the track as an MP3.

## Theme and Compatibility

- The GUI uses `sv-ttk` and `pywinstyles` to automatically adjust the interface based on your system’s dark/light mode.
- Theme settings are applied automatically on Windows systems.

## Troubleshooting

- **FFmpeg Issues:**  
  If you encounter errors related to FFmpeg, ensure it is installed and properly added to your system's PATH.

- **URL Errors:**  
  Verify that you are entering valid YouTube or Spotify URLs.
