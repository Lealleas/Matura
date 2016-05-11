import Gui
import sys
from PySide.QtGui import *
from PySide.QtCore import  *
from PySide import  QtGui
import Model
class Controller(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.gui = Gui.Ui_MainWindow(self)
        self.gui.setupUi(self)
        self.gui.actionSelect.triggered.connect(self.selectFile)
        self.gui.pushButtonUpper.clicked.connect(self.uppercase)
        self.gui.pushButtonLower.clicked.connect(self.lowercase)
        self.gui.pushButtonKV.clicked.connect(self.kennen)
        self.gui.pushButtonKE.clicked.connect(self.kennde)
        self.gui.pushButtonCV.clicked.connect(self.cesaren)
        self.gui.pushButtonCE.clicked.connect(self.cesarde)
    def selectFile(self):
        fname, _ = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '', 'Text(*.txt)')
        self.file=Model.model(fname)
    def uppercase(self):
        if hasattr(self,"file"):
            self.file.Uppercase()
        else:
            QtGui.QMessageBox.warning(self, "Textchanger", "Select a file first")

    def lowercase(self):
        if hasattr(self, "file"):
            self.file.Lowercase()
        else:
            QtGui.QMessageBox.warning(self, "Textchanger", "Select a file first")

    def cesaren(self):
        if hasattr(self, "file"):
            try:
                siftvalue = int(self.gui.plainTextEditc.toPlainText())
                self.file.Cesaren(siftvalue)
            except ValueError:
                QtGui.QMessageBox.warning(self, "Textchanger", "Shift Value Incorect")
        else:
            QtGui.QMessageBox.warning(self, "Textchanger", "Select a file first")

    def cesarde(self):
        if hasattr(self, "file"):
            try:
                siftvalue = int(self.gui.plainTextEditc.toPlainText())
                self.file.Cesarde(siftvalue)
            except ValueError:
                QtGui.QMessageBox.warning(self, "Textchanger", "Shift Value Incorect")
        else:
            QtGui.QMessageBox.warning(self, "Textchanger", "Select a file first")

    def kennen(self):
        if hasattr(self, "file"):
            kennwort = self.gui.plainTextEditk.toPlainText()
            self.file.Kennen(kennwort)
        else:
            QtGui.QMessageBox.warning(self, "Textchanger", "Select a file first")

    def kennde(self):
        if hasattr(self, "file"):
            kennwort = self.gui.plainTextEditk.toPlainText()
            self.file.Kennde(kennwort)
        else:
            QtGui.QMessageBox.warning(self, "Textchanger", "Select a file first")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    c = Controller()
    c.show()
    sys.exit(app.exec_())