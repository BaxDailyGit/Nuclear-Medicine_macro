#!/usr/bin/env python
# coding: utf-8

from tkinter import mainloop
import pyautogui
import pandas as pd
import time
import sys

#Modality�� PT�� �����ϰ� ����

def before_run(): # ��Ʈ������ INFINITT�� ���ư��� �Լ�
    pyautogui.click(1, 1)
    pyautogui.keyDown('alt')
    time.sleep(0.1)
    pyautogui.hotkey('tab')
    time.sleep(0.1)
    pyautogui.keyUp('alt')

    
f_id = open("C:\\Users\\ajounm\\Desktop\\BRCL_PNG\\BRCL_PNG_ID_LIST.txt", 'r',encoding='UTF8') #ID_LIST.txt ��� �缳���ϱ�
f_date = open("C:\\Users\\ajounm\\Desktop\\BRCL_PNG\\BRCL_PNG_DATE_LIST.txt", 'r',encoding='UTF8') #DATE_LIST.txt ��� �缳���ϱ�

id_lines = f_id.readlines()
date_lines = f_date.readlines()







def search(index): #�˻��ϱ��� ����â�� ID�� DATE�� �Է��ϰ� �˻��մϴ�.
    i=index
    time.sleep(0.1)
    pyautogui.click(200, 150)#���̵� ���� �̵��� Ŭ�� 
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.write(id_lines[i]) #i��° ���̵� ����
    time.sleep(0.1)
    pyautogui.click(420, 150)#��¥ ���� �̵��� Ŭ�� 
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.write(date_lines[i])#i��° ��¥ ����
    time.sleep(0.2)
    #���� �� ��Ȯ�� �˻��� ���Ͻø� id,date�ܿ� �� ���� ������ �Է��ϴ� �ڵ带 �ۼ��Ͻø� �˴ϴ�.






def move_1(): #�˻��� ȯ�ڳ������ ��Ĩ�ϴ�.
    pyautogui.click(175, 200)
    time.sleep(1)
    pyautogui.click(175, 200)
    time.sleep(1)




def Wholebody(): #ĸó�� �̹����� �����Ͽ� ����Ŭ���ϴ� �Լ��Դϴ�. �ν��� �ѹ��� �ȵǴ°�찡 �ִµ� ���� �õ��� �غ���� ĸó ���� �� ���� ���� ������ ���̰� ������ �ν��� ���ϴ°Ͱ����ϴ�.
    time.sleep(0.7)
    img_capture_1 = pyautogui.locateOnScreen("C:\\Users\\ajounm\\Desktop\\BRCL_PNG\\Wholebody_top.png") #����� ������ �ִ°��
    img_capture_2 = pyautogui.locateOnScreen("C:\\Users\\ajounm\\Desktop\\BRCL_PNG\\Wholebody_bottom.png") #����� ������ �ƴ� ���
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


def convert(): ##convert�մϴ�.

    pyautogui.click(1185, 185)
    time.sleep(1)
    pyautogui.rightClick()
    pyautogui.hotkey('c')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('enter')
    time.sleep(1.2)
    pyautogui.click(1, 1)



def one(index): #�� �Լ����� ��Ƴ��� �Լ��Դϴ�.
    index_1=index
    search(index_1)
    time.sleep(0.5)
    move_1()
    time.sleep(1)
    Wholebody()
    time.sleep(1)
    convert()
    time.sleep(1)




#one�Լ��� ȯ�ڼ���ŭ �ݺ��մϴ�.
index=0
before_run()
time.sleep(0.1)
if (len(id_lines) == len(date_lines)):#id_list.txt�� date_list.txt�� �ټ��� ���ƾ� �ݺ����� ����˴ϴ�.
    for index in range(len(id_lines)): #�ݺ� Ƚ���� �����մϴ�. ���⼱ id_list.txt�ټ���ŭ �ݺ��մϴ�.
        one (index)