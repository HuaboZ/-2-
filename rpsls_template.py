#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者 张瑛
日期 2020年4月10日
目的 通过自定义函数，实现RPSLS游戏 
"""

import random



# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """
    if name=="石头":
	    a=0
    elif name=="史波克":
	    a=1
    elif name=="布":
        a=2
    elif name=="蜥蜴":
	    a=3
    elif name=="剪刀": 
        a=4
    else:	
        a="Error: No Correct Name"
    return a				
 

def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if number==0:
       b="石头"
    elif number==1:
       b="史波克"
    elif number==2:
       b="布"
    elif number==3:
       b="蜥蜴"
    elif number==4: 
       b="剪刀"
    return b



    

def rpsls(player_choice):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

    """
   
    player_choice_number=name_to_number(player_choice)
    x=player_choice_number
    
    computer_number=random.randint(0,4)
    y=computer_number
    
    print("计算机的选择是：")
    print(number_to_name(computer_number))
    if x==y:
       print("您和计算机选择一样呢")
    elif x==0 and (y==4 or y==3):
       print("您赢了")
   
	      	  
    elif x==1 and (y==0 or y==4):
       print("您赢了")
     
    elif x==2 and (y==0 or y==1):
	    print("您赢了")
		 
    elif x==3 and (y==2 or y==1):
	    print("您赢了")					
    elif x==4 and (y==2 or y==3):
	    print("您赢了")
    elif x=="Error: No Correct Name":
	    print("Error: No Correct Name")
    else:
	    print("计算机赢了")    			
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()

rpsls(choice_name)

#
