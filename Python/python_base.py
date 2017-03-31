#!/usr/bin/python
# -*- coding: UTF-8 -*-

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