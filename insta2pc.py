import sys, time, os
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QPushButton,QLabel,QGroupBox,QLineEdit,QApplication,QMainWindow,QMessageBox
from PyQt5.QtGui import QIcon,QFont
from selenium import webdriver
import chromedriver_autoinstaller

"""
    bin 디렉토리로 부터 필요한 함수 모듈 가져옴
"""
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from bin import onePostMultiPics
from bin import oneAccAllThumbs
from bin import oneAccAllPics
app = QApplication(sys.argv)

"""
    하나의 게시물에 있는 여러 사진을 다운로드하는 클래스
"""
class OnePost_MultiPics(QThread):
    finished=pyqtSignal() # 다운로드 작업이 끝났는지 여부에 대한 signal
    fuzzed=pyqtSignal() # 오류 여부에 대한 signal
    btn_onoff=pyqtSignal(int) # 버튼 on/off 조절 signal
    def __init__(self,parent=None):
        super().__init__()
        self.mainGUI=parent
    def run(self):
        url=self.mainGUI.urlBox.text()
        id=self.mainGUI.idBox.text()
        pw=self.mainGUI.pwBox.text()
        path=chromedriver_autoinstaller.install(cwd=True)
        driver = webdriver.Chrome(path)
        time.sleep(1)
        try:
            onePostMultiPics.onepost_multi_download(driver,url,id,pw)
        except: # 다운로드 중간에 오류가 생기면 안전하게 중단
            driver.quit()
            self.fuzzed.emit()
            self.btn_onoff.emit(1)
            self.mainGUI.btn1.setText("게시물하나의 모든사진 가져오기")
        else:
            self.finished.emit()
            self.btn_onoff.emit(1)
            self.mainGUI.btn1.setText("게시물하나의 모든사진 가져오기")

"""
    하나의 게시물에 있는 여러 사진을 다운로드하는 클래스
    (이하 소스내용은 OnePost_MultiPics 와 동일)
"""
class OneAcc_AllThumbs(QThread):
    finished=pyqtSignal()
    fuzzed=pyqtSignal()
    btn_onoff=pyqtSignal(int)
    def __init__(self,parent=None):
        super().__init__()
        self.mainGUI=parent
    def run(self):
        url=self.mainGUI.urlBox.text()
        id=self.mainGUI.idBox.text()
        pw=self.mainGUI.pwBox.text()
        path=chromedriver_autoinstaller.install(cwd=True)
        driver = webdriver.Chrome(path)
        time.sleep(1)
        try:
            oneAccAllThumbs.oneacc_all_thumbs_download(driver,url,id,pw)
        except:
            driver.quit()
            self.fuzzed.emit()
            self.btn_onoff.emit(1)
            self.mainGUI.btn1.setText("게시물하나의 모든사진 가져오기")
        else:
            driver.quit()
            self.finished.emit()
            self.btn_onoff.emit(1)
            self.mainGUI.btn2.setText("계정하나의 모든 썸네일 가져오기")

class OneAcc_AllPics(QThread):
    finished=pyqtSignal()
    btn_onoff=pyqtSignal(int)
    def __init__(self,parent=None):
        super().__init__()
        self.mainGUI=parent
    def run(self):
        url=self.mainGUI.urlBox.text()
        id=self.mainGUI.idBox.text()
        pw=self.mainGUI.pwBox.text()
        path=chromedriver_autoinstaller.install(cwd=True)
        driver = webdriver.Chrome(path)
        driver.get(url)
        time.sleep(2)
        oneAccAllPics.oneacc_all_pics_download(driver,url,id,pw)
        driver.quit()
        self.finished.emit()
        self.btn_onoff.emit(1)
        self.mainGUI.btn3.setText("계정하나의 모든 사진들 가져오기")

