#coding utf-8
import serial
import subprocess
import time


def main():

    ser = serial.Serial('COM3',9600,timeout=1)

    ###################################
    cmd1 = "C:\\00_okamoto\\uwsc523\\uwsc.exe  C:\\00_okamoto\\uwsc523\\3DPrint\\00_AutoMake.UWS"
    dist1min=1
    dist1max= 5
    dist1wait=10
    dist1chk=3

    cmd2 = "C:\\00_okamoto\\sound\\play.exe C:\\00_okamoto\\sound\\irasyai_yama-rei.mp3"
    dist2min=10
    dist2max= 45
    dist2wait=1
    dist2chk=3

    cmd3 = "C:\\00_okamoto\\sound\\play.exe C:\\00_okamoto\\sound\\voice-konnithiha.wav"
    dist3min=50
    dist3max= 200
    dist3wait=1
    dist3chk=3
    ###################################
 
    cont=0

    while True:
        c = ser.readline()
        n=(c.rstrip().decode('utf-8'))
        dst = n.split(".")
        if dst[0].isdigit():
            p1=int(dst[0])
        else:
            p1=0
        num=p1
        print (num)
        #print(type(num))

        if cont>=dist1chk and num>=dist1min and num<=dist1max:
            print ('cmd_1 start')
            print (cont, num, cmd1)
            proc1 = subprocess.call( cmd1, shell=True )
            time.sleep(dist1wait)
            line = ser.read(1000)
            cont=0

        if cont>=dist2chk and num>=dist2min and num<=dist2max:
            print ('cmd_2 start')
            print (cont, num, cmd2)
            proc2 = subprocess.call( cmd2 )
            time.sleep(dist2wait)
            line = ser.read(1000)
            cont=0

        if cont>=dist3chk and num>=dist3min and num<=dist3max:
            print ('cmd_3 start')
            print (cont, num, cmd3)
            proc3 = subprocess.call( cmd3 )
            time.sleep(dist3wait)
            line = ser.read(1000)
            cont=0

        if num<=0 or num>dist3max:
            cont=0
            #print ('Reset')

        cont=cont+1

    ser.close()

if __name__=="__main__":
    main()
