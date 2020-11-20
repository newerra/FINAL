import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from BD import bel, ugl, kal, name, zir
from PyQt5.QtCore import Qt
from PIL import Image
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from BD import bel, ugl, kal, name, zir  # Импортируем переменые из программы с БД
from PyQt5.QtCore import Qt
from PIL import Image
from scrpts import dvizenye, velosiped  # Импортируем файлы с функциями нахождения калорий
from QT_PY import MainWindow, BegF, Vel, PerevodF, PlavanyeF, FoodF, Calc  # Импортируем файлы с дизайном


class Food(QMainWindow, FoodF):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        for i in name:
            self.produkt.addItem(i)
        self.produkt.activated.connect(self.pass_Net_Adap)
        self.grammovka.textChanged[str].connect(self.onChanged)
        self.vicheslit.clicked.connect(self.vich)
        self.sbros.clicked.connect(self.swbros)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F1:
            f = open('help_food', 'r')
            print('INFO_ERROR')
        if event.key() == Qt.Key_Q:
            image = Image.open('BUBA.jpg')
            image.show()
            print('Буба')

    def vich(self):
        self.f = name.index(self.produkt.currentText())
        self.b = int(bel[self.f])
        self.z = int(zir[self.f])
        self.k = int(kal[self.f])
        self.u = int(ugl[self.f])
        self.bw = (self.b / 100) * self.mnoz
        self.zw = (self.z / 100) * self.mnoz
        self.kw = (self.k / 100) * self.mnoz
        self.uw = (self.u / 100) * self.mnoz
        self.belki.display(self.bw)
        self.kalorii.display(self.kw)
        self.uglevodi.display(self.uw)
        self.zhiri.display(self.zw)

    def pass_Net_Adap(self):
        self.f = name.index(self.produkt.currentText())
        self.b = int(bel[self.f])
        self.z = int(zir[self.f])
        self.k = int(kal[self.f])
        self.u = int(ugl[self.f])
        self.belki.display(self.b)
        self.kalorii.display(self.k)
        self.uglevodi.display(self.u)
        self.zhiri.display(self.z)

    def onChanged(self, text):
        if text == '':
            text = 100
        self.mnoz = int(text)
        print(self.mnoz)

    def swbros(self):
        self.mnoz = 0
        self.b = 0
        self.z = 0
        self.k = 0
        self.u = 0
        self.f = name.index(self.produkt.currentText())
        self.belki.display(self.b)
        self.kalorii.display(self.k)
        self.uglevodi.display(self.u)
        self.zhiri.display(self.z)
        self.grammovka.setText('0')


class Sport(QMainWindow, Calc):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        pol = ['Мужской', 'Женский']
        self.polt = True
        self.caloris = 0
        self.valuerost = 1
        self.valueves = 1
        self.vid_sporta.clicked.connect(self.on_clickBeg)
        self.vid_sporta_2.clicked.connect(self.on_clickVel)
        for i in pol:
            self.floor_pol.addItem(i)
        self.pushButton.clicked.connect(self.getValue)
        self.pushButton_2.clicked.connect(self.Sbrosvalue)
        self.vid_sporta_5.clicked.connect(self.Plavan)

    def Ves(self):
        f = int(self.valueves)
        return f

    def Rost(self):
        f = int(self.valuerost)
        return f

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F1:
            f = open('help_sport', 'r')
            print('INFO_ERROR')
        if event.key() == Qt.Key_Q:
            image = Image.open('BUBA.jpg')
            image.show()
            print('Буба')

    def on_clickBeg(self):
        self.window_of_seeing_all = Beg()
        self.window_of_seeing_all.show()

    def on_clickVel(self):
        self.window_of_seeing_all = Velos()
        self.window_of_seeing_all.show()

    def getValue(self):
        self.valueves = self.ves.value()
        self.valuerost = self.rost.value()
        self.valueAge = self.Age.value()
        pol = self.floor_pol.currentText()
        print(self.valueAge, self.valueves, self.valuerost)
        if pol == "м":
            self.polt = True
        else:
            self.polt = False
        if pol:
            self.caloris = 66.5 + 13.75 * self.valueves + 5.003 * self.valuerost - 6.775 * self.valueAge
        else:
            self.caloris = 655.1 + 9.563 * self.valueves + 1.85 * self.valuerost - 4.676 * self.valueAge
        self.caloris = int(self.caloris)
        round(self.caloris)
        self.caloris = str(self.caloris)
        self.Kolvo_kaloriy.setText(self.caloris)

    def Plavan(self):
        self.window_of_seeing_all = Plavan()
        self.window_of_seeing_all.show()

    def Sbrosvalue(self):
        self.Kolvo_kaloriy.setText('0')
        self.ves.setValue(0)
        self.rost.setValue(0)
        self.Age.setValue(0)


