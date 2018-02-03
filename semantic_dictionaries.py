#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = "Rodrigo Pasti e Ahirton Lopes"
__copyright__ = "Copyright 2015/2016/2017, Mackenzie University"
__credits__ = ["Ahirton Lopes", "Rodrigo Pasti", "Leandro de Castro"]
__license__ = "None"
__version__ = "1.0"
__maintainer__ = "Ahirton Lopes"
__email__ = "ahirton.xd@gmail.com"
"""

#Palavras que não agregam semântica alguma ao texto

def stop_words():
    sw = ['a', 'o', 'que', 'e', 'do', 'da', 'em', 'um', 'para', 'é', 'com',
    'não', 'uma', 'os', 'no', 'se', 'na', 'por', 'mais', 'as', 'dos', 'como', 
    'mas', 'foi', 'ao', 'ele', 'das', 'tem', 'à', 'seu', 'sua', 'ou', 'ser',
    'quando', 'muito', 'há', 'nos', 'já', 'está', 'eu', 'também', 'só', 'pelo',
    'pela', 'até', 'isso', 'ela', 'entre', 'era', 'depois', 'sem', 'mesmo', 
    'aos', 'ter', 'seus', 'quem', 'nas', 'me', 'esse', 'eles', 'estão', 'você', 
    'tinha', 'foram', 'essa', 'num', 'nem', 'suas', 'meu', 'às', 'minha', 'têm', 
    'numa', 'pelos', 'elas', 'havia', 'seja', 'qual', 'será', 'nós', 'tenho', 
    'lhe', 'deles', 'essas', 'esses', 'pelas', 'este', 'fosse', 'dele', 'tu', 
    'te',  'vocês', 'vos', 'lhes', 'meus', 'minhas', 'teu', 'tua', 'teus', 'tuas',
    'nosso', 'nossa', 'nossos', 'nossas', 'dela', 'delas', 'esta', 'estes', 'estas', 
    'aquele', 'aquela', 'aqueles', 'aquelas', 'isto', 'aquilo', 'estou', 'está',
    'estamos', 'estão', 'estive', 'esteve', 'estivemos', 'estiveram', 'estava',
    'estávamos', 'estavam', 'estivera', 'estivéramos', 'esteja', 'estejamos',
    'estejam', 'estivesse', 'estivéssemos', 'estivessem', 'estiver', 'estivermos',
    'estiverem', 'hei', 'há', 'havemos', 'hão', 'houve', 'houvemos', 'houveram', 
    'houvera', 'houvéramos', 'haja', 'hajamos', 'hajam', 'houvesse', 'houvéssemos',
    'houvessem', 'houver', 'houvermos', 'houverem', 'houverei', 'houverá', 'houveremos',
    'houverão', 'houveria', 'houveríamos', 'houveriam', 'sou', 'somos', 'são', 'era',
    'éramos', 'eram', 'fui', 'foi', 'fomos', 'foram', 'fora', 'fôramos', 'seja', 'sejamos',
    'sejam', 'fosse', 'fôssemos', 'fossem', 'for', 'formos', 'forem', 'serei',
    'será', 'seremos', 'serão', 'seria', 'seríamos', 'seriam', 'tenho', 'tem',
    'temos', 'tém', 'tinha', 'tínhamos', 'tinham', 'tive', 'teve', 'tivemos', 
    'tiveram', 'tivera', 'tivéramos', 'tenha', 'tenhamos', 'tenham', 'tivesse',
    'tivéssemos', 'tivessem', 'tiver', 'tivermos', 'tiverem', 'terei', 'terá',
    'teremos', 'terão', 'teria', 'teríamos', 'teriam']

    return sw


