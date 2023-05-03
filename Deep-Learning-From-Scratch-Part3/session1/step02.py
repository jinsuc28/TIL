import numpy as np

# 노드를 화살표로 연결해 계산 과정을 계산 그래프(computational graph)라고 부름.

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
        raise NotImplementedError() # 예외처리 발생시켜 클래스 상속하여 구현해야된다는 것을 알려줌.

class Square(Function):
    def forward(self, x):
        return x ** 2
    
x = Variable(np.array(10))
f = Function()
y = f(x)

print(type(y))
print(y.data)


