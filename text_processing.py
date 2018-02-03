# -*- coding: utf-8 -*-

"""
__author__ = "Ahirton Lopes e Rodrigo Pasti"
__copyright__ = "Copyright 2015/2016/2017, Mackenzie University"
__credits__ = ["Ahirton Lopes", "Rodrigo Pasti", "Leandro de Castro"]
__license__ = "None"
__version__ = "1.0"
__maintainer__ = "Ahirton Lopes"
__email__ = "ahirton.xd@gmail.com"
"""
'''
"""
-----------------------------------------------------------------------------------------------------------------------
FUNÇÕES PARA TRATAMENTO TEXTUAL E FORMATAÇÃO
-----------------------------------------------------------------------------------------------------------------------
"""
'''
import nltk
import semantic_dictionaries
import file_utils
from nltk.corpus import mac_morpho
      
"""
Recebe uma lista de documentos e retorna o tratamento destes na forma de lista
de tokens
"""
def tokenize(documents):
    nDocs = len(documents) # len = Retorna o comprimento (o número de itens) de um objeto
    documentsProcessed = [] # Cria lista para todos os documentos a serem processados
    for iDoc in range(0,nDocs): # Ordenação dos diferentes documentos a serem processados
        documentsProcessed.append(nltk.word_tokenize(documents[iDoc]))
    return documentsProcessed
    
"""
Separa um texto em sentenças (frases) 
"""
def tokenize_sentence(documents):    
    tkr = nltk.data.load('tokenizers/punkt/portuguese.pickle')
    nDocs = len(documents) # len = Retorna o comprimento (o número de itens) de um objeto
    documentsProcessed = [] # Cria lista para todos os documentos a serem processados
    for iDoc in range(0,nDocs): # Ordenação dos diferentes documentos a serem processados    
        documentsProcessed.append(tkr.tokenize(documents[iDoc]))
    return documentsProcessed
    
"""
Executa tagging (análise morfológica de uma lista de documentos)
"""
def tagging(documents):
    nDocs = len(documents)
    documentsProcessed = []
    unigram_tagger = []
    try:        
        unigram_tagger = file_utils.load_object('tagger1','tagger', None)
    except:
        train_set =  mac_morpho.tagged_sents() # Treinamento do tagger via dicionário mac_morpho
        unigram_tagger = nltk.UnigramTagger(train_set) # Aplicação do tagger ao documento
        file_utils.save_object(unigram_tagger, 'tagger1','tagger', None) # Salva os unigramas tagueados a serem dicionados aos documentos processados 
    for iDoc in range(0,nDocs): # Ordenação dos diferentes documentos a serem processados
        documentsProcessed.append(unigram_tagger.tag(documents[iDoc])) # Adiciona à lista a partir da ordenação
    return documentsProcessed

"""
Remove palavras de um documento que contenham algum dos simbolos contidos em 
uma lista de entrada
"""
def remove_words_with(documents,listSym): 

    nDocs = len(documents) # len = Retorna o comprimento (o número de itens) de um objeto
    documentsProcessed = [] # Cria lista para todos os documentos a serem processados
    for iDoc in range(0,nDocs): # Ordenação dos diferentes documentos a serem processados
        tokens = documents[iDoc]
        tokensNR = [] # Cria lista para os tokens gerados
        nTokens = len(tokens) # len = Retorna o comprimento dos tokens gerados
        for iToken in range(0,nTokens):
            foundSymbol = False # Se não é encontrado nenhum símbolo dos explicitados em lista
            for sym in listSym: # Se é encontrado algum dos símbolos explicitados em lista
                if tokens[iToken].find(sym) != -1: # Remove-se apenas o símbolo específico
                    foundSymbol = True
                    break                    
            if foundSymbol == False:
                tokensNR.append(tokens[iToken]) # Senão, reconfigura-se o documento com os tokens originais
        #if len(tokensNR) > 0:
        documentsProcessed.append(tokensNR) # Se sim, reconfigura-se o documento sem os tokens que contém símbolos da lista
    return documentsProcessed
    
