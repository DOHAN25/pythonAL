# 덧셈을 하여 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
# 입력 : nums = [2, 7, 11, 15], target = 9
# 출력 : [0.1]


nums = [2, 7, 11, 15]

target = 9

def towSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

print(towSum(nums, target))
