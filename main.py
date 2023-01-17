import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title)
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Indi") 
    except:
        print("hay sikeym")
    
#system settings
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

#app frame
app = customtkinter.CTk()
app.geometry("720x487")
app.title("YouTube Downloader")


#ui elements
title = customtkinter.CTkLabel(app, text="URL")
title.pack(padx=10, pady=10)


#link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

##finished downladnadw
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack



#Download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)


#runwhole
app.mainloop()