# Arrays & Hashing

def contains_duplicate(nums):
    """
    217. Contains Duplicate
    Given an integer array nums, return true if any value appears at least twice in the array, 
    and return false if every element is distinct.
    """
    return len(set(nums)) != len(nums)

def valid_anagram(s, t):
    """
    242. Valid Anagram
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.
    """
    # if len(s) != len(t):
    #     return False
    # return sorted(s) == sorted(t)

    if len(s) != len(t):
        return False
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for c in t:
        count[c] = count.get(c, 0) - 1
        if count[c] < 0:
            return False
    return all(c==0 for c in count.values())

def two_sum(nums, target):
    """
    1. Two Sum
    Given an array of integers nums and an integer target, return indices of the two numbers 
    such that they add up to target.
    """
    mp = {}
    for i, num in enumerate(nums):
        if target-num in mp:
            return [mp[target-num], i]
        mp[num] = i
    return [-1, -1]

def group_anagrams(strs):
    """
    49. Group Anagrams
    Given an array of strings strs, group the anagrams together.
    """
    mp = {}

    for str in strs:
        s = tuple(sorted(str))
        if s in mp:
            mp[s].append(str)
        else:
            mp[s] = [str]
    
    return [v for v in mp.values()]

def top_k_frequent(nums, k):
    """
    347. Top K Frequent Elements
    Given an integer array nums and an integer k, return the k most frequent elements.
    """
    pass

def product_except_self(nums):
    """
    238. Product of Array Except Self
    Given an integer array nums, return an array answer such that answer[i] is equal to 
    the product of all the elements of nums except nums[i].
    """
    pass

def is_valid_sudoku(board):
    """
    36. Valid Sudoku
    Determine if a 9 x 9 Sudoku board is valid.
    """
    pass

def encode_decode():
    """
    271. Encode and Decode Strings
    Design an algorithm to encode a list of strings to a string and decode it back.
    """
    def encode(strs):
        pass
    
    def decode(s):
        pass
    
    return encode, decode

def longest_consecutive(nums):
    """
    128. Longest Consecutive Sequence
    Given an unsorted array of integers nums, return the length of the longest 
    consecutive elements sequence.
    """
    pass
