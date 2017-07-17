####insert data into mysql
import MySQLdb

class con:
	def __init__(self):
		conn= MySQLdb.connect(
        		host='127.0.0.1',
        		port = 3306,
        		user='root',
        		passwd='',
        		db ='user_info',
        		)
		self.conn=conn
		self.cur=self.conn.cursor()
	def execute(self,str1):
		self.result=self.cur.execute(str1)
		if str1.find('insert')>=0 or str1.find('update')>=0:
			print('the insert line or a update line')
		if str1.find('select')>=0:
			print self.cur.fetchall()
	def close(self):
		self.cur.close()
		self.conn.commit()
		self.conn.close()
	
