#generators

def increaseNumberGen(max=0):
    num = 1
    while num <= max:
        yield num
        num += 1

# duyệt bằng vong lặp for
print("using loop for")
for a in increaseNumberGen(4):
    print(a)

# duyệt bằng next qua từng phần tu
print("\nusing generator")
y = increaseNumberGen(4)
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y)) # khi n > 4 sẽ raise "StopIteration"