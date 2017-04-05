#!/usr/bin/python
# -*- coding: UTF-8 -*-

##
#\mainpage Python语言
#
#\section Python的数据类型
#
#	This is.
#
#\setcion Python的条件语句
#

##
#\defgroup python_var_type Python的数据类型
#@{
#

##
#\brief 变量类型，输出如下
#
#	100<br/>
#	1000.0<br/>
#	John<br/>
#	1 2 end<br/>
#
def p_var_type_fun():
	counter = 100	# 赋值整型变量
	miles = 1000.0	# 浮点型
	name = "John"	# 字符串
	"输出"
	print counter
	print miles
	print name
	"多变量赋值"
	a, b, c = 1, 2, "end"
	print a, b, c
	"字符串"
	str = "Hello World!"
	return

##
#\brief 字符串操作
#	
#	+ Python的字符串有2中取值顺序
#		- 从左到右索引默认0开始的，最大范围是字符串长度少1
#		- 从右到左索引默认从-1开始的， 最大范围是字符串开头
def p_string_operator_fun():
	str = "I'm study Python"
	print str					# 输出字符串
	print str[0:3]				# 输出I'm
	print str[-6:]				# 输出Python
	print str + " Language!"	# 输出I'm study Python Language!
	return

##
#\brief 列表操作
#
#	操作类似字符串
#
def p_list_operator_fun():
	list1 = ['123', 456]
	list2 = [789, '000']
	print list1			# 输出 ['123', 456]
	print list1[0]		# 输出 123
	print list1[1]		# 输出 456
	print list1[0:2]	# 输出 ['123', 456]
	print list1 + list2	# 输出 ['123', 456, 789, '000']
	return

##
#\brief 字典类型操作
#
#	字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型
#	列表是有序的对象结合，字典是无序的对象集合。key-value
#
def p_dict_operator_fun():
	dict = {"one":1,"two":2}
	dict["four"] = 4
	print dict				# 输出所有的字典信息 {'four': 4, 'two': 2, 'one': 1}
	print dict["two"]		# 输出 2
	print dict.keys()		# 输出所有的键 ['four', 'two', 'one']
	print dict.values()		# 输出所有的值 [4, 2, 1]
	return

p_var_type_fun()

p_string_operator_fun()

p_list_operator_fun()

p_dict_operator_fun()

##
#@}
#

##
#\defgroup python_condition_command Python的条件语句
#@{
#

##
#\brief 条件语句
#
#	- 任何非0和非空（null）值为true，0或者null为false
#
def p_if_operator():
	flag = 5
	"单个的if语句"
	if (flag == 5):
		print "flag is five"
	"if/else"
	if (flag == 4):
		print "flag is four"
	else:
		print "flag is not four"
	"if/elif"
	if (flag == 4):
		print "flag is four"
	elif (flag == 6):
		print "flag is six"
	elif (flag == 5):
		print "flag is five"
	else:
		print "flag is other values"
	return
	
p_if_operator()
##
#@}
#

##
#\defgroup python_loop_statement Python的循环语句
#@{
#

##
#\brief 循环语句操作
#
#	- Python提供了 for 和 while 循环 没有do...while循环
#		- 在python中， while ... else 在循环条件为false时执行else语句
#
def p_loop_opertator():
	numbers = [12, 37, 5, 4]
	even = []
	odd = []
	while len(numbers) > 0:
		number = numbers.pop()
		if (number % 2 == 0):
			even.append(number)
		else:
			odd.append(number)
	else:
		print "while loop is over"
	"输出结果"
	print "\teven:", even
	print "\todd:", odd
	names = ['y', 'yx', 'yxf']
	for name in names:
		print name
	for idx in range(len(names)):
		print names[idx]
	else:
		print "for loop is over"
	return
	
p_loop_opertator()

##
#@}
#

##
#\defgroup p_number_class Python Number(数字)
#@{
#

