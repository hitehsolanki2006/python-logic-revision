def binarySearch(num, list1):
    low = 0
    high = len(list1) - 1

    while low <= high:
        mid = low + (high - low) // 2

        # Check if num is present at mid
        if list1[mid] == num:
            return f"Location of {num} is at index {mid}"
        elif list1[mid] < num:
            low = mid + 1
        else:
            high = mid - 1

    return f"{num} does not exist in the list"