"""
Remove stop words de uma lista de documentos com base em dicionário 
(vide semantic_dictionaries)
"""
def remove_stopwords(documents):
    nDocs = len(documents) # len = Retorna o comprimento (o número de itens) de um objeto
    documentsProcessed = [] # Cria lista para todos os documentos a serem processados
    stopwords = semantic_dictionaries.stop_words() #+ semantic_dictionaries.stop_words_sincronica() # Indicação das stopwords a serem utilizadas, via dicionários 
    for iDoc in range(0,nDocs): # Ordenação dos diferentes documentos a serem processados
        tokens = documents[iDoc] # Lista para verificação dos tokens gerados via documentos       
        #stop words para cada token do documento corrente
        nTokens = len(tokens) # len = Retorna o comprimento dos tokens gerados
        importantWords = []        
        for iToken in range(0,nTokens): # Para cada token gerado segundo ordenação            
            if tokens[iToken] not in stopwords: # Verificar se cada token é ou não stopword
                importantWords.append(tokens[iToken]) # Se for stopword, processa-se como palavra importante
        documentsProcessed.append(importantWords) # Reconfigura-se o documento e mostra-se as stopwords encontradas
    return documentsProcessed

"""
Executa a redução de palavras flexionadas (ou às vezes derivadas) 
ao seu mínimo radical, geralmente uma forma da palavra escrita.
"""    
def stemming(documents):#,lang):
    nDocs = len(documents) # len = Retorna o comprimento (o número de itens) de um objeto
    documentsProcessed = [] # Cria lista para todos os documentos a serem processados
    stemmer = nltk.stem.RSLPStemmer()
    for iDoc in range(0,nDocs): # Ordenação dos diferentes documentos a serem processados
        tokens = documents[iDoc] # Lista para verificação dos tokens gerados via documentos    
        nTokens = len(tokens) # len = Retorna o comprimento dos tokens gerados
        stemWords = [] # Cria lista de palavras para stemming
        for iToken in range(0,nTokens): # Para cada token gerado segundo ordenação        
            stemWords.append(stemmer.stem(tokens[iToken])) # Processa-se os tokens eleiminando as variações morfológicas de uma palavra (redução)
        tokens = stemWords # Lista para verificação dos tokens gerados (sentenças sem variações morfológicas)
        documentsProcessed.append(tokens) # Reconfigura-se o documento com as as variações morfológicas removidas
    return documentsProcessed

"""
Faz com que todas as palavras da sentença ou documento 
apareçam em lower case. 
"""      
def text_lower(documents):
    nDocs = len(documents) # len = Retorna o comprimento (o número de itens) de um objeto
    documentsProcessed = [] # Cria lista para todos os documentos a serem processados
    for iDoc in range(0,nDocs): # Ordenação dos diferentes documentos a serem processados
        tokens = documents[iDoc] # Lista para verificação dos tokens gerados via documentos
        nTokens = len(tokens) # len = Retorna o comprimento dos tokens gerados
        for iToken in range(0,nTokens): # Para cada token gerado segundo ordenação
            tokens[iToken] = tokens[iToken].lower() # Processa-se os tokens, fazendo com que cada token esteja em letras minúsculas       
        documentsProcessed.append(tokens) # Reconfigura-se o documento para que seja apresentado em letras minúsculas
    return documentsProcessed


"""
Remoção dos sinais de pontuação.
"""        
def remove_punctuation(documents):  
    nDocs = len(documents) # len = Retorna o comprimento (o número de itens) de um objeto
    documentsProcessed = [] # Cria lista para todos os documentos a serem processados
    for iDoc in range(0,nDocs): # Ordenação dos diferentes documentos a serem processados
        tokens = documents[iDoc] # Lista para verificação dos tokens gerados via documentos
        tokensNR = [] # Cria lista para os tokens a serem apresentados quando do processamento do documento
        nTokens = len(tokens) # len = Retorna o comprimento dos tokens gerados
        for iToken in range(0,nTokens): # Ordenação dos diferentes tokens a serem processados
           # print tokens[iToken].decode('utf-8')           
            punctuation = ',.?!:;"' # Definição dos sinais de pontuação a serem "resgatados" a partir dos tokens do documento
            for sym in punctuation: # Se encontrado símbolo de pontuação
                tokens[iToken] = tokens[iToken].replace(sym,'') # Remoção do símbolo de pontuação
            if len(tokens[iToken]) > 0: # Se ainda restarem outros tokens quando da remoção dos símbolos de pontuação
                tokensNR.append(tokens[iToken]) # Gerar nova apresentação do documento somente com os tokens que não envolvem pontuação
      #  if len(tokensNR) > 0:       
        documentsProcessed.append(tokensNR) # Reconfigura-se o documento para que sejam apresentados somente tais tokens 
    return documentsProcessed 
     #nDocs = len(documentsProcessed)
     #for iDoc in range(0,nDocs):
      #   if len(documentsProcessed[iDoc])<1:
      #      print 'êta, algo deu errado mermão agora pode chorar'
     #return documentsProcessed