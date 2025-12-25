# Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    """
    206. Reverse Linked List
    Given the head of a singly linked list, reverse the list, and return the reversed list.
    """
    pass

def merge_two_sorted_lists(list1, list2):
    """
    21. Merge Two Sorted Lists
    You are given the heads of two sorted linked lists list1 and list2.
    """
    pass

def reorder_list(head):
    """
    143. Reorder List
    You are given the head of a singly linked-list. Reorder the list to be on the following form:
    L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
    """
    pass

def remove_nth_from_end(head, n):
    """
    19. Remove Nth Node From End of List
    Given the head of a linked list, remove the nth node from the end of the list and return its head.
    """
    pass

class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

def copy_random_list(head):
    """
    138. Copy List with Random Pointer
    A linked list of length n is given such that each node contains an additional random pointer, 
    which could point to any node in the list, or null.
    """
    pass

def add_two_numbers(l1, l2):
    """
    2. Add Two Numbers
    You are given two non-empty linked lists representing two non-negative integers.
    """
    pass

def has_cycle(head):
    """
    141. Linked List Cycle
    Given head, the head of a linked list, determine if the linked list has a cycle in it.
    """
    pass

def find_duplicate(nums):
    """
    287. Find the Duplicate Number
    Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
    """
    pass

class LRUCache:
    """
    146. LRU Cache
    Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
    """
    def __init__(self, capacity):
        pass

    def get(self, key):
        pass

    def put(self, key, value):
        pass

def merge_k_sorted_lists(lists):
    """
    23. Merge k Sorted Lists
    You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
    """
    pass

def reverse_nodes_in_k_group(head, k):
    """
    25. Reverse Nodes in k-Group
    Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
    """
    pass
