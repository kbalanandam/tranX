import json


def test():
    data = json.loads( '[{"type": "P", "ccode": "91", "phoneno": "6301414334"},\
     {"type": "E", "ccode": "91", "phoneno": "7780654655"}]')
    phones =[]

    for p in data:
        phones.append(p)

    for i in phones:
        print(i['type'])
test()