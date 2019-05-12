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


# 17、输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
# s = input('请输入字符串：')
# letters = 0
# space = 0
# digit = 0
# others = 0
# for c in s:
# 	if c.isalpha():
# 		letters += 1
# 	elif c.isspace():
# 		space += 1
# 	elif c.isdigit():
# 		digit += 1
# 	else:
# 		others += 1
# print('char = %d,space = %d,digit = %d,others = %d' % (letters, space, digit, others))

# s = input('请输入一个字符串:')
# letters = 0
# space = 0
# digit = 0
# others = 0
# i = 0
# while i < len(s):
#     c = s[i]
#     i += 1
#     if c.isalpha():
#         letters += 1
#     elif c.isspace():
#         space += 1
#     elif c.isdigit():
#         digit += 1
#     else:
#         others += 1
# print('char = %d,space = %d,digit = %d,others = %d' % (letters, space, digit, others))


# 18、求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字
# a = input('输入数字')
# count = int(input('几个数字相加'))
# ret = []
# for i in range(1, count+1):
# 	ret.append(int(a*i))
# 	print(ret[i-1])
# print(sum(ret))

# Tn = 0
# Sn = []
# n = int(input('n = '))
# a = int(input('a = '))
# for count in range(n):
# 	Tn = Tn + a
# 	a = a * 10
# 	Sn.append(Tn)
# 	print(Tn)
# print("计算和为：", sum(Sn))


# 19、一个数如果恰好等于它的因子之和，这个数就称为"完数"
# for j in range(2, 1001):
# 	k = []
# 	n = 0
# 	s = j
# 	for i in range(1, j):
# 		if j % i == 0:
# 			n += 1
# 			s -= i
# 			k.append(i)
# 	if s == 0:
# 		print(j)
# 		for i in range(n):
# 			print(str(k[i]), end=' ')
# 		print()


# 20、一球从100米高度自由落下，每次落地后反跳回原高度的一半；
# 再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
# tour = []
# height = []
# hei = 100.0
# tim = 10
# for i in range(1, tim + 1):
# 	if i == 1:
# 		tour.append(hei)
# 	else:
# 		tour.append(2 * hei)
# 	hei /= 2
# 	height.append(hei)
# print('总高度：tour = {0}'.format(sum(tour)))
# print('第10次反弹高度：height = {0}'.format(height[-1]))

# th = []
# h = 100.0
# for i in range(1, 11):
# 	if i == 1 or i == 2:
# 		th.append(h)
# 	else:
# 		h /= 2
# 		th.append(h)
# 	if i == 10:
# 		print('第10次反弹高度:{0}'.format(h/4))
# print('总高度:{0}'.format(sum(th)))


# 21、猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，
# 又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少
# x = 1
# for i in range(1, 10):
# 	x = (x+1) * 2
# print(x)


# 22、两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。
# 有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单
# for i in range(ord('x'), ord('z') + 1):
# 	for j in range(ord('x'), ord('z') + 1):
# 		if i != j:
# 			for k in range(ord('x'), ord('z') + 1):
# 				if (i != k) and (j != k):
# 					if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
# 						print('order is a -- %s\t b -- %s\tc--%s' % (chr(i), chr(j), chr(k)))


# 23、打印出菱形图案
# for i in range(4):
# 	print(' ' * (4-i) + '*' * (2*i+1))
# for i in range(3):
# 	print(' ' * (2+i) + '*' * (4-2*i+1))


# 24、有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和
# a = 2.0
# b = 1.0
# ls = []
# ls.append(a / b)
# for i in range(19):
# 	b, a = a, a+b
# 	ls.append(a / b)
# print(sum(ls))

# a = 2.0
# b = 1.0
# s = 0
# for n in range(1, 21):
# 	s += a / b
# 	t = a
# 	a = a + b
# 	b = t
# print(s)


