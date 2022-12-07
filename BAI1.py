import os
print(os.getcwd())
os.chdir(r"D:/data")
print(os.getcwd())
path = "D:/data/nnlt"
os.makedirs(path)
path1 = "D:/Python"
dir_list = os.listdir(path1)
print(dir_list)
ex = os.path.exists("D:/data/text.txt")
print(ex)xdcf
os.remove("D:/data/text.txt")
os.rmdir("D:/data/nltk")
