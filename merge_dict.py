# -*- coding:utf-8 -*-
# author:   terry
# email:    terryoyty@163.com
# datetime: 2022/06/15 12:46
# ide:      PyCharm
from copy import deepcopy
from pprint import pprint


def merge_dict(source_dict, update_dict) -> dict:
    """
    深度合并Dict

    :param source_dict:
        {
            'key0': 'a',
            'key1': 'b',
            'key2': {
                'inner_key0': 'c',
                'inner_key1': 'd'
            }
        }
    :param update_dict:
        {
            'key1': 'x',
            'key2': {
                'inner_key0': 'y'
            }
        }
    :return:
        {
            'key0': 'a',
            'key1': 'x', # overridden by update_dict
            'key2': {
                'inner_key0': 'y', # overridden by update_dict
                'inner_key1': 'd'
            }
        }
    """

    if not source_dict:
        return deepcopy(update_dict)

    if not update_dict:
        return deepcopy(source_dict)

    result = {}

    overlapping_keys = source_dict.keys() & update_dict.keys()

    for k in overlapping_keys:
        if isinstance(source_dict[k], dict) and isinstance(update_dict[k], dict):
            result[k] = merge_dict(source_dict[k], update_dict[k])
        elif isinstance(source_dict[k], list) and isinstance(update_dict[k], list):
            result[k] = copy(update_dict[k])
        else:
            result[k] = update_dict[k]

    for k in source_dict.keys() - overlapping_keys:
        result[k] = deepcopy(source_dict[k])

    for k in update_dict.keys() - overlapping_keys:
        result[k] = deepcopy(update_dict[k])

    return result


if __name__ == '__main__':

    s = {
        'key0': 'a',
        'key1': 'b',
        'key2': {
            'inner_key0': 'c',
            'inner_key1': 'd'
        }
    }
    u = {
        'key1': 'x',
        'key2': {
            'inner_key0': 'y'
        }
    }

    r = merge_dict(s, u)
    pprint(r)
