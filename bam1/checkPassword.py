import requests

PASSWORD_URL = "https://gist.githubusercontent.com/semenogka/5cfbb5f09528f83361ef7de0c6c1ad19/raw/ca5004e16e83e037010f9c2d04ab32e774635a78/gistfile1.txt"

def get_password_from_gist():
    try:
        resp = requests.get(PASSWORD_URL, timeout=5)
        if resp.status_code == 200:
            return resp.text.strip()
    except requests.RequestException:
        print("⚠️ Не удалось получить пароль с сервера.")
    return None

def check_password():
    real_password = get_password_from_gist()
    if not real_password:
        return False

    user_input = input("Введите пароль: ").strip()
    if user_input == real_password:
        return True
    else:
        return False