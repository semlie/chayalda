import subprocess, os


def conToUtf(top_directory):
	for root, dirs, files in os.walk(top_directory):
		for fil in files:
			
			p = subprocess.Popen(["file", "-bi", os.path.join(root, fil)], stdout=subprocess.PIPE)
			output, err = p.communicate()
			encod=output.split('=')[-1]
			print encod
			# document = open(os.path.join(root, fil)).read() # read the entire document, as one big string
			# yield utils.tokenize(document, lower=True) # or whatever tokenization suits you



if __name__ == '__main__':
	conToUtf('/home/sem/chayadocs/')