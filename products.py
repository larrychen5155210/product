#記帳程式
#二維清單

products = []
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

for product in products:
	print(product[0], '的價格是', product[1])

with open('products.txt', 'w') as f: # 'w' : 寫入模式
	for product in products:
		f.write(product[0] + ',' + product[1] + '\n')

with open('products.csv', 'w') as f: 
	for product in products:
		f.write(product[0] + ',' + product[1] + '\n')