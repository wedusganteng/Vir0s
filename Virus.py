#!/usr/bin/python2
# coding=utf-8
import time
import os
import sys
os.system('clear')
banner = '''
_   _ _
| | | (_)
| | | |_ _ __ _   _ ___
| | | | | '__| | | / __|
\ \_/ / | |  | |_| \__ \ 
 \___/|_|_|   \__,_|___/   Berbahaya
'''
print (f'{banner}')

num = input('Masukkan Nomor Target : ')
if len(num) < 11:
        print ('Masukkan Nomornya Dengan Benar')
        exit()
for i in range(100000):
        print (f'Mengirim Virus Ke Nomor {num}')
        time.sleep(0.3)