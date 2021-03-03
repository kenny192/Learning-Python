# coding: UTF-8
"""
将十进制数（包括小数）转换为二进制数。
"""

def dec2bin(x):
    if isinstance(x, int):
        return bin(x)
    elif isinstance(x,float):
        s = ''              # 初始化一个空字符串，准备用来记录转换结果
        if x < 0:
            x = -x
            s += '-'        # 如果是小数，则加个负号，把数据转换为正数来处理
        xint = int(x)       # 取出小数点前面的整数部分
        x -= xint           # 取出小数点后面的小数部分
        s += bin(xint)      # 把整数部分转换为二进制
        if x == 0:
            return s        # 如果小数部分是0，则直接返回
        else:
            s += '.'        # 如果有小数，则加个小数点
            while x != 0:   # 按小数转换为二进制数的算法循环做下去
                x *=2
                xint = int(x)
                x -= xint
                s += str(xint)
            return s
    else:
        return "Can't be converted to binary for it isn't a decimal."

x = -2.5
print(x, '=', dec2bin(x))