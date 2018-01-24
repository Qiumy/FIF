#-*- coding:utf-8 -*-
'''
covert news json object to mySQL
'''

import pymysql
import json

def saveSQL():
	connection = pymysql.connect(
		host="172.18.219.88",
		port=3306,
		user="qiumy",
		passwd="qiumy",
		db="stockPre",
		charset="utf8",
		cursorclass=pymysql.cursors.DictCursor)

	try:
		with connection.cursor() as cur:
			sql = "insert into allNews(title, content, time, link, img) values(%s,%s,%s,%s,%s)"

			with open("reuterNews2.json", "r") as f:
				cnt = 0
				for line in f:
					data = json.loads(line)
					cur.execute(sql,(data['title'], data['content'], data['time'], data['link'], data['img']))
					cnt += 1
					if cnt%50==0:
						connection.commit()
		connection.commit()
	finally:
		connection.close()

if __name__ == '__main__':
	saveSQL()