from scipy.special import comb


def main():
    K = int(input())
    for i in range(K):
        iPj = []
        for j in range(i + 1):
            iPj.append(comb(i, j, exact=True))
        print(" ".join(map(str, iPj)))


if __name__ == "__main__":
    main()
