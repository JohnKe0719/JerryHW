
# coding: utf-8

# In[ ]:


from source import calculate as c

while True:
    try:
        x=input("請輸入數字（用空格分開）：").split(" ")
        cal=input("請輸入要做的運算符號(+,-,*,/)：")
        for i in range(0,len(x)):
            x[i] = eval(x[i])
        print(c.calculator(cal,x))
        break
    except:
        print("輸入錯誤,請重新輸入")

