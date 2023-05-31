from typing import List


def contain_duplicates(nums: List[int]) -> bool:
    return len(nums) != len(set(nums))


def is_anagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


def two_sum(nums: List[int], target: int) -> List[int]:
    numbers = []
    new_nums = sorted(filter(lambda x: x <= target, nums), reverse=True)
    new_target = target
    for i in new_nums:
        if new_target == 0:
            break
        if i > new_target:
            continue
        new_target = new_target - i
        numbers.append(i)
    print(numbers)


print(two_sum([3, 1, 2, 7, 11, 15], 9))