class MyWindow(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        # QMainWindow 의 멤버함수
        self.initUI()
    def initUI(self):
        self.setWindowTitle("insta2pc v1.04.18.")
        self.setWindowIcon(QIcon("./static/insta2pc_con.ico"))
        self.setGeometry(700, 200, 400, 700)
        self.setFixedSize(400,700)
        self.initTitle()
        self.urlBar()
        self.accountBar()
        # 버튼1
        self.btn1=QPushButton("게시물하나의 모든사진 가져오기",self)
        self.btn1.move(20,300) # 정가운데
        self.btn1.resize(360,60)
        self.btn1.clicked.connect(self.get_MultiPics_from_onePost)
        # 버트2
        self.btn2=QPushButton("계정하나의 모든 썸네일 가져오기",self)
        self.btn2.move(20,370)
        self.btn2.resize(360,60)
        self.btn2.clicked.connect(self.get_AllThumbs_from_oneAcc)
        # 2021.12.15. 임시 비활성화
        # self.btn3=QPushButton("계정하나의 모든 사진들 가져오기",self)
        # self.btn3.move(20,440)
        # self.btn3.resize(360,60)
        # self.btn3.clicked.connect(self.get_AllPics_from_oneAcc)
    def initTitle(self):
        # Title Label
        self.title=QLabel("Insta2pc",self)
        self.title.move(80,30)
        self.title.resize(220,55) 
        self.title.setStyleSheet("color: #FF5733; border-style: solid; border-width: 2px; border-color: #FFC300; border-radius: 10px;")
        self.title_font=self.title.font()
        self.title_font.setPointSize(30)
        self.title_font.setFamily('HY헤드라인M')
        self.title.setFont(self.title_font)
        # Version Label
        self.version=QLabel("v1.04.18.",self)
        self.version.move(300,30)
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
        self.pwBox.setEchoMode(QLineEdit.Password)
        self.pwBox.setPlaceholderText('PW를 입력해주세요')
        self.pwBox.move(200,220)
        self.pwBox.resize(170,25)
    def input_checking(self):
        if(self.urlBox.text()==''):
            self.warn("url")
            return 0
        if(self.idBox.text()=='' or self.pwBox.text()==''):
            self.warn("account")
            return 0
        return 1
    def enabling_btn(self,n):
        if(n):
            self.btn1.setEnabled(True)
            self.btn2.setEnabled(True)
            #self.btn3.setEnabled(True)
        else:
            self.btn1.setEnabled(False)
            self.btn2.setEnabled(False)
            #self.btn3.setEnabled(False)
            
    def get_MultiPics_from_onePost(self): # 모든 기능은 해당 구문을 따르도록
        if(self.input_checking()):
            self.enabling_btn(0)
            self.btn1.setText("잠시만기다려주세요...")
            self.th=OnePost_MultiPics(self)
            self.th.btn_onoff.connect(self.enabling_btn)
            self.th.fuzzed.connect(lambda:QMessageBox.critical(self,"insta2pc","오류로 인해 중단되었습니다!"))
            self.th.finished.connect(lambda:QMessageBox.information(self,"insta2pc","다운이 완료되었습니다!"))
            self.th.start()
    def get_AllThumbs_from_oneAcc(self):
        if(self.input_checking()):
            self.enabling_btn(0)
            self.btn2.setText("잠시만기다려주세요...")
            self.th=OneAcc_AllThumbs(self)
            self.th.btn_onoff.connect(self.enabling_btn)
            self.th.finished.connect(lambda:QMessageBox.information(self,"insta2pc","다운이 완료되었습니다!"))
            self.th.start()
    def get_AllPics_from_oneAcc(self):
        if(self.input_checking()):
            self.enabling_btn(0)
            self.btn3.setText("잠시만기다려주세요...")
            self.th=OneAcc_AllPics(self)
            self.th.btn_onoff.connect(self.enabling_btn)
            self.th.finished.connect(lambda:QMessageBox.information(self,"insta2pc","다운이 완료되었습니다!"))
            self.th.start()
    def warn(self,text):
        if(text=="url"):
            QMessageBox.question(self,'Warning','url 을 입력해주세요!',QMessageBox.Yes,QMessageBox.NoButton)
        if(text=="account"):
            QMessageBox.question(self,'Warning','계정을 입력해주세요!',QMessageBox.Yes,QMessageBox.NoButton)
            
window = MyWindow()
window.show()
app.exec_() # To avoid confliction with the earlier version of 'exec()'...