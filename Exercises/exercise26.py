#write to a file using writeline

#Write to a file

with open("myFile.txt","w") as file:
    file.writelines(["This is something new\n","This is the writeline method"])
    
    
