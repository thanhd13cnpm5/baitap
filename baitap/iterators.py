# iterators
# tạo lớp iterator
class increaseNumber():
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if self.num <= self.max:
            value = self.num
            self.num += 1

            return value
        else:
            raise StopIteration

# duyệt bằng vong lặp for
print("using loop for")
for num in increaseNumber(4):
    print(num)

# duyệt bằng next qua từng phần tu
print("\nusing iterator")
num = increaseNumber(4)
n = iter(num)
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))# khi n > 4 sẽ raise "StopIteration"