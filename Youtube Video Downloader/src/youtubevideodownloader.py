import tkinter as tk
from pytube import YouTube

#Definition
def youtube_find():
    try:
        get_text = link.get()
        youtube = YouTube(get_text)
        video_title = youtube.title
        video_length = youtube.length
        length_in_minutes = video_length / 60

        #Video Title in GUI
        title = tk.Label(
            text= video_title + "     " + str(length_in_minutes) + " Mins",
            foreground="white",  # Set the text color to white
            background="black",  # Set the background color to black
            font=("Callibri", 15),
            width=50,
        ).grid(
            row=3,
            column=0,
            columnspan=2,
        )

    except:
        error = tk.Label(
            text= "Error! Try Again!",
            foreground="red",  # Set the text color to white
            background="black",  # Set the background color to black
            font=("Callibri", 15),
            width=50,
        ).grid(
            row=3,
            column=0,
            columnspan=2,
        )

def youtube_download():
    try:
        get_text = link.get()
        youtube = YouTube(get_text)
        video = youtube.streams.get_highest_resolution()
        video.download()
        success = tk.Label(
            text= "DONE!!",
            foreground="green",  # Set the text color to white
            background="black",  # Set the background color to black
            font=("Callibri", 15),
        ).grid(
            row=6,
            column=0,
            columnspan=2,
        )
    except:
        error = tk.Label(
            text= "Error! Try Again!",
            foreground="red",  # Set the text color to white
            background="black",  # Set the background color to black
            font=("Callibri", 15),
        ).grid(
            row=6,
            column=0,
            columnspan=2,
        )

#GUI
window = tk.Tk()
window.title("Youtube Video Downloader")
window.configure(bg="black")
window.resizable(0, 0)

#Title
label = tk.Label(
    text="Hi There!",
    foreground="white",  # Set the text color to white
    background="black",  # Set the background color to black
    font=("Callibri", 35),
    width=25,
).grid(
    row=1,
    column=0,
    columnspan=2,
)
description = tk.Label(
    text="Type in the URL of the Youtube Video Here:\n*Insert Clown Face!*",
    foreground="white",  # Set the text color to white
    background="black",  # Set the background color to black
    font=("Arial", 10),
).grid(
    row=2,
    column=0,
    columnspan=2,
)

#URL Box
link = tk.Entry(
    text="Type in the URL of the Youtube Video Here:\n*Insert Clown Face!*",
    foreground="black",
    background="white",
    font=("Arial", 10),
    width="35"
)
link.grid(
    row=4,
    column=0,
)

#Find Button
find_button = tk.Button(
    text="Find Video!",
    foreground="black",
    background="white",
    font=("Arial", 10),
    activebackground="grey",
    height="2",
    command= youtube_find
).grid(
    row=4,
    column=1,
)

#Download Button
download_button = tk.Button(
    text="Download!",
    foreground="black",
    background="white",
    font=("Arial", 10),
    activebackground="grey",
    height="2",
    width= "50",
    command= youtube_download,
).grid(
    row=5,
    column=0,
    pady= 10,
    columnspan=2,
)
window.mainloop()