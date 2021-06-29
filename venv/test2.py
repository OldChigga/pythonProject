# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# number = int(input("请输入您的6位奖票号码："))     # 输入奖票号码
# if number  == 432678 :         # 判断是否符合条件，即输入奖票号码是否等于432678
#     print(number,"你中了本期大奖，请速来领奖！！")  # 等于中奖号码，输出中奖信息
# if number  != 432678 :        # 判断是否符合条件，即输入奖票号码不等于432678
#     print(number,"你未中本期大奖！！")   # 不等于中奖号码，输出未中奖信息


# number = int(input("请输入您的6位奖票号码："))     # 输入奖票号码
# if number  == 432678 :         # 判断是否符合条件，即输入奖票号码是否等于432678
#     print(number,"你中了本期大奖，请速来领奖！！")  # 等于中奖号码，输出中奖信息
# else:
#     print(number,"你未中本期大奖！！")  # 不等于中奖号码，输出未中奖信息


# data = 105       # 商品日销量为105
# if data >=100 :         # 判断是否符合条件，即日销售量是否大于或等于100
#     print(data,"此商品为A类商品！！")    # 大于或等于100时，输出A类商品信息
# else:        # 判断是否符合条件，即日销售量是否小于100
#     print(data,"此商品为B类商品！！")  # 小于100时，输出B类商品信息

# a = -9
# b = a if a>0 else -a
# print(b)

# number = int(input("请输入商品7天销量："))  # 输入某个商品7天销量
# if number  >= 1000:           # 判断是否符合条件，即输入销量是否大于或等于1000
#     print("本商品7天销量为A！！")      # 大于或等于1000，输出销量评价
# elif number  >= 500:          # 判断是否符合条件，即输入销量是否大于或等于500
#      print("本商品7天销量为B！！")      # 大于或等于500，输出销量评价
# elif number  >=300:          # 判断是否符合条件，即输入销量是否大于或等于300
#      print("本商品7天销量为C！！")      # 大于或等于300，输出销量评价
# else:          # 判断是否符合条件，即输入销量如果小于300
#      print("本商品7天销量为D！！")      # 小于300，输出销量评价


# number = int(input("请输入商品7天销量："))  # 输入某个7天商品销量
# if number >= 1000:     # 判断是否符合条件，即输入销量是否大于或等于1000
#     print("本商品7天销量为A！！")     # 大于或等于1000，输出销量评价
# else:
#     if number >= 500:     # 判断是否符合条件，即输入销量是否大于或等于500
#         print("本商品7天销量为B！！")     # 大于或等于500，输出销量评价
#     else :
#         if number >= 300:     # 判断是否符合条件，即输入销量是否大于或等于300
#             print("本商品7天销量为C！！")   # 大于或等于300，输出销量评价
#         else:     # 判断是否符合条件，即输入销量如果小于300
#             print("本商品7天销量为D！！")   # 小于300，输出销量评价

# age = int(input("请输入您的年龄："))       # 输入年龄
# if age >= 18  and age <= 70:         # 输入年龄是否在18~70之间
#     print("您可以申请小型汽车驾驶证！")    # 输出“您可以申请小型汽车驾驶证”

# age = int(input("请输入您的年龄："))       # 输入年龄
# if age  >= 18 :       # 输入年龄是否在18~70之间
#     if age  <= 70:
#         print("您可以申请小型汽车驾驶证！")  # 输出“您可以申请小型汽车驾驶证”

# print("今有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二，问几何？\n")
# number = int(input("请输入您认为符合条件的数："))     # 输入一个数
# if number%3 == 2 and number%5 == 3 and number%7 == 2:  # 判断是否符合条件
#     print(number,"符合条件：三三数之剩二，五五数之剩三，七七数之剩二")


# sales = int(input("请输入商品日销量"))   # 输入商品日销量
# if sales  <10  or sales > 100:         # 判断条件
#     print("该商品为重点关注商品")      # 输出“该商品为重点关注商品”


# sales = int(input("请输入商品日销量"))  # 输入商品日销量
# if sales  <10 :         # 判断条件
#     print("该商品为重点关注商品")      # 输出“该商品为重点关注商品”
# if  sales > 100:       # 判断条件
#     print("该商品为重点关注商品")      # 输出“该商品为重点关注商品”

# data = None
# if not data:   # 代码并未为data赋值，所以data是空值，即data为False
#     print("You lost!")   # 输出结果为“You lost!”（你输了!）
# else:
#     print("You win!")   # 输出结果为“You win!”（你赢了!）

# a = input("请输入1位数字密码")   # 输入数字密码
# b = ['0','1','2','3','4','5','6','7','8','9']  # 设定数字密码的数字列表
# if a not in b:   # 输入内容未在数字列表中
#     print("非法输入")   # 输出“非法输入”

for i in [1, 2, 3]:
    print("笑傲江湖")  # 输出“笑傲江湖”

for i in ["明日", "科技", "与您", "同行"]:
    print(i)  # 循环输出“明日”“科技”“与您”“同行”

print("计算1+2+3+……+100的结果为：")
result = 0  # 保存累加结果的变量
for i in range(101):
    result += i  # 实现累加功能
print(result)  # 在循环结束时输出结果