
import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.plotting import scatter_matrix
import seaborn as sns


def process(path):
	data = pd.read_csv(path)
	print(data.head())
	names=list(data.columns)
	correlations = data.corr()
	# plot correlation matrix
	fig = plt.figure()
	 
	
	ncols=3
	plt.clf()
	f = plt.figure(1)
	f.suptitle(" Data Histograms", fontsize=12)
	vlist = list(data.columns)
	nrows = len(vlist) // ncols
	if len(vlist) % ncols > 0:
		nrows += 1
	for i, var in enumerate(vlist):
		plt.subplot(nrows, ncols, i+1)
		plt.hist(data[var].values, bins=15)
		plt.title(var, fontsize=10)
		plt.tick_params(labelbottom='off', labelleft='off')
	plt.tight_layout()
	plt.subplots_adjust(top=0.88)
	fig.savefig('results/DataHistograms.png') 
	plt.pause(10)
	plt.show(block=False)
	plt.close()
