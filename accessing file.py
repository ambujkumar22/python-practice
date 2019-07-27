details = open("details.txt","a") #for opening a file the open function is used and in that we have tp mention 2 parameters 1)name of file 2) type (r- readable,w- writable,r+- readable and writable,a- append )
details.write("\nRoll number - 15-CSE-3015") # in this append will add a line to the last. write() function is used to write in a file and if we use (w) which means write then it will overwrite the whole file.
details.close() #close function is for closing the file (it is important to close the file)
det = open("details.txt","r")
for detail in det.readlines(): #the readlines function read multiple lines
    print(detail)
det.close()