class Beg(QMainWindow, BegF):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ves = sp.Ves()
        self.rost = sp.Rost()
        print(self.ves)
        print(self.rost)
        self.lineEdit_2.textChanged[str].connect(self.onChangedVr)
        self.lineEdit.textChanged[str].connect(self.onChangedRast)
        self.pushButton.clicked.connect(self.getValue)
        self.pushButton_2.clicked.connect(self.Sbrosvalue)

    def onChangedVr(self, text):
        if text == '':
            text = 0
        self.Vrema = int(text)
        print(self.Vrema)

    def onChangedRast(self, text):
        if text == '':
            text = 0
        self.Rast = int(text)
        print(self.Rast)

    def getValue(self):
        R = self.Rast
        V = self.Vrema
        ro = int(self.rost)
        ve = int(self.ves)
        self.caloris = dvizenye(R, V, ro, ve)
        self.caloris = int(self.caloris)
        round(self.caloris)
        self.caloris = str(self.caloris)
        self.lineEdit_3.setText(self.caloris)

    def Sbrosvalue(self):
        self.lineEdit_3.setText('0')
        self.lineEdit_2.setText('')
        self.lineEdit.setText('')


def keyPressEvent(self, event):
    if event.key() == Qt.Key_F1:
        f = open('help_beg.txt', 'r')
        print('INFO_ERROR')
    if event.key() == Qt.Key_Q:
        image = Image.open('BUBA.jpg')
        image.show()
        print('Буба')


class Velos(QMainWindow, Vel):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ves = sp.Ves()
        self.lineEdit_4.textChanged[str].connect(self.onChangedPl)
        self.lineEdit_2.textChanged[str].connect(self.onChangedVr)
        self.pushButton.clicked.connect(self.getValue)
        self.pushButton_2.clicked.connect(self.Sbrosvalue)

    def onChangedVr(self, text):
        if text == '':
            text = 0
        self.Vrema = int(text)
        print(self.Vrema)

    def onChangedPl(self, text):
        if text == '':
            text = 100
        self.Pl = int(text)
        print(self.Pl)

    def getValue(self):
        v = self.Vrema
        ro = self.Pl
        ve = self.ves
        self.caloris = velosiped(v, ro, ve)
        print(self.caloris)
        self.caloris = int(self.caloris)
        round(self.caloris)
        self.caloris = str(self.caloris)
        self.lineEdit_3.setText(self.caloris)

    def Sbrosvalue(self):
        self.lineEdit_3.setText('0')
        self.lineEdit_2.setText('')
        self.lineEdit_4.setText('')

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F1:
            f = open('help_veloseped.txt', 'r')
            print('INFO_ERROR')
        if event.key() == Qt.Key_Q:
            image = Image.open('BUBA.jpg')
            image.show()
            print('Буба')


class Menu(QMainWindow, MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sport.clicked.connect(self.menusport)
        self.food.clicked.connect(self.menufood)
        self.pushButton.clicked.connect(self.menuperevod)

    def menusport(self):
        print(101)
        self.window_of_seeing_all = Sport()
        self.window_of_seeing_all.show()

    def actionClicked(self):
        action = self.sender()

    def menufood(self):
        print(202)
        self.window_of_seeing_all = Food()
        self.window_of_seeing_all.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F1:
            f = open('help_menu', 'r')
            print('INFO_ERROR')
        if event.key() == Qt.Key_Q:
            image = Image.open('BUBA.jpg')
            image.show()
            print('Буба')

    def menuperevod(self):
        self.window_of_seeing_all = Perevod()
        self.window_of_seeing_all.show()


class Perevod(QMainWindow, PerevodF):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lineEdit_2.setText('0')
        self.lineEdit.setText('0')
        self.lineEdit_2.textChanged[str].connect(self.onChangedgram)
        self.lineEdit.textChanged[str].connect(self.onChangedkal)
        self.pushButton.clicked.connect(self.kalgr)
        self.pushButton_2.clicked.connect(self.grkal)

    def onChangedgram(self, text):
        if text == '':
            text = 0
        self.gram = text
        print(self.gram)

    def onChangedkal(self, text):
        if text == '':
            text = 0
        self.kal = text
        print(self.kal)

    def grkal(self):
        self.gram = int(self.gram)
        m = self.gram
        F = m * 7.7
        round(F)
        F = str(F)
        self.lineEdit.setText(F)
        self.kal = F

    def kalgr(self):
        self.kal = int(self.kal)
        m = self.kal
        F = m * 7.7
        round(F)
        F = str(F)
        self.lineEdit_2.setText(F)
        self.gram = F


class Plavan(QMainWindow, PlavanyeF):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F1:
            f = open('help_plvaniye', 'r')
            print('INFO_ERROR')
        if event.key() == Qt.Key_Q:
            image = Image.open('BUBA.jpg')
            image.show()
            print('Буба')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    sp = Sport()
    ex.show()
    sys.exit(app.exec_())
