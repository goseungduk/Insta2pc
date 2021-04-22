import sys, time, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QFont
from selenium import webdriver
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from bin import onePostMultiPics
# 멀티스레딩 요함 

'''
QtWidgets 모듈에는 QApplication 클래스가 정의되어 있습니다. 해당 클래스에 대한 객체를 생성합니다. 
이때 현재 소스코드 파일에 대한 경로를 담고 있는 파이썬 리스트를 클래스의 생성자로 전달합니다. 
PyQt5를 이용한 모든 프로그램은 반드시 QApplication 객체를 생성해야합니다.
'''
app = QApplication(sys.argv) # gui.py 전달

'''
QMainWindow 주춧돌 역할함. 상속받아옴.
생성자의 행동은 QMainWindow 의 상속자.
'''
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # QMainWindow 의 멤버함수
        self.initUI()
    def initUI(self):
        self.setWindowTitle("insta2pc v1.04.18.")
        self.setWindowIcon(QIcon("../static/insta2pc_con.ico"))
        self.setGeometry(700, 200, 400, 700)
        self.setFixedSize(400,700)
        self.initTitle()
        self.urlBar()
        self.accountBar()
        # 버튼1
        self.btn1=QPushButton("게시물하나의 모든사진 가져오기",self)
        self.btn1.move(20,300) # 정가운데
        self.btn1.resize(360,60)
        self.btn1.clicked.connect(self.btn_clicked)
    def initTitle(self):
        # Title Label
        self.title=QLabel("Insta2pc",self)
        self.title.move(100,30)
        self.title.resize(180,50) 
        self.title.setStyleSheet("color: #FF5733; border-style: solid; border-width: 2px; border-color: #FFC300; border-radius: 10px;")
        self.title_font=self.title.font()
        self.title_font.setPointSize(30)
        self.title_font.setFamily('HY헤드라인M')
        self.title.setFont(self.title_font)
        # Version Label
        self.version=QLabel("v1.04.18.",self)
        self.version.move(295,30)
        self.version.resize(60,20)
        self.version.setStyleSheet("color: #FF5733;")
    def urlBar(self):
        url_gb=QGroupBox("URL",self)
        url_gb.move(20,120)
        url_gb.resize(360,60)
        self.url_gb_font=QFont()
        self.url_gb_font.setPointSize(13)
        self.url_gb_font.setFamily('휴먼매직체')
        url_gb.setFont(self.url_gb_font)
        self.urlBox=QLineEdit(self)
        self.urlBox.setPlaceholderText('계정 혹은 게시물의 URL을 입력해주세요') 
        self.urlBox.move(30,140)
        self.urlBox.resize(340,25)
    def accountBar(self):
        acc_gb=QGroupBox("Account",self)
        acc_gb.move(20,200)
        acc_gb.resize(360,60)
        self.acc_gb_font=QFont()
        self.acc_gb_font.setPointSize(13)
        self.acc_gb_font.setFamily('휴먼매직체')
        acc_gb.setFont(self.acc_gb_font)
        self.idBox=QLineEdit(self)
        self.idBox.setPlaceholderText('ID를 입력해주세요')
        self.idBox.move(30,220)
        self.idBox.resize(150,25)
        self.pwBox=QLineEdit(self)
        self.pwBox.setPlaceholderText('PW를 입력해주세요')
        self.pwBox.move(200,220)
        self.pwBox.resize(170,25)

    def btn_clicked(self):
        if(self.urlBox.text()==''):
            self.warn("url")
            return 0
        if(self.idBox.text()=='' or self.pwBox.text()==''):
            self.warn("account")
            return 0
        self.onePost()
        
    def onePost(self):
        url=self.urlBox.text()
        id=self.idBox.text()
        pw=self.pwBox.text()
        driver=webdriver.Chrome("../chromedriver.exe")
        driver.get(url)
        time.sleep(2)
        onePostMultiPics.onepost_multi_download(driver,url,id,pw)
        driver.quit()

    def warn(self,text):
        if(text=="url"):
            QMessageBox.question(self,'Warning','url 을 입력해주세요!',QMessageBox.Yes,QMessageBox.NoButton)
        if(text=="account"):
            QMessageBox.question(self,'Warning','계정을 입력해주세요!',QMessageBox.Yes,QMessageBox.NoButton)
window = MyWindow()
window.show()

'''
이벤트 루프가 시작되면 GUI 프로그램은 사용자가 '닫기' 버틑을 누를 때 까지 종료하지 않고 계속 실행됩니다. 
이벤트 루프는 반복문 내에서 사용자로 부터 입력되는 이벤트를 처리하기 때문에 그 이름이 '이벤트 루프' 인 것입니다.
'''
app.exec_()