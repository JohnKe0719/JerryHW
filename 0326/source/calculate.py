
# coding: utf-8

# In[ ]:


def plus(num=[]):
    return sum(num)
def sub(num=[]):
    return num[0]-sum(num[1:])
def multiple(num=[]):
    result=1
    for i in num:
        result = result * i
    return result
def divide(num=[]):
    result=num[0]
    s=1
    for i in range(1,len(num)):
        s=s*num[i]
    result = result/s
    return result

def calculator(func,num=[]):
    dis={"+":plus,"-":sub,"*":multiple,"/":divide}
    return dis[func](num)
