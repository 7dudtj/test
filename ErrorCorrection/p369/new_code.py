import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

class ChartWidget(QWidget):
    def __init__(self, parent=None, ticker="BTC"):
        super().__init__(parent)
        uic.loadUi("resource/chart.ui", self)
        self.ticker = ticker

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    cw = ChartWidget() # "BTC"는 오타인듯 함
    cw.show()
    exit(app.exec_())