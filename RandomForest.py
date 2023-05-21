import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
#from sklearn.externals import joblib
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from sklearn.metrics import accuracy_score
import joblib


def process(path):

	#importing the dataset
	dataset = pd.read_csv("datasets/phishcoop.csv")
	dataset = dataset.drop('id', 1) #removing unwanted column

	x = dataset.iloc[ : , :-1].values
	y = dataset.iloc[:, -1:].values

	#spliting the dataset into training set and test set
	x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.25, random_state =0 )

	#----------------applying grid search to find best performing parameters 
	parameters = [{'n_estimators': [100, 700],'max_features': ['sqrt', 'log2'],'criterion' :['gini', 'entropy']}]

	grid_search = GridSearchCV(RandomForestClassifier(),  parameters,cv =5, n_jobs= -1)
	grid_search.fit(x_train, y_train)
	#printing best parameters 
	print("Best Accurancy =" +str( grid_search.best_score_))
	print("best parameters =" + str(grid_search.best_params_)) 
	#-------------------------------------------------------------------------

	#fitting RandomForest regression with best params 
	classifier = RandomForestClassifier(n_estimators = 100, criterion = "gini", max_features = 'log2',  random_state = 0)
	classifier.fit(x_train, y_train)

	#predicting the tests set result
	y_pred = classifier.predict(x_test)

	#confusion matrix
	cm = confusion_matrix(y_test, y_pred)
	print(cm)


	#pickle file joblib
	joblib.dump(classifier, 'final_models/rf_final.pkl')


	#-------------Features Importance random forest
	names = dataset.iloc[:,:-1].columns
	importances =classifier.feature_importances_
	sorted_importances = sorted(importances, reverse=True)
	indices = np.argsort(-importances)
	var_imp = pd.DataFrame(sorted_importances, names[indices], columns=['importance'])



	#-------------plotting variable importance
	plt.title("Variable Importances")
	plt.barh(np.arange(len(names)), sorted_importances, height = 0.7)
	plt.yticks(np.arange(len(names)), names[indices], fontsize=7)
	plt.xlabel('Relative Importance')
	plt.savefig('results/RFRelativeImportance.png') 
	plt.pause(10)
	plt.show(block=False)
	plt.close()

	result2=open("results/resultRF.csv","w")
	result2.write("ID,Predicted Value" + "\n")
	for j in range(len(y_pred)):
	    result2.write(str(j+1) + "," + str(y_pred[j]) + "\n")
	result2.close()
	
	mse=mean_squared_error(y_test, y_pred)
	mae=mean_absolute_error(y_test, y_pred)
	r2=r2_score(y_test, y_pred)
	
	
	print("---------------------------------------------------------")
	print("MSE VALUE FOR RandomForest IS %f "  % mse)
	print("MAE VALUE FOR RandomForest IS %f "  % mae)
	print("R-SQUARED VALUE FOR RandomForest IS %f "  % r2)
	rms = np.sqrt(mean_squared_error(y_test, y_pred))
	print("RMSE VALUE FOR RandomForest IS %f "  % rms)
	ac=accuracy_score(y_test,y_pred)
	print ("ACCURACY VALUE RandomForest IS %f" % ac)
	print("---------------------------------------------------------")
	

	result2=open('results/RFMetrics.csv', 'w')
	result2.write("Parameter,Value" + "\n")
	result2.write("MSE" + "," +str(mse) + "\n")
	result2.write("MAE" + "," +str(mae) + "\n")
	result2.write("R-SQUARED" + "," +str(r2) + "\n")
	result2.write("RMSE" + "," +str(rms) + "\n")
	result2.write("ACCURACY" + "," +str(ac) + "\n")
	result2.close()
	
	
	df =  pd.read_csv('results/RFMetrics.csv')
	acc = df["Value"]
	alc = df["Parameter"]
	colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
	explode = (0.1, 0, 0, 0, 0)  
	
	fig = plt.figure()
	plt.bar(alc, acc,color=colors)
	plt.xlabel('Parameter')
	plt.ylabel('Value')
	plt.title(' Random Forest Metrics Value')
	fig.savefig('results/RFMetricsValue.png') 
	plt.pause(10)
	plt.show(block=False)
	plt.close()