##
#\brief 数字对象的操作
#
#	- 数据类型是不允许改变的， 这就意味着如果改变Number数据类型的值， 将重新分配内存空间。
#	- 可以使用del语句删除一些Number对象引用
#	- 数学函数
#	- 随机函数
#	- 三角函数
#	- 数学常量
#
def p_number_object():
	var1 = 100
	var2 = 1000
	print var1, var2
	del var1, var2
	#print var1, var2 # 会提示 UnboundLocalError: local variable 'var1' referenced before assignment
	x = 1024
	print int('32', 10)		# 输出32
	print long('31', 10)	# 输出31
	print float(x)			# 输出1024.0
	print str(x)			# 输出字符串1024
	print chr(97)			# 输出字符 a
	return

	
p_number_object()

##
#@}
#


##
#\defgroup p_string_class Python String(字符串)
#@{
#

##
#\brief 字符串对象的操作
#
#	- Python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符及其他的特殊字符。
#	- Python 中定义一个Unicode字符串和定义一个普通字符串一样
#	- Python 的字符串内建函数
#
def p_string_object():
	str1 = 'Python'
	str2 = "Hello, My Son!"
	"字符串的格式化"
	print "%s Are you sleeping?" % str2
	print "%s Are you sleeping or studying %s?" % (str2, str1)
	"Unicode 字符串"
	ustr = u'Hello Kitty!'
	print ustr
	return


p_string_object()

##
#@}
#

##
#\defgroup p_list_class Python List(列表)
#@{
#

##
#\brief 列表对象的操作
#
#	+ 访问列表中的值
#		- 使用下标索引访问列表中的值[0]
#		- 使用方括号的形式截取字符
#
def p_list_access_list():
	list = ["gaosu", "yuwen", "jihe", "daishu"]
	print "list[0]: ", list[0]
	print "list[1:3]: ", list[1:3]
	return

##
#\brief 列表对象的操作
#
#	+ 更新列表
#		- 可以直接对列表中的值记性修改或更新
#		- 通过append方法向列表中追加
#
def p_list_update_list():
	list = ["yu", "zhao", "cheng", 10, 12, 13]
	print list
	list[3] = "chenghao"
	print list
	list.append("5678")
	print list
	return

##
#\brief 列表对象的操作
#
#	+ 删除列表元素
#		- 使用 del 语句来删除列表中元素
#
def p_list_delete_list():
	list = ["one", "two", "three", "four"]
	print list
	del list[1]
	print list
	del list[1:3]
	print list
	return
	
p_list_access_list()
p_list_update_list()
p_list_delete_list()
##
#@}
#

##
#\defgroup p_tuple_class Python Tuple(元组)
#@{
#

##
#\brief 元组对象的操作
#
#	Python的元组与列表类似， 不同在于元组的元素不能修改
#	元组使用小括号， 列表使用方括号
#
def p_tuple_operator():
	tup1 = ("30", )
	print tup1[0]
	print tup1
	print tup1 + ("33", "66")
	del tup1	# 删除元组
	return

p_tuple_operator()
##
#@}
#

##
#\defgroup p_dictionary_class Python Dictionary(字典)
#@{
#

##
#\brief 字典操作
#
#	字典是一种可变容器模型，且可存储任意类型对象
#	字典的没个键值对用冒号分割，没个对之间用逗号分割，整个字典是一ongoing花括号包裹的
#
def p_dictionary_operator():
	dict = {"a":16, "b":32}
	"访问字典里的值"
	print "dict['a']:", dict["a"]	# 输出 dict['a']: 16
	print "dict:", dict				# 输出 dict: {'a': 16, 'b': 32}
	dict["a"] = 8
	dict["c"] = 64
	print "dict:", dict	# 输出 dict: {'a': 8, 'c': 64, 'b': 32}
	del dict["a"]	# 删除键为"a"的条目
	dict.clear()	# 清空词典所有条目
	print "dict:", dict	# dict: {}
	del dict		# 删除词典
	return
	
p_dictionary_operator()

##
#@}
#