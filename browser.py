import network
import socket
from time import sleep
import machine
import os
import urequests
def connect(ssid, password):
    use_pass = input("Use password for connecting [Y/n]? ")
    if use_pass == "Y" or use_pass == "n":
        connect_pass(ssid, password)
    elif use_pass == "N" or use_pass == "n":
        connect_no_pass(ssid)
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
        print(response.text)
        print(f"Loaded {url}")
    else:
        print(f"Error loading {url}")
