import pandas as pd
from pandas.io.data import DataReader
from datetime import datetime

nasdaqlist = pd.read_csv(r'brycelist.csv')
symbols = []
for symbol in stocklist.Symbol:
    symbols.append(symbol)
    
stock = []
for symbol in stocklist.Symbol:
    print symbol
    if (symbol.find('^')) == -1 and symbol.find('/') == -1 and symbol.find('BGX') == -1 and symbol.find('BGX') == -1 and symbol.find('CBX') == -1  and symbol.find('CBL^D') == -1 and symbol.find('CBL^E') == -1 and symbol.find('CBX') == -1  and symbol.find('CBL^D') == -1 and symbol.find('CBO') == -1 and symbol.find('ECOM') == -1 and symbol.find('CBA') == -1 and symbol.find('ETX') == -1 and symbol.find('FEI') == -1 and symbol.find('FPL') == -1 and symbol.find('GPRK') == -1 and symbol.find('ONE') == -1 and symbol.find('STAR') == -1 and symbol.find('JMI') == -1 and symbol.find('KMPA') == -1 and symbol.find('KOG') == -1 and symbol.find('JMLP') == -1 and symbol.find('REN') == -1 and symbol.find('ZYY') == -1 and symbol.find('ZZA') == -1 and symbol.find('ZZB') == -1 and symbol.find('ZZ') == -1 and symbol.find('SPB') == -1 and symbol.find('TNET') == -1 and symbol.find('PIH') == -1 and symbol.find('ADXSW') == -1 and symbol.find('AMBCW') == -1 and symbol.find('AQUUW') == -1 and symbol.find('BLIN') == -1 and symbol.find('CAMBW') == -1 and symbol.find('CLACW') == -1 and symbol.find('CATYW') == -1 and symbol.find('CACGW') == -1 and symbol.find('CREG') == -1 and symbol.find('CHSC') == -1 and symbol.find('CISAW') == -1 and symbol.find('COA') == -1 and symbol.find('JACQW') == -1 and symbol.find('CYHHZ') == -1 and symbol.find('CRESW') == -1 and symbol.find('ENZY') == -1 and symbol.find('EAC') == -1 and symbol.find('HART') == -1 and symbol.find('HCACW') == -1 and symbol.find('INXBW') == -1 and symbol.find('ICLDW') == -1 and symbol.find('LLEN') == -1 and symbol.find('LEVYW') == -1 and symbol.find('MEILW') == -1 and not(len(symbol)==5 and (symbol[-1]=='W' or symbol[-1] == 'Z'))  and symbol.find('MEILZ') == -1 and symbol.find('QTETR') == -1 and symbol.find('RDIB') == -1 and symbol.find('SHLDV') == -1 and symbol.find('TORM') == -1 and symbol.find('WETF') == -1 and symbol.find('IBO') == -1 and symbol.find('NTS') == -1 and symbol.find('SAND') == -1 and symbol.find('ZXX') == -1:
        stock.append([symbol, DataReader(symbol, "yahoo", datetime(1800, 1, 1))])