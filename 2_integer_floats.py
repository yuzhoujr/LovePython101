#!/usr/bin/python
# -*- coding: utf-8 -*-
def star():
  print "********************"


#第二课， 加减乘除，Integer/Floats
# String的问题所在，以及计算的Introduction
# num1 = "20"
# num2 = "30"
# print num1 + num2

star()
#加
print "加: 3+2= ", 3 + 2
#减
print "减: 3-4= ", 3 - 4
#乘
print "乘: 3*4= ", 3 * 4
#除
print "除: 3/2 = ", 3 / 2   #讲明白这里面的 3/2 和 3/2.0 的区别
print "除: 3/2.0 = ", 3 / 2.0  # 2.0 英语的梗
print "除: 3/float(2) = ", 3 / float(2)
star()


# Exponential
print "指数： 3^3: ", 3 ** 3
# Modulus
# 确认一个数是基数还是偶数 ， 是否能被整除
# 举例： fizzbuzz
print "取模运算符: 3%2= ", 3 % 2
#大杂烩
print "大杂烩: ", 3 * (2+1)
star()

# Count增加
print "增量:"
num = 1
num = num + 1
num += 1
print num
num *= 10
print num
num /= 5
print num
star()

#绝对值
print "绝对值: abs(-100): ", abs(-100)

#四舍五入
print "四舍五入: round(3.99, 1)", round(3.99, 1)


# String casting
print "Casting: "
num1 = int("20")
num2 = int("30")
print num1 + num2
star()



# 体脂测量方法一：

# 女性的身体脂率公式
#     参数a = 腰围厘米(腰部的周长) x 0.74
#     参数b = 总体重公斤 x 0.082 + 34.89
#     身体脂肪总重量公斤 = a - b
#     身体脂肪百分比= (身体脂肪总重量÷ 体重) x 100%

# 男性的身体脂率公式
#     参数a = 腰围厘米 x 0.74
#     参数b =  体重公斤 x 0.082 + 44.74
#     身体脂肪总重量公斤= a - b
#     体脂率(身体脂肪百分比) = (身体脂肪总重量÷ 体重) x 100%


waist = 69 * 0.74
weight = 58 * 0.082 + 34.89
p1 = (waist - weight) / 58 * 100
print "脂肪含量1= ", p1

# 测量方法二：BMI公式法

# 体脂% =1.2×BMI+0.23× 年龄-5.4-10.8×性别（男为1，女为0）
# BMI=体重kg÷ （身高×身高）

BMI = 58/(1.65*1.65)
p2 = (1.20 * BMI + (0.23 * 25) - 5.4)
print "脂肪含量2= ", p2
star()






# 草船借箭，智力题作业
# 好了，诸葛亮要牛逼逼的去干一票大的，奈何他的数学智商为0，他需要10万之箭
# 目前市场上只能通过江湖奸商购买稻草人来装箭， 诸葛亮不知道自己最少需要多少钱
# 才能买到足够的稻草人。
# 他只能求助聪明的周瑜（也就是你），来帮忙计算最终的价格
#
# 价格如下，聪明的周瑜，请问诸葛亮一共需要多少钱(四舍五入哟)才能去借箭呢？

# 计算机给出了江湖奸商的价格表格：

# 品种               载重           数量           价格
# 普通稻草人          500           x无限          100
# VIP稻草人          1532           x5            150
# Maggie专用稻草人   2000           x1             1

p_maggie = 1
p_vip = 150*5
quan_reg = (100000 - 2000 - (1532*5)) / 500.0   #记得提醒float操作
p_reg = round(quan_reg) * 100  #数量需要整数
total = p_vip + p_maggie + p_reg
print "需要总额: ", total
