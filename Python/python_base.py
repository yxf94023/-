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

