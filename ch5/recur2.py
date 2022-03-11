# 재귀호출 거꾸로

def recur(n: int)-> int:
    if n > 0:
        recur(n-2)
        print(n)
        recur(n-1)

x = int(input('정수 값을 입력하세요: '))
recur(x)