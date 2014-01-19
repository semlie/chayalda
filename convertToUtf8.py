import subprocess, os

listoffiles =[]
def conToUtf(top_directory):
	for root, dirs, files in os.walk(top_directory):
		for fil in files:
			
			p = subprocess.Popen(["file", "-bi", os.path.join(root, fil)], stdout=subprocess.PIPE)
			output, err = p.communicate()
			encod=output.split('=')[-1]
			if str(encod) != "utf-8":
				p = subprocess.Popen(["mv", os.path.join(root, fil), os.path.join(root, fil+"veryold")], stdout=subprocess.PIPE)
				listoffiles.append(os.path.join(root, fil+"veryold"))
				print encod , os.path.join(root, fil)
				#p = subprocess.Popen(["rm", os.path.join(root, fil+"veryold")], stdout=subprocess.PIPE)
				output, err = p.communicate()
			for x in listoffiles:
				p = subprocess.Popen(["iconv", "-f", str(encod), '-t','utf8', x,"-o",x.replace('veryold','')], stdout=subprocess.PIPE)
				output, err = p.communicate()
				print x,err,output
			
			# document = open(os.path.join(root, fil)).read() # read the entire document, as one big string
			# yield utils.tokenize(document, lower=True) # or whatever tokenization suits you



if __name__ == '__main__':
	conToUtf('/home/sem/chayadocs/')