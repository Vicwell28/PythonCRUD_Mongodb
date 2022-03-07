import pymongo

myclient = pymongo.MongoClient('mongodb+srv://VicWell:vicwell@sandbox.rwi8f.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

mydb = myclient["BaseDeDatosAnimales"]

mycol = mydb["Personas"]


