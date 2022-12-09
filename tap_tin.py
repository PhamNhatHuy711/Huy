def bai1(text, file):
    with open(file, 'w') as f:
        f.write(text)
#---------------------------------------------------------------------------
def bai2(file):
    with open(file, 'r') as f:
        print(f.read())

#---------------------------------------------------------------------------
def bai3(text, file):
    with open(file, 'a') as f:
        f.write(text)
#--------------------------------------------------------------------------
def bai4(file):
      with open(file, 'r') as f:
          print(f.read())
#--------------------------------------------------------------------------
def main():
    a = str(input("Nhập chuỗi ký tự cần thềm vào tập tin: "))
    b = str(input("Nhập tên tập tin: "))
    bai1(a, b)
    bai2(b)
    bai3(a, b)
    bai4(b)
if __name__=="__main__":
    main()
