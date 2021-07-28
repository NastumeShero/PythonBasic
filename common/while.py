'''
用法：
	while bool_result：
		do
	当bool_result的值为true时，执行do的语句
	当bool_result的值为false时，不执行do的语句
	bool_result可以是一个或多个条件语句组成
'''
count = 0
total = 0
while count<=100:
    total+=count
    count += 1
    print(count,total)
    if count ==10:
        print('已经循环到10了')
    elif count == 50:
        print('循环到50次了')
    elif count == 99:
        print('马上结束')
print(total)


'''
用法：
	while bool_result：
		continue
	for item in iterable:
		continue
		print(item)
	continue 表示执行到continue时跳过此次循环（后续的代码块不会继续往下执行），进入到下一次循环
'''
users = [
    {'username':'xiaomu','age':33,'top':174,'sex':'男'},
    {'username':'xiaohong','age':24,'top':174,'sex':'男'},
    {'username':'xiaoyun','age':33,'top':174,'sex':'女'},
    {'username':'xiaogao','age':33,'top':174,'sex':'男'},
]

man = []

for user in users:
    if user.get('sex') == '女':
        print('continue前')
        continue   # 跳过了for循环中的此次循环，后续的代码块均不会执行
        print('continue后')
    man.append(user)
    print('%s 加入了帮忙的队伍'% user.get('username'))

print(man)

'''
用法：
	while bool_result：
		break
	for item in iterable:
		print(item)
		break
	break 表示执行到break时，退出循环
'''
for i in range(100):
    if i == 80:
        print('============')
        print('已经循环了80次，马上要退出了')
        break  # 当执行到break时，表示循环被打断，后续未执行完的循环都不会被执行
    print(i)
else:
	print('循环正常退出了！')