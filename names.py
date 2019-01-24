#!C:\Python27\python.exe

with open("C:\\Users\\arche\\Documents\\BillionLives\\Automation\\girl_names.txt") as f1:
    girls_data = f1.read()
    girls_data = girls_data.split("\n")

print girls_data , len(girls_data)

with open("C:\\Users\\arche\\Documents\\BillionLives\\Automation\\boys_names.txt") as f1:
    boys_data = f1.read()
    boys_data = boys_data.split("\n")

print boys_data , len(boys_data)