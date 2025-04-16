_, A, B = map(str.split, open(0))
print(len({*A} ^ {*B}))