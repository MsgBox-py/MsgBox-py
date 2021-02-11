from os import system, remove, startfile
from time import sleep
from sys import path
def message(content, windowname, number, getresult=True):
	f = open('MsgBox.vbs', 'w')
	f.write('x=MsgBox(' + "\"" + content + "\"" + ',' + number + ',' + "\"" + windowname + "\"" + ')\nDim fso, oFile\nSet fso = CreateObject("Scripting.FileSystemObject")\nSet oFile = fso.OpenTextFile("Result.txt",  2)\noFile.Write(x)')
	f.close()
	startfile('MsgBox.vbs')
	sleep(0.1)
	remove('MsgBox.vbs')
	result = open('Result.txt')
	if getresult:
		while True:
			a = result.read()
			if a == "":
				pass
			else:
				result.close()
				result = open('Result.txt', 'w')
				result.write("")
				break
		if a == "1":
			return "OK"
		elif a == "2":
			return "Cancel"
		elif a == "3":
			return "Abort"
		elif a == "4":
			return "Retry"
		elif a == "5":
			return "Ignore"
		elif a == "6":
			return True
		elif a == "7":
			return False
	else:
		while True:
			a = result.read()
			if a != "":
				result.close()
				result = open('Result.txt', 'w')
				result.write("")
				result.close()
			else:
				pass


if __name__ == "__main__":
	print(message('This is MsgBox tools! How to use: message(content, windowname, number of MsgBox).', 'How to use', '65'))