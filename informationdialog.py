from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QWidget, QPushButton, QTextBrowser
import util.resources

class InformationDialog(QWidget):
    def __init__(self, path, strFileName, widget):
        super(InformationDialog, self).__init__(widget)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        self.setWindowFlags(QtCore.Qt.Window |
                            QtCore.Qt.CustomizeWindowHint |
                            QtCore.Qt.WindowTitleHint |
                            QtCore.Qt.WindowCloseButtonHint |
                            QtCore.Qt.WindowStaysOnTopHint)
        self.name = 'browser'
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.setWindowIcon(QtGui.QIcon(':/icons/ico.png'))
        self.setWindowTitle('Справка')
        self.resize(900, 700)

        pBack = QPushButton('<<')
        pHome = QPushButton('Главная')
        pForward = QPushButton('>>')

        pBrowser = QTextBrowser()

        pBack.clicked.connect(pBrowser.backward)
        pHome.clicked.connect(pBrowser.home)
        pForward.clicked.connect(pBrowser.forward)

        pBrowser.backwardAvailable.connect(pBack.setEnabled)
        pBrowser.forwardAvailable.connect(pForward.setEnabled)

        pBrowser.setSearchPaths([path])
        pBrowser.setSource(QUrl(strFileName))

        pvbxLayout = QtWidgets.QVBoxLayout()
        phbxLayout = QtWidgets.QHBoxLayout()

        phbxLayout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignCenter)
        pvbxLayout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignCenter)

        phbxLayout.addWidget(pBack)
        phbxLayout.addWidget(pHome)
        phbxLayout.addWidget(pForward)
        pvbxLayout.addLayout(phbxLayout)
        pvbxLayout.addWidget(pBrowser)
        self.setLayout(pvbxLayout)

    def closeEvent(self, e):
        e.accept()
