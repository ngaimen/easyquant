#!/usr/bin/python3
import json

def file2dict():
    with open('config.json', mode='r', encoding='utf-8') as f:
        return json.load(f)


def dict2file(data):
    with open('config.json', mode='w', encoding='utf-8') as f:
        json_str = json.dumps(data)
        f.write(json_str)
        f.flush()

data = file2dict()
choose = int(input('1.add/edit 2.delete \n'))
code = str(input('input stock code you will edit:\n'))

if choose == 2:
    del data[code]
else:
    high = float(input('input high price of this code:\n'))
    zhisunbili1 = float(input('input 止损比例1 of this code:\n'))
    zhisunbili2 = float(input('input 止损比例2 of this code:\n'))

    if code not in data.keys():
        data[code] = {}

    data[code]['zsbl'] = str(zhisunbili1)
    data[code]['zsbl2'] = str(zhisunbili2)
    data[code]['zs'] = str(high * zhisunbili1)
    data[code]['zs2'] = str(high * zhisunbili2)

dict2file(data)