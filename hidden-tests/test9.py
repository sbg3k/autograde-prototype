test = {
    "name": "test8",
    "points": 2,
    "hidden": True,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> 'Node' in dir() and 'append' in dir() and 'pop' in dir() 
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    arr=[84, 45, 65, 62, 34, 86, 50, 39, 17, 21, 76, 23, 54, 32, 73, 89, 79, 97, 99, 7, 29, 34, 92, 40, 23, 65, 78, 90, 36, 14, 89, 28, 16, 79, 60, 63, 4, 84, 55, 51, 13, 73, 69, 73, 26, 50, 9, 53, 24, 42, 24, 23, 38, 90, 39, 58, 67, 23, 49, 72, 17, 81, 76, 69, 67, 68, 59, 47, 16, 34, 93, 34, 63, 76, 66, 51, 55, 13, 26, 90, 5, 93, 1, 94, 6, 22, 15, 67, 15, 60, 70, 61, 97, 8, 83, 75, 77, 14, 47, 83]
                    >>> def count(head):
                    ...     ans=0
                    ...     while head:
                    ...         ans+=1
                    ...         head=head.next
                    ...     return ans
                    ...
                    >>> head=Node(arr[0])
                    >>> for i in arr[1:]:
                    ...     append(head,i)
                    ...
                    >>> count(head)
                    100
                    >>> for i in range(50):
                    ...     pop(head)
                    ...
                    >>> h=head
                    >>> while h.next:
                    ...     h=h.next
                    ...
                    >>> h.value==arr[49]
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
            ],
            "scored": False,
            "setup": "",
            "teardown": "",
            "type": "doctest"
        }
    ]
}
