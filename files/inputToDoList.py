toDoFile = open("/home/pi/PythonMinecraftBW/files/toDoFile.txt","r+")

toDoList = ""

toDoItem = input("Enter a to-do list item: ")

while toDoItem != 'exit':
    toDoList = toDoList + toDoItem + "\n"
    toDoItem = input("Enter a to-do list item: ")
    
toDoFile.write(toDoList)
toDoFile.close()