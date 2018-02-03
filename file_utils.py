# -*- coding: utf-8 -*-

"""
__author__ = "Rodrigo Pasti"
__copyright__ = "Copyright 2015/2016/2017, Mackenzie University"
__credits__ = ["Ahirton Lopes", "Rodrigo Pasti", "Leandro de Castro"]
__license__ = "None"
__version__ = "1.0"
__maintainer__ = "Ahirton Lopes"
__email__ = "ahirton.xd@gmail.com"
"""

import pickle

#Abre um arquivo texto e coloca 
def textToList1(file_name):
    file = open(file_name, 'r')
    wordsList = []
    for line in file.readlines():        
        line = line[0:line.find('/')]
        #print line
        wordsList.append(line)
    file.close()
    return wordsList
    
def textToList2(file_name):
    file = open(file_name, 'r')
    documents = []
    for line in file.readlines():        
        documents.append(line)
    file.close()
    return documents
    
#Salva um objeto ou estrutura em um arquivo
def save_object(obj, objName, objType,fileNamePath):
    if fileNamePath is None:
        file = open('C:\\Users\\Ahirton\\Desktop\\Python2\OutputFiles\\' + objName + '.' + objType, 'w+') #Modificar de acordo com a pasta criada para o tagger
    else:
        file = open(fileNamePath + objName + '.' + objType, 'w+')
    pickle.dump(obj, file)
    file.close()
    
#Carrega um objeto de um arquivo
def load_object(objName,objType,fileNamePath):
    if fileNamePath is None:
        file = open('C:\\Users\\Ahirton\\Desktop\\Python2\OutputFiles\\' + objName + '.' + objType, 'r') #Modificar de acordo com a pasta criada para o tagger
    else:
        file = open(fileNamePath + objName + '.' + objType, 'r') 
    obj = pickle.load(file)    
    file.close()
    return obj
    
