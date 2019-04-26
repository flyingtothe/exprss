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
# a(100)


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
# i = int(input('利润;'))
# arr = [1000000, 600000, 400000, 200000, 100000, 0]
# rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
# a(i, arr, rat, 0, 0)

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
# 			# m = (i + j) / 2
# 			n = (i - j) / 2
# 			x = n * n - 100
# 			print(x)
# 	if i == 85:
# 		return
# 	else:
# 		i += 1
# 		a(i)
# a(1)


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
# 		l.sort()
# 		print(l)
# 		return
# 	n += 1
# 	a(l, n)
# a([], 0)



# 6、斐波那契数列
# arr = [1, 1]
# for i in range(0, 100):
# 	x = arr[i] + arr[i+1]
# 	arr.append(x)
# print(arr)

# def a(arr, i):
# 	x = arr[i] + arr[i+1]
# 	arr.append(x)
# 	if i == 7:
# 		print(arr)
# 		return
# 	i += 1
# 	a(arr, i)
# a([1, 1], 0)

# def fib(n):
# 	a, b = 1, 1
# 	for i in range(n-1):
# 		a, b = b, a+b
# 	return a
# print(fib(10))

# def fib(n):
# 	if n == 1 or n == 2:
# 		return 1
# 	return fib(n-1)+fib(n-2)
# print(fib(10))

# 7、将一个列表的数据复制到另一个列表中
# a = [1, 2, 3, 4]
# b = a.copy()
# print(b)

# a = [1, 2, 3, 4]
# b = a[:]
# print(b)

# 8、输出 9*9 乘法口诀表
# for i in range(1,10):
# 	for j in range(1, i+1):
# 		print("%d*%d=%d" % (i, j, i*j), end=' ')
# 	print()

# def get_result(num):
# 	if num == 1:
# 		print('1 x 1 = 1')
# 	else:
# 		get_result(num-1)
# 		for i in range(1, num+1):
# 			print('%dx%d=%d' % (i, num, i*num), end=' ')
# 		print()
# get_result(9)


# 9、暂停一秒输出
# import time
# d = {1: 'a', 2: 'b'}
# for key, value in dict.items(d):
# 	print(key, value)
# 	time.sleep(1)


# 10、暂停一秒输出，并格式化当前时间
# import time
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
# time.sleep(1)
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


# 11、古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
# 假如兔子都不死，问每个月的兔子总数为多少？
# f1 = 1
# f2 = 1
# for i in range(1, 22):
#     print('%12ld %12ld' % (f1, f2))
#     if (i % 3) == 0:
#         print()
#     f1 = f1 + f2
#     f2 = f1 + f2

# arr = [1, 1]
# for i in range(0, 12):
# 	x = arr[i] + arr[i+1]
# 	arr.append(x)
# 	print('%d月，共有%d对兔子' % (i+1, arr[i]))


# 12、判断101-200之间有多少个素数，并输出所有素数
# 用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数
# h = 0
# leap = 1
# from math import sqrt
# for m in range(101, 201):
#     k = int(sqrt(m + 1))
#     for i in range(2, k + 1):
#         if m % i == 0:
#             leap = 0
#             break
#     if leap == 1:
#         print('%-4d' % m)
#         h += 1
#         if h % 10 == 0:
#             print()
#     leap = 1
# print('The total is %d' % h)


# 13、打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# for i in range(100, 1000):
# 	s = str(i)
# 	j = int(s[0]) ** 3
# 	k = int(s[1]) ** 3
# 	l = int(s[2]) ** 3
# 	if i == j + k + l:
# 		print(i)

# for n in range(100, 1000):
# 	i = int(n / 100)
# 	j = int(n / 10 % 10)
# 	k = int(n % 10)
# 	if n == i ** 3 + j ** 3 + k ** 3:
# 		print(n)


# 14、将一个正整数分解质因数
# n = int(input('请输入一个整数：'))
# print('%d=' % n, end='')
# while n > 1:
# 	for i in range(2, n+1):
# 		if n % i == 0:
# 			n = int(n/i)
# 			if n == 1:
# 				print('%d' % i, end='')
# 			else:
# 				print('%d*' % i, end='')
# 			break
# print()

# from math import sqrt
# while 1:
# 	n = int(input('请输入整数：'))
# 	print("%d = " % n, end='')
# 	while 1:
# 		for i in range(2, int(sqrt(n)+1)):
# 			if n % i == 0:
# 				print('%d*' % i, end='')
# 				n = int(n/i)
# 				break
# 		else:
# 			print(n)
# 			break

# def prime(n):
# 	L = [ ]
# 	while n > 1:
# 		for i in range(2, n+1):
# 			if n % i == 0:
# 				n = int(n/i)
# 				L.append(i)
# 				break
# 	return L
# while 1:
# 	s = input('请输入一个正整数：')
# 	if s.isdigit() and int(s)>0:
# 		print(s, '=', '*'.join([str(x) for x in prime(int(s))]))
# 	else:
# 		print('请输入一个正整数：')


# 15、利用条件运算符的嵌套来完成此题
# 学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示
# score = int(input('输入分数:\n'))
# if score >= 90:
# 	grade = 'A'
# elif score >= 60:
# 	grade = 'B'
# else:
# 	grade = 'C'
# print('%d 属于 %s' % (score, grade))


# 16、输出指定格式的日期
# import datetime
# if __name__ == '__main__':
# 	print(datetime.date.today().strftime('%d/%m/%Y'))
# 	BirthDate = datetime.date(1941, 1, 5)
# 	print(BirthDate.strftime('%d/%m/%Y'))
# 	BirthNextDay = BirthDate + datetime.timedelta(days=1)
# 	print(BirthNextDay.strftime('%d/%m/%Y'))
# 	FirstBirthday = BirthDate.replace(year=BirthDate.year + 1)
# 	print(FirstBirthday.strftime('%d/%m/%Y'))






