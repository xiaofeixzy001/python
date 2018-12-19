# 打印100以内的斐波那契数列
"""
分析：
0 1 1 2 3 5 8 13 ..
从第三项开始，等于前两个数的和,这个和最大不能大于100
第一项：x = 0
第二项：y = 1
第三项：x + y = 1
第四项：(y) + (x+y) = 2
第五项：(x+y) + ((y) + (x+y)) = 3
...
"""
# 方法1：
x = 0
y = 1

while y < 100:
    print(y)
    x, y = y, x + y

# 方法2：
a = 0
b = 1
print(a)
print(b)
while True:
    c = a+b
    if c <= 100:
        print(c)
        a=b
        b=c
    else:
        break

# 方法3
def fibs(x):

    result = [0, 1]
    for index in range(x - 2):  # 前两位已固定
        result.append(result[-2] + result[-1])  # result[-2]倒数第二个数，result[-1]倒数第一个数

    return result


if __name__ == '__main__':
    num = input('Enter one number: ')
    num = int(num)
    print(fibs(num))

# 使用 Python 实现随机生成 200 个无重复激活码（或者优惠券），字符串长度大于5以上
import random
def v_code(n=5):
    res=''
    for i in range(n):
        num=random.randint(0,9) # 随机选择数字
        s=chr(random.randint(65,90)) # 随机选择字母,chr()转换数字为ASCII码对应的字母
        t = chr(random.randint(97,122))
        add=random.choice([num,s,t])
        res+=str(add)  # res = res + str(add) 字符串拼接
    return res
print(v_code())

for i in range(1,201):
    k = v_code(10)
    print(k)



"""
(0 + 0)

    优惠码有重复的时候，无法添加到200个
"""














        