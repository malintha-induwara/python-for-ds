#Reading files from python

#To Open a files   (we can use following without passing "r" its because the default mode is read)

file_1 = open("myFile.txt","r")


#Read the file

#read_content = file_1.read()

#readline is used to read the content from the file line by line (until it met a newline character \n)
#read_content= file_1.readline()

read_content= file_1.readlines()


#Type of content is string
print(type(read_content))
print(read_content)


#Best pratice is to close the file after it being used

file_1.close()


#File Reading mode


# r - open a file for reading (default) 
# w - open a file for writing create a new file if it does not exsist or truncate the file if it  exsist
# x - open a file for exclusive creation. if the file already exsists, the opertion fails.
# a - open a file for appending  at the end of the file without truncateing it , create a new file if it does not exist
# t - open in text mode (default)

#You can handle files with "with" statement (this is similer to try with resources )

with open("myFile.txt","r") as file:
    content = file.read()
    print(content)


    
