import sys
import hou
import icons
import os
import platform
from PySide2 import QtWidgets,QtGui,QtCore
import kr_houdini
import dep_system


iconpath = "".join(icons.__path__)

class ToolsWidget(QtWidgets.QWidget):
    def __init__(self,*args,**kwargs):
        super(ToolsWidget,self).__init__(*args,**kwargs)

        #ToolsA
        self.ToolsLayout = QtWidgets.QGridLayout(self)
        self.ToolsLayout.setSpacing(15)
        self.ToolsA = QtWidgets.QPushButton("Set_Dependency")
        self.ToolsA.setIcon(QtGui.QPixmap(iconpath + '/' + 'dependency.png'))
        self.ToolsA.setIconSize(QtCore.QSize(50,50))
        self.ToolsA.setFixedSize(200,80)
        self.ToolsA.setStyleSheet("color: White ; font-size 13pt;")

        self.ToolsA.clicked.connect(self.Set_Dep)

        #ToolsB
        self.ToolsB = QtWidgets.QPushButton("RenderSet")
        self.ToolsB.setIcon(QtGui.QPixmap(iconpath + '/' + 'Renderset.png'))
        self.ToolsB.setIconSize(QtCore.QSize(50,50))
        self.ToolsB.setFixedSize(200,80)
        self.ToolsB.setStyleSheet("color: White ; font-size 13pt;")

        self.ToolsB.clicked.connect(self.Set_Renderset)

        #ToolsC
        self.ToolsC = QtWidgets.QPushButton("Add_Pallete",self)
        self.ToolsC.setIcon(QtGui.QPixmap(iconpath + '/' + 'EmptyPalette.png'))
        self.ToolsC.setIconSize(QtCore.QSize(50,50))
        self.ToolsC.setFixedSize(200,80)
        self.ToolsC.setStyleSheet("color: White ; font-size 13pt;")

        self.ToolsC.clicked.connect(self.Set_Palette)


        #ToolsD
        self.ToolsD = QtWidgets.QPushButton("Add_RenderPallete",self)
        self.ToolsD.setIcon(QtGui.QPixmap(iconpath + '/' + 'Package.png'))
        self.ToolsD.setIconSize(QtCore.QSize(50,50))
        self.ToolsD.setFixedSize(200,80)
        self.ToolsD.setStyleSheet("color: White ; font-size 13pt;")

        self.ToolsD.clicked.connect(self.Set_RenderPalette)


        #ToolsE
        self.ToolsE = QtWidgets.QPushButton("Set_Alien",self)
        self.ToolsE.setIcon(QtGui.QPixmap(iconpath + '/' + 'Alien.svg'))
        self.ToolsE.setIconSize(QtCore.QSize(50,50))
        self.ToolsE.setFixedSize(200,80)
        self.ToolsE.setStyleSheet("color: White ; font-size 13pt;")

        self.ToolsE.clicked.connect(self.SetAlien)

        #ToolsF
        self.ToolsF = QtWidgets.QPushButton("Set_Pyro",self)
        self.ToolsF.setFixedSize(200,80)
        self.ToolsF.setStyleSheet("color: White ; font-size 13pt;")
        self.ToolsF.setIcon(QtGui.QPixmap(iconpath + '/' + 'Fire.png'))
        self.ToolsF.setIconSize(QtCore.QSize(50,50))

        self.ToolsF.clicked.connect(self.SetPyro)

        #ToolsG
        self.ToolsG = QtWidgets.QPushButton("MotionTrail",self)
        self.ToolsG.setIcon(QtGui.QPixmap(iconpath + '/' + 'M_trail.png'))
        self.ToolsG.setIconSize(QtCore.QSize(50,50))
        self.ToolsG.setFixedSize(200,80)
        self.ToolsG.setStyleSheet("color: White ; font-size 13pt;")

        self.ToolsG.clicked.connect(self.Trail)


        #--7#Self.ScrollArea&Tools
        self.ToolsLayout.addWidget(self.ToolsA,0,0)
        self.ToolsLayout.addWidget(self.ToolsB,0,1)
        self.ToolsLayout.addWidget(self.ToolsC,1,0)
        self.ToolsLayout.addWidget(self.ToolsD,1,1)
        self.ToolsLayout.addWidget(self.ToolsE,2,0)
        self.ToolsLayout.addWidget(self.ToolsF,2,1)
        self.ToolsLayout.addWidget(self.ToolsG,3,0)


    def Set_Dep(self):
        try:
            dep_system.createDepsys("obj")
        except:
            pass

    def Set_Renderset(self):
        try:
            kr_houdini.BaseRenderSet()
        except:
            pass

    def Set_Palette(self):
        try:
            kr_houdini.palette()
        except:
            pass

    def Set_RenderPalette(self):
        try:
            kr_houdini.render_palette()
        except:
            pass


    def SetAlien(self):
        try:
            kr_houdini.setAlienSim(1)
        except:
            pass

    def SetPyro(self):
        try:
            kr_houdini.setPyroSim(1)
        except:
            pass

    def Trail(self):
        try:
            kr_houdini.MotionTrail()
        except:
            pass
            
