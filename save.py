import xmltodict
from xmltodict import parse as import_xml
from xmltodict import unparse as export_xml
import os

path=os.getcwd()

def create():
	save_file = open(path+"/save.xml", "w+")
	save_file.close()
 
def export(): #create a seperate save file containing the current save data
	export_file = open(path+"/export.xml", "w+")
	export_file.write(open(path+"/save.xml", "r").read())
	export_file.close()
 
def save(): #save the current save data
	save_file = open(path+"/save.xml", "w+")
	save_file.write(export_xml(save_data))

def load(): #load the current save data
	global save_data
	save_data = import_xml(open(path+"/save.xml", "r").read())
 
def createProfile(name,playerName,difficulty): #create a new profile
	save_data[name]={
		playerName:playerName,
		difficulty:difficulty 
	 }
	
	

	
