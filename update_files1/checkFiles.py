import os
import requests
import hashlib
import sys
def file_sha256(path):
    if not os.path.exists(path):
        return None
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()
    
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


# def get_cache(buttons_files):
#     os.makedirs(resource_path("cache"), exist_ok=True) 

#     for file in buttons_files:
#         filename = os.path.basename(buttons_files[file])
#         raw_url = f"https://raw.githubusercontent.com/semenogka/lamp_photos/main/cache/{filename}"

#         print(f"Загрузка: {file}")
#         res = requests.get(raw_url)
#         if res.status_code == 200:
#             local_path = resource_path(os.path.join("cache", filename))
#             remote_hash = hashlib.sha256(res.content).hexdigest()
#             local_hash = file_sha256(local_path)
#             if local_hash != remote_hash or not os.path.exists(local_path):
#               with open(local_path, "wb") as f:
#                 f.write(res.content)
#         else:
#             print(f"Ошибка загрузки {file}: HTTP {res.status_code}")

def get_dicts(filters):
   for fil in filters:
      raw = f"https://raw.githubusercontent.com/semenogka/lamp_photos/main/dictsJson/{os.path.basename(fil)}"
      res = requests.get(raw)
      if res.status_code == 200:
          remote_hash = hashlib.sha256(res.content).hexdigest()
          local_hash = file_sha256(fil)
          if remote_hash != local_hash or not os.path.exists(fil):
            with open(fil, "wb") as f:
              f.write(res.content)

def get_bam(bam_files):
   for bam in bam_files:
      raw = f"https://raw.githubusercontent.com/semenogka/lamp_photos/main/bam/{os.path.basename(bam)}"
      res = requests.get(raw)
      if res.status_code == 200:
          remote_hash = hashlib.sha256(res.content).hexdigest()
          local_hash = file_sha256(bam)
          if remote_hash != local_hash or not os.path.exists(bam):
            os.makedirs(os.path.dirname(bam), exist_ok=True)
            with open(bam, "wb") as f:
              f.write(res.content)