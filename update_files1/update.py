import os
import requests
import hashlib
import sys
import subprocess
def file_sha256(path):
    if not os.path.exists(path):
        return None
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()
    
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
def checking():
    res = requests.get("https://raw.githubusercontent.com/semenogka/lamp_photos/main/dist/appTest/appTest.exe")
    if res.status_code == 200:
        print("проверка на наличие обновлений")
        local_path = "appTest.exe"
        remote_hash = hashlib.sha256(res.content).hexdigest()
        local_hash = file_sha256(local_path)
        if local_hash != remote_hash or not os.path.exists(local_path):
            print("новое обновление")
            with open(local_path, "wb") as f:
                f.write(res.content)
        res = requests.get("https://raw.githubusercontent.com/semenogka/lamp_photos/main/update_files/checkFiles.pyd")
        if res.status_code == 200:
            os.makedirs(resource_path("update_files"), exist_ok=True)
            with open(resource_path(os.path.join("update_files", "checkFiles.pyd")), "wb") as f:
                f.write(res.content)



    subprocess.Popen("appTest.exe")