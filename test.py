def solution(N):
    # write your code in Python 3.6
    answer = []
    if N % 2 == 0:
        answer = ['a' for i in range(N - 1)]
        answer.append('b')
    else:
        answer = ['a' for i in range(N)]

    return (answer)

print(solution(7))
