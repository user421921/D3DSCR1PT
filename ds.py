#!/bin/python3
#authors user421921, d3dm4n
# hack the world
# todo:
from os import system as c
import sleep
import scapy
def startup():
  print("establishing uplink")
  sleep(1)
  print(".")
  sleep(1)
  c("timg -C -t25 v3.mp4")
def menu():
  print(""" ---menu---
  1. Search for Cameras
  2. Generate Identity
  3. Jam comms
  4. Greenlight
  5. Phone
  6. 

        """)
def main():
  startup()
  
  
