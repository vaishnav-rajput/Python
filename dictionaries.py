x = {'key': 4}
value_x = x['key']
x['key2'] = 5
x[2] = 8
check_present = 'key' in x
print(check_present)

get_all_values = list(x.values())
del x['key']

for key,value in x.items():
    print(key, value)

for key in x:
    print(key, x[key])    