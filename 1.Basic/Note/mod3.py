PI = 3.141592

class Math:
    def solve(self,r): # class에서 정의할 때, self 꼭 적어야함 (부를때는 상관없음)
        return PI * (r**2) # 원의 넓이(면적) 반환
    def sum(self,a,b):
        return a + b

# 아래 부분이 실행됨
if __name__ == "__main__":
    print(PI)
    a = Math()
    print(a.solve(2))
    print(a.sum(PI,4.4))