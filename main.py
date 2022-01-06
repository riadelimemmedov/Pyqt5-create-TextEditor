import  sys
from PyQt5  import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt,QRegExp,QSize
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
import time
import about

textChanged =False
url = ''
tbchecked = True
dockchecked = True
statusbarched = True

class FindDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Find ve Replace')
        self.setGeometry(450,250,350,200)
        self.UI()
        
    def UI(self):
        ###############################
        formlayaut = QtWidgets.QFormLayout(self)
        ###############################
        hbox = QtWidgets.QHBoxLayout()
        txtFind = QtWidgets.QLabel('Find: ')
        txtReplace = QtWidgets.QLabel('Replace: ')
        txtEmpty = QtWidgets.QLabel('')
        self.findInput = QtWidgets.QLineEdit()
        self.replaceInput = QtWidgets.QLineEdit()
        self.btnFind = QtWidgets.QPushButton('Find ')
        self.btnReplace = QtWidgets.QPushButton('Replace ')
        ################################################################
        hbox.addWidget(self.btnFind)
        hbox.addWidget(self.btnReplace)#yan yana olsun deye horizantola elave eleeidm
        ###############################
        formlayaut.addRow(txtFind,self.findInput)
        formlayaut.addRow(txtReplace,self.replaceInput)
        formlayaut.addRow(txtEmpty,hbox)
        ###############################
        
        
