from shutil import copyfile,rmtree
import tempfile
import tensorflow as tf
import json
import numpy as np
path='D:/GitHub/Roldo/'
def get_data(N,file):
	Y=[]
	X=[]
	out_d=[]
	json_d=open(file, "r").read()
	data=json.loads(json_d)
	p=len(data)-1
	for key, value in data.items():
		temp = [key,{int(k):v for k,v in value.items()}]
		out_d.append(temp)

	for it in range(len(out_d[0][1])):
		item=[]
		for i in range(p):
			item.append(out_d[i][1][it])
		Y.append(out_d[p][1][it])
		X.append(item)
  	return X,Y

class Model:
	def __init__(self,model=None):
		x_test,y_test=get_data(path+'features_extracted_t.json')
		x_train,y_train=get_data(path+'features_extracted.json')
		if model==None:
			self.model=tf.keras.models.Sequential()
			self.model.add(tf.keras.layers.Flatten())
			self.model.add(tf.keras.layers.Dense(400,activation=tf.nn.relu))
			self.model.add(tf.keras.layers.Dense(500,activation=tf.nn.relu))
			self.model.add(tf.keras.layers.Dense(600,activation=tf.nn.relu))
			self.model.add(tf.keras.layers.Dense(400,activation=tf.nn.relu))
			self.model.add(tf.keras.layers.Dense(2,activation=tf.nn.softmax))
		else:
			self.model=tf.keras.models.load_model(model)
		self.model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
  
	def train(self,iterations):
		self.model.fit(x_train,y_train,epochs=iterations)
  
	def predict_from_data(data):
		out=[]
		prediction=self.model.predict(x_test)
		for i in range(len(prediction)):
			out.append(np.argmax(prediction[i]))
		return out
  
  	def predic_from_file_list(self,file_list):
		dirpath = tempfile.mkdtemp()
		for f in file_list:
			copyfile(f, dirpath+f)
		[mid_term_features, wav_file_list, mid_feature_names] =  mF.directory_feature_extraction(dirpath, 0.1,0.1, 0.01, 0.01, compute_beat=False)
		features = np.concatenate((mid_term_features, mid_term_features_nocough))
		rmtree(dirpath)
		return self.predict_from_data(features)
  
  	def predict_test(self):
		prediction=model.predict(x_test)
		for i in range(len(prediction)):
	  		print('prediction:'+str(np.argmax(prediction[i]))+'      expected_val:'+y_test[i])
  
  	def get_stats(self):
		val_loss,val_acc=model.evaluate(x_test,y_test)
		print(val_loss,val_acc)

  	def save(self,file):
		model.save(file)