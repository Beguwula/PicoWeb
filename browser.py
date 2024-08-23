import network
import socket
from time import sleep
import machine
import os
import urequests
import re
def connect(ssid, password):
    if password is None:
        connect_no_pass(ssid)
    else:
        connect_pass(ssid, password)
def connect_no_pass(ssid):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    print(wlan.ifconfig())
def connect_pass(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    print(wlan.ifconfig())
def load_page(url):
    response = urequests.get(url)
    if response.status_code == 200:
        print(f"Loaded {url}")
        sleep(1)
        print(parse(response.text))
    else:
        print(f"Error loading {url}")
def download(url, filename):
    path = filename
    response = urequests.get(url)
    if response.status_code == 200:
        with open(path, 'wb') as f:
            f.write(response.content)
        print(f"File saved as {path}")
    else:
        print(f"Error downloading file from {url}")
def parse(html_text):
    # Convert <br> to newline
    clean_text = html_text.replace('<br>', '\n')
    # Remove everything inside <>
    clean_text = re.sub(r'<.*?>', '', clean_text)
    return clean_text