# 25、求1+2!+3!+...+20!的和
# s = 0
# t = 1
# for n in range(1, 21):
# 	t *= n
# 	s += t
# print('1! + 2! + 3! + ... + 20! = %d' % s)

# s = 0
# l = range(1, 21)
# def op(x):
# 	r = 1
# 	for i in range(1, x + 1):
# 		r *= i
# 	return r
# s = sum(map(op, l))
# print('1! + 2! + 3! + ... + 20! = %d' % s)


# 26、利用递归方法求5!
# def a(x):
# 	sum = 0
# 	if x == 0:
# 		sum = 1
# 	else:
# 		sum = x * a(x-1)
# 	return sum
# print(a(5))


# 27、利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来
# def output(s, l):
# 	if l == 0:
# 		return
# 	print(s[l - 1])
# 	output(s, l - 1)
# s = input('Input a string:')
# l = len(s)
# output(s, l)

# def a(s):
# 	# l = list(s)
# 	# l.reverse()
#
# 	# l = s[::-1]
#
# 	# x = list(s)
# 	# l = "".join(x[::-1])
# 	print(l)
# a(input('输入'))

# def func(s):
#     l = list(s)
#     result = ""
#     while len(l) > 0:
#         result += l.pop()
#     return result
# print(func(input()))


# 28、有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。
# 问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。
# 请问第五个人多大
# n = 10
# for i in range(5):
# 	print("第%s人,%s岁" % (i+1, n))
# 	n += 2

# def a(n):
# 	if n == 1:
# 		c = 10
# 	else:
# 		c = a(n - 1) + 2
# 	return c
# print(a(5))


# 29、给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字
# x = int(input("请输入一个数:\n"))
# a = x / 10000
# b = x % 10000 / 1000
# c = x % 1000 / 100
# d = x % 100 / 10
# e = x % 10
# if a != 0:
# 	print("5 位数：", e, d, c, b, a)
# elif b != 0:
# 	print("4 位数：", e, d, c, b)
# elif c != 0:
# 	print("3 位数：", e, d, c)
# elif d != 0:
# 	print("2 位数：", e, d)
# else:
# 	print("1 位数：", e)

# n = str(int(input('shuru')))
# for i in range(len(n)):
# 	print(n[-i-1])
# print(i+1)


# 30、一个5位数，判断它是不是回文数
# a = str(int(input("数字：")))
# flag = True
# for i in range(int(len(a) / 2)):
# 	if a[i] != a[-i-1]:
# 		flag = False
# if flag:
# 	print("是回文")
# else:
# 	print("不是回文")


# 31、请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母
# letter = input('输入:')
# if letter == 'M':
# 	print("Monday")
# elif letter == 'T':
# 	letter = input("输入:")
# 	if letter == 'u':
# 		print("Tuesday")
# 	elif letter == 'h':
# 		print("Thursday")
# 	else:
# 		print('input err')
# elif letter == 'W':
# 	print("Wednesday")
# elif letter == 'F':
# 	print("Friday")
# elif letter == "S":
# 	letter = input("输入:")
# 	if letter == 'a':
# 		print('Saturday')
# 	elif letter == 'u':
# 		print('Sunday')
# 	else:
# 		print('input err')
# else:
# 	print('input err')


# 32、按相反的顺序输出列表的值
# a = ['one', 'two', 'three']
# for i in a[::-1]:
# 	print(i)

# a.reverse()
# for i in a:
# 	print(i)

# 33、按逗号分隔列表
# L = [1, 2, 3, 4, 5]
# s1 = ','.join(str(n) for n in L)
# print(s1)


# 34、练习函数调用
# def hello():
# 	print('hello world')
# def five_hello():
# 	for i in range(5):
# 		hello()
# five_hello()


