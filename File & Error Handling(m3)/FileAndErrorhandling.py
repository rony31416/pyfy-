#Create file 
"""


with open('example.text', "w") as myFile : 
    myFile.write("This is an example text file.\n")
    myFile.write("It contains multiple lines of text.\n")
    myFile.write("This is the third line of the file.\n")
    myFile.write("print('hello Bangladesh')")

"""


#read file 

"""

with open('example.text', 'r') as myFile : 
    content = myFile.read()
    print(content)
     
"""


#rename  File Name 

"""

import os 
old_name = 'example.text'

new_name = 'newFilename.csv'

os.rename(old_name,new_name)


"""


#remove file 

"""

import os 
os.remove('newFilename.csv')


"""

#Folder Creation 
"""
import os 
os.mkdir('newFolder')
os.makedirs('newFolder/subFolder')  # Creates a subfolder within the 
"""


#Folder Delation 

"""
import os 
os.rmdir('newFolder')

"""

#rename Folder 

"""
import os 
old_name  = 'newFolder' 
new_name = 'renamedFolder'  
os.rename(old_name,new_name)

"""


#how to make zip from Directory 
"""
import shutil 
shutil.make_archive('newFolder','zip', './newFolder') 
 # Creates a zip file of the newFolder directory

"""


#How to extract zip file 
"""
import zipfile
with zipfile.ZipFile('newFolder.zip', 'r') as myZipFile : 
    myZipFile.extractall()  # Extracts the contents of the zip file to a new directory
"""



#how to make a csv file 
"""
import csv 

data = [
    ['Name', 'Age', 'City', 'Score'],
    ['Alice', 23, 'Dhaka', 88],
    ['Bob', 27, 'Chittagong', 75],
    ['Charlie', 22, 'Khulna', 92],
    ['Diana', 25, 'Rajshahi', 81]
]

with open("example.csv", "w" , newline='') as csvFile :
    csvFileWriter = csv.writer(csvFile)
    csvFileWriter.writerows(data)
"""
#how to read a csv file 
"""
import csv 
with open("example.csv", "r") as csvFile :
    csvFileReader = csv.reader(csvFile)
    for row in csvFileReader :
        print(row)

"""


# 1. Basic Try-Except Block
"""

try:
    x = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
"""

#✅ 2. Catching Multiple Exceptions

"""
try:
    num = int("abc")
    result = 10 / num
except ValueError:
    print("Invalid number format!")
except ZeroDivisionError:
    print("Number cannot be zero!")

"""


#✅ 3. Using Else with Try-Except
"""

try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input! Not a number.")
else:
    print(f"Good job! You entered {num}")


"""

#4. Finally Block – Runs No Matter What
"""
try:
    file = open('sample.txt', 'r')
    data = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("Closing file...")
    # You’d normally use file.close() here if file exists
"""


# 5. Custom Exception Handling
"""
def check_age(age):
    if age < 0:
        raise ValueError("Age can't be negative!")
    return f"Age is {age}"

try:
    print(check_age(-5))
except ValueError as ve:
    print(f"Error: {ve}")
"""