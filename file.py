def sum(a,b):
        #print("Hello")
        #bashCommand = "ls -l /root/"
        bashCommand = "ls -a /root/p/test/"
        import subprocess
        #process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        #output  =subprocess.call('test', shell=True, executable='/bin/bash')
        output = subprocess.call(['/bin/bash', '-i', '-c', bashCommand])
        #output, error = process.communicate()
        str = "this is string example....wow!!!"
        #print (output.splitlines( ))
        print (output)
        #print (str.split('\n',100))
        #return a+b

