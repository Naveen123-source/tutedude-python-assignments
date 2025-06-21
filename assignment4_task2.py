# write content in file
with open('simple.txt','w') as file:
    fileContent = file.write('Line 1: This is a simple text file.')
    print(fileContent)

# append content in file
with open('simple.txt','a') as file:
    fileContent = file.write('\nLine 2: It contains multiple lines.')
    print(fileContent)

# read file content
with open('simple.txt','r') as file:
    fileContent = file.read()
    print(f"Reading file content\n{fileContent}")