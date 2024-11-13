class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None


my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)

print('Bolts:', my_hash_table.get_item('bolts'))
print('Washers:', my_hash_table.get_item('washers'))
print('Lumber:', my_hash_table.get_item('lumber'))


# find duplicates in array
def find_duplicates(nums):
    num_counts = {}

    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1

    duplicates = []

    for num, count in num_counts.items():
        if count > 1:
            duplicates.append(num)
    return duplicates


def group_anagrams(strings):
    anagram_groups = {}

    for string in strings:
        canonical = ''.join(sorted(string))
        if canonical in anagram_groups:
            anagram_groups[canonical].append(string)
        else:
            anagram_groups[canonical] = [string]
    return list(anagram_groups.values())


def two_sum(nums, target):
    hashmap = {}

    for index, num in enumerate(nums):
        x = target - num
        if x in hashmap:
            return [hashmap[x], index]
        hashmap[num] = index
    return []


def subarray_sum(nums, target):
    current_sum = 0
    sum_dict = {}

    for i, num in enumerate(nums):
        current_sum += num

        if current_sum == target:
            return [0, i]
        elif current_sum - target in sum_dict:
            return [sum_dict[current_sum - target]+1, i]
        sum_dict[current_sum] = i
    return []


print(two_sum([5, 1, 7, 2, 9, 3], 10))
print(two_sum([4, 2, 11, 7, 6, 3], 9))
print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))
print(two_sum([1, 3, 5, 7, 9], 10))
print(two_sum([1, 2, 3, 4, 5], 10))
print(two_sum([1, 2, 3, 4, 5], 7))
print(two_sum([1, 2, 3, 4, 5], 3))
print(two_sum([], 0))

print(find_duplicates([1, 3, 5, 2, 6, 9, 1, 2, 3, 6, 7, 9, 3]))

print(group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]))

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
