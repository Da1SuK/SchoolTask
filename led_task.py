# /usr/bin/python3
# -*- coding: utf-8 -*-
#
# led_task.py : 3つのLEDを使った第3Q課題
# deadline : 2021/11/30(Tue) ~8:00 am
# coded by Daisuke Sugioka

import time
import sys
import termios
import pigpio

R_led = 18
Y_led = 23
G_led = 24

pi = pigpio.pi()

pi.set_mode(R_led, pigpio.OUTPUT)
pi.set_mode(Y_led, pigpio.OUTPUT)
pi.set_mode(G_led, pigpio.OUTPUT)

def Flash(red, yel, gre, lr, ly, lg, t1):
    pi.write(red, lr)
    pi.write(yel, ly)
    pi.write(gre, lg)
    time.sleep(t1)
    
def Stairs():
    n = int(input('繰り返し回数を入力してね! → '))
    if n == 0:
        sys.exit(0)
    for i in range(n):
        Flash(R_led, Y_led, G_led, 0, 0, 0, 0.1)
        Flash(R_led, Y_led, G_led, 1, 0, 0, 0.1)
        Flash(R_led, Y_led, G_led, 0, 1, 0, 0.1)
        Flash(R_led, Y_led, G_led, 0, 0, 1, 0.1)
    Flash(R_led, Y_led, G_led, 0, 0, 0, 0.1)
    
def Binary():
    Flash(R_led, Y_led, G_led, 0, 0, 0, 0.5)
    Flash(R_led, Y_led, G_led, 1, 0, 0, 0.5)
    Flash(R_led, Y_led, G_led, 0, 1, 0, 0.5)
    Flash(R_led, Y_led, G_led, 1, 1, 0, 0.5)
    Flash(R_led, Y_led, G_led, 0, 0, 1, 0.5)
    Flash(R_led, Y_led, G_led, 1, 0, 1, 0.5)
    Flash(R_led, Y_led, G_led, 0, 1, 1, 0.5)
    Flash(R_led, Y_led, G_led, 1, 1, 1, 0.5)
    Flash(R_led, Y_led, G_led, 0, 0, 0, 0.5)
    
try:
    print('Hello!')
    Flash(R_led, Y_led, G_led, 1, 1, 1, 0.5)
    Flash(R_led, Y_led, G_led, 0, 0, 0, 0.5)
    print('数字の1か2のどちらかやりたいことができるよ！')
    time.sleep(1)
    print('Ctrl+Cで終了できるよ')
    time.sleep(1)
    print('-'*10)
    while True:
        number = int(input('1か2を入力してね! → '))
        if number == 1:
            Stairs()
            continue
        elif number == 2:
            Binary()
            continue
        else:
            print('+' * 24)
            print('入力できるのは1か2だけだよ！')
            print('+' * 24)
            break
        
except KeyboardInterrupt as e:
    print('\n----------')
    print('Ctrl+Cが押されたよ!')
    
finally:
    Flash(R_led, Y_led, G_led, 0, 0, 0, 0)
    print('See you!')
    
sys.exit(0)