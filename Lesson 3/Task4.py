import xml.etree.ElementTree as ET
a = '<root><element1 /><element2 /><element3><element4 /></element3></root>'
tree = ET.fromstring(a)
root = getroot(a)

print(tree[0], root)
# def foo(a):
#     d = {}

#     return d



# foo(a) -> 
# {
#     'name': 'root', 
#     'children': [
#         {'name': 'element1', 'children': []},
#         {'name': 'element2', 'children': []},
#         {'name': 'element3', 'children': [{'name': 'element4', 'children': []}]}
#     ]
# }, 2