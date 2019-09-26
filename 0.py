# a = '    hello worldf'
# print(a.strip().title())
x = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(x('nyimas', 'AMALIA'))

def bqf (a,b,c):
    return lambda x: a*x**2 +b*x +c
# f= bqf(2,3,-5)
# a= f(0)
# print(a)
print(bqf(2,3,-5)(0))

# tes commit