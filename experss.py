# 1、有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# for i in range(1, 5):
# 	for j in range(1, 5):
# 		for k in range(1,5):
# 			if(i != k) and (i != j) and (j != k):
# 				print(i,j,k)

# 正则方式
# import re
# for i in range(100, 433):
# 	if re.search('[1-4]{3}', str(i)):
# 		if (str(i)[0] != str(i)[1]) and (str(i)[1] != str(i)[2]) and (str(i)[0] != str(i)[2]):
# 			print(i)

# 递归方式
# import re
# def a(i):
# 	if re.search('[1-4]{3}', str(i)) and (str(i)[0] != str(i)[1]) and (str(i)[1] != str(i)[2]) and (str(i)[0] != str(i)[2]):
# 		print(i)
# 	if i > 500:
# 		return
# 	else:
# 		i += 1
# 		a(i)
# if __name__ == '__main__':
# 	a(100)


# 2、企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，
# 低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
# i = int(input('利润:'))
# arr = [1000000, 600000, 400000, 200000, 100000, 0]
# rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
# r = 0
# for idx in range(0, 6):
# 	if i > arr[idx]:
# 		r += (i - arr[idx]) * rat[idx]
# 		i = arr[idx]
# print(r)

# 递归方式
# def a(i, arr, rat, r, idx):
# 	if i > arr[idx]:
# 		r += (i-arr[idx]) * rat[idx]
# 		i = arr[idx]
# 	if i == 0:
# 		print(r)
# 	else:
# 		idx += 1
# 		a(i, arr, rat, r, idx)
# if __name__ == '__main__':
# 	i = int(input('利润;'))
# 	arr = [1000000, 600000, 400000, 200000, 100000, 0]
# 	rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
# 	a(i, arr, rat, 0, 0)

# 暂未想到更好的解决办法
# i = int(input('利润：'))
# r = 0
# if i < 100000:
# 	r = i * 0.1
# elif i > 100000 and i < 200000:
# 	r = 10000 + (i - 100000) * 0.075
# elif i > 200000 and i < 400000:
# 	r = 10000 + 7500 + (i - 200000) * 0.05
# elif i > 400000 and i < 600000:
# 	r = 10000 + 7500 + 10000 + (i - 400000) * 0.03
# elif i > 600000 and i < 1000000:
# 	r = 10000 + 7500 + 10000 + 6000 + (i - 600000) * 0.015
# else:
# 	r = 10000 + 7500 + 10000 + 6000 + 6000 + (i - 1000000) * 0.01
# print(r)

# 3、一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
# for i in range(1, 85):
# 	if 168 % i == 0:
# 		j = 168 / i
# 		if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
# 			m = (i + j) / 2
# 			n = (i - j) / 2
# 			x = n * n - 100
# 			print(x)

# def a(i):
# 	if 168 % i == 0:
# 		j = 168 / i
# 		if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
# 			m = (i + j) / 2
# 			n = (i - j) / 2
# 			x = n * n - 100
# 			print(x)
# 	if i == 85:
# 		print('结束')
# 	else:
# 		i += 1
# 		a(i)
# if __name__ == '__main__':
# 	a(1)


# 4、输入某年某月某日，判断这一天是这一年的第几天？
# year = int(input('year:'))
# month = int(input('month:'))
# day = int(input('day:'))
# months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
# if 0 < month < 13:
# 	sum = months[month - 1]
# else:
# 	print('data error')
# sum += day
# if (month > 2) and (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
# 	sum += 1
# print('it is the %dth day.' % sum)

# year = int(input('年份：'))
# month = int(input('月份：'))
# day = int(input('日期:'))
# if 0 < month < 13:
# 	for i in range(1, month):
# 		if i in [1, 3, 5, 7, 8, 10, 12]:
# 			day += 31
# 		if i in [4, 6, 9, 11]:
# 			day += 30
# 		if i == 2 and (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
# 			day += 29
# 		elif i == 2:
# 			day += 28
# 	print('it is the %dth day.' % day)
# else:
# 	print('data error')


# 5、输入三个整数x,y,z，请把这三个数由小到大输出
# l = []
# for i in range(3):
# 	x = int(input())
# 	l.append(x)
# l.sort(reverse=False)
# print(l)

# def a(l, n):
# 	x = int(input())
# 	l.append(x)
# 	if n == 2:
# 		return
# 	n += 1
# 	a(l, n)
# if __name__ == '__main__':
# 	l = []
# 	a([], 0)
# 	l.sort()
# 	print(l)