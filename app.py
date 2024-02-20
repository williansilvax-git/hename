from PySide6.QtWidgets import QApplication
import sys
from views.MainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MainWindow()
    window.setWindowTitle('Hename - Renomear arquivos de uma só vez em diretórios')
    window.show()
    app.exec()
