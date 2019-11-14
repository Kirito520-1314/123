#coding:gbk
"""
剪刀裁剪纸；纸包裹石头；石头砸碎剪刀；石头砸死蜥蜴；蜥蜴毒死史波克
王志鸿
"""

# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀
print("欢迎使用RPSLS游戏")
print('-----------------')
print("请输入您的选择:")
choice_name=input()
def name_to_number(name):
	"""
	将游戏对象对应到不同的整数
	"""
	if name=='石头':
		return 0
	if name=='史波克':
		return 1
	if name=='纸':
		return 2
	if name=='蜥蜴':
		return 3
	if name=='剪刀':
		return 4
def number_to_name(num):
	if num==0:
		return "石头"
	elif num==1:
		return "史波克"
	elif num==2:
		return "纸"
	elif num==3:
		return "蜥蜴"
	elif num==4:
		return "剪刀"

def rpsls(i,choice_name):
	if i=='石头' and choice_name=='剪刀':
		print("电脑赢了")
	elif i=='石头' and choice_name=='蜥蜴':
		print("电脑赢了")
	elif i=='史波克' and choice_name=='石头':
		print("电脑赢了")
	elif i=='史波克' and choice_name=='剪刀':
		print("电脑赢了")
	elif i=='纸' and choice_name=='石头':
		print("电脑赢了")
	elif i=='纸' and choice_name=='史波克':
		print("电脑赢了")
	elif i=='蜥蜴' and choice_name=='史波克':
		print("电脑赢了")
	elif i=='蜥蜴' and choice_name=='纸':
		print("电脑赢了")
	elif i=='剪刀' and choice_name=='纸':
		print("电脑赢了")
	elif i=='剪刀' and choice_name=='蜥蜴':
		print("电脑赢了")
	elif i=='石头' and choice_name=='史波克':
		print("您赢了")
	elif i=='石头' and choice_name=='纸':
		print("您赢了")
	elif i=='史波克' and choice_name=='蜥蜴':
		print("您赢了")
	elif i=='史波克' and choice_name=='纸':
		print("您赢了")
	elif i=='纸' and choice_name=='剪刀':
		print("您赢了")
	elif i=='纸' and choice_name=='蜥蜴':
		print("您赢了")
	elif i=='蜥蜴' and choice_name=='石头':
		print("您赢了")
	elif i=='蜥蜴' and choice_name=='剪刀':
		print("您赢了")
	elif i=='剪刀' and choice_name=='史波克':
		print("您赢了")
	elif i=='剪刀' and choice_name=='石头':
		print("您赢了")
	elif i=='蜥蜴' and choice_name=='蜥蜴':
		print("平局")
	elif i=='石头' and choice_name=='石头':
		print("平局")
	elif i=='史波克' and choice_name=='史波克':
		print("平局")
	elif i=='剪刀' and choice_name=='剪刀':
		print("平局")
	elif i=='纸' and choice_name=='纸':
		print("平局")
	else:
		print("Error: No Correct Name")
import random
x=random.randint(0,4)
i=number_to_name(x)
print("----------------")
print("您的选择为：%s"%(choice_name))
print("计算机的选择为：%s"%(i))
rpsls(i,choice_name)
