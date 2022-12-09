import numpy as np
def sinh_ngau_nhien():
    v = np.random.randint(low= -1000, high= 1000, size=1000, dtype= int)
    return v
def sap_xep(x, file):
    with open(file, 'w', encoding='utf-8') as f:
        for i in range(1, len(x)+1):
            f.write(str(x[i-1]))
            if i % 10 ==0:
                f.write('\n')
            else:
                f.write(',')
def in_ra_mh(file):
    with open(file, 'r', encoding='utf-8') as f:
        dong = f.readline()
        for i in dong:
            a = dong.strip()
            b = a.replace(',', '    ')
            print(b)
def main():
    f = str(input("Nhập tên tập tin: "))
    v = sinh_ngau_nhien()
    sap_xep(v, f)
    print('-------------------------')
    in_ra_mh(f)
if __name__ == '__main__':
    main()