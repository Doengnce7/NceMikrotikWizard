# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\tni\python\project\mtk.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
#
# Worrachon Panomchon 58121011-9
#

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from firebase import firebase
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication)


class Ui_MainWindow(object):
    FullConfig=""
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(784, 550)
        MainWindow.setMinimumSize(QtCore.QSize(784, 550))
        MainWindow.setAcceptDrops(False)
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 100, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 771, 71))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 220, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pppoe_password = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.pppoe_password.setGeometry(QtCore.QRect(20, 250, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.pppoe_password.setFont(font)
        self.pppoe_password.setPlainText("")
        self.pppoe_password.setObjectName("pppoe_password")
        self.pppoe_user = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.pppoe_user.setGeometry(QtCore.QRect(20, 180, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.pppoe_user.setFont(font)
        self.pppoe_user.setPlainText("")
        self.pppoe_user.setObjectName("pppoe_user")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 310, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.wifipassword = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.wifipassword.setGeometry(QtCore.QRect(20, 460, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.wifipassword.setFont(font)
        self.wifipassword.setReadOnly(False)
        self.wifipassword.setPlainText("")
        self.wifipassword.setObjectName("wifipassword")
        self.ssid = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ssid.setGeometry(QtCore.QRect(20, 390, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.ssid.setFont(font)
        self.ssid.setPlainText("")
        self.ssid.setObjectName("ssid")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 360, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 430, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(380, 100, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.GetScript = QtWidgets.QPushButton(self.centralwidget)
        self.GetScript.setGeometry(QtCore.QRect(20, 510, 111, 31))
        self.GetScript.setObjectName("GetScript")
        self.GetFile = QtWidgets.QPushButton(self.centralwidget)
        self.GetFile.setGeometry(QtCore.QRect(160, 510, 111, 31))
        self.GetFile.setObjectName("GetFile")
       
        self.textpreview = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textpreview.setGeometry(QtCore.QRect(380, 150, 361, 385))
        
        self.textpreview.setObjectName("textpreview")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

        self.GetScript.clicked.connect(self.gatdate)
        self.GetFile.clicked.connect(self.saveFileDialog)
       

    def retranslateUi(self, MainWindow):
        import time
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " Wizard For Config Script Mikrotik Device  V.0.7 "))
        self.label.setText(_translate("MainWindow", "Internet (WAN)"))
        self.label_2.setText(_translate("MainWindow", "Wizard For Config Script Mikrotik Device"))
        self.label_3.setText(_translate("MainWindow", "PPPoE User"))
        self.label_4.setText(_translate("MainWindow", "PPPoE Password"))
        self.label_6.setText(_translate("MainWindow", "Your Network (LAN)"))
        self.label_9.setText(_translate("MainWindow", "WiFi Name (SSID)"))
        self.label_10.setText(_translate("MainWindow", "WiFi Password "))
        self.label_5.setText(_translate("MainWindow", "Preview Script"))
        self.GetScript.setText(_translate("MainWindow", "Get Script"))
        self.GetFile.setText(_translate("MainWindow", "Get File"))
       
        self.textpreview.setPlainText(_translate("MainWindow", "Initial...\n\n"))
         
    
    def editconfig(self,configdata,pppuser,ppppassword,wifissid,wifipassword):

        configpass=configdata.replace("PPPOEPASSOWRD1",ppppassword )
        configuser=configpass.replace("PPPOEUSER1",pppuser)
        configwifi=configuser.replace("WIFISSID1",wifissid)
        configF=configwifi.replace("WIFIPASSWORD1",wifipassword)

        return configF


    def gatdate(self):
        import time
        global FullConfig
        pppuser=self.pppoe_user.toPlainText()
        ppppassword=self.pppoe_password.toPlainText()
        wifissid=self.ssid.toPlainText()
        wifipassword=self.wifipassword.toPlainText()
      

        if self.Checkinput(pppuser,ppppassword,wifissid,wifipassword):
            try:
                firebasex = firebase.FirebaseApplication('https://pymtk-1089b.firebaseio.com/', None)
            
                result = firebasex.get('/configfile', None)
                
                configtext=result["-L_mgWtr36LPHkdaNebR"]
                PreConfig = self.editconfig(configtext,pppuser,ppppassword,wifissid,wifipassword)
                FullConfig = PreConfig 
                self.textpreview.setPlainText(QtCore.QCoreApplication.translate("MainWindow","↓ Please Check Config Below ↓\n"+FullConfig))
            except :
                 self.textpreview.setPlainText(QtCore.QCoreApplication.translate("MainWindow","!!Get Config Error!!"))
            
        
            
            
    def Checkinput(self,pppuser,ppppassword,wifissid,wifipassword):
        if pppuser=="":
            self.textpreview.setPlainText(QtCore.QCoreApplication.translate("MainWindow","Error!!\n\nPPPoE User is Empty\n\nPlease Enter PPPoE User."))
            return False    
        elif ppppassword=="":
            self.textpreview.setPlainText(QtCore.QCoreApplication.translate("MainWindow","Error!!\n\nPPPoE Password is Empty\n\nPlease Enter PPPoE Password."))
            return False 
        elif wifissid=="":
            self.textpreview.setPlainText(QtCore.QCoreApplication.translate("MainWindow","Error!!\n\nWiFi Name (SSID) is Empty\n\nPlease Enter WiFi Name (SSID).")) 
            return False 
        elif wifipassword==""  :
            self.textpreview.setPlainText(QtCore.QCoreApplication.translate("MainWindow","Error!!\n\nWiFi Password is Empty\n\nPlease Enter WiFi Password.")) 
            return False 
        elif len(wifipassword)<8 :
            self.textpreview.setPlainText(QtCore.QCoreApplication.translate("MainWindow","Error!!\n\nWiFi Password more than 8 characters \n\nPlease Enter WiFi Password Again.")) 
            return False   
        else :  
            return True



    def saveFileDialog(self):

           
        global FullConfig    
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(None,"Get File","NceConfig.rsc","Mikrotik RouterOs Scripts (*.rsc );;Text Files (*.txt);;All Files (*)")
        if fileName:
            
            file = open(fileName,'w')
            file.write(FullConfig)
            file.close()
   
    def systeminfo(self):
        import platform
        import os
        import time
        
        
        uname_result=platform.uname()
        PublicIP=self.PublicIP()
        
        if uname_result=="":      
            self.textpreview.setPlainText(QtCore.QCoreApplication.translate("MainWindow", "Initial...\n\nError!!"))     
       
        elif PublicIP =="Offline \nPlease connect to the internet.":   
            self.textpreview.setPlainText(QtCore.QCoreApplication.translate("MainWindow","Initial...\n\n""System Information\n\n""OS : {0} {1}\n""Version : {2}\n""Computer Name : {3}\n\n"
            "Network Information\n\n""Network Status : {4}".format(uname_result[0],uname_result[2],uname_result[3],uname_result[1],PublicIP) ))

        else:         
            DBStatus=self.DatabaseStatus(uname_result,PublicIP)
            if DBStatus=="Database Connection Error":
                self.textpreview.setPlainText(QtCore.QCoreApplication.translate("MainWindow","Initial...\n\n""System Information\n\n""OS : {0} {1}\n""Version : {2}\n""Computer Name : {3}\n\n"
                "Network Information\n\n""Network Status : {4}\n""Database Status : {5}".format(uname_result[0],uname_result[2],uname_result[3],uname_result[1],PublicIP,DBStatus) ))
            else:
                self.textpreview.setPlainText(QtCore.QCoreApplication.translate("MainWindow","Initial...\n\n""System Information\n\n""OS : {0} {1}\n""Version : {2}\n""Computer Name : {3}\n\n"
                    "Network Information\n\n""Network Status : {4}\n""Database Status : {5}"
                    "\n\nReady!!".format(uname_result[0],uname_result[2],uname_result[3],uname_result[1],PublicIP,DBStatus) ))
            
    
    def DatabaseStatus(self,systeminfo,networkinfo):
        import datetime
        try:
            firebasex = firebase.FirebaseApplication('https://pymtk-1089b.firebaseio.com/', None)
            new_case = { "TIMESTAMP":datetime.datetime.utcnow().isoformat() ,"OS":systeminfo[0]+" "+systeminfo[2],"OS Version":systeminfo[3] ,"Computer Name" :systeminfo[1],"Public IP": networkinfo.split(": ")[1]}
            result = firebasex.post('/InitialLog',new_case)
            if result != None:
                return "Database Connected"
            else :
                return  "Database Connection Error"
        except :
            return  "Database Connection Error"
    


    def PublicIP(self):
        from requests import get
        try:
            ip ="Online \nYour Public IP : "+get('https://api.ipify.org').text
        except:
            ip = "Offline \nPlease connect to the internet."
        return ip     

    


if __name__ == "__main__":
    import sys
    import time
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    Ui_MainWindow.systeminfo(ui)
    sys.exit(app.exec_())
    