import os
import sys
from dotenv import find_dotenv, load_dotenv
import panel as pn

pn.extension()

class Utils:
    def __init__(self):
        _ = load_dotenv(find_dotenv())

    def get_dlai_api_key(self):
        return os.getenv("DLAI_API_KEY")
    
    def get_dlai_url(self):
        return os.getenv("DLAI_API_URL")

class upld_file:
    def __init__(self, upload_dir):
        self.widget_file_upload = pn.widgets.FileInput(accept=".pdf,.ppt,.png,.html", multiple=False)
        self.widget_file_upload.param.watch(self.save_filename, "filename")
        self.upload_dir = upload_dir

    def save_filename(self, _):
        if len(self.widget_file_upload.value) > 2e6:
            print("file too large. 2 M limit")
        else:
            # self.widget_file_upload.save("./data/Lesson_2/example_files/" + self.widget_file_upload.filename)
            self.widget_file_upload.save(os.path.join(self.upload_dir, self.widget_file_upload.filename))
