# -*- coding:utf-8 -*-
# author:   terry
# email:    terryoyty@163.com
# datetime: 2022/06/15 12:54
# ide:      PyCharm
import itertools


def phonenum_handler(digits_str) -> list:
    """
    电话组合排列
    给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
    给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
    示例: 输入："23" 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
    说明：尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序.
    :param digits_str:
    :return:
    """
    if not digits_str:
        return list()

    mapping = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    groups = (mapping[digit] for digit in digits_str)
    return ["".join(combination) for combination in itertools.product(*groups)]


if __name__ == '__main__':

    print(phonenum_handler('23'))