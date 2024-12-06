from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

import random
from typing import Callable
import os


class Vars:
    def __init__(self):
        self.trials_to_random_passport = 10


def check_save_files(loc_main:Callable):
    check_save = False
    for i in os.listdir('saves'):
        print(i[-3:])
        if i[-4:] == '.sav':
            check_save = True
            loc_main()
    
    if check_save: print('сохранения были обнаружены')
    else: print('СОХРАНЕНИЯ НЕ БЫЛИ НАЙДЕНЫ!')


def generate_passport_ID(button:QPushButton, label_pass_num:QLabel):
    global VARS
    
    VARS.trials_to_random_passport -= 1
    
    label_pass_num.setStyleSheet('')
    
    if VARS.trials_to_random_passport > 1:
        button.setText(f'Генерация паспорта ({VARS.trials_to_random_passport} попыток)')
    elif VARS.trials_to_random_passport:
        button.setText(f'Генерация паспорта ({VARS.trials_to_random_passport} попытка)')
    else:
        button.setText(f'Генерация паспорта (0 попыток)')
        button.setEnabled(False)
    
    return f'{random.randint(10, 99)} {random.randint(10, 99)} {random.randint(100000, 999999)}'


def center_window(win:QMainWindow):
    qr = win.frameGeometry()

    cp = win.screen().availableGeometry().center()
    qr.moveCenter(cp)
        
    win.move(qr.topLeft())


def check_inserted_data_in_reg(passport:QLabel, name:QLineEdit, func_to_start_play:Callable):
    if passport.text() == '00 00 000000':
        print('РАНДОМИЗИРУЙТЕ ПАСПОРТ!')
        passport.setStyleSheet('color: red')
    
    if not name.text():
        print('ВВЕДИТЕ СВОЁ ИМЯ!')
    
    else:
        func_to_start_play()

VARS = Vars()