class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Text Editor')
        self.setWindowIcon(QIcon('notepad.png'))
        self.setGeometry(450,150,1000,800)
        self.UI()
        
        
    def UI(self):
        self.editor = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.editor)
        self.editor.setFontPointSize(12.0)
        self.editor.textChanged.connect(self.funcTextChanged)
        self.menu()
        self.toolbar()
        self.dockbar()
        self.statusbar()
        
    def statusbar(self):
        self.status_bar = QtWidgets.QStatusBar()
        self.setStatusBar(self.status_bar)
    
    def funcTextChanged(self):
        global textChanged 
        textChanged = True
        text = self.editor.toPlainText()
        herf_sayi = len(text)
        words = len(text.split())
        self.status_bar.showMessage('Herf Sayi: ' + str(herf_sayi) + 'Soz Sayi: ' + str(words))
        
        
    
    def dockbar(self):
        self.dock = QtWidgets.QDockWidget('Short Cut',self)
        self.dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea | Qt.TopDockWidgetArea)
        self.addDockWidget(Qt.LeftDockWidgetArea,self.dock)
        self.dockWidget = QtWidgets.QWidget(self)
        self.dock.setWidget(self.dockWidget)
        ###############################
        formlayaut = QtWidgets.QFormLayout()
        #########################################################################
        btnFind = QtWidgets.QToolButton()
        btnFind.setIcon(QIcon('find_large.png'))
        btnFind.setText('Find')
        btnFind.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        btnFind.setIconSize(QSize(50,50))
        btnFind.setCheckable(True)
        btnFind.toggled.connect(self.Find)
        #########################################################################
        btnNew = QtWidgets.QToolButton()
        btnNew.setIcon(QIcon("new_large.png"))
        btnNew.setText('New')
        btnNew.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        btnNew.setIconSize(QSize(50,50))
        btnNew.setCheckable(True)
        btnNew.toggled.connect(self.newFile)
        #########################################################################
        btnOpen = QtWidgets.QToolButton()
        btnOpen.setIcon(QIcon('open_large.png'))
        btnOpen.setText('Open')
        btnOpen.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        btnOpen.setIconSize(QSize(50,50))
        btnOpen.setCheckable(True)
        btnOpen.toggled.connect(self.openFile)
        #########################################################################
        btnSave = QtWidgets.QToolButton()
        btnSave.setIcon(QIcon('save_large.png'))
        btnSave.setText('Save')
        btnSave.setIconSize(QSize(50,50))
        btnSave.setCheckable(True)
        btnSave.toggled.connect(self.saveFile)
        ###############################################################
        formlayaut.addRow(btnFind,btnNew)
        formlayaut.addRow(btnOpen,btnSave)
        ########################################################################
        self.dockWidget.setLayout(formlayaut)
        ########################### DockBar Bitis ###################################
        
    def toolbar(self):
        self.tb = self.addToolBar('Tool Bar')
        ################################################################
        self.fontFamily = QtWidgets.QFontComboBox(self)
        self.fontFamily.currentFontChanged.connect(self.changeFont)
        ###############################
        self.tb.addWidget(self.fontFamily)
        self.tb.addSeparator()
        self.tb.addSeparator()
        ###############################
        self.fontsize = QtWidgets.QComboBox(self)
        self.tb.addWidget(self.fontsize)
        self.fontsize.setEditable(True)
        ###############################
        for i in range(8,101):
            self.fontsize.addItem(str(i))
        self.fontsize.setCurrentText('12')
        self.fontsize.currentTextChanged.connect(self.changeFontsize)    
            
        self.tb.addSeparator()
        self.tb.addSeparator()
        
        ###############################
        self.bold = QtWidgets.QAction(QIcon('bold.png'),'Bold Et',self)
        self.tb.addAction(self.bold)
        self.bold.triggered.connect(self.Bold)
        ##############################################################
        self.italic = QtWidgets.QAction(QIcon('italic.png'),'Italic Et',self)
        self.tb.addAction(self.italic)
        self.italic.triggered.connect(self.Italic)
        #########################################################################
        self.underline = QtWidgets.QAction(QIcon('underline.png'),'Alt Xett',self)
        self.tb.addAction(self.underline)
        self.underline.triggered.connect(self.Underline)
        self.tb.addSeparator()
        self.tb.addSeparator()
        ##########################################################################
        self.fontColor = QtWidgets.QAction(QIcon('color.png'),'Change Color',self)
        self.fontColor.triggered.connect(self.funcFontColor)
        self.tb.addAction(self.fontColor)
        ##############################################################################################
        self.fontBackColor = QtWidgets.QAction(QIcon("backcolor.png"),'Back Color',self)
        self.tb.addAction(self.fontBackColor)
        self.fontBackColor.triggered.connect(self.funcBackColor)
        self.tb.addSeparator()
        self.tb.addSeparator()
        ########################################################################################
        self.alignLeft = QtWidgets.QAction(QIcon('alignleft.png'),'Saga Surustur',self)
        self.alignLeft.triggered.connect(self.funcAlignLeft)
        self.tb.addAction(self.alignLeft)
        #########################################################################
        self.alignCenter = QtWidgets.QAction(QIcon('aligncenter.png'),'Ortala',self)
        self.alignCenter.triggered.connect(self.funcAlignCenter)
        self.tb.addAction(self.alignCenter)
        ################################################################################
        self.alignRight = QtWidgets.QAction(QIcon('alignright.png'),'Sola Surustur',self)
        self.alignRight.triggered.connect(self.funcAlignRight)
        self.tb.addAction(self.alignRight)
        #########################################################################
        self.alignJustify = QtWidgets.QAction(QIcon('alignJustify.png'),'Align Justify',self)
        self.tb.addAction(self.alignJustify)
        self.alignJustify.triggered.connect(self.funcAlignJustify)
        self.tb.addSeparator()
        self.tb.addSeparator()
        ################################################################################
        self.bulletList = QtWidgets.QAction(QIcon('bulletlist.png'),'Bullet List',self) 
        self.tb.addAction(self.bulletList)
        self.bulletList.triggered.connect(self.funcBulletList)
        ################################################################################
        self.numberedList = QtWidgets.QAction(QIcon('numberlist.png'),'Numbered List',self)
        self.tb.addAction(self.numberedList)
        self.numberedList.triggered.connect(self.FuncNumberList)
        self.tb.addSeparator()
    def  FuncNumberList(self):
        self.editor.insertHtml("<ol><li><h3>&nbsp;</h3></li></ol>")
    
    def funcBulletList(self):
        self.editor.insertHtml("<ul><li><h3>&nbsp;</h3></li><ul>")
        
    def funcAlignLeft(self):
        self.editor.setAlignment(Qt.AlignLeft)
    
    def funcAlignCenter(self):
        self.editor.setAlignment(Qt.AlignHCenter)
        
    def funcAlignRight(self):
        self.editor.setAlignment(Qt.AlignRight)
    
    def funcAlignJustify(self):
        self.editor.setAlignment(Qt.AlignJustify)
    
    def funcFontColor(self):
        color = QtWidgets.QColorDialog.getColor()
        self.editor.setTextColor(color)
        
    def funcBackColor(self):
        bck = QtWidgets.QColorDialog.getColor()
        self.editor.setTextBackgroundColor(bck)
    
    def Bold(self):
        fontweight = self.editor.fontWeight()
        if fontweight == 50:
            self.editor.setFontWeight(QFont.Bold)
        elif fontweight == 70:
            self.editor.setFontWeight(QFont.Normal)
        
    def Italic(self):
        italic = self.editor.fontItalic()
        if italic == True:
            self.editor.setFontItalic(False)
        
        else:
            self.editor.setFontItalic(True)
    
    def Underline(self):
        underline = self.editor.fontUnderline()
        if underline == True:
            self.editor.setFontUnderline(False)
        
        else:
            self.editor.setFontUnderline(True)
    
    def changeFont(self,font):
        font = QFont(self.fontFamily.currentFont())
        self.editor.setCurrentFont(font)
        
    def changeFontsize(self,fontsize):
        self.editor.setFontPointSize(float(fontsize))
        
        
        
        ############################ ToolBar Bitis ########################################################
        
    def menu(self):
        ######################################## AnaMenu ###############################
        menubar = self.menuBar()
        ################################################################################
        
        file = menubar.addMenu('File')
        edit = menubar.addMenu('Edit')
        view = menubar.addMenu('View')
        help_menu = menubar.addMenu('Help')
        ######################################## AltMenu ##############################
        new = QtWidgets.QAction(QIcon('new.png'),'New',self)
        new.setShortcut('Alt+Insert')
        new.triggered.connect(self.newFile)
        file.addAction(new)
        ##############################################################
        openn = QtWidgets.QAction(QIcon('open.png'),'Open',self)
        openn.setShortcut('Ctrl+O')
        openn.triggered.connect(self.openFile)
        file.addAction(openn)
    ##################################################################
        save = QtWidgets.QAction(QIcon('save.png'),'Save',self)
        save.setShortcut('Ctrl+S')
        save.triggered.connect(self.saveFile)
        file.addAction(save)
        ##################################################################################
        exit = QtWidgets.QAction(QIcon('exit.png'),'Exit',self)
        exit.triggered.connect(self.exitFile)
        file.addAction(exit)
        ##################################################################################
        undo = QtWidgets.QAction(QIcon('undo.png'),'Undo',self)
        undo.setShortcut('Ctrl+Z')
        undo.triggered.connect(self.Undo)
        edit.addAction(undo)
        ################################################################################
        cut = QtWidgets.QAction(QIcon('cut.png'),'Cut',self)
        cut.setShortcut('Ctrl+X')
        cut.triggered.connect(self.Cut)
        edit.addAction(cut)
        ################################################################################
        copy = QtWidgets.QAction(QIcon('copy.png'),'Copy',self)
        copy.setShortcut('Ctrl+C')
        copy.triggered.connect(self.Copy)
        edit.addAction(copy)
        ################################################################################
        paste = QtWidgets.QAction(QIcon('paste.png'),'Paste',self)
        paste.setShortcut('Ctrl+V')
        paste.triggered.connect(self.Paste)
        edit.addAction(paste)
        ################################################################################################################
        find = QtWidgets.QAction(QIcon('find.png'),'Find',self)
        find.setShortcut('Ctrl+F')
        find.triggered.connect(self.Find)
        edit.addAction(find)
        ################################################################################
        time_date = QtWidgets.QAction(QIcon('datetime.png'),'Insert Time and Date',self)
        time_date.setShortcut('F5')
        time_date.triggered.connect(self.Time_Date)
        edit.addAction(time_date)
        ################################################################################
        toggleStatusBar = QtWidgets.QAction('Toggle StatusBar',self,checkable=True)
        toggleStatusBar.triggered.connect(self.funcToggleStatusBar)
        view.addAction(toggleStatusBar)
        ################################################################################
        toggleToolBar = QtWidgets.QAction('Toggle ToolBar',self,checkable=True)
        toggleToolBar.triggered.connect(self.funcToggleToolBar)
        view.addAction(toggleToolBar)
        ################################################################################
        toggleDockBar = QtWidgets.QAction('Toggle DockBar',self,checkable=True)
        toggleDockBar.triggered.connect(self.funcToggleDockBar)
        view.addAction(toggleDockBar)
        ################################################################################
        about_us = QtWidgets.QAction('About Us',self)
        about_us.triggered.connect(self.About)
        help_menu.addAction(about_us)
        ###############################
        ####################################################################
    
    def  About(self):
        self.help = about.Help()
        self.help.show()
    
    def funcToggleDockBar(self):
        global dockchecked
        if dockchecked == True:
            self.dock.hide()
            dockchecked = False
        
        else:
            self.dock.show()
            tbchecked = True 
        
    def funcToggleToolBar(self):
        global tbchecked
        if tbchecked == True:
            self.tb.hide()
            tbchecked = False
        
        else:
            self.tb.show()
            tbchecked = True
        
    def funcToggleStatusBar(self):
        global statusbarched
        if statusbarched == True:
            self.status_bar.hide()
            statusbarched = False
        else:
            self.status_bar.show()
            statusbarched = True
        
    
    def Time_Date(self):
        time_date = time.strftime(" %d.%m.%Y %H:%M") 
        self.editor.append(time_date)
        
    def Find(self):
        self.find = FindDialog()
        self.find.show()
        
        def fineWords():
            global word 
            word = self.find.findInput.text()
            if word != '':
                cursor = self.editor.textCursor()
                format1 = QtWidgets.QTextCharFormat()
                format1.setBackground(QBrush(QColor('grey')))
                regex = QWidgets.QRegExp(word)
                pos = 0
                index = regex.indexIn(self.editor.toPlainText(),pos)
                self.count = 0
                while (index != -1):
                    cursor.setPosition(index)
                    cursor.movePosition(QTextCursor.EndOfWord,1)
                    cursor.mergeCharFormat(format1)
                    pos = index + regex.matchedLength()
                    index = regex.indexIn(self.editor.toPlainText(),pos)
                    self.count += 1
                self.status_bar.showMessage(str(self.count) + 'Result Found')
            
            
            else:
                QtWidgets.QMessageBox.information(self,'Info','Bos Deyer Ola Bilmez')
        
        def replaceWords():
            replaceText = self.find.replaceInput.text()
            word = self.find.findInput.text()
            text = self.editor.toPlainText()
            newvalue= text.replace(word,replaceText)
            self.editor.clear()
            self.editor.append(newvalue)
            
                        

        def replaceWords():
            pass
        
        self.find.btnFind.clicked.connect(fineWords)
        self.find.btnReplace.clicked.connect(replaceWords)
    
        
    def Paste(self):
        self.editor.paste()
    
    def Copy(self):
        self.editor.copy()
    
    def Cut(self):
        self.editor.cut()
    
    def Undo(self):
        self.editor.undo()
        
    def exitFile(self):
        global url
        try:
            if textChanged == True:
                mbox = QtWidgets.QMessageBox.information(self,'Info','Are You Sure This File Save:', QtWidgets.QMessageBox.Save | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel, QtWidgets.QMessageBox.Cancel)
                if mbox == QtWidgets.QMessageBox.Save:
                    if url != '':
                        content = self.editor.toPlainText()
                        with open(url[0],'w',encoding='utf-8') as file:
                            file.write(content)
                    else:
                        url = QtWidgets.QFileDialog.getSaveFileName(self,'Save File',"","Txt files(*.txt)")
                        content2 = self.editor.toPlainText()
                        with open(url[0],'w',encoding='utf-8') as file2:
                                file2.write(content2)
                elif mbox == QtWidgets.QMessageBox.No:
                    qApp.quit()
                    
            else:
                qApp.quit()
        except:
            pass
                            
    def saveFile(self):
        global url
        try:
            if textChanged == True:
                if url != '':
                    content = self.editor.toPlainText()
                    with open(url[0],'w',encoding='utf-8') as file:
                        file.write(content)
                else:
                    #else durumunda fayl bosdur temiz sifirdan yaradirig
                    url = QtWidgets.QFileDialog.getSaveFileName(self,'Fayli Save Et','',"Txt Files (*.txt)")
                    content2 = self.editor.toPlainText()
                    with open(url[0],'w',encoding='utf-8') as file2:
                        file2.write(content2)
        except:
            pass    
        
    def openFile(self):
        global url
        try:
            url = QtWidgets.QFileDialog.getOpenFileName(self,"Fayli Ac",'',"All Files(*);;Txt Files * txt" )
            with open(url[0],'r+',encoding='utf-8') as file:
                content = file.read()
                self.editor.clear()
                self.editor.setText(content)
        except:
            pass
    
    def newFile(self):
        try:
            global url
            url = ''
            self.editor.clear()
        except :
            pass
    ###############################MenuBitir###########################################
def main():
    app = QtWidgets.QApplication(sys.argv)
    mk = Main()
    mk.show()
    sys.exit(app.exec())
if __name__ == '__main__':
    main()
    