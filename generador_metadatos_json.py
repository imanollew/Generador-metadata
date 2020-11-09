
import pandas as pd
import os
import json


def GenerarJson(archivo):
	df = pd.read_csv(archivo)
	columnas=df.columns.tolist()
	dic={"recurso":{
			"displayName":archivo,
			"description":" ",
			"attributesDescription": []
			},
		"organizacion":{
			"name":" "
			}
		}
	listaTipos=[]
	for i in columnas:
		dic['recurso']['attributesDescription'].append({"title": i,"description":i, "type": "string"})
		#print(i)
	#print(len(dic['recurso']['attributesDescription']))
	print(dic)
	return dic






listaArchivos=os.listdir()
listaArchivos.remove('generador_metadatos_json.py')
print(listaArchivos)
for a in listaArchivos:
	myjson=GenerarJson(a)
	#print(json.dumps(jsonn, indent=3))
	x = open ("metadata_"+a+".json", "w")
	x.write(json.dumps(myjson, indent=3))
	x.close()
	