# 35、文本颜色设置
# \033[0m				关闭所有属性			\033[1m				设置高亮度
# \033[4m				下划线					\033[5m				闪烁
# \033[7m				反显					\033[8m				消隐
# \033[30m-\33[37m	设置前景颜色			\033[40m-\33[47m	设置背景颜色
# \033[nA				光标上移n行				\033[nB				光标下移n行
# \033[nC				光标右移n行				\033[nD				光标左移n行
# \033[y;xH			设置光标位置			\033[2J				清屏
# \033[K				清除从光标到行尾的内容	\034[s				保存光标位置
# \033[u				恢复光标位置			\033[?25l			隐藏光标
# \033[?25h			显示光标
# 背景色：40:黑 41:深红 42:绿 43:黄色 44:蓝色 45:紫色 46:深绿 47:白色
# 前景色：30:黑 31:红 32:绿 33:黄 34:蓝色 35:紫色 36:深绿 37:白色
# class bcolors:
# 	HEADER = '\033[95m'
# 	OKBLUE = '\033[94m'
# 	OKGREEN = '\033[92m'
# 	WARNING = '\033[93m'
# 	FAIL = '\033[91m'
# 	ENDC = '\033[0m'
# 	BOLD = '\033[1m'
# 	UNDERLINE = '\033[4m'
# print(bcolors.WARNING + '警告的字体颜色' + bcolors.ENDC)


# 36、求100之内的素数
# for i in range(2, 101):
# 	for j in range(2, i):
# 		if i % j == 0:
# 			break
# 	else:
# 		print(i)

# 37、对10个数进行排序
# ls = []
# for i in range(10):
# 	ls.append(int(input('数字')))
# # ls.sort()
# for i in range(9):
# 	min = i
# 	for j in range(i+1, 10):
# 		if ls[min] > ls[j]: min = j
# 	ls[i], ls[min] = ls[min], ls[i]
# for i in range(10):
# 	print(ls[i])


# 38、求一个3*3矩阵主对角线元素之和
# a = []
# sum = 0.0
# for i in range(3):
# 	a.append([])
# 	for j in range(3):
# 		a[i].append(float(input("num")))
# for i in range(3):
# 	sum += a[i][i]
# print(sum)

# sum = 0.0
# for i in range(3):
# 	for j in range(3):
# 		a = float(input("num"))
# 		if i == j:
# 			sum += a
# print(sum)


# 39、有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中
# a = [1, 4, 6, 9, 13, 16, 19, 28, 40, 100, 0]
# number = int(input("插入一个数字:"))
# if number > a[9]:
# 	a[10] = number
# else:
# 	for i in range(11):
# 		if a[i] > number:
# 			b = a[i]
# 			a[i] = number
# 			for j in range(i+1, 11):
# 				c = a[j]
# 				a[j] = b
# 				b = c
# 			break
# for i in range(11):
# 	print(a[i])

# a = [1, 4, 6, 9, 13, 16, 19, 28, 40, 100]
# a.append(int(input("number")))
# a.sort()
# print(a)


# 40、将一个数组逆序输出
# a = [9, 6, 5, 4, 1]
# for i in a[::-1]:
# 	print(i)

# a = [9, 6, 5, 4, 1]
# for i in range(len(a)):
# 	print(a[-i-1])

# a = [9, 6, 5, 4, 1]
# for i in range(int(len(a) / 2)):
# 	a[i], a[-i-1] = a[-i-1], a[i]
# print(a)


# 40、模仿静态变量的用法
# def varfunc():
# 	var = 0
# 	print('var = %d' % var)
# 	var += 1
# if __name__ == '__main__':
# 	for i in range(3):
# 		varfunc()
#
# class Static:
# 	StaticVar = 5
# 	def varfunc(self):
# 		self.StaticVar += 1
# 		print(self.StaticVar)
#
# print(Static.StaticVar)
# a = Static()
# for i in range(3):
# 	a.varfunc()

# class Static:
# 	svar = 5
# 	def varfunc(self):
# 		self.svar += 1
# 		print(self.svar)
#
# print(Static.svar)
# a = Static()
# for i in range(3):
# 	a.varfunc()















