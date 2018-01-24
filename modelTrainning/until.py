#-*- coding:utf8 -*-

import pandas as pd
import datetime
import pickle

from gensim.models import word2vec

import pymysql

'''
set stock isPre label
param: raw stock file
output: save stockinfo into pickle

dataframes: [date, open, close, label]
with index: date
'''


def my_date_parser(dt):
    return datetime.datetime.strptime(dt, "%Y-%m-%d")


def getStockInfo(filename):
    # stock_info = np.load(open("","rb"),)
    stock_info = pd.read_csv(filename, date_parser=my_date_parser, parse_dates=['Date'],
                             usecols=['Date', 'Open', 'Close'], index_col='Date')
    tmp = []
    for index, row in stock_info.iterrows():
        # print(row)
        if row[0] < row[1]:
            tmp.append(1)
        else:
            tmp.append(0)
    stock_info['label'] = tmp
    pickle.dump(stock_info, open("./traindata/stock_info.pkl", "wb"), True)

'''
use textcropus to get word2vec model
param: textcropus
output: word2vec model
        wordsDic ## wordsDic[word] = Array(1*100)
'''
def wordToVec(filename):
    # 加载语料
    sentences = word2vec.LineSentence(filename)
    # 训练skip-gram模型; 默认window=5
    model = word2vec.Word2Vec(sentences, size=100)
    save_model = open("./traindata/word2vecModel", "wb")
    model.save_word2vec_format(save_model, binary=False)

    words = model.index2word

    wordsDic = {}
    for word in words:
        wordsDic[word] = model[word]

    pickle.dump(wordsDic, open("./traindata/wordsDic.pkl","wb"), True)

'''
select from mysql
subWord eventWord objWord time
param: none
output: [{subWord:XX, eventWord:XX, objWord:XX, time: XX}] file
'''
def saveEventTime():
    connection = pymysql.connect(
        host="172.18.219.88",
        port=3306,
        user="qiumy",
        passwd="qiumy",
        db="Reuters_news",
        charset="utf8",
        cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cur:
            sql = "select `subWord`, `eventWord`, `objWord`, `time` from `event_word`"
            cur.execute(sql)
            r = cur.fetchall()
            print(len(r))
    finally:
        connection.close()
    pickle.dump(r, open("./traindata/eventWord_time.pkl","wb"), True)

if __name__ == '__main__':
    # getStockInfo("./rawdata/raw_stock.csv")
    # wordToVec("./rawdata/raw_news.txt")
    saveEventTime()