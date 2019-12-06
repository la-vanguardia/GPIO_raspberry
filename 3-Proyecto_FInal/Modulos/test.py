import json

test = {
    'XX': [251, 0],
    'YY': 30,
    'YY_LSB': 0,
    'ZZ': 30,
    'ZZ_LSB': 30,
    'Nombre': 'Pepe',
}

test_2 = {
    'cosa': 1,
    'hola': 3
}


for keys in test_2:
    print(keys)
    print('\n')



test['cosa'] = test_2

test_json = json.dumps(test)

test = json.loads(test_json)

print(test['XX'][0])