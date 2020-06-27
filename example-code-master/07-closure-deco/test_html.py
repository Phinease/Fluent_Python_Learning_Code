import html


def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)


print(htmlize("SW ktp 32"))
print(htmlize([32, 52, 'ym']))
print('-'*20, 'test repr', '-'*20)
print(repr.__doc__)
print(repr([32, 52, [32, 22]]))
print(repr(htmlize))
print('-'*20, 'test repr', '-'*20)
print(htmlize(htmlize))
