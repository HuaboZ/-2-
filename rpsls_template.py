#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���� ����
���� 2020��4��10��
Ŀ�� ͨ���Զ��庯����ʵ��RPSLS��Ϸ 
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name=="ʯͷ":
	    a=0
    elif name=="ʷ����":
	    a=1
    elif name=="��":
        a=2
    elif name=="����":
	    a=3
    elif name=="����": 
        a=4
    else:	
        print("Error: No Correct Name")
    return a				
 

def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number==0:
       b="ʯͷ"
    if number==1:
       b="ʷ����"
    if number==2:
       b="��"
    if number==3:
       b="����"
    elif number==4: 
       b="����"
    return b



    

def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
   
    player_choice_number=name_to_number(player_choice)
    x=player_choice_number
    
    computer_number=random.randint(0,4)
    y=computer_number
    
    print("�������ѡ���ǣ�")
    print(number_to_name(computer_number))
    if x==y:
       print("���ͼ����ѡ��һ����")
    if (x==0,y==4)or(x==0,y==3):
       print("��Ӯ��")
	  
    elif (x==1,y==0)or(x==1,y==4):
       print("��Ӯ��")
      
    elif (x==2,y==0)or(x==2,y==1):
	    print("��Ӯ��")
		 
    elif (x==3,y==2)or(x==3,y==1):
	    print("��Ӯ��")
					
    elif (x==4,y==2)or(x==4,y==3):
	    print("��Ӯ��")
    else:
	    print("�����Ӯ��")			
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)

#
