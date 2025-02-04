# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os

from PySide6.QtCore import QCoreApplication, QLocale, QMetaObject, QObject, QSize, Qt, Signal
from PySide6.QtGui import QIcon, QImage, QPixmap
from PySide6.QtWidgets import (QGraphicsView, QGridLayout, QHBoxLayout,
                               QLabel, QLayout, QPlainTextEdit, QPushButton,
                               QSizePolicy, QSpinBox, QTabWidget, QVBoxLayout,
                               QWidget, QFileDialog, QGraphicsScene)
from PIL import Image
from PIL.ImageQt import ImageQt

from steganography import Prestige


class UIMainWidget(QObject):
    cover_image_selected = Signal(object)

    def setupUi(self, MainWidget):
        if not MainWidget.objectName():
            MainWidget.setObjectName(u"MainWidget")
        MainWidget.resize(1029, 680)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWidget.sizePolicy().hasHeightForWidth())
        MainWidget.setSizePolicy(sizePolicy)
        MainWidget.setMinimumSize(QSize(1024, 680))
        MainWidget.setMouseTracking(False)
        MainWidget.setWindowOpacity(1.0)
        MainWidget.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout_3 = QHBoxLayout(MainWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.tabWidget = QTabWidget(MainWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Triangular)

        self.encoderTab = QWidget()
        self.encoderTab.setObjectName(u"encoderTab")
        sizePolicy.setHeightForWidth(self.encoderTab.sizePolicy().hasHeightForWidth())
        self.encoderTab.setSizePolicy(sizePolicy)

        self.gridLayout_2 = QGridLayout(self.encoderTab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.encoderLayout = QVBoxLayout()
        self.encoderLayout.setObjectName(u"encoderLayout")
        self.encoderLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.encoderGraphLayout = QHBoxLayout()
        self.encoderGraphLayout.setObjectName(u"encoderGraphLayout")

        self.coverLayout = QVBoxLayout()
        self.coverLayout.setObjectName(u"coverLayout")
        self.coverGraphicsView = QGraphicsView(self.encoderTab)
        self.coverGraphicsView.setObjectName(u"coverGraphicsView")
        sizePolicy.setHeightForWidth(self.coverGraphicsView.sizePolicy().hasHeightForWidth())
        self.coverGraphicsView.setSizePolicy(sizePolicy)

        self.coverLayout.addWidget(self.coverGraphicsView)

        self.selectCoverButton = QPushButton(self.encoderTab)
        self.selectCoverButton.setObjectName(u"selectCoverButton")
        # PS: QIcon.fromTheme() get the theme name directly
        icon = QIcon.fromTheme("camera-photo")
        self.selectCoverButton.setIcon(icon)
        self.selectCoverButton.clicked.connect(self.select_cover_image)
        self.cover_image_selected.connect(self.handle_cover_image_selected)

        self.coverLayout.addWidget(self.selectCoverButton)

        self.encoderGraphLayout.addLayout(self.coverLayout)

        self.stegoLayout = QVBoxLayout()
        self.stegoLayout.setObjectName(u"stegoLayout")
        self.stegoGraphicsView = QGraphicsView(self.encoderTab)
        self.stegoGraphicsView.setObjectName(u"stegoGraphicsView")
        sizePolicy.setHeightForWidth(self.stegoGraphicsView.sizePolicy().hasHeightForWidth())
        self.stegoGraphicsView.setSizePolicy(sizePolicy)

        self.stegoLayout.addWidget(self.stegoGraphicsView)

        self.stegoPushButton = QPushButton(self.encoderTab)
        self.stegoPushButton.setObjectName(u"stegoPushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stegoPushButton.sizePolicy().hasHeightForWidth())
        self.stegoPushButton.setSizePolicy(sizePolicy1)
        icon1 = QIcon.fromTheme("document-save")
        self.stegoPushButton.setIcon(icon1)
        self.stegoPushButton.clicked.connect(self.save_stego_image)

        self.stegoLayout.addWidget(self.stegoPushButton)

        self.encoderGraphLayout.addLayout(self.stegoLayout)

        self.encoderLayout.addLayout(self.encoderGraphLayout)

        self.encoderConfigLayout = QVBoxLayout()
        self.encoderConfigLayout.setObjectName(u"encoderConfigLayout")
        self.textEditLayout = QHBoxLayout()
        self.textEditLayout.setObjectName(u"textEditLayout")
        self.encoderPlainTextEdit = QPlainTextEdit(self.encoderTab)
        self.encoderPlainTextEdit.setObjectName(u"encoderPlainTextEdit")

        self.textEditLayout.addWidget(self.encoderPlainTextEdit)

        self.encoderConfigLayout.addLayout(self.textEditLayout)

        self.encoderRunLayout = QHBoxLayout()
        self.encoderRunLayout.setObjectName(u"encoderRunLayout")
        self.encoderBitLabel = QLabel(self.encoderTab)
        self.encoderBitLabel.setObjectName(u"encoderBitLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.encoderBitLabel.sizePolicy().hasHeightForWidth())
        self.encoderBitLabel.setSizePolicy(sizePolicy2)

        self.encoderRunLayout.addWidget(self.encoderBitLabel)

        self.encoderBitSpinBox = QSpinBox(self.encoderTab)
        self.encoderBitSpinBox.setObjectName(u"encoderBitSpinBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(3)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.encoderBitSpinBox.sizePolicy().hasHeightForWidth())
        self.encoderBitSpinBox.setSizePolicy(sizePolicy3)
        self.encoderBitSpinBox.setFrame(True)
        self.encoderBitSpinBox.setMaximum(8)
        self.encoderBitSpinBox.setSingleStep(1)
        self.encoderBitSpinBox.setValue(1)

        self.encoderRunLayout.addWidget(self.encoderBitSpinBox)

        self.hideButton = QPushButton(self.encoderTab)
        self.hideButton.setObjectName(u"hideButton")
        sizePolicy3.setHeightForWidth(self.hideButton.sizePolicy().hasHeightForWidth())
        self.hideButton.setSizePolicy(sizePolicy3)
        self.hideButton.clicked.connect(self.hide_message)

        self.encoderRunLayout.addWidget(self.hideButton)

        self.encoderConfigLayout.addLayout(self.encoderRunLayout)

        self.encoderLayout.addLayout(self.encoderConfigLayout)

        self.gridLayout_2.addLayout(self.encoderLayout, 0, 0, 1, 1)

        self.tabWidget.addTab(self.encoderTab, "")
        self.decoderTab = QWidget()
        self.decoderTab.setObjectName(u"decoderTab")
        self.decoderTab.setEnabled(True)
        sizePolicy.setHeightForWidth(self.decoderTab.sizePolicy().hasHeightForWidth())
        self.decoderTab.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(self.decoderTab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.decoderLayout = QVBoxLayout()
        self.decoderLayout.setObjectName(u"decoderLayout")
        self.decoderGraphLayout = QVBoxLayout()
        self.decoderGraphLayout.setObjectName(u"decoderGraphLayout")
        self.decoderGraphView = QGraphicsView(self.decoderTab)
        self.decoderGraphView.setObjectName(u"decoderGraphView")

        self.decoderGraphLayout.addWidget(self.decoderGraphView)

        self.selectStegoButton = QPushButton(self.decoderTab)
        self.selectStegoButton.setObjectName(u"selectStegoButton")
        self.selectStegoButton.setIcon(icon)
        self.selectStegoButton.clicked.connect(self.select_stego_image)

        self.decoderGraphLayout.addWidget(self.selectStegoButton)

        self.decoderLayout.addLayout(self.decoderGraphLayout)

        self.decoderConfigLayout = QVBoxLayout()
        self.decoderConfigLayout.setObjectName(u"decoderConfigLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.decoderPlainTextEdit = QPlainTextEdit(self.decoderTab)
        self.decoderPlainTextEdit.setObjectName(u"decoderPlainTextEdit")

        self.horizontalLayout.addWidget(self.decoderPlainTextEdit)

        self.decoderConfigLayout.addLayout(self.horizontalLayout)

        self.decoderRunLayout = QHBoxLayout()
        self.decoderRunLayout.setObjectName(u"decoderRunLayout")
        self.decoderBitLabel = QLabel(self.decoderTab)
        self.decoderBitLabel.setObjectName(u"decoderBitLabel")
        sizePolicy2.setHeightForWidth(self.decoderBitLabel.sizePolicy().hasHeightForWidth())
        self.decoderBitLabel.setSizePolicy(sizePolicy2)

        self.decoderRunLayout.addWidget(self.decoderBitLabel)

        self.decoderBitSpinBox = QSpinBox(self.decoderTab)
        self.decoderBitSpinBox.setObjectName(u"decoderBitSpinBox")
        sizePolicy3.setHeightForWidth(self.decoderBitSpinBox.sizePolicy().hasHeightForWidth())
        self.decoderBitSpinBox.setSizePolicy(sizePolicy3)
        self.decoderBitSpinBox.setMaximum(8)
        self.decoderBitSpinBox.setValue(1)

        self.decoderRunLayout.addWidget(self.decoderBitSpinBox)

        self.decodeButton = QPushButton(self.decoderTab)
        self.decodeButton.setObjectName(u"decodeButton")
        sizePolicy3.setHeightForWidth(self.decodeButton.sizePolicy().hasHeightForWidth())
        self.decodeButton.setSizePolicy(sizePolicy3)
        self.decodeButton.clicked.connect(self.decode_message)

        self.decoderRunLayout.addWidget(self.decodeButton)

        self.decoderConfigLayout.addLayout(self.decoderRunLayout)

        self.decoderLayout.addLayout(self.decoderConfigLayout)

        self.gridLayout_3.addLayout(self.decoderLayout, 0, 0, 1, 1)

        self.tabWidget.addTab(self.decoderTab, "")

        self.horizontalLayout_3.addWidget(self.tabWidget)

        self.retranslateUi(MainWidget)

        # Set initial tab (encode)
        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWidget)
        # setupUi

    def retranslateUi(self, MainWidget):
        MainWidget.setWindowTitle(QCoreApplication.translate("MainWidget", u"Steganography LSB", None))
        self.selectCoverButton.setText(QCoreApplication.translate("MainWidget", u"Select Cover", None))
        self.stegoPushButton.setText(QCoreApplication.translate("MainWidget", u"Save Stego", None))
        self.encoderPlainTextEdit.setPlaceholderText(QCoreApplication.translate("MainWidget", u"Please type text that will be hided", None))
        self.encoderBitLabel.setText(QCoreApplication.translate("MainWidget", u"Bit Count", None))
        self.hideButton.setText(QCoreApplication.translate("MainWidget", u"Hide", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.encoderTab), QCoreApplication.translate("MainWidget", u"Encoder", None))
        #if QT_CONFIG(accessibility)
        self.decoderTab.setAccessibleName("")
        #endif // QT_CONFIG(accessibility)
        self.selectStegoButton.setText(QCoreApplication.translate("MainWidget", u"Select Stego", None))
        self.decoderBitLabel.setText(QCoreApplication.translate("MainWidget", u"Bit Count", None))
        self.decodeButton.setText(QCoreApplication.translate("MainWidget", u"Decode", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.decoderTab), QCoreApplication.translate("MainWidget", u"Decoder", None))
        # retranslateUi

    def select_cover_image(self):
        file_name, _ = QFileDialog.getOpenFileName(None, "Select Cover Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if file_name:
            cover_image = Image.open(file_name)
            self.cover_image_selected.emit(cover_image)

    def handle_cover_image_selected(self, cover_image):
        # Compose QPixmap by using temporal file
        self.cover_image = cover_image
        temp_file = "temp_cover_image.png"
        self.cover_image.save(temp_file)
        pixmap = QPixmap(temp_file)


        scene = QGraphicsScene()
        scene.addPixmap(pixmap)
        self.coverGraphicsView.setScene(scene)
        # Fit the image inside GraphView by keeping its aspect ratio
        self.coverGraphicsView.fitInView(scene.itemsBoundingRect(), Qt.KeepAspectRatio)

        # If it need numpy convertion:
        # import numpy as np
        # self.cover_image_np = np.array(cover_image)

        if os.path.exists(temp_file):
            try:
                os.remove(temp_file)
            except Exception as e:
                print("Occured error:", e)
        else:
            print("Not found error:", temp_file)

    def hide_message(self):
        secret_text = self.encoderPlainTextEdit.toPlainText()
        bit_value = self.encoderBitSpinBox.value()

        if not hasattr(self, "cover_image"):
            print("Please select a cover image first!")
            return

        self.stego_image = Prestige.encode(secret_text, self.cover_image.copy(), bit_value)

        qimage = ImageQt(self.stego_image)
        pixmap = QPixmap.fromImage(QImage(qimage))

        scene = QGraphicsScene()
        scene.addPixmap(pixmap)
        self.stegoGraphicsView.setScene(scene)
        self.stegoGraphicsView.fitInView(scene.itemsBoundingRect(), Qt.KeepAspectRatio)

    def save_stego_image(self):
        if not hasattr(self, "stego_image"):
            print("Please compose stego image by hiding process")
            return

        file_name, _ = QFileDialog.getSaveFileName(None, "Save Stego Image", "", "PNG Files (*.png);;JPEG Files (*.jpg *.jpeg);;BMP Files (*.bmp)")
        if file_name:
            try:
                self.stego_image.save(file_name)
                print(f"Image saved: {file_name}")
            except Exception as e:
                print("Image can not be saved", e)

    def select_stego_image(self):
        file_name, _ = QFileDialog.getOpenFileName(
            None,
            "Select Stego Image",
            "",
            "Image Files (*.png *.jpg *.jpeg *.bmp)"
        )
        if file_name:
            stego_image = Image.open(file_name)
            self.stego_image = stego_image 
            
            temp_file = "temp_stego_image.png"
            stego_image.save(temp_file)
            pixmap = QPixmap(temp_file)
            scene = QGraphicsScene()
            scene.addPixmap(pixmap)
            self.decoderGraphView.setScene(scene)
            self.decoderGraphView.fitInView(scene.itemsBoundingRect(), Qt.KeepAspectRatio)

        if os.path.exists(temp_file):
            try:
                os.remove(temp_file)
            except Exception as e:
                print("Occured error:", e)
        else:
            print("Not found error:", temp_file)

    def decode_message(self):
        if not hasattr(self, "stego_image"):
            print("Please select stego image")
            return

        bit_value = self.decoderBitSpinBox.value()

        decoded_message = Prestige.decode(self.stego_image, bit_value)
        self.decoderPlainTextEdit.setPlainText(decoded_message)

