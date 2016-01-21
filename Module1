#!/usr/bin/python
#BU PROGRAM REQUESTKING Tarafindan Yazilmistir.Ve Sadece Linux/GNU 'da calismaktadir.
import os,time,random
clear = os.system('clear')
#randomMAC Yedek


def randomMAC():
      mac = [0x00, 0x16, 0x3e,
             random.randint(0x00, 0x7f),
             random.randint(0x00, 0xff),
             random.randint(0x00, 0xff)]
      return ':'.join(map(lambda x: "%02x" % x, mac))
#randomMAC Yedek


def gizlenme(a,b,c,ip,host): 
     if c == 'eth0':
          try:
            for i in range(a):
               print "\n\n\n\n\n\n\n\n\n\n\n\n\n"
               os.system('macchanger -a eth0')
               os.system('proxychains telnet '+ip)
               time.sleep(b)
               os.system('clear')
          except:
             clear
             print "[-]Baglantinizda Sorun Var Veya macchanger Yuklenmemis! "
     elif c == 'eth1':
          try:
            for i in range(a):
                print "\n\n\n\n\n\n\n\n\n\n\n\n\n"
                os.system('macchanger -a eth1')
                os.system('proxychains telnet '+d)
                time.sleep(b)
                os.system('clear')
          except:
            clear
            print "[-]Baglantinizda Sorun Var Veya macchanger Yuklenmemis! "

     elif c == 'wlan0':
            try:
              for i in range(a):
                 print "\n\n\n\n\n\n\n\n\n\n\n\n\n"
                 os.system('macchanger -a wlan0')
                 os.system('proxychains telnet '+d)                 
                 time.sleep(b)
                 os.system('clear')
            except:
              clear
              print "[-]Baglantinizda Sorun Var Veya macchanger Yuklenmemis! "
     elif c == 'wlan1':
           try:
              for i in range(a):
                print "\n\n\n\n\n\n\n\n\n\n\n\n\n"
                os.system('macchanger -a wlan1')
                os.system('proxychains telnet '+d)
                time.sleep(b)
                os.system('clear')
           except:
               clear
               print "[-]Baglantinizda Sorun Var Veya macchanger Yuklenmemis! "
     else:
         print "[-]Boyle Bir Baglanti Eklenmemis.Kurgulayan Kisiye Iletin"


bsqlm2 = " \'python 2.py\'"
delay = input("[?] MAC Adresi Degisme Gecikmesi? \n + ")
loop = input("[?]MAC Adresi Kac Defa Degistirme Sayisi? \n + ")
wore = raw_input('[?]MAC Adresini Degistirmek Istediiniz Ag Arayuzu.wlan0,wlan1,eth0,eth1 \n + ')
ip = raw_input('[?]Hedefin Ipsi nedir ? \n + ')
host = raw_input('[?]Hedefin Hostu nedir ? \n + ')
if os.name=="posix":
        
        os.system('gnome-terminal -e python 2.py')
        print "Sqlmap Aciliyor....."
        os.system('proxychains firefox '+host)
        gizlenme(loop,delay,wore,ip,host)
else:
   print "[-]Linux Kullanmiyorsunuz. "
   print "[-_-]Gorusmek Uzere!!!"


