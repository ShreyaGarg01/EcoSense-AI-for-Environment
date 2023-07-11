import csv
import json
# import datetime
from datetime import datetime


def make_json(csvFilePath):

	# create a dictionary
	data = []

	with open(csvFilePath, encoding='utf-8') as csvf:
		csvReader = csv.DictReader(csvf)

		for rows in csvReader:
			dic = {}
			dic['Date'] = rows['ds']
			dic['value'] = rows['yhat']
			data.append(dic)
	jsonFilePath = "city_AQI.json"
	with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
		jsonf.write(json.dumps(data, indent=4))
		
# make_json("AQI_Predictions\Bombay_AQI.csv", "city_AQI.json")
