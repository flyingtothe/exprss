# 1、有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# for i in range(1, 5):
# 	for j in range(1, 5):
# 		for k in range(1,5):
# 			if(i != k) and (i != j) and (j != k):
# 				print(i,j,k)

# 未找到正确结束条件
# import random
# ls = []
# def a():
# 	i = random.choice(range(1, 5))
# 	j = random.choice(range(1, 5))
# 	k = random.choice(range(1, 5))
# 	try:
# 		if (i != k) and (i != j) and (j != k):
# 			if [i, j, k] in ls:
# 				a()
# 			ls.append([i, j, k])
# 			a()
# 		else:
# 			a()
# 	except :
# 		b(ls)
# def b(ls):
# 	print(ls)
# if __name__ == '__main__':
#     a()

# 2、企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，
# 低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
i = int(input('利润:'))
arr = [1000000, 600000, 400000, 200000, 100000, 0]
rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
r = 0
for idx in range(0, 6):
	if i > arr[idx]:
		r += (i - arr[idx]) * rat[idx]
		i = arr[idx]
print(r)

i = int(input('利润：'))
r = 0
if i < 100000:
	r = i * 0.1
elif i > 100000 and i < 200000:
	r = 10000 + (i - 100000) * 0.075
elif i > 200000 and i < 400000:
	r = 10000 + 7500 + (i - 200000) * 0.05
elif i > 400000 and i < 600000:
	r = 10000 + 7500 + 10000 + (i - 400000) * 0.03
elif i > 600000 and i < 1000000:
	r = 10000 + 7500 + 10000 + 6000 + (i - 600000) * 0.015
else:
	r = 10000 + 7500 + 10000 + 6000 + 6000 + (i - 1000000) * 0.01
print(r)