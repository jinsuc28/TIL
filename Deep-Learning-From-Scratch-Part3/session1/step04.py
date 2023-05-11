# 미분은 변화율을 의미함
# 어떤 f(x)을 미분한 f'(x)는 도함수이다.

# 전진차분과 중앙차분
# 미분을 위해서는 x 와 x+h 사이에 거리가 극한 값으로 정의해서 미분해야하지만
# 컴퓨터 특성상 극한으로 미분하기가 어렵기 때문에 근사치로 미분을 하게 된다.
# 이때 전진차분, 중앙차분이라는 개념이 나오며 중앙차분이 더 정확하다.(테일러 급수로 증명 가능)

# 중앙차분을 이용한 수치미분 구현
import numpy as np

def numerical_diff(f, x, eps=1e-4):
    x0 = Variable(x.data - eps)
    x1 = Variable(x.data + eps)
    y0 = f(x0)
    y1 = f(x1)
    return (y1.data - y0.data) / (2 * eps)

class Variable:
    def __init__(self, data):
        self.data = data

class Function:
    def __call__(self, input):
        x = input.data # 데이터를 꺼낸다.
        y = x ** 2 # 실제 계산
        output = Variable(y) # Variable 형태로 되돌린다.
        return output
    
    def forward(self, x):
        raise NotImplementedError()
    
class Square(Function):
    def forward(self, x):
        return x ** 2

class Exp(Function):
    def forward(self, x):
        return np.exp(x)

f = Square()
x = Variable(np.array(2.0))
dy = numerical_diff(f, x)
print(dy)

# 합성함수의 미분 구현

def f(x):
    A = Square()
    B = Exp()
    C = Square()
    return C(B(A(x)))

x = Variable(np.array(0.5))
dy = numerical_diff(f, x)
print(dy)