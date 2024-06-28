import tkinter
import customtkinter as ctk
from pytube import YouTube

def download():
    try:
        ytLink=link.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()
        video.download(output_path='C:\\Users\\bmano\\Downloads')
        print("Downloaded")
    except:
       print("Invalid Link")


#System settings
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

#Our app frame
app = ctk.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

#Adding UI element
title = ctk.CTkLabel(app, text="Insert a Youtube Link")
title.pack(padx=10, pady=10)

#Link Entry
url_var = tkinter.StringVar()
link = ctk.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

#Download Button
download = ctk.CTkButton(app, text="Download", command=download)
download.pack(padx=10, pady=10)

#Run app
app.mainloop()