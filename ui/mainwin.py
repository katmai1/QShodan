# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot,  QUrl
from PyQt5.QtWidgets import QMainWindow,  QFileDialog

from .Ui_mainwin import Ui_MainWindow
from extreu import Extreu

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_btn_save_csv_released(self):
        """
        Slot documentation goes here.
        """
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, selectedFilter = QFileDialog.getSaveFileName(
            self,
            self.tr("Guardar CSV..."),
            "",
            self.tr("*.csv"),
            self.tr("*.csv"), 
            options=options)
        # añadimos extension si
        if len(filename) > 0:
            if not filename.endswith(".csv"):
                filename = filename + ".csv"
            with open(filename,  "w") as f:
                for index in range(self.list_export.count()):
                    f.write(self.list_export.item(index).text() + "\n")
    
    @pyqtSlot()
    def on_btn_home_released(self):
        """
        Carga en el web browser la pagina principal de shodan
        """
        self.webView.setUrl(QUrl("http://www.shodan.io"))
    
    @pyqtSlot()
    def on_btn_extract_released(self):
        """
        Slot documentation goes here.
        """
        raw_html = self.webView.page().currentFrame().toHtml()
        ex = Extreu(raw_html)
        for ip in ex.ips:
            self.list_export.addItem(ip)
    
    @pyqtSlot(bool)
    def on_webView_loadFinished(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type bool
        """
        if self.btn_autoextract.isChecked():
            self.on_btn_extract_released()
    
    @pyqtSlot()
    def on_btn_duplicates_released(self):
        """
        Elimina los duplicados de la lista de IPs
        """
        # guardamos las ips a la lista items
        items = []
        for index in range(self.list_export.count()):
            items.append(self.list_export.item(index).text())
        # eliminamos duplicados
        ips = list(set(items))
        # limpiamos widget
        self.list_export.clear()
        # cargamos la nueva lista
        self.list_export.addItems(ips)
