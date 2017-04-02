#!/usr/bin/python
# -*- coding: UTF-8 -*-

##
#\mainpage Python����
#
#\section Python����������
#
#	This is.
#
#\setcion Python���������
#

##
#\defgroup python_var_type Python����������
#@{
#

##
#\brief �������ͣ��������
#
#	100<br/>
#	1000.0<br/>
#	John<br/>
#	1 2 end<br/>
#
def p_var_type_fun():
	counter = 100	# ��ֵ���ͱ���
	miles = 1000.0	# ������
	name = "John"	# �ַ���
	"���"
	print counter
	print miles
	print name
	"�������ֵ"
	a, b, c = 1, 2, "end"
	print a, b, c
	"�ַ���"
	str = "Hello World!"
	return

##
#\brief �ַ�������
#	
#	+ Python���ַ�����2��ȡֵ˳��
#		- ����������Ĭ��0��ʼ�ģ����Χ���ַ���������1
#		- ���ҵ�������Ĭ�ϴ�-1��ʼ�ģ� ���Χ���ַ�����ͷ
def p_string_operator_fun():
	str = "I'm study Python"
	print str					# ����ַ���
	print str[0:3]				# ���I'm
	print str[-6:]				# ���Python
	print str + " Language!"	# ���I'm study Python Language!
	return

##
#\brief �б����
#
#	���������ַ���
#
def p_list_operator_fun():
	list1 = ['123', 456]
	list2 = [789, '000']
	print list1			# ��� ['123', 456]
	print list1[0]		# ��� 123
	print list1[1]		# ��� 456
	print list1[0:2]	# ��� ['123', 456]
	print list1 + list2	# ��� ['123', 456, 789, '000']
	return

##
#\brief �ֵ����Ͳ���
#
#	�ֵ�(dictionary)�ǳ��б�����python֮���������������ݽṹ����
#	�б�������Ķ����ϣ��ֵ�������Ķ��󼯺ϡ�key-value
#
def p_dict_operator_fun():
	dict = {"one":1,"two":2}
	dict["four"] = 4
	print dict				# ������е��ֵ���Ϣ {'four': 4, 'two': 2, 'one': 1}
	print dict["two"]		# ��� 2
	print dict.keys()		# ������еļ� ['four', 'two', 'one']
	print dict.values()		# ������е�ֵ [4, 2, 1]
	return

p_var_type_fun()

p_string_operator_fun()

p_list_operator_fun()

p_dict_operator_fun()

##
#@}
#

##
#\defgroup python_condition_command Python���������
#@{
#

##
#\brief �������
#
#	- �κη�0�ͷǿգ�null��ֵΪtrue��0����nullΪfalse
#
def p_if_operator():
	flag = 5
	"������if���"
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
#\defgroup python_loop_statement Python��ѭ�����
#@{
#

##
#\brief ѭ��������
#
#	- Python�ṩ�� for �� while ѭ�� û��do...whileѭ��
#		- ��python�У� while ... else ��ѭ������Ϊfalseʱִ��else���
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
	"������"
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

