def sum(a,b):
	#print("Hello")
	#bashCommand = "ls -l /root/"
	bashCommand = "test"
	import subprocess
	import csv
	mylist=[]
	#mylist=output
		
	#way to execute a bash command
	#process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
	#output  =subprocess.call('test', shell=True, executable='/bin/bash')
	#way to execute a bash alias
	#mylist= subprocess.call(['/bin/bash', '-i', '-c', bashCommand])
	output  =subprocess.call('test', shell=True, executable='/bin/bash')
	#output, error = process.communicate()
	#str = "this is string example....wow!!!"
	#print (output.decode('ascii').splitlines())
	#print (mylist[0])
	#print (str.split('\n',100))
	
	#process = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE)
	process  = subprocess.Popen('test' , shell=True, bufsize=0, stdout=subprocess.PIPE)
	#process = subprocess.Popen('test', stdout=subprocess.PIPE)
	stdout, stderr = process.communicate()
	
	reader = csv.DictReader(stdout.decode('ascii').splitlines(),
		                delimiter=' ', skipinitialspace=True,
		                fieldnames=['permissions', 'links',
		                            'owner', 'group', 'size',
		                            'date', 'time', 'name'])
	
	for row in reader:
	    print(row)	
	return a+b

print(sum(1,3))
#import sys
#sys.path.append('/root/p/')
#import file
#file.sum(1,4)

