#記帳程式
#二維清單

import os # operating system 作業系統

# 讀取舊有檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding = 'utf-8') as f: 
		for line in f:
			if '商品,價格' in line:
				continue # 跳過此次迴圈, 跳至下一迴圈
			name, price = line.strip().split(',') # strip 去除空格(\n), split 分割
			products.append([name, price])
	return products
	print(products)

#讓使用者輸入
def user_input(products):
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
	return products

#印出所有購買紀錄
def print_products(products):
	for product in products:
		print(product[0], '的價格是', product[1])

#寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8')as f: # 'w' 寫入模式 , encoding 編碼
		f.write('商品,價格\n')
		for product in products:
			f.write(product[0] + ',' + product[1] + '\n')

# main function
def main():
	filename = 'products.csv'
	if os.path.isfile(filename): # 檢查檔案是否存在
		print('找到檔案!!')
		products = read_file(filename)
	else:
		print('找不到檔案.....')
	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()