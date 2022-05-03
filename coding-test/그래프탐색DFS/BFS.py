# 탐색이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정을 말한다.
# 대표적인 그래프 탐색 알고리즘에는 DFS와 BFS가 있습니다.


# 1. 스택 자료구조
# 먼저 들어 온 데이터가 나중에 나가는 형식(선입후출)의 자료구조입니다.
# 입구와 출구가 동일한 형태로 스택을 시각화할 수 있습니다.
# ex) 박스쌓기

# 큐 자료구조
# 먼저 들어온 데이터가 먼저 나가는 형식(선입선출)의 자료구조
# 큐는 입구와 출구가 모두 뚫려 있는 터널과 같은 형태로 시각화 할 수 있습니다.
from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse()
print(queue) # 나중에 들어온 원소부터 출력


# 재귀함수
# 재귀 함수(Recursive Function)란 자기 자신을 다시 호출하는 함수를 의미한다.
def recursive_funtion():
    print('재귀 함수를 호출합니다.')
    #recursive_function()

recursive_funtion()
# 재귀 함수를 문제풀이에서 사용할 때는 재귀 함수의 종료 조건을 반드시 명시해야 한다.
# 종료 조건을 제대로 명시하지 않으면 함수가 무한히 호출될 수 있다.
def recursive2_function(i):
    if i == 100:
        return
    print(i, '번재 재귀함수에서', i+1, '번째 재귀함수를 출력합니다.')
    recursive2_function(i+1)
    print(i, 'i번째 재귀함수를 호출합니다.')
recursive2_function(100)


