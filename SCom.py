#!/usr/bin/python
import time
import serial
from report import *

DOC= open('MSG.txt','a')
aux = ""
trigger = False
value = ""
tuples = []
print "Starting program..."

ser = serial.Serial('/dev/ttyUSB0', baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                    )  ##Modulo USB-TTL
##ser = serial.Serial('/dev/rfcomm0', baudrate=115200,
##                    parity=serial.PARITY_NONE,
##                    stopbits=serial.STOPBITS_ONE,
##                    bytesize=serial.EIGHTBITS
##                    )
##Para conectar ejecutar comando> sudo rfcomm connect hci0 98:D3:32:10:D0:31 1


try:
##    ser.write('\nPairing Succes\r')
##    ser.write('Serial Communication Using Raspberry Pi\r')
##    ser.write('By: Mstr HCR \r')
##
##    ser.write('Digimundo Tecnologies \n')
##    ser.write('yo soy tu, :... \r\n')
    print '--------------Data Echo Mode Enabled--------------'
    while True:
        if ser.inWaiting() > 0:
            DOC=open('MSG.txt','a')
            data = ser.read()
            c = data
            ##write(data)
##            print (data),
            DOC.write(data)
            if trigger == True:
                if c == "\n" :
                    trigger = False
                    print(value)
                    tuples.append(value)
                    value=""
                elif c == "%":
                    print(value)
                    print "---------Create report"#create_report()
                    trigger = False
                    value = value + c
                    tuples.append(value)
                    #            print(value)
                    value = ""
                    create_report(tuples)
                    sendmail()
                    #sendmail()
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
         
            
##        else:
##            DOC.write('--------end of message--------\n')
##            DOC.close()
                      
    
         
    
except KeyboardInterrupt:
    print "Terminando el programa"

except:
    print "Se ha detectado un problema (...)"

finally:
    ser.close()
    DOC.close()
    pass
