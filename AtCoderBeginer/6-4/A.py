def main(line):
    N = int(line)
    print(f"{N % 100:0=2}")


if __name__ == "__main__":
    line = str(input())
    main(line)
