#!/usr/bin/python3
import json
from evan_utils import config_io

data = config_io.file2dict()
choose = int(input('1.add/edit 2.delete \n'))
code = str(input('input stock code you will edit:\n'))

if choose == 2:
    del data[code]
else:
    high = float(input('输入该股票的阻力价格:\n'))
    high = high * 1.15
    zhisunbili1 = float(input('input 止损比例1 of this code:\n'))
    zhisunbili2 = float(input('input 止损比例2 of this code:\n'))

    if code not in data.keys():
        data[code] = {}

    data[code]['zsbl'] = str(zhisunbili1)
    data[code]['zsbl2'] = str(zhisunbili2)
    data[code]['zs'] = str(high * zhisunbili1)
    data[code]['zs2'] = str(high * zhisunbili2)

config_io.dict2file(data)