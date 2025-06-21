try:
    file = open('simple.txt','r+')
    fileContent = file.read()
    print(f"Reading file content\n{fileContent}")
    file.close()
except FileNotFoundError:
    print("Error: The file simple.txt was not found")