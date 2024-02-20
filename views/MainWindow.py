import os
import sys
from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from ui.mainwindow_ui import Ui_MainWindow

DIRETORIO = None


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionSair.triggered.connect(self.sair)
        self.ui.push_selecionar.clicked.connect(self.event_push_selecionar)
        self.ui.push_executar.clicked.connect(self.event_push_executar)

    

    def salvar_arquivo_original(self,diretorio:str):
        if diretorio:
            with open('arquivos_originais.txt','w+') as arquivo:
                lista_arquivos = os.listdir(diretorio)
                for f in lista_arquivos:
                    arquivo.write(f + '\n')

    def listar_arquivos_diretorio(self,diretorio:str):
        self.ui.list_arquivos.clear()
        if diretorio:
            lista_arquivos = [f for f in os.listdir(diretorio)]
            self.ui.list_arquivos.addItems(lista_arquivos)

    def event_push_selecionar(self):
        if self.ui.line_diretorio.text() == '':
            folder_dialog = QFileDialog()
            folder_dialog.setFileMode(QFileDialog.FileMode.Directory)
            diretorio_selecionado = folder_dialog.getExistingDirectory(
                None, 'Selecione o diretório', '', QFileDialog.Option.DontUseNativeDialog)

            if diretorio_selecionado:
                DIRETORIO = diretorio_selecionado
                self.ui.line_diretorio.setText(DIRETORIO)
        else:
            DIRETORIO = self.ui.line_diretorio.text()

        self.listar_arquivos_diretorio(DIRETORIO)
        self.salvar_arquivo_original(DIRETORIO)

    def event_push_executar(self):
        pass

    def sair(self):
        sys.exit(-1)

    
