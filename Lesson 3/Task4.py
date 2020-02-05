import xml.etree.ElementTree as ET

def foo(a):
    root = ET.fromstring(a)
    d = dict(name=root.tag, children=[])
    l = []
    for i in root:
        d1 = dict(name=i.tag, children=[])
        l.append(d1)
        l2 = []
        for j in i:
            d2 = dict(name=j.tag, children=[])
            l2.append(d2)
        d1['children'] = l2
    d['children'] = l
    return d


a = '<root><element1 /><element2 /><element3><element4 /></element3></root>'
print(foo(a))