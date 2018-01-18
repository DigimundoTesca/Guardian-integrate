#!/usr/bin/python
import time
import serial
from report import *

DOC= open('MSG.txt','w')
aux = ""
trigger = False
value = ""
tuples = []
ticket = ""
print "Starting program..."

##ser = serial.Serial('/dev/ttyUSB0', baudrate=9600,
##                    parity=serial.PARITY_NONE,
##                    stopbits=serial.STOPBITS_ONE,
##                    bytesize=serial.EIGHTBITS
##                    )  ##Modulo USB-TTL
ser = serial.Serial('/dev/rfcomm0', baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                    )  ##Puerto Serial bluetooth [Raspberrie]
##Para conectar ejecutar comandos>
##sudo rfcomm connect hci0 98:D3:32:10:D0:31 1  [AIR Module]
##sudo rfcomm connect hci1 AC:3F:A4:14:44:78 1  [Zebra printer]

try:
##    ser.write('\nPairing Succes\r')
##    ser.write('Serial Communication Using Raspberry Pi\r')
##    ser.write('By: Mstr HCR \r')
##    ser.write('Digimundo Tecnologies \n')
##    ser.write('yo soy tu, :... \r\n')

    print '******************************Data Echo Mode Enabled*****************************'
    while True:
        if ser.inWaiting() > 0:
            data = ser.read()
            c = data
            ticket += data
            if trigger == True:
                if c == "\n" :
                    trigger = False
                    print(value)
                    tuples.append(value)
                    value=""
                elif c == "%":
                    print(value)
##                    ser.write(ticket)
                    DOC.write(ticket)
                    ticket = ""
                    trigger = False
                    value = value + c
                    tuples.append(value)
                    value = ""
                    create_report(tuples)
                    print "<---------Create report--------->[DONE]"
                    sendmail()
                    #sendmail()
##                  print "<-----------Send Email---------->[DONE]"
                else:
                    value = value+c
            elif c == " " and aux == ":":
                trigger = True
            elif c == " " and aux == "=":
                trigger = True
            elif c == "\n" and aux == ":":
                trigger = True
            elif c == "\n" and aux == " ":
                trigger = True
            aux=c                          
   
except KeyboardInterrupt:
    print "Terminando el programa"

except:
    print "Se ha detectado un problema (...)"

finally:
    ser.close()
    DOC.close()
    pass
