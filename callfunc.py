#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
__author__ = "Ahirton Lopes"
__copyright__ = "Copyright 2015/2016/2017, Mackenzie University"
__credits__ = ["Ahirton Lopes", "Rodrigo Pasti", "Leandro de Castro"]
__license__ = "None"
__version__ = "1.0"
__maintainer__ = "Ahirton Lopes"
__email__ = "ahirton.xd@gmail.com"
"""

import text_processing as tp


'''
-----------------------------------------------------------------------------------------------------------------------
(1) TESTE DO PROCESSADOR TEXTUAL
-----------------------------------------------------------------------------------------------------------------------
'''

docsTokenized = tp.tokenize(['Governo de SP vai pagar 25 mil a quem denunciou suspeito de matar ambulante no metro. Secretaria de Seguranca Publica fixou valor nesta quarta (18) no Diario Oficial.'])
#print(docsTokenized)

#docsTokenizedSentence = tp.tokenize_sentence(['Governo de SP vai pagar 25 mil a quem denunciou suspeito de matar ambulante no metro. Secretaria de Seguranca Publica fixou valor nesta quarta (18) no Diario Oficial.'])
#print(docsTokenizedSentence)

docsTagged = tp.tagging(docsTokenized)
print (docsTagged)

#docsRemovedTerms = tp.remove_words_with((docsTokenized),['Governo'])
#print(docsRemovedTerms)

#docsStopwordRemoval = tp.remove_stopwords(docsTokenized)
#print(docsStopwordRemoval)

#docsStemming = tp.stemming(docsTokenized)
#print(docsStemming)

#docsLowercase = tp.text_lower(docsTokenized)
#print(docsLowercase)

#docsRemovePunctuation = tp.remove_punctuation(docsTokenized)
#print(docsRemovePunctuation)









