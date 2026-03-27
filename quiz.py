def pul_11(*num):
    return sum(num)

def pul_12(func):
    def wrapper(*num):
        a = func(*num) / len(num)
        return a
    return wrapper

pul_11 = pul_12(pul_11)
print(pul_11(1, 2, 3, 4, 5))
