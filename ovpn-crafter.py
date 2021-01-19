#!/usr/bin/python3
"""
Name : ovpn-crafter
Author : Althafrhomen
"""
import os , sys

class Crafter:

	def __init__(self,name)
		self.name = name

	def ca_cert(self,file):
	#server ca file extraction
		cacert=open(file,'r')
		ca_crt=cacert.read()
		cacert.close()
		self.ca_crt=ca_crt.strip()
		self.cain=True

	def cl_cert(self,file):
	#client certificate
		cacert=open(file,'r')
		client_crt=cacert.read()
		seting=client_crt.split("BEGIN",1)
		client_crt='-----BEGIN'+seting[1]
		cacert.close()
		self.client_crt=client_crt.strip()
		self.clin=True

	def cl_key(self,file):
	#client key
		cacert=open(file,'r')
		client_key=cacert.read()
		cacert.close()
		self.client_key=client_key.strip()
		self.kyin =True
	def tls(self,file,encryption):
	#encryption key
		cacert=open(file,'r')
		tls_key=cacert.read()
		cacert.close()
		self.tls_key=tls_key.strip()
		self.tlsin= True
		self.type=encryption

	def craft(self):
		#headerfile
		cacert=open('header','r')
		header=cacert.read()
		cacert.close()
		header=header.strip()
		#create a ovpn
		if self.cain and self.clin and self.kyin and tlsin:
			#filename
			filedata=self.name
			ovpn=open(filedata,'w+')
			content=header+"\n<ca>\n"+ca_crt+'\n</ca>\n<cert>\n'+client_crt+'\n</cert>\n<key>\n'+client_key+'\n</key>\n<self.type>\n'+tls_key+'\n</self.type>\n'
			ovpn.write(content)
			ovpn.close()
		elif self.cain and self.clin and self.kyin:
			filedata=self.name
			ovpn=open(filedata,'w+')
			content=header+"\n<ca>\n"+ca_crt+'\n</ca>\n<cert>\n'+client_crt+'\n</cert>\n<key>\n'+client_key+'\n</key>\n'
			ovpn.write(content)
			ovpn.close()
	
		else:
			return False:
	
