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
import pydot
import graphviz
import tensorflow.python.keras.callbacks
from keras import optimizers

listeFonc=["sgd","adam","Adagrad","RMSprop","Adamax"]
#listeFonc=["tanh","softplus","softsign","relu","sigmoid","linear"]
for element in listeFonc:
	print(element)


seed=7
dataset = csv.reader(open("Alldataset.csv","rt"),delimiter=",")

x = list(dataset)
result = np.array(x)
np.random.shuffle(result)
#here
X = result[:55000,0:8].astype(float)
Y_all= result[:,8]
x_test = result[55000:,0:8].astype(float)

#fit: Ajuster l'encodeur d'étiquettes
#transform: Transformez les étiquettes en codage normalisé.
#codifier target.
objLabel = LabelEncoder()
objLabel.fit(Y_all) #va mapper les labels avec leur codification
Y_codifier=objLabel.transform(Y_all)
#list(objLabel.classes_)
#diviser Y_all en y_train et y_test
y_train= Y_codifier[:55000,]
y_test= Y_codifier[55000:,] #prendre une partie du target pour la phase de validation
print ("y_all codifié")
print (Y_codifier)
print("y_test codifié")
print(y_test)

'''
Converts a class vector (integers) to binary class matrix.

E.g. for use with categorical_crossentropy.
A binary matrix representation of the input.

'''
target_train = np_utils.to_categorical(y_train) 
target_test = np_utils.to_categorical(y_test)

model = Sequential()
model.add(Dense(36,input_dim=8,activation='relu'))

best=0
i=0
for fonction in listeFonc:
	i += 1
	j = 1
	while j<= 2 :
		model.add(Dense(10*i*j,activation='relu'))
		j += 1
	#stat=CSVLogger("stat.log")
	model.add(Dense(4,activation ='softmax'))
	for p in (0,20):
		print('debut entrainement')
		nbiter=50
		# For a multi-class classification problem :loss='categorical_crossentropy'
		while nbiter <= 550:
			nbiter += 50
			model.compile(loss = 'categorical_crossentropy',optimizer=fonction,metrics=['accuracy'])
			history=model.fit(X,target_train,validation_data=(x_test, target_test),epochs=nbiter,batch_size=111)#,callbacks=[stat]) #training data will be randomly shuffled at each epoch.
			scores = model.evaluate(x_test, target_test)#récuperer lost sur l'entrainement 
			exactitude= (scores[1]*100)
			print("\nExactitude sur testing data: %.2f%%" % exactitude)
			if best<scores[1]:
				bestAcc=exactitude.astype(int)
				fichier="C:/Users/TOSHIBA/AppData/Local/Programs/Python/Python36/model"+str(i)+"Acc"+str(bestAcc)+"FT"+fonction+"Epoch"+str(nbiter)+".hd5"
				model.save(fichier)
				print("Saved model to disk")
				plt.plot(history.history['acc'])  
				plt.plot(history.history['val_acc'])  
				plt.title('Model accuracy for best Neural Network')  
				plt.ylabel('accuracy')  
				plt.xlabel('epoch')  
				plt.legend(['Train', 'Test'], loc='upper left') 
				plt.show()
				plt.plot(history.history['loss'])  
				plt.plot(history.history['val_loss'])  
				plt.title('Model loss for best Neural Network')  
				plt.ylabel('loss')  
				plt.xlabel('epoch')  
				plt.legend(['Train', 'Test'], loc='upper left')  
				plt.show()	 
				best=scores[1]
			else:
				print("Nothing")
	print('fin entrainement du model')
print("Fin du training")

loaded_model = load_model(fichier)
loaded_model.compile(loss = 'categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
history=loaded_model.fit(X,target_train,validation_data=(x_test, target_test),epochs=200,batch_size=111)
#training data will be randomly shuffled at each epoch.

plt.plot(history.history['acc'])  
plt.plot(history.history['val_acc'])  
plt.title('model accuracy for best net')  
plt.ylabel('accuracy')  
plt.xlabel('epoch')  
plt.legend(['train', 'test'], loc='upper left') 
plt.show()


plt.plot(history.history['loss'])  
plt.plot(history.history['val_loss'])  
plt.title('model loss for best net')  
plt.ylabel('loss')  
plt.xlabel('epoch')  
plt.legend(['train', 'test'], loc='upper left')  
plt.show()	 

# evaluate loaded model on test data
score = loaded_model.evaluate(x_test,target_test)
print("Exactitude du modele %s: %.2f%%" % (loaded_model.metrics_names[1], score[1]*100))