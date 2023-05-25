giimport http.client
import json

# Задаем условия операций json
def execute(res, num):
    if fjson['operation'] == 'sum':
        return res + num
    if fjson['operation'] == 'sub':
        return res - num
    if fjson['operation'] == 'mul':
        return res * num
    if fjson['operation'] == 'div':
        return res / num

# Задание 1 - Отправить HTTP запрос GET
print('Задание №1')
connection = http.client.HTTPConnection("167.172.172.227:8000")
connection.request('GET', '/number/4', )

a1 = connection.getresponse().read().decode()
a1_json = json.loads(a1)
print('Число:', a1_json['number'])

# Задание 2 - Отправить HTTP запрос GET с параметром
print('Задание №2')
connection.request('GET', '/number/?option=4', )
a2 = connection.getresponse().read().decode()
a2_json = json.loads(a2)
print(a2_json['number'])

s = a2_json['number'] + a1_json['number']
print('Конечное число:',s)

# Задание 3 - Отправить HTTP запрос POST
print('Задание №3')
head= {'Content-type': 'application/x-www-form-urlencoded'}
connection.request('POST', '/number/', 'option=4', head)
response = connection.getresponse().read().decode()
response_json = json.loads(response)
print(response_json['number'])

e = s + response_json['number']
print('Конечное число:',e)

# Задание 4 - Отправить HTTP запрос PUT с телом JSON
print('Задание №4')
head = {'Content-type': 'application/json'}
body = json.dumps({'option': 4})
connection.request('PUT', '/number/', body, head)
response = connection.getresponse().read().decode()
response_json = json.loads(response)
print(response_json['number'])

w = (e * (response_json['number']))
print('Конечное число:',w)

# Задание 5 - Отправить HTTP запрос DELETE с телом JSON
print('Задание №5')
body = json.dumps({'option': 4})
connection.request('DELETE', '/number/', body)
response = connection.getresponse().read().decode()
response_json = json.loads(response)
print(response_json['number'])

print('Конечное число:',(response_json['number']) / w)