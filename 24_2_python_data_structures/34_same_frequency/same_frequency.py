def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    list_nums1 = list(map(int, str(num1)))
    list_nums2 = list(map(int, str(num2)))

    unique_nums1 = set(list_nums1)
    unique_nums2 = set(list_nums2)

    nums1_frequency = {}
    nums2_frequency = {}

    if(unique_nums1 != unique_nums2):
        return False
    
    for num in unique_nums1:
        if num in nums1_frequency:
            nums1_frequency[num] += 1
        else:
            nums1_frequency.update({num:1})

        if num in nums2_frequency:
            nums2_frequency[num] += 1
        else:
            nums2_frequency.update({num:1})

    return nums1_frequency == nums2_frequency