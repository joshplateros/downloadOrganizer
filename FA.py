import os
import json
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
class MyHandler(FileSystemEventHandler):
    def on_modified(self,event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            if (filename.endswith('.txt')):
                folder_destination = "/mnt/d/Josh/Documents/textFiles/"
            elif (filename.endswith('.png') or filename.endswith('.jpg')):
                folder_destination = "/mnt/d/Josh/Documents/pictureFiles/"
            elif (filename.endswith('.zip')):
                folder_destination = "/mnt/d/Josh/Documents/zipFiles/"
            elif (filename.endswith('.pdf')):
                folder_destination = "/mnt/d/Josh/Documents/pdfFiles/"
            elif (filename.endswith('.exe')):
                folder_destination = "/mnt/d/Josh/Documents/applicationFiles/"
            elif (filename.endswith('.docx')):
                folder_destination = "/mnt/d/Josh/Documents/docFiles/"
            elif (filename.endswith('.ppt') or filename.endswith('.pptx')):
                folder_destination = "/mnt/d/Josh/Documents/pptFiles/"
            elif (filename.endswith('.mp3') or filename.endswith('.mp4')):
                folder_destination = "/mnt/d/Josh/Documents/mediaFiles/"
            else:
                folder_destination = "/mnt/d/Josh/Documents/miscFiles/"
            new_destination = folder_destination + "/" + filename
            os.rename(src, new_destination)

folder_to_track = "/mnt/d/Josh/Documents/organize/"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
