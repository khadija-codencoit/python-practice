items = [
    ('product1',10000),
    ('product2',200),
    ('product',300),
]

items.sort(key=lambda item:item[1])
print(items)