#!/usr/bin/env python
# coding: utf-8

from tkinter import mainloop
import pyautogui
import pandas as pd
import time
import sys

#Modality를 PT로 설정하고 시작

def before_run():
    pyautogui.click(1, 1)
    pyautogui.keyDown('alt')
    time.sleep(0.1)
    pyautogui.hotkey('tab')
    time.sleep(0.1)
    pyautogui.keyUp('alt')
    
f_id = open("C:\\Users\\ajounm\\Desktop\\BRCL_PNG\\BRCL_PNG_ID_LIST.txt", 'r',encoding='UTF8')
f_date = open("C:\\Users\\ajounm\\Desktop\\BRCL_PNG\\BRCL_PNG_DATE_LIST.txt", 'r',encoding='UTF8')

id_lines = f_id.readlines()
date_lines = f_date.readlines()

#id_lines_d= [l.strip() for l in id_lines]
#date_lines_d= [l.strip() for l in date_lines]




#pyautogui.hotkey('alt', 'tab')
def search(index):
    i=index
    time.sleep(0.1)
    pyautogui.click(200, 150)#아이디 슬롯 이동후 클릭 
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.write(id_lines[i]) #i번째 아이디 쓰기
    time.sleep(0.1)
    pyautogui.click(420, 150)#날짜 슬롯 이동후 클릭 
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.write(date_lines[i])#i번째 날짜 쓰기
    time.sleep(0.2)


def move_1():
    pyautogui.click(175, 200)
    time.sleep(1)
    pyautogui.click(175, 200)
    time.sleep(1)




def Wholebody():
    time.sleep(0.7)
    img_capture_1 = pyautogui.locateOnScreen("C:\\Users\\ajounm\\Desktop\\BRCL_PNG\\Wholebody_top.png") 
    img_capture_2 = pyautogui.locateOnScreen("C:\\Users\\ajounm\\Desktop\\BRCL_PNG\\Wholebody_bottom.png") 
    img_capture_3 = pyautogui.locateOnScreen("C:\\Users\\ajounm\\Desktop\\BRCL_PNG\\WB_top.png") 
    img_capture_4 = pyautogui.locateOnScreen("C:\\Users\\ajounm\\Desktop\\BRCL_PNG\\WB_bottom.png") 
    if img_capture_1 != None:
        print(img_capture_1)
        time.sleep(1.5)
        pyautogui.doubleClick(img_capture_1)
        return

    if img_capture_2 != None:
        print(img_capture_2)
        time.sleep(1.5)
        pyautogui.doubleClick(img_capture_2)
        return

    if img_capture_3 != None:
        print(img_capture_3)
        time.sleep(1.5)
        pyautogui.doubleClick(img_capture_3)
        return

    if img_capture_4 != None:
        print(img_capture_4)
        time.sleep(1.5)
        pyautogui.doubleClick(img_capture_4)
        return


def convert():

    pyautogui.click(1185, 185)
    time.sleep(1)
    pyautogui.rightClick()
    pyautogui.hotkey('c')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('enter')
    time.sleep(1.2)
    pyautogui.click(1, 1)



def one(index):
    index_1=index
    search(index_1)
    time.sleep(0.5)
    move_1()
    time.sleep(1)
    Wholebody()
    time.sleep(1)
    convert()
    time.sleep(1)






#pyautogui.moveTo(560, 960)





















index=0
before_run()
time.sleep(0.1)
if (len(id_lines) == len(date_lines)):
    for index in range(563):
        one (index)