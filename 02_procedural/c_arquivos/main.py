import json

d1 = {
	'Pessoa 1': {
		'nome': 'Luiz',
		'idade': 24
	},
	'Pessoa 2': {
		'nome': 'Ana',
		'idade': 26
	}
}

d1_json = json.dumps(d1, indent = True)
print(d1_json)

with open('abc.json', 'w+') as file:
	file.write(d1_json)

with open('abc.json', 'r') as file:
	d1_json = file.read()
	d1_json = json.loads(d1_json)

for k, v in d1_json.items():
	print(k)
	for k1, v1 in v.items():
		print(k1, v1)
