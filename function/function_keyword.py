def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)

func(3, 7)
func(25, c=24) #称其为关键字参数
func(c=50, a=100)
# 两大优点
# 其一，我们不再需要考虑参数的顺序，函数的使用将更加容易。
# 其二，我们可以只对那些我们希望赋予的参数以赋值，只要其它的参数都具有默认参数值。
