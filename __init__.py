import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('D:/Nnlt R/Dataset/Dataset/Temperature.xls')
print(df)
# Dùng loc để lọc ở trước là hàng ở sau là cột ghi bằng tên
print(df.loc[1:5, ["Year", "Season"]])
# iloc tương tụ loc nhưng ở sau là số
print(df.iloc[1:5, 1:3])
# Tìm cột hoặc hàng trong file excel
print(df.loc[(df["Year"] == 1990) & (df["Month"] == 4)])
print(df["Year"])
# Sắp xếp theo thứ tự tăng dần của đối tượng, nếu ascending=True và giảm dần nếu bằng False
print(df.sort_values("Year", ascending=True, ignore_index=True))    
# Thông kê đối tượng theo giá trị trung bình max min
dl = df[["Season", "Temperature"]]
dl.max = df.groupby("Season").mean()
print(dl.max)
# Muốn ghi dữ liệu trong pychamr vào excel thì ta dùng ExcelWriter, nếu có file sẵn thì sẽ ghi đè lên file còn nếu muốn
# ghi thêm vào file thì thêm mode = 'a'
with pd.ExcelWriter('D:/Nnlt R/Dataset/Dataset/sosanh.xlsx') as ew:
    dl.max.to_excel(ew, sheet_name=" Nhiệt độ")
dl.max.plot.bar(rot=0)
plt.show()
