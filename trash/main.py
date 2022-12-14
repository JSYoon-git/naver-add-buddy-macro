# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ver1_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from naver_add_buddy_class import NAVER_ADD_BUDDY
import webbrowser


class Ui_Form(object):
    def setupUi(self, Form):
        # qt designer
        Form.setObjectName("Form")
        Form.setFixedSize(506, 337)

        self.formLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 490, 321))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_id = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_id.setObjectName("label_id")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_id)
        self.edit_id = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.edit_id.setText("")
        self.edit_id.setObjectName("edit_id")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.edit_id)
        self.label_pw = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_pw.setObjectName("label_pw")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_pw)
        self.edit_pw = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.edit_pw.setText("")
        self.edit_pw.setObjectName("edit_pw")
        self.edit_pw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.edit_pw)
        self.btn_login = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.btn_login.setObjectName("btn_login")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.btn_login)
        self.formLayout_2.setLayout(
            1, QtWidgets.QFormLayout.LabelRole, self.formLayout_3
        )
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_keyword = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_keyword.setObjectName("label_keyword")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.label_keyword
        )
        self.edit_keyword = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.edit_keyword.setText("")
        self.edit_keyword.setObjectName("edit_keyword")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.edit_keyword)
        self.label_add_buddy_cnt = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_add_buddy_cnt.setObjectName("label_add_buddy_cnt")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.label_add_buddy_cnt
        )
        self.label_cnt = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_cnt.setObjectName("label_cnt")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_cnt)
        self.edit_each_buddy_cnt = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.edit_each_buddy_cnt.setObjectName("edit_each_buddy_cnt")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.edit_each_buddy_cnt
        )
        self.label_page = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_page.setObjectName("label_page")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_page)
        self.edit_page = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.edit_page.setObjectName("edit_page")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.edit_page)
        self.edit_add_buddy_cnt = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.edit_add_buddy_cnt.setText("")
        self.edit_add_buddy_cnt.setObjectName("edit_add_buddy_cnt")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.edit_add_buddy_cnt
        )
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.formLayout)
        self.edit_content = QtWidgets.QTextEdit(self.formLayoutWidget_2)
        self.edit_content.setObjectName("edit_content")
        self.formLayout_2.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.edit_content
        )
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_start = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.btn_start.setObjectName("btn_start")
        self.verticalLayout.addWidget(self.btn_start)
        self.btn_start1 = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.btn_start1.setObjectName("btn_start1")
        self.verticalLayout.addWidget(self.btn_start1)
        self.btn_guitar = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.btn_guitar.setObjectName("btn_guitar")
        self.verticalLayout.addWidget(self.btn_guitar)
        self.formLayout_2.setLayout(
            3, QtWidgets.QFormLayout.FieldRole, self.verticalLayout
        )
        self.list_buddy = QtWidgets.QListWidget(self.formLayoutWidget_2)
        self.list_buddy.setObjectName("list_buddy")
        self.formLayout_2.setWidget(
            2, QtWidgets.QFormLayout.SpanningRole, self.list_buddy
        )
        self.title = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.title.setObjectName("title")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.title)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # disable
        self.edit_keyword.setDisabled(True)
        self.edit_page.setDisabled(True)
        self.edit_each_buddy_cnt.setDisabled(True)
        self.edit_add_buddy_cnt.setDisabled(True)

        self.list_buddy.setDisabled(True)
        self.list_buddy.setDisabled(True)
        self.btn_start.setDisabled(True)
        self.btn_start1.setDisabled(True)
        # callbacks
        self.btn_login.clicked.connect(self.naver_login)
        self.btn_start.clicked.connect(self.get_parsing)
        self.btn_start1.clicked.connect(self.add_buddy)
        self.list_buddy.itemDoubleClicked.connect(self.double_click_event)
        # naver add buddy class
        self.naver_macro = NAVER_ADD_BUDDY()
        self.url_list = []

    def naver_login(self):
        id_ = self.edit_id.text()
        pw = self.edit_pw.text()
        self.naver_macro.login(ID=id_, PW=pw)
        # disable
        self.btn_login.setDisabled(True)
        self.edit_id.setDisabled(True)
        self.edit_pw.setDisabled(True)
        # able
        self.edit_page.setDisabled(False)
        self.edit_keyword.setDisabled(False)
        self.list_buddy.setDisabled(False)
        self.btn_start.setDisabled(False)

    def get_parsing(self):
        self.list_buddy.clear()
        if not self.edit_page.text():
            page = 1
        else:
            page = self.edit_page.text()

        if not self.edit_keyword.text():
            keyword = "?????????"
        else:
            keyword = self.edit_keyword.text()

        a, b, list_b = self.naver_macro.get_blogs_url(
            keyword=keyword, page_cnt=int(page)
        )
        self.list_buddy.addItems(list_b)

        self.url_list = list_b

        # able
        self.edit_each_buddy_cnt.setDisabled(False)
        self.edit_add_buddy_cnt.setDisabled(False)
        self.btn_start1.setDisabled(False)

    def double_click_event(self):
        webbrowser.open(str(self.list_buddy.currentItem().text()))

    def add_buddy(self):
        if not self.edit_each_buddy_cnt.text():
            max_buddy = 100
        else:
            max_buddy = int(self.edit_each_buddy_cnt.text())

        if not self.edit_add_buddy_cnt.text():
            wanted_buddy = 1
        else:
            wanted_buddy = int(self.edit_add_buddy_cnt.text())

        if wanted_buddy > 100:
            wanted_buddy = 100

        if not self.edit_content.toPlainText():
            content = "?????? ??????????????????."
        else:
            content = self.edit_content.toPlainText()

        self.naver_macro.add_buddy(
            url_list=self.url_list,
            content=content,
            max_buddy=max_buddy,
            wanted_buddy=wanted_buddy,
        )
        del self.naver_macro

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "????????? ?????? ?????? ?????? ???????????? ver1.2"))
        self.label_id.setText(_translate("Form", "?????????"))
        self.edit_id.setPlaceholderText(_translate("Form", "????????? ?????????"))
        self.label_pw.setText(_translate("Form", "????????????"))
        self.edit_pw.setPlaceholderText(_translate("Form", "????????? ????????????"))
        self.btn_login.setText(_translate("Form", "?????????"))
        self.label_keyword.setText(_translate("Form", "?????????"))
        self.edit_keyword.setPlaceholderText(_translate("Form", "??????) ??????"))
        self.label_add_buddy_cnt.setText(_translate("Form", "?????? ?????? ???"))
        self.label_cnt.setText(_translate("Form", "?????? ??? ??????"))
        self.edit_each_buddy_cnt.setPlaceholderText(_translate("Form", "??????) 100 ~"))
        self.label_page.setText(_translate("Form", "????????? "))
        self.edit_page.setPlaceholderText(_translate("Form", "??????) 1~10"))
        self.edit_add_buddy_cnt.setPlaceholderText(_translate("Form", "?????? 200??? ?????? ??????"))
        self.btn_start.setText(_translate("Form", "?????????"))
        self.btn_start1.setText(_translate("Form", "????????????"))
        self.btn_guitar.setText(_translate("Form", "??????"))
        self.title.setText(_translate("Form", "????????? ?????? ?????? ?????? ???????????? ver1.2"))
        self.edit_content.setText("?????? ?????? ????????????~!")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")

    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
