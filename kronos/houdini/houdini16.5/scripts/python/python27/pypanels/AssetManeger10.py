import sys
import hou
import icons
import os
import platform
import pypanels.Tools
import kr_houdini
import web

from PySide2 import QtWidgets,QtGui,QtCore


iconpath = "".join(icons.__path__)

class ManegerWindow(QtWidgets.QWidget):
    def __init__(self,*args,**kwargs):
        super(ManegerWindow,self).__init__(*args,**kwargs)


        self.build()


    def build(self):

        self.setStyleSheet(hou.qt.styleSheet())
        self.setProperty("houdiniStyle", True)

        #Base MainLayout
        self.mainLayout = QtWidgets.QVBoxLayout(self)
        self.mainLayout.setAlignment(QtCore.Qt.AlignTop)

        #Title Layout
        self.TitleLayout = QtWidgets.QHBoxLayout()
        self.TitleLayout.setAlignment(QtCore.Qt.AlignLeft| QtCore.Qt.AlignTop)
        self.TitleLayout.setSpacing(10)
        #LVS imgs Layout
        self.LvsimgLayout = QtWidgets.QVBoxLayout(self)
        self.LvsimgLayout.setAlignment(QtCore.Qt.AlignRight| QtCore.Qt.AlignTop)

        #JupmButton Layout
        self.JumpButtonTitleLayout = QtWidgets.QVBoxLayout(self)
        self.JumpButtonTitleLayout.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)

        self.JumpButonLayout = QtWidgets.QGridLayout(self)
        self.JumpButonLayout.setSpacing(15)

        #infomation Layout
        self.infomationLayout =  QtWidgets.QVBoxLayout(self)
        self.infomationLayout.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)


        #PartationLine Layout
        self.LineLayout_A = QtWidgets.QVBoxLayout()
        self.LineLayout_B = QtWidgets.QVBoxLayout()
        self.LineLayout_C = QtWidgets.QVBoxLayout()
        self.LineLayout_D = QtWidgets.QVBoxLayout()
        self.LineLayout_E = QtWidgets.QVBoxLayout()

        #Image Widget
        self.lvsImgWidget = QtWidgets.QLabel(self)
        icon_Lvs = QtGui.QPixmap(iconpath + '/' + 'levius.jpg')
        self.lvsImgWidget.setPixmap(icon_Lvs)

        self.lvsImgWidget.setSizePolicy(QtWidgets.QSizePolicy.Fixed,QtWidgets.QSizePolicy.Fixed)

        #Project TitleWidget
        self.ProjectTitleLayout = QtWidgets.QVBoxLayout(self)
        self.ProjectTitleLayout.setAlignment(QtCore.Qt.AlignCenter|QtCore.Qt.AlignTop)
        self.ProjectTitle = QtWidgets.QLabel("~Projects~LVS~ AssetManeger")
        self.ProjectTitle.setStyleSheet("color: White ; font-size :20pt;")


        #Title Widget&TitleWidget
        self.FontTitleLayout = QtWidgets.QVBoxLayout(self)
        self.FontTitleLayout.setAlignment(QtCore.Qt.AlignCenter|QtCore.Qt.AlignTop)

        self.FontTitle = QtWidgets.QLabel("~User Infomation~")
        self.FontTitle.setStyleSheet("color: White ; font-size :20pt;")

        self.gifA = QtWidgets.QLabel(self)
        self.gifobject = QtGui.QMovie(iconpath + '/' + 'loading_spy.gif')
        self.gifobject.setScaledSize(QtCore.QSize(200,70))
        #self.gifobject.start()
        #self.gifA.setMovie(self.gifobject)
        self.gifA.setAlignment(QtCore.Qt.AlignCenter|QtCore.Qt.AlignTop)



        #JumpButtons
        self.JpTitle = QtWidgets.QLabel(":ProjectsMenu")
        self.JpTitle.setStyleSheet("color: White ; font-size :15pt;")


        self.JumpButton_A =  QtWidgets.QPushButton("Projectpage",self)
        self.JumpButton_A.setIcon(QtGui.QPixmap(iconpath + '/' + 'Browser_icon.png'))
        self.JumpButton_A.setIconSize(QtCore.QSize(30,30))
        #self.JumpButton_A.setFixedWidth(200)
        self.JumpButton_A.setStyleSheet("color: White ; font-size :14pt;")
        self.JumpButton_A.setSizePolicy(QtWidgets.QSizePolicy.Fixed,QtWidgets.QSizePolicy.Fixed)

        self.JumpButton_A.clicked.connect(self.Project_url_Open)

        self.JumpButton_B =  QtWidgets.QPushButton("Shotgun        ",self)
        self.JumpButton_B.setIcon(QtGui.QPixmap(iconpath + '/' + 'Shotgun.png'))
        self.JumpButton_B.setIconSize(QtCore.QSize(30,30))
        #self.JumpButton_B.setFixedWidth(200)
        self.JumpButton_B.setStyleSheet("color: White ; font-size :14pt;")
        self.JumpButton_B.setSizePolicy(QtWidgets.QSizePolicy.Fixed,QtWidgets.QSizePolicy.Fixed)

        self.JumpButton_C =QtWidgets.QPushButton("Help_JP        ",self)
        self.JumpButton_C.setIcon(QtGui.QPixmap(iconpath + '/' + 'houdini_icon01.png'))
        self.JumpButton_C.setIconSize(QtCore.QSize(30,30))
        #self.JumpButton_C.setFixedWidth(200)
        self.JumpButton_C.setStyleSheet("color: White ; font-size :14pt;")
        self.JumpButton_C.setSizePolicy(QtWidgets.QSizePolicy.Fixed,QtWidgets.QSizePolicy.Fixed)

        self.JumpButton_C.clicked.connect(self.Help_url_Open)

        #bgeoAssemble
        self.AssembleLayout = QtWidgets.QVBoxLayout(self)

        self.bgeoAssemble_button = QtWidgets.QPushButton("Assemble",self)
        self.bgeoAssemble_button.setIcon(QtGui.QPixmap(iconpath + '/' + 'Assemble.png'))
        self.bgeoAssemble_button.setStyleSheet("color: White ; font-size :13pt;")
        self.bgeoAssemble_button.setIconSize(QtCore.QSize(110,110))
        self.bgeoAssemble_button.setSizePolicy(QtWidgets.QSizePolicy.Fixed,QtWidgets.QSizePolicy.Fixed)

        self.bgeoAssemble_button.clicked.connect(self.Assemble)



        #FileInfomation
        try:
           info_dict = {":currentUser":os.environ.get("USERNAME"),":Platform":platform.system(),":Version": 'houdini' + hou.applicationVersionString(),
                        ":HipName":hou.hipFile.basename(),":FilePath":hou.hipFile.path(),":JOB":hou.getenv("JOB"),"LatestSaveTime":hou.getenv("_HIP_SAVETIME")}
        except:
           pass
        self.infomation = QtWidgets.QTextEdit(self)
        self.infomation.isReadOnly()
        self.infomation.setFixedWidth(220)
        try:
           self.infomation.setPlainText("Houdini_Help\n:ID  houdini16user\n:Pass  sRkadN29CA\n\n"
                                        +"__Hip infomation__\n"+ "~LatestSaveTime~\n" + str(info_dict["LatestSaveTime"]) +"\n\n:CurrentUser---" + str(info_dict[":currentUser"])
                                        + "\n:Platform---" + str(info_dict[":Platform"]) + "\n:Version---" + str(info_dict[":Version"])+"\n\n__EnviromentVariables__\n"
                                        +"\n:$HIPNAME---\n" +str(info_dict[":HipName"]) + "\n:$HIP---\n"+str(info_dict[":FilePath"])
                                        +"\n$JOB---\n" +str(info_dict[":JOB"]) )
        except:
           self.infomation.setPlainText("pass")
        self.infomation.setSizePolicy(QtWidgets.QSizePolicy.Fixed,QtWidgets.QSizePolicy.Fixed)


        #===ScrollArea
        self.ScrollLayout = QtWidgets.QVBoxLayout(self)
        self.ScrollAreaA = QtWidgets.QScrollArea(self)
        self.ScrollAreaA.ensureVisible(100,100)
        self.inner = pypanels.Tools.ToolsWidget()
        self.ScrollAreaA.setWidget(self.inner)

        self.ScrollLayout.addWidget(self.ScrollAreaA)


        ###LineFrame
        self.LineA =  QtWidgets.QFrame(self)
        self.LineA.setFrameShape(QtWidgets.QFrame.HLine)
        self.LineA.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.LineB =  QtWidgets.QFrame(self)
        self.LineB.setFrameShape(QtWidgets.QFrame.HLine)
        self.LineB.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.LineC =  QtWidgets.QFrame(self)
        self.LineC.setFrameShape(QtWidgets.QFrame.HLine)
        self.LineC.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.LineD =  QtWidgets.QFrame(self)
        self.LineD.setFrameShape(QtWidgets.QFrame.HLine)
        self.LineD.setFrameShadow(QtWidgets.QFrame.Sunken)


        #AddWidget
        #---1 #LineLayout
        self.LineLayout_A.addWidget(self.LineA)
        self.LineLayout_B.addWidget(self.LineB)
        self.LineLayout_C.addWidget(self.LineC)
        self.LineLayout_D.addWidget(self.LineD)
        #---2
        self.ProjectTitleLayout.addWidget(self.ProjectTitle)
        #---3
        self.TitleLayout.addWidget(self.lvsImgWidget)
        #---4
        #JumpButtonsLayout
        self.FontTitleLayout.addWidget(self.gifA)
        self.FontTitleLayout.addWidget(self.FontTitle)
        #Assemble

        self.AssembleLayout.addWidget(self.bgeoAssemble_button)

        self.JumpButtonTitleLayout.addWidget(self.JpTitle)
        self.JumpButonLayout.addWidget(self.JumpButton_A,0,0)
        self.JumpButonLayout.addWidget(self.JumpButton_B,1,0)
        self.JumpButonLayout.addWidget(self.JumpButton_C,2,0)
        #--5#infomation
        self.infomationLayout.addWidget(self.infomation)
        #--6
        self.ProjectLayout = QtWidgets.QHBoxLayout()
        self.ProjectLayout.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.JumpButtonTitleLayout.addLayout(self.JumpButonLayout)

        self.ProjectLayout.addLayout(self.JumpButtonTitleLayout)
        self.ProjectLayout.addLayout(self.AssembleLayout)

        #--8


        #---1
        self.FontTitleLayout.addLayout(self.infomationLayout)
        self.TitleLayout.addLayout(self.FontTitleLayout)

        #---1
        self.mainLayout.addLayout(self.LineLayout_A)
        #---2
        self.mainLayout.addLayout(self.ProjectTitleLayout)
        #---3
        self.mainLayout.addLayout(self.LineLayout_B)
        #---4
        self.mainLayout.addLayout(self.TitleLayout)
        #---5
        self.mainLayout.addLayout(self.LineLayout_C)
        #---6
        self.mainLayout.addLayout(self.ProjectLayout)

        #---7
        self.mainLayout.addLayout(self.LineLayout_D)
        #---8

        self.mainLayout.addLayout(self.ScrollLayout)

        self.setLayout(self.mainLayout)

    def Assemble(self):
        try:
            kr_houdini.Assenble_bgeo()
        except:
            pass

    def Project_url_Open(self):
        try:
            web.kr_browser.OpenBrowser("https://sites.google.com/a/ppi.co.jp/project-pages/home/lvs")
        except:
            pass

    def Help_url_Open(self):
        try:
            web.kr_browser.OpenBrowser("http://houdinifx.jp/aup/houdini16.0/")
        except:
            pass
