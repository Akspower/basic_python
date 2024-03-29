# file handling means storing or access any data from storage 
# file handling modes
# r ,w ,a ,r+,w+,a+

def writing(abcfile,text):
    file=open(abcfile,"w")
    file.write(text)
    file.close()


writing("file.txt","file created successfully\n Thank You")


#for append
def append(abcfile,text): #append use to edit the file do not delete old text 
    file=open(abcfile,"a")
    file.write(text)
    file.close()


append("file.txt"," \nappend successfully")


#for read
def reading(abcfile):
    try:
        file=open(abcfile,"r")
        text=file.read()
        print(text)
        file.close()
    except FileNotFoundError:
        print("file does not exist")


reading("file.txt")