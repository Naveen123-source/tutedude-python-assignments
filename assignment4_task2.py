# write content in file
userInput = input("Enter text to write to the file:")

with open('simple.txt','w') as file:
    fileContent = file.write(userInput)
    print("Data successfully written to simple.txt.")

# append content in file
userInput = input("Enter additional text to append:")
with open('simple.txt','a') as file:
    fileContent = file.write(f"\n{userInput}")
    print("Data append successfully")

# read file content
with open('simple.txt','r') as file:
    fileContent = file.read()
    print(f"Final content of simple.txt:\n{fileContent}")