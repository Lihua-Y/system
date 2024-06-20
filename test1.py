import sys

from PySide6.QtGui import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QVBoxLayout, QLabel, QSizePolicy
from PySide6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # 左侧菜单背景框架
        self.LeftMenuBg = QFrame(self)
        self.LeftMenuBg.setObjectName("LeftMenuBg")
        self.LeftMenuBg.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.LeftMenuBg.setGeometry(0, 0, 200, 400)

        # 顶部Logo信息框架
        self.TopLogoInfo = QFrame(self.LeftMenuBg)
        self.TopLogoInfo.setObjectName("TopLogoInfo")
        self.TopLogoInfo.setEnabled(True)
        self.TopLogoInfo.setMinimumSize(QSize(0, 70))
        self.TopLogoInfo.setMaximumSize(QSize(16777215, 70))
        self.TopLogoInfo.setFrameShape(QFrame.StyledPanel)
        self.TopLogoInfo.setFrameShadow(QFrame.Raised)
        self.TopLogoInfo.setStyleSheet("background-color: rgb(70, 70, 70);")

        # 布局管理器
        layout = QVBoxLayout(self.LeftMenuBg)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.TopLogoInfo)

        # 添加一个标签到顶部Logo信息框架
        label = QLabel("Logo Here", self.TopLogoInfo)
        label.setStyleSheet("color: white;")
        label.setAlignment(Qt.AlignCenter)

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Main Window Example")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
