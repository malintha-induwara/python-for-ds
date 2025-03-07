# write to a file

with open("myFile.txt","w") as file:
    file.write("This is test.\n")
    file.write("Hello World")



#Write lines

with open("myFile.txt","w") as file:
    my_list = ["This is something new\n","Hello world"]
    file.writelines(my_list)    
