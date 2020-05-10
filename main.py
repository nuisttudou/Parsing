from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Ui_main import Ui_MainWindow

from defination import *
from myLaxicalAnalysis import ui_use_lexer,set_LaxicalAnalysis_content

content=None
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.set_trigger()
        self.show()
    def set_trigger(self):
        # self.actionloadFile.triggered.connect()
        self.action_lex.triggered.connect(self.set_lex_button)
    # def load_file(self):    
    def set_lex_button(self):
        global content
        content=self.textEdit_in.toPlainText()
        set_LaxicalAnalysis_content(content)
        ans=ui_use_lexer()
        self.textEdit_out.setText(ans)

if __name__ == '__main__':

    app = QApplication([])
    window = MainWindow()
    app.exec_()