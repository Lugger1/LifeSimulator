# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause
from __future__ import annotations
import sys

from PyQt6.QtCore import QTime, QTimer, pyqtSlot, Qt
from PyQt6.QtWidgets import QApplication, QLCDNumber


class DigitalClock(QLCDNumber):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        self.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)
        self.setDigitCount(8)
        self.setStyleSheet('background: black; color: green')
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_time)
        self.timer.start(1000)

        self.show_time()

        self.setWindowTitle("Digital Clock")
        self.resize(250, 60)

    @pyqtSlot()
    def show_time(self):
        time = QTime.currentTime()
        text = time.toString("hh:mm:ss")

        # Blinking effect
        
        self.display(text)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec())