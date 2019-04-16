# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# for i in range(1, 5):
# 	for j in range(1, 5):
# 		for k in range(1,5):
# 			if(i != k) and (i != j) and (j != k):
# 				print(i,j,k)
import random
ls = []
def a():
	i = random.choice(range(1,5))
	j = random.choice(range(1,5))
	k = random.choice(range(1,5))
	if (i != k) and (i != j) and (j != k):
		ls.append([i, j, k])
		if [i, j, k] in ls:
			print(ls)
			b()
		else:
			a()
	else:
		a()
def b():
	print('结束')
if __name__ == '__main__':
    a()