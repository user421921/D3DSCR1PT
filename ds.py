#!/bin/python3
#authors user421921, d3dm4n
# hack the world
# todo:
from os import system as c
from time import sleep
def startup():
    frames = ["establishing uplink", "establishing uplink.", "establishing uplink..", "establishing uplink..."]
    for frame in frames:
        # clear screen
        #c("cls" if os.name == "nt" else "clear")
        c("clear")
        print(frame)
        sleep(1)
  c("timg -C -t25 v3.mp4")


def menu():
  print(""" ---menu---
  1. Search for (C)ameras
  2. Generate (I)dentity
  3. (J)am comms
  4. (G)reenlight
  5. Loop (A)nimation
  6. (T)arget Identity
  """)
  
def help():
  print("""
  1. Search for (C)ameras - scans local network for unencrypted camera frames.
  2. Generate (I)dentity - generates Fake Idendity for Privacy
  3. (J)am comms - Jams local WiFi, Bluetooth, and Radio Comms
  4. (G)reenlight - Triggers Green Light on traffic nearby traffic lights
  5. Loop (A)nimation - Shows a looped WD themed animation
  6. (T)arget Identity - Takes information about identity and sends a mass attack.
  """)
def main():
  startup()
  
  

