#!/usr/bin/env python
# coding: utf-8

from tkinter import mainloop
import pyautogui
import pyperclip
import time
import sys

#Modality를 PT로 설정하고 시작

paste_list=[]



def before_run():
    #pyautogui.click(1, 1)
    pyautogui.keyDown('alt')
    time.sleep(0.1)
    pyautogui.hotkey('tab')
    time.sleep(0.1)
    pyautogui.keyUp('alt')

    
f_id = open("C:\\Users\\ajounm\\Desktop\\HOMD\\HOMD_id_list.txt", 'r',encoding='UTF8')
f_date = open("C:\\Users\\ajounm\\Desktop\\HOMD\\HOMD_date_list.txt", 'r',encoding='UTF8')

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






def drag():
    time.sleep(0.5)
    pyautogui.click(110, 1165)
    pyautogui.mouseDown()
    img_capture = pyautogui.locateOnScreen("image.png") 
    time.sleep(1)
    pyautogui.moveTo(img_capture)
    time.sleep(1)
    pyautogui.mouseUp()



def copy_paste():
    pyautogui.hotkey('ctrl','c')
    time.sleep(1)
    paste_var = pyperclip.paste()
    paste_list.append(paste_var)
    #paste_list.append("_DELIMITER_")
    time.sleep(0.5)
  


def one(index):
    index_1=index
    search(index_1)
    time.sleep(1.2)
    move_1()
    time.sleep(1.2)
    drag()
    time.sleep(1)
    copy_paste()
    print(paste_list)






#pyautogui.moveTo(560, 960)





















index=0
before_run()
time.sleep(0.1)
if (len(id_lines) == len(date_lines)):
    for index in range(len(id_lines)):#3340
        one (index)


with open('HOMD_result.txt','w',encoding='ANSI') as f:
    for name in paste_list:
       f.write(name+'\n'+"_DELIMITER_")


