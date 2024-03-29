#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   415. 字符串相加.py
@Time    :   2019/11/15 08:32:02
@Author  :   吉祥鸟
@GitHub  :   https://github.com/jixn-hu
@CSDN    :   https://me.csdn.net/qq_37462361
'''

"""
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：

num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    """
    将数字0-9和字符串做一一对应，从而变成int型，然后相加
    """
    def addStrings(self, num1: str, num2: str) -> str:

        num_num1 = self.num(num1)
        num_num2 = self.num(num2)
        return str(num_num1+num_num2)

    def num(self, num1): 
        """
        str变成int型
        """
        dic_num = {'1': 1,
                    '2': 2,
                    '3': 3,
                    '4': 4,
                    '5': 5,
                    '6': 6,
                    '7': 7,
                    '8': 8,
                    '9': 9,
                    "0":0 }
        num_num1 = 0
        a = 0
        for i in num1:  # 多少位数
            a += 1
        for i in num1:
            a -= 1
            num_num1 += dic_num[i]*10**a
        return num_num1


if __name__ == "__main__":
    a = Solution().addStrings("0", "0")
    print(a)
