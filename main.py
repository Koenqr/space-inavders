import pygame
#from save import *
import os
import time

from entities import *

from xmltodict import parse as import_xml
from xmltodict import unparse as export_xml



class mainGame():
	
	def __init__(self):
     
		#check save file
		saveFile="save.xml"
		if os.path.isfile(saveFile):
			save=open(saveFile,"x")
			save.write(export_xml({
				'width':800,
				'height':600,
				'difficulty':0
		  	}))
			save.close()

		#load save file
		file = open(saveFile, "r")
		self.save = import_xml(file)
		file.close()
 
	def mainMenu(self):
		#main menu
		#start game
		#load game
		#options
		#exit
		pass


    
    
    
    
	
 
 
 
 
if __name__=="__main__":
	mainGame()