from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Ui_main import Ui_MainWindow

from defination import *
from myLaxicalAnalysis import ui_use_lexer,set_LaxicalAnalysis_content,ui_use_lexer_table
from mySyntax import ui_use_parser,set_Syntax_content

content=None
# lex_content=None
# def set_main_lex_content(content_token):
#     global lex_content
#     lex_content=content_token
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.set_trigger()
        self.show()
    def set_trigger(self):
        self.open_action.triggered.connect(self.open_file)
        # self.action_lex.triggered.connect(self.ui_lex)
        self.action_lex.triggered.connect(self.change_table)
        self.action_parser.triggered.connect(self.ui_parser)
    def ui_lex(self):
        global content
        content=self.textEdit_in.toPlainText()
        set_LaxicalAnalysis_content(content)
        ans=ui_use_lexer()
        self.textEdit_out.setText(ans)
    def open_file(self):
        openfile_name = QFileDialog.getOpenFileName(self,'选择文件','','Excel files(*.test)')
        print(openfile_name)
        f = open(openfile_name[0], 'r')
        with f:
            data = f.read()
            self.textEdit_in.setText(data)
    def ui_parser(self):
        global content
        content=self.textEdit_in.toPlainText()
        set_Syntax_content(content)
        ui_use_parser()
        self.img_label.setPixmap(QPixmap('parser.png'))
        
        self.change_table()
    def change_table(self):
        global content
        content=self.textEdit_in.toPlainText()
        set_LaxicalAnalysis_content(content)
        ans=ui_use_lexer_table()
        print(ans)
        self.rowNum    = len(ans)  #获取查询到的行数
        self.columnNum = 2 #len(self.data[0]) #获取查询到的列数
        self.tableWidget.setRowCount(self.rowNum)  #设置表格行数
        self.tableWidget.setColumnCount(self.columnNum)
        for i in range(0,self.rowNum):
            for j in range(0,2):
                self.itemContent = QTableWidgetItem(ans[i][j])
                self.tableWidget.setItem(i,j,self.itemContent)
        
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec_()