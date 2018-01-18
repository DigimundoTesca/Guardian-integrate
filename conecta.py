import socket
import time
import prueba
import process 

process.call('sudo rfcomm connect hci0 00:25:BF:F0:33:EF 1', shell=Ture)

def verificar():
  conection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

  try:
      conection.connect(('www.google.com', 80))
      print ("conexión establecida")
      prueba.saluda()

  except:
      print ("sin conexión")
while True:
  time.sleep(3)
  verificar()
