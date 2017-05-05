import socket
import RPi.GPIO as GPIO
import sys
import Read
UDP_IP = "192.168.1.104"
UDP_Port = 5028
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
while True:
	try:
			MESSAGE=Read.reading_rfid()
		  print(MESSAGE)
		  sock.sendto(str(MESSAGE), (UDP_IP, UDP_Port))
		  print("data sent")
	except KeyboardInterrupt:
		  try:
         print(" the final block")
			   sock.shutdown(1)	
			   sock.close()
		  finally:
			   sys.exit()
