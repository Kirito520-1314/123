#coding:gbk
"""
�����ü�ֽ��ֽ����ʯͷ��ʯͷ���������ʯͷ�������棻���涾��ʷ����
��־��
"""

# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����
print("��ӭʹ��RPSLS��Ϸ")
print('-----------------')
print("����������ѡ��:")
choice_name=input()
def name_to_number(name):
	"""
	����Ϸ�����Ӧ����ͬ������
	"""
	if name=='ʯͷ':
		return 0
	if name=='ʷ����':
		return 1
	if name=='ֽ':
		return 2
	if name=='����':
		return 3
	if name=='����':
		return 4
def number_to_name(num):
	if num==0:
		return "ʯͷ"
	elif num==1:
		return "ʷ����"
	elif num==2:
		return "ֽ"
	elif num==3:
		return "����"
	elif num==4:
		return "����"

def rpsls(i,choice_name):
	if i=='ʯͷ' and choice_name=='����':
		print("����Ӯ��")
	elif i=='ʯͷ' and choice_name=='����':
		print("����Ӯ��")
	elif i=='ʷ����' and choice_name=='ʯͷ':
		print("����Ӯ��")
	elif i=='ʷ����' and choice_name=='����':
		print("����Ӯ��")
	elif i=='ֽ' and choice_name=='ʯͷ':
		print("����Ӯ��")
	elif i=='ֽ' and choice_name=='ʷ����':
		print("����Ӯ��")
	elif i=='����' and choice_name=='ʷ����':
		print("����Ӯ��")
	elif i=='����' and choice_name=='ֽ':
		print("����Ӯ��")
	elif i=='����' and choice_name=='ֽ':
		print("����Ӯ��")
	elif i=='����' and choice_name=='����':
		print("����Ӯ��")
	elif i=='ʯͷ' and choice_name=='ʷ����':
		print("��Ӯ��")
	elif i=='ʯͷ' and choice_name=='ֽ':
		print("��Ӯ��")
	elif i=='ʷ����' and choice_name=='����':
		print("��Ӯ��")
	elif i=='ʷ����' and choice_name=='ֽ':
		print("��Ӯ��")
	elif i=='ֽ' and choice_name=='����':
		print("��Ӯ��")
	elif i=='ֽ' and choice_name=='����':
		print("��Ӯ��")
	elif i=='����' and choice_name=='ʯͷ':
		print("��Ӯ��")
	elif i=='����' and choice_name=='����':
		print("��Ӯ��")
	elif i=='����' and choice_name=='ʷ����':
		print("��Ӯ��")
	elif i=='����' and choice_name=='ʯͷ':
		print("��Ӯ��")
	elif i=='����' and choice_name=='����':
		print("ƽ��")
	elif i=='ʯͷ' and choice_name=='ʯͷ':
		print("ƽ��")
	elif i=='ʷ����' and choice_name=='ʷ����':
		print("ƽ��")
	elif i=='����' and choice_name=='����':
		print("ƽ��")
	elif i=='ֽ' and choice_name=='ֽ':
		print("ƽ��")
	else:
		print("Error: No Correct Name")
import random
x=random.randint(0,4)
i=number_to_name(x)
print("----------------")
print("����ѡ��Ϊ��%s"%(choice_name))
print("�������ѡ��Ϊ��%s"%(i))
rpsls(i,choice_name)
