'''Given an array A[] of size n. The task is to find the largest element in it'''
def largest( arr, n):
    maxx=arr[0]
    for i in arr:
        if i>maxx:
            maxx=i
    return maxx
def main():
    T = int(input())
    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        print(largest(a, n))
        T -= 1
if __name__ == "__main__":
    main()