#記帳程式
#二維清單

import os # operating system 作業系統

products = []

# 讀取舊有檔案
if os.path.isfile('products.csv'): # 檢查檔案是否存在
	print('找到檔案!!')
	with open('products.csv', 'r', encoding = 'utf-8') as f: 
		for line in f:
			if '商品,價格' in line:
				continue # 跳過此次迴圈, 跳至下一迴圈
			name, price = line.strip().split(',') # strip 去除空格(\n), split 分割
			products.append([name, price])
	print(products)
else:
	print('找不到檔案.....')

#讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	p = [] # p = [name, price]
	p.append(name)
	p.append(price)
	products.append(p) # products.append([name, price])
print(products)

#印出所有購買紀錄
for product in products:
	print(product[0], '的價格是', product[1])

#寫入檔案
with open('products.txt', 'w') as f: # 'w' : 寫入模式
	for product in products:
		f.write(product[0] + ',' + product[1] + '\n')

with open('products.csv', 'w', encoding = 'utf-8')as f: # encoding 編碼
	f.write('商品,價格\n')
	for product in products:
		f.write(product[0] + ',' + product[1] + '\n')