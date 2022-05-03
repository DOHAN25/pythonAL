# 정렬이란 데이터를 특정한 기준에 따라 순서대로 나열하는 것을 말한다.
# 일반적으로 문제 상황에 따라 적절한 정렬 알고리즘이 공식처럼 사용된다.

# 선택정렬
# 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 만 앞에 있는 데이터와 바꾸는 것을 반복한다.
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
        array[i], array[min_index] = array[min_index], array[i] # 스와프

print(array)