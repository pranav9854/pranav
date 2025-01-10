with open ("abc.txt","r") as file:
    #using read() to read the entire file
    content = file.read()
    print("using read():")
    print(content)