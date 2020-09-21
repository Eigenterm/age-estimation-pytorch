from PyQt5 import QtCore, QtGui, QtWidgets
from Eage import Ui_Dialog
#from PyQt5.QtWidgets import QFileDialog
#from imageedit import imageedit_self
#from bottombutton import button_self
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2, os

cwd = os.getcwd()

class mywindow(QtWidgets.QMainWindow, Ui_Dialog):
    def  __init__ (self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.OpenButton.clicked.connect(self.read_file)#打开
        self.ProcessButton.clicked.connect(self.process_file)#处理
        self.SaveButton.clicked.connect(self.save_file)#保存
        self.CameraButton.clicked.connect(self.camera_open)#打开相机

    def read_file(self):
        filename, filetype =QtWidgets.QFileDialog.getOpenFileName(self, "打开文件", cwd+"\\input\\", "All Files(*)")# ;;Text Files(*.png)
        self.img = cv2.imread(filename)
        cv2.imwrite(cwd+"\\input\\1.jpg",self.img)
        imgshow = QtGui.QPixmap(filename).scaled(self.inputimage.width(), self.inputimage.height())
        self.inputimage.setPixmap(imgshow) 
        

    def process_file(self):
        os.chdir(cwd)
        # os.system(r"cd C:\Users\11323\Desktop\design\age-estimation-pytorch-master&&python demo.py --img_dir input --output_dir output")
        os.system(r"python demo.py --img_dir input --output_dir output")
        
        filename = cwd+"\\output\\1.jpg"
        imgshow = QtGui.QPixmap(filename).scaled(self.inputimage.width(), self.inputimage.height())
        self.outputimage.setPixmap(imgshow)


    def save_file(self):
        filename=QtWidgets.QFileDialog.getSaveFileName(self,'save file',cwd+"\\output\\")
        # print(filename)
        self.img2 = cv2.imread(cwd+"\\output\\1.jpg")
        cv2.imwrite(filename[0]+".jpg",self.img2)

    def camera_open(self):
        os.chdir(cwd)
        os.system(r"python demo.py")

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    ui = mywindow()
    ui.show()
    app.exec_()





        
