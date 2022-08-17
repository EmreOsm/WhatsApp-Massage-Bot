# 16/6/2022
# This program is a whatsapp bot to send multiple massage or a massage to multiple phone numbers in a txt file.
# Created by Emre Osman.

import webbrowser as web
import pyautogui as gui
import time

print('Whatsapp Message Sender')

web.open('https://web.whatsapp.com', new=0)
input('Scan the QR code')

numbers = str(input('File Location For Phone Numbers: '))
phone_numbers = open(numbers, 'r', encoding='utf-8')
phone_list = []
message_list = []

link_1 = 'https://web.whatsapp.com/send?phone='
link_3 = '&text&app_absent=0'

count = int(input('message count: '))
for c in range(1, count+1):
    x = str(input('message_'+str(c)+': '))
    message_list.append(x)
print(message_list)


for a in phone_numbers:
    phone_list.append(a[0:-1])

print(phone_list)

for link_2 in phone_list:
    the_link = link_1 + link_2 + link_3
    web.open(the_link, new=0)
    time.sleep(15)
    for message in message_list:
        time.sleep(0.5)
        print(message)
        gui.typewrite(message)
        gui.press('enter')
        time.sleep(1)
    gui.hotkey('ctrl', 'w')
    time.sleep(0.5)

print('process finished')
web.open('https://web.whatsapp.com', new=0)
