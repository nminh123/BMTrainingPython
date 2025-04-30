import json

data = '''
[
    {"name": "Cao Nhat Minh", "year": "2004", "city": "Tp.HCM"},
    {"name": "Nguyen Van A", "year": "2222", "city": "Thread City"},
    {"name": "Pham Quach B", "year": "3333", "city": "OnlyFan City"}
]
'''


y = json.loads(data)

print(y)