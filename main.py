# так вова, прошу тебя, молю... НЕ ЗАБРАСЫВАЙ ЭТОТ ШЕДЕВРАЛЬНЫЙ ПРОЕКТ...
'''
документация для себя:

center_w = всегда главный виджет
'''

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

from scripts.backend import *

import sys


class GAME(QMainWindow):
    def __init__(self):
        super().__init__()
        self.apply_settings()
        self.loc_hello()
    
    '''ЛОКАЦИЯ [ПРИВЕТСТВИЕ]'''
    
    def loc_hello(self):
        self.center_w = QWidget(self)
        
        self.grid_lt = QGridLayout(self.center_w)
        
        self.title = QLabel()
        self.title.setText('Добро пожаловать в Life Sim!')
        
        self.logo = QLabel()
        self.logo.setPixmap(QPixmap('assets/free-icon-money-bags-3331745.png').scaled(100, 100, transformMode=Qt.TransformationMode.SmoothTransformation))
        self.logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.button_load_started_play = QPushButton()
        self.button_load_started_play.setText('Продолжить')
        self.button_load_started_play.clicked.connect(lambda: check_save_files(lambda: print('')))

        self.button_start_play = QPushButton()
        self.button_start_play.setText('Начать')
        self.button_start_play.clicked.connect(self.loc_reg)

        self.button_settings = QPushButton()
        self.button_settings.setText('Настройки')

        self.button_quit = QPushButton()
        self.button_quit.setText('Выход')
        self.button_quit.clicked.connect(sys.exit)
        
        self.grid_lt.addWidget(self.title, 0, 0)
        self.grid_lt.addWidget(self.button_load_started_play, 2, 0)
        self.grid_lt.addWidget(self.button_start_play, 3, 0)
        self.grid_lt.addWidget(self.button_settings, 4, 0)
        self.grid_lt.addWidget(self.button_quit, 5, 0)
        self.grid_lt.addWidget(self.logo, 0, 1, 5, 1)
        
        self.setCentralWidget(self.center_w)
    
    def loc_reg(self):
        self.center_w = QWidget(self)
        
        self.grid_lt = QGridLayout(self.center_w)
        
        self.label_passport_title = QLabel()
        self.label_passport_title.setText('Регистрация')
        
        self.label_description = QLabel()
        self.label_description.setText('Приветствую тебя, игрок. Чтобы начать играть, тебе нужно указать своё ФИО и рандомизировать номер паспорта(не переживай, заполняй такие данные, какие хочешь, это игра, а не реальная жизнь)')
        self.label_description.setWordWrap(True)
        
        self.button_random_pass_num = QPushButton()
        self.button_random_pass_num.setText('Генерация паспорта (10 попыток)')
        self.button_random_pass_num.clicked.connect(lambda: self.label_passport_number.setText(generate_passport_ID(self.button_random_pass_num, self.label_passport_number)))
        
        self.label_passport_number = QLabel()
        self.label_passport_number.setText('00 00 000000')
        
        self.input_name = QLineEdit()
        self.input_name.setPlaceholderText('Введите имя')  
        
        self.button_start = QPushButton()
        self.button_start.setText('начать новую жизнь!')
        self.button_start.clicked.connect(lambda: check_inserted_data_in_reg(self.label_passport_number, self.input_name, self.loc_main))
        
        self.button_exit = QPushButton()
        self.button_exit.setText('вернуться')
        self.button_exit.clicked.connect(self.loc_hello)
        
        self.grid_lt.addWidget(self.label_description, 0, 0, 1, 2)
        self.grid_lt.addWidget(self.button_random_pass_num, 1, 0)
        self.grid_lt.addWidget(self.label_passport_number, 1, 1)
        self.grid_lt.addWidget(self.input_name, 2, 0, 1, 2)
        self.grid_lt.addWidget(self.button_start, 3, 0, 1, 2)
        self.grid_lt.addWidget(self.button_exit, 4, 0, 1, 2)
        
        self.setCentralWidget(self.center_w)
    
    def loc_main(self):
        self.resize(1920, 1080)
        self.setWindowFlag(Qt.WindowType.)
        center_window(self)
        self.center_w = QWidget(self)
        
        self.grid_lt = QGridLayout(self.center_w)
        
        self.time = QLabel()
        self.time.setText('Время')

        self.news = QLabel()
        self.news.setText('новости')
        
        self.grid_lt.addWidget(self.time)
        self.grid_lt.addWidget(self.news)
        
        self.setCentralWidget(self.center_w)
        
    # настройка приложения
    def apply_settings(self):
        self.setWindowTitle('Life Sim [ver 0.0.0.0 Pre-Alpha]')
        self.setMinimumSize(640, 480)        


if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        ui = GAME()
        ui.show()
        app.exec()
    except SystemExit:
        print('приложение было закрыто.')
