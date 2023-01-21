from os.path import exists
filename1 = "MyFile.txt"
filename2 = "Reading_Files.txt"
print("Copy from %s to %s" %(filename1 , filename2))
in_file = open(filename1)
indata = in_file.read()
print("The input file is %d bytes long." %len(indata))
print("Does the output file exist? %r" %exists(filename2))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input(">")
out_file = open(filename2 , 'w')
out_file.write(indata)
print("Alright, all done.")
in_file.close()
out_file.close()