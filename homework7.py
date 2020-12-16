
score = list()
def enterscore():
    a=int(input("請輸入班級人數"))
    for i in range(a):
        b=int(input("請輸入分數"))
        score.append(b)
def average(score):
    total = 0
    return sum(score)/len(score)
def highest(score):
    return max(score)
def lowest(score):
    return min(score)
enterscore()
b = average(score)
c = highest(score)
d = lowest(score)
print("平均:" ,b)
print("最高:" ,c)
print("最低:" ,d)