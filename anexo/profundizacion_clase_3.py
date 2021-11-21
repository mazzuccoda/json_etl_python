import json
import requests
import numpy as np
import re as re
import matplotlib.pyplot as plt

def fetch(page_number, location_id):
    url = "https://jsonmock.hackerrank.com/api/transactions/search?txnType=debit&page={}".format(page_number)
    
    response = requests.get(url)
    data = response.json()
    
    #lista = [{"userId":x["userId"],"amount":x["amount"]} for x in data["data"] if x["location"]["id"]== location_id]
    
    lista2 = [{"userId":x["userId"],"amount":float(re.sub(r'[^\d\-.]', '', x["amount"]))} for x in data["data"] if x["location"]["id"]== location_id]
    
    return lista2


def consolidar(data):

    user_id_unicos = np.unique([x["userId"] for x in data])
    
    lista_suma = []
    
    for x in range(len(user_id_unicos)):
        
        suma = [y["amount"] for y in data if y["userId"]== user_id_unicos[x] ]      
        
        lista_suma.append([user_id_unicos[x],np.sum(suma)])
    
    return lista_suma    

def reporte(data):
    x = [x[0] for x in data]
    y = [ y[1] for y in data]

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.bar(x,y)  
    plt.show()

if __name__ == '__main__':
    print("Ejercicio profundización clase 3")

 

dataset =  fetch(1,7)  

print(dataset)

print(consolidar(dataset))

reporte(consolidar(dataset))