def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    sorted_a = sorted(a)
    for i in range(K):
        before_a = []
        after_a = []
        for j in range(i, N, K):
            before_a.append(a[j])
            after_a.append(sorted_a[j])
        before_a.sort()
        if before_a != after_a:
            print("No")
            break
    else:
        print("Yes")


if __name__ == "__main__":
    main()
