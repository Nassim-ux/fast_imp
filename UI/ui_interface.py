# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(823, 482)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"* {\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background:transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #fff;\n"
"	font: 10pt \"Lucida Sans Unicode\";\n"
"}\n"
"#centralwidget {\n"
"	background-color: #1f232a;\n"
"}\n"
"#leftMenuSubContainer{\n"
"	background-color: #16191d;\n"
"}\n"
"#leftMenuSubContainer QPushButton {\n"
"	text-align: left;\n"
"	padding: 5px 10px;\n"
"	color: #fff;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
" QPushButton {\n"
"	color: #fff;\n"
"}\n"
"\n"
"QLabel {\n"
"	color: #fff;\n"
"}\n"
"\n"
"#centerMenuSubContainer {\n"
"	background-color: #2c313c;\n"
"}\n"
"\n"
"#frame_4 {\n"
"	background-color: #16191d;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#headerContainer {\n"
"	background-color: #2c313c;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QWidget(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftMenuSubContainer.sizePolicy().hasHeightForWidth())
        self.leftMenuSubContainer.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.frame = QFrame(self.leftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        font = QFont()
        font.setFamily(u"Lucida Sans Unicode")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.menuBtn.setFont(font)
        self.menuBtn.setIconSize(QSize(14, 14))

        self.horizontalLayout_2.addWidget(self.menuBtn)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.leftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.homeBtn = QPushButton(self.frame_2)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setFont(font)
        self.homeBtn.setAutoFillBackground(False)
        self.homeBtn.setStyleSheet(u"")
        self.homeBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.homeBtn)

        self.reportBtn = QPushButton(self.frame_2)
        self.reportBtn.setObjectName(u"reportBtn")
        self.reportBtn.setFont(font)
        self.reportBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.reportBtn)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 10, 0, 10)
        self.settingsBtn = QPushButton(self.frame_3)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setFont(font)
        self.settingsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.settingsBtn)

        self.infoBtn = QPushButton(self.frame_3)
        self.infoBtn.setObjectName(u"infoBtn")
        self.infoBtn.setFont(font)
        self.infoBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.infoBtn)

        self.helpBtn = QPushButton(self.frame_3)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setFont(font)
        self.helpBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.helpBtn)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuSubContainer, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, Qt.AlignLeft)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy2)
        self.verticalLayout_11 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.horizontalLayout_4 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_5 = QFrame(self.headerContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.backBtn = QPushButton(self.frame_5)
        self.backBtn.setObjectName(u"backBtn")

        self.horizontalLayout_5.addWidget(self.backBtn)

        self.nextBtn = QPushButton(self.frame_5)
        self.nextBtn.setObjectName(u"nextBtn")

        self.horizontalLayout_5.addWidget(self.nextBtn)

        self.reloadBtn = QPushButton(self.frame_5)
        self.reloadBtn.setObjectName(u"reloadBtn")

        self.horizontalLayout_5.addWidget(self.reloadBtn)


        self.horizontalLayout_4.addWidget(self.frame_5, 0, Qt.AlignLeft)

        self.frame_7 = QFrame(self.headerContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.minusBtn = QPushButton(self.frame_7)
        self.minusBtn.setObjectName(u"minusBtn")

        self.horizontalLayout_3.addWidget(self.minusBtn)

        self.squareBtn = QPushButton(self.frame_7)
        self.squareBtn.setObjectName(u"squareBtn")

        self.horizontalLayout_3.addWidget(self.squareBtn)

        self.xcloseBtn = QPushButton(self.frame_7)
        self.xcloseBtn.setObjectName(u"xcloseBtn")

        self.horizontalLayout_3.addWidget(self.xcloseBtn)


        self.horizontalLayout_4.addWidget(self.frame_7, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.headerContainer, 0, Qt.AlignTop)

        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy)
        self.mainBodyContent.setFont(font)
        self.horizontalLayout_6 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(self.mainBodyContent)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout_6.addWidget(self.label, 0, Qt.AlignTop)


        self.verticalLayout_11.addWidget(self.mainBodyContent)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"LOGO", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(tooltip)
        self.reportBtn.setToolTip(QCoreApplication.translate("MainWindow", u"View reports", None))
#endif // QT_CONFIG(tooltip)
        self.reportBtn.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
#if QT_CONFIG(tooltip)
        self.settingsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Go to settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.infoBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Information about the app", None))
#endif // QT_CONFIG(tooltip)
        self.infoBtn.setText(QCoreApplication.translate("MainWindow", u"Information", None))
#if QT_CONFIG(tooltip)
        self.helpBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Get more help", None))
#endif // QT_CONFIG(tooltip)
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.backBtn.setText("")
        self.nextBtn.setText("")
        self.reloadBtn.setText("")
        self.minusBtn.setText("")
        self.squareBtn.setText("")
        self.xcloseBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"File d'attente pour l'impression", None))
    # retranslateUi

