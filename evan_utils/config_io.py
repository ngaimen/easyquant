import json

def file2dict():
    with open('config.json', mode='r', encoding='utf-8') as f:
        return json.load(f)


def dict2file(data):
    with open('config.json', mode='w', encoding='utf-8') as f:
        json_str = json.dumps(data)
        f.write(json_str)
        f.flush()