from random import randint

set_ = set()
while True:
    x = randint(1,10)
    if x in set_:
        break
    set_.add(x)
print(len(set_)+1)