import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QCheckBox
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('Activate Cam', self)
        btn2 = QPushButton('Deactivate Cam', self)

        cb1 = QCheckBox('Face', self)
        cb1.move(20, 50)
        #cb1.stateChanged.connect(self.showFace)
        cb2 = QCheckBox('Eyes', self)
        cb2.move(20, 70)
        #cb2.stateChanged.connect(self.showEyes)
        cb3 = QCheckBox('Mask', self)
        cb3.move(20, 90)
        #cb3.stateChanged.connect(self.showMask)

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)

        self.setLayout(vbox)
        self.setWindowTitle('PyQt5_Face_Detector')
        self.setGeometry(100, 100, 800, 800)
        self.show()

    def showFace(self, faceState):
        if faceState == Qt.Checked:
            pass
        else:
            pass

    def showEyes(self, eyesState):
        if eyesState == Qt.Checked:
            pass
        else:
            pass

    def showMask(self, maskState):
        if maskState == Qt.Checked:
            pass
        else:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())