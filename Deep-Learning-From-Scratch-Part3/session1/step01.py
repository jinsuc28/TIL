class Variable:
    def __init__(self, data):
        self.data = data

import numpy as np

data = np.array(1,0)
x = Variable(data)
print(x.data)


# Variable 클래스는 data를 인스턴스 변수로 갖는다.
# 스칼라(0차원 배열), 벡터(2차원 배열), 행렬(3차원 배열) 축을 기준으로 차원이 늘어난다.
# 다차원 배열(텐서)는 0차원 텐서(스칼라), 1차원 텐서(벡터), 2차원 텐서(행렬), 3차원 텐서(3차원 이상의 배열)로 부를 수 있다.