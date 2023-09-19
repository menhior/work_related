import pandas as pd
import numpy as np

home_ids = []
individual_ids = []
individual_weights = []
sectors = []
viewever_types = []
sample_types = []


with open(r"file_name", 'r') as f:
	lines = f.readlines()
	for line in lines:
		#print(line)
		if str(line[0:7]).startswith('0'):
			home_ids.append(line[1:7])
		else:
			home_ids.append(line[0:7])
		if str(line[7:9]).startswith('0'):
			individual_ids.append(line[8:9])
		else:
			individual_ids.append(line[7:9])
		individual_weights.append(line[9:17])
		sectors.append(line[17:19])
		viewever_types.append(line[19])
		sample_types.append(line[20])
	print(viewever_types)
#print(individual_weights)