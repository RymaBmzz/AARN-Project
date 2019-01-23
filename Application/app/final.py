# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
import Main  # import du fichier gui.py généré par pyuic5
import csv
import numpy as np
import tensorflow as tf
import json

from keras.models import Sequential
from keras.layers import Dense, Activation
from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils
from keras.models import Sequential
from keras.models import load_model
from keras.utils.vis_utils import plot_model
import matplotlib.pyplot as plt
from keras.utils import plot_model


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None,ui=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        if ui is not None:
            self.ui = ui
            self.ui.setupUi(self)
        else:
            self.ui = Main.Ui_MainWindow()
            self.ui.setupUi(self)

        #un clic sur le bouton appellera la méthode 'action_bouton'
            self.ui.pushButton.clicked.connect(self.action_bouton)



      #fonction qui permet d afficher le resultat du target de l instance
    def imageAff(self,j):
        if j == "1":
            self.ui.label_3.setStyleSheet("background-image: url(alit.jpg);")
        #assis sur une chaise
        if j == "2":
            self.ui.label_3.setStyleSheet("background-image: url(chaise.jpg);")
        #allonge sur le lit
        if j == "3":
            self.ui.label_3.setStyleSheet("background-image: url(dort.jpg);")
        # debout,se promener dans la piéce
        if j == "4":
                self.ui.label_3.setStyleSheet("background-image: url(mov.jpg);")

    # fonction qui permet d afficher le resultat de predicte sous forme d une image
    def imageres(self, j):
        if j == 1:
            self.ui.label_6.setStyleSheet("background-image: url(alit.jpg);")
        # assis sur une chaise
        if j == 2:
            self.ui.label_6.setStyleSheet("background-image: url(chaise.jpg);")
        # allonge sur le lit
        if j == 3:
            self.ui.label_6.setStyleSheet("background-image: url(dort.jpg);")
        # debout,se promener dans la piéce
        if j == 4:
            self.ui.label_6.setStyleSheet("background-image: url(mov.jpg);")

    def action_bouton(self):
        #ouvrir le fichier et charger le dataset
        dataset = csv.reader(open("dataTest.csv", "rt"), delimiter=",")
        p = list(dataset)
        X = np.array(p)
        #recupere les donneés test
        x_test = X[:, 0:8].astype(float)
        y_test = X[:, 8]
        #recupere l instance du combBox
        i = self.ui.comboBox.currentIndex()
        #recupere le target de l instance choisi
        j = y_test[i-1]
        #afficher le resultat dans le label cible
        self.imageAff(j)
        #charger le RN
        model = load_model("model.hd5")
        input = np.array(x_test[i-1])
        mat=[]
        mat.append(input)
        mat=np.asarray(mat)
        print(type(input))
        y_pred = model.predict(mat)
        max=y_pred.argmax(axis=1)
        #afficher le resultat de test fait sur l instance choisi
        #appel a la fonction
        self.imageres(max+1)
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())