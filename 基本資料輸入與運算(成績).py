'''
print("歡迎使用成績輸入系統")
name=input("請輸入名字:")
engh=input("請輸入英文成績:")
math=input("請輸入數學成績:")
total=int(engh)+int(math)

print("%s你的總分是:%d" %(name,total))




'''
#用eval呈現上述公式
print("歡迎使用成績輸入系統")
name=input("請輸入名字:")
engh=eval(input("請輸入英文成績:"))
math=eval(input("請輸入數學成績:"))
total=engh+math

print("%s你的總分是:%d" %(name,total))
