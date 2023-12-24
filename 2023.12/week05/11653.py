N = int(input())

divide = 2;
while N!= 1 :
    if N%divide != 0:
        divide +=1
    else:
        N //= divide
        print(divide)

# import math

# N = int(input())

# def optimized_prime(N):
#     # 2로 나누기 (짝수)
#     while N % 2 == 0:
#         print(2)
#         N //= 2

#     # 3부터 sqrt(n)까지의 홀수로 나누기
#     for i in range(3, int(math.sqrt(N)) + 1, 2):
#         while N % i == 0:
#             print(i)
#             N //= i

#     # 남은 수가 소수인 경우 출력
#     if N > 1:
#         print(N)

# # 최적화된 소인수분해 함수 호출
# optimized_prime(N)