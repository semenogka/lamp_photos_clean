from helper import resource_path
import torch
import os
import requests
import io
_cache = {}



def load_cache(buttons_files):
    global _cache
    for category in buttons_files:
      filename = os.path.basename(buttons_files[category])
      raw_url = f"https://raw.githubusercontent.com/semenogka/lamp_photos/main/cache/{filename}"
      print(f"Загрузка: {category}")
      res = requests.get(raw_url)
      try:
            buffer = io.BytesIO(res.content)
            entry = torch.load(buffer, map_location="cpu")
            _cache[category] = entry
      except Exception as e:
            print(f"[!] Ошибка torch.load({category}): {e}")
            continue

    return _cache