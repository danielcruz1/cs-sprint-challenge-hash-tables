def value_in_all_dicts(value, dicts):
        for dict in dicts:
            if value not in dict:
                return False

        return True


def intersection(arrays):
   
    # Your code here
    if len(arrays) == 0:
        return []

    results = {}
    for nums in arrays:
        for num in nums:
            if num in results:
                results[num] += 1
            else:
                results[num] = 1
    return [num for (num, result) in results.items() if result == len(arrays)]

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
