#coding: utf-8
import pymysql
con = pymysql.connect('localhost','root', 'factos1048576') # conecta no servidor
con.select_db('odonto') # seleciona o banco de dados
cursor = con.cursor()
#cursor.execute("INSERT INTO ALUNO values ('CARALHACILDO', 20159007758,'RenatoAlmeida','minhasenha')")
#cursor.execute("SELECT * FROM ALUNO WHERE nome = 'CARALHACILDO'")
#rs = cursor.fetchone()
#print (rs)

def login():
	log = input("Login:\t")
	passw = input("Senha:\t")
	cursor.execute ("SELECT * FROM PROFESSOR WHERE lsigaa = '" + log + "'")
	rs = cursor.fetchone()
	if (rs != None):
		print ("Tenta acesso como professor\n")
		if (rs[3]==passw):
			print("Autenticado como professor\n")
			if (log == 'root'):
				print ("loga como root\n")
				#loginroot()
			else:
				print ("loga como prof")
				#loginprof()
		else: 
			print ("Senha incorreta\n")
	else:
		print ("Tenta acesso como aluno")
		cursor.execute ("SELECT * FROM ALUNO WHERE lsigaa = '" + log + "'")
		rs = cursor.fetchone()
		if (rs == None):
			print ("Login não encontrado!\n")
		else:
			if (rs[3]==passw):
				print ("Autenticado como aluno")
				#loginaluno()



while (True):
	login ()
