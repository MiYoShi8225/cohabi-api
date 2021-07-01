# 標準ライブラリー
import os

class FileName():
    def __init__(self, file_name: str):
        self.file_name = os.path.basename(file_name.split('.')[0])
    
    def __str__(self) -> str:
        return self.file_name

    def file_name(self):
        return self.file_name
