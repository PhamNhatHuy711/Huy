import os
f = open("D:/data/test.txt")
f = open("test.txt",'w')
f = open("D:/data/H.png",'r+b')
f = open("test.txt", mode='r', encoding='utf-8')
f.close()
try:
   f = open("test.txt", encoding = 'utf-8')
finally:
   f.close()
with open("D:/data/test.txt", mode='w', encoding='utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")
f = open("D:/data/test.txt", "r")
print(f.read())
f.close()
im = open("D:/data/H.png", "r+b")
print(im.read())
im.close()

