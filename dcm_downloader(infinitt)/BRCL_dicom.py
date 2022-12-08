#!/usr/bin/env python
# coding: utf-8

from tkinter import mainloop
import pyautogui
import pandas as pd
import time
import sys

#Modality를 PT로 설정하고 시작

def before_run(): # 알트탭으로 INFINITT로 돌아가는 함수
    pyautogui.click(1, 1)
    pyautogui.keyDown('alt')
    time.sleep(0.1)
    pyautogui.hotkey('tab')
    time.sleep(0.1)
    pyautogui.keyUp('alt')

    
f_id = open("C:\\Users\\ajounm\\Desktop\\BRCL_PNG\\BRCL_PNG_ID_LIST.txt", 'r',encoding='UTF8') #ID_LIST.txt 경로 재설정하기
f_date = open("C:\\Users\\ajounm\\Desktop\\BRCL_PNG\\BRCL_PNG_DATE_LIST.txt", 'r',encoding='UTF8') #DATE_LIST.txt 경로 재설정하기

id_lines = f_id.readlines()
date_lines = f_date.readlines()







def search(index): #검색하기전 필터창에 ID와 DATE를 입력하고 검색합니다.
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
    #보다 더 정확한 검색을 원하시면 id,date외에 더 많은 정보를 입력하는 코드를 작성하시면 됩니다.






def move_1(): #검색된 환자내용들을 펼칩니다.
    pyautogui.click(175, 200)
    time.sleep(1)
    pyautogui.click(175, 200)
    time.sleep(1)




def Wholebody(): #캡처된 이미지를 추적하여 더블클릭하는 함수입니다. 인식이 한번에 안되는경우가 있는데 여러 시도를 해본결과 캡처 영역 밖 적은 범위 내에서 차이가 있으면 인식을 못하는것같습니다.
    time.sleep(0.7)
    img_capture_1 = pyautogui.locateOnScreen("C:\\Users\\ajounm\\Desktop\\BRCL_PNG\\Wholebody_top.png") #대상이 맨위에 있는경우
    img_capture_2 = pyautogui.locateOnScreen("C:\\Users\\ajounm\\Desktop\\BRCL_PNG\\Wholebody_bottom.png") #대상이 맨위가 아닌 경우
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


def convert(): ##convert합니다.

    pyautogui.click(1185, 185)
    time.sleep(1)
    pyautogui.rightClick()
    pyautogui.hotkey('c')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('enter')
    time.sleep(1.2)
    pyautogui.click(1, 1)



def one(index): #위 함수들을 모아놓은 함수입니다.
    index_1=index
    search(index_1)
    time.sleep(0.5)
    move_1()
    time.sleep(1)
    Wholebody()
    time.sleep(1)
    convert()
    time.sleep(1)




#one함수를 환자수만큼 반복합니다.
index=0
before_run()
time.sleep(0.1)
if (len(id_lines) == len(date_lines)):#id_list.txt와 date_list.txt의 줄수가 같아야 반복문이 실행됩니다.
    for index in range(len(id_lines)): #반복 횟수를 설정합니다. 여기선 id_list.txt줄수만큼 반복합니다.
        one (index)