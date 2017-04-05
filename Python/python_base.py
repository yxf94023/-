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

##
#\defgroup p_number_class Python Number(����)
#@{
#

##
#\brief ���ֶ���Ĳ���
#
#	- ���������ǲ�����ı�ģ� �����ζ������ı�Number�������͵�ֵ�� �����·����ڴ�ռ䡣
#	- ����ʹ��del���ɾ��һЩNumber��������
#	- ��ѧ����
#	- �������
#	- ���Ǻ���
#	- ��ѧ����
#
def p_number_object():
	var1 = 100
	var2 = 1000
	print var1, var2
	del var1, var2
	#print var1, var2 # ����ʾ UnboundLocalError: local variable 'var1' referenced before assignment
	x = 1024
	print int('32', 10)		# ���32
	print long('31', 10)	# ���31
	print float(x)			# ���1024.0
	print str(x)			# ����ַ���1024
	print chr(97)			# ����ַ� a
	return

	
p_number_object()

##
#@}
#


##
#\defgroup p_string_class Python String(�ַ���)
#@{
#

##
#\brief �ַ�������Ĳ���
#
#	- Python����������һ���ַ�������У��ַ����п��԰������з����Ʊ���������������ַ���
#	- Python �ж���һ��Unicode�ַ����Ͷ���һ����ͨ�ַ���һ��
#	- Python ���ַ����ڽ�����
#
def p_string_object():
	str1 = 'Python'
	str2 = "Hello, My Son!"
	"�ַ����ĸ�ʽ��"
	print "%s Are you sleeping?" % str2
	print "%s Are you sleeping or studying %s?" % (str2, str1)
	"Unicode �ַ���"
	ustr = u'Hello Kitty!'
	print ustr
	return


p_string_object()

##
#@}
#

##
#\defgroup p_list_class Python List(�б�)
#@{
#

##
#\brief �б����Ĳ���
#
#	+ �����б��е�ֵ
#		- ʹ���±����������б��е�ֵ[0]
#		- ʹ�÷����ŵ���ʽ��ȡ�ַ�
#
def p_list_access_list():
	list = ["gaosu", "yuwen", "jihe", "daishu"]
	print "list[0]: ", list[0]
	print "list[1:3]: ", list[1:3]
	return

##
#\brief �б����Ĳ���
#
#	+ �����б�
#		- ����ֱ�Ӷ��б��е�ֵ�����޸Ļ����
#		- ͨ��append�������б���׷��
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
#\brief �б����Ĳ���
#
#	+ ɾ���б�Ԫ��
#		- ʹ�� del �����ɾ���б���Ԫ��
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
#\defgroup p_tuple_class Python Tuple(Ԫ��)
#@{
#

##
#\brief Ԫ�����Ĳ���
#
#	Python��Ԫ�����б����ƣ� ��ͬ����Ԫ���Ԫ�ز����޸�
#	Ԫ��ʹ��С���ţ� �б�ʹ�÷�����
#
def p_tuple_operator():
	tup1 = ("30", )
	print tup1[0]
	print tup1
	print tup1 + ("33", "66")
	del tup1	# ɾ��Ԫ��
	return

p_tuple_operator()
##
#@}
#

##
#\defgroup p_dictionary_class Python Dictionary(�ֵ�)
#@{
#

##
#\brief �ֵ����
#
#	�ֵ���һ�ֿɱ�����ģ�ͣ��ҿɴ洢�������Ͷ���
#	�ֵ��û����ֵ����ð�ŷָû����֮���ö��ŷָ�����ֵ���һongoing�����Ű�����
#
def p_dictionary_operator():
	dict = {"a":16, "b":32}
	"�����ֵ����ֵ"
	print "dict['a']:", dict["a"]	# ��� dict['a']: 16
	print "dict:", dict				# ��� dict: {'a': 16, 'b': 32}
	dict["a"] = 8
	dict["c"] = 64
	print "dict:", dict	# ��� dict: {'a': 8, 'c': 64, 'b': 32}
	del dict["a"]	# ɾ����Ϊ"a"����Ŀ
	dict.clear()	# ��մʵ�������Ŀ
	print "dict:", dict	# dict: {}
	del dict		# ɾ���ʵ�
	return
	
p_dictionary_operator()

##
#@}
#