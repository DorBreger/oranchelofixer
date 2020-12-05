import os
from cairosvg import svg2svg

def splitter(text, filters):
	splitted = []
	counter = 0
	for letterindex in range(len(text)):
		if text[letterindex] in filters:
			splitted.append(text[counter:letterindex])
			splitted.append(text[letterindex])
			counter = letterindex+1

	return splitted






def fix_file(file):
	try: # acommodating for all of the broken symlinks
		fileobject =open(file, "r+")
		fileobject.close()		
	except FileNotFoundError:
		return None
	else:
		try:
			svg2svg(url=file)
		except :
			fileobject = open(file, 'r')
			filedsmnld = fileobject.readlines()
			fileobject.close()
			filedsmnld = ''.join(filedsmnld)
			filedsmnld = splitter(filedsmnld, [" ", "\n"])
			newfile = open(file, "w")
			in_svgtag = False
			for i in range(len(filedsmnld)):
				if filedsmnld[i] ==  "<svg":
					in_svgtag = True
				if filedsmnld[i][-1] == '>'and in_svgtag:
					filedsmnld.insert(i, 'xmlns:osb="http://www.openswatchbook.org/uri/2009/osb" ')
					break # just in case 


			filedsmnld = ''.join(filedsmnld)
			newfile.write(filedsmnld)
			newfile.close()







def main(path):
	for  filename in os.listdir(path):
		if path == ".":
			if os.path.isdir(filename):
				main(filename + "/")
			elif filename.endswith(".svg")and path != ".":
				fix_file(path  + filename)
							
			
		else:
			if os.path.isdir(path + filename):
				main(path + filename + "/")
			elif filename.endswith(".svg")and path != ".":
				fix_file(path  + filename)
			






main(".")
