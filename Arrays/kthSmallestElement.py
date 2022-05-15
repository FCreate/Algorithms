#Two sorted arrays: a, b
#Find kth smalles of a + b in O(log(min(n, m, k))
def kthSmallest(a, b, k):
    if len(a) > len(b):
        return kthSmallest(b, a, k)

    low, high = max(0, k - len(b)), min(len(a), k)
    while low <= high:
        mid = (low + high) // 2
        l1 = a[mid - 1] if mid != 0 else float("-inf")
        r1 = a[mid] if mid < len(a) else float("inf")
        l2 = b[k - mid - 1] if k - mid > 0 else float("-inf")
        r2 = b[k - mid] if k - mid < len(b) else float("inf")
        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)
        elif l1 > r2:
            high = mid - 1
        else:
            low = mid + 1

    print("Input is incorrect")
    return


a = [3, 4, 7, 10, 15]
b = [1]
k = 5
print(kthSmallest(a, b, k))