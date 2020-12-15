def main():
    X = [0, 3, 6]
    X = [2, 1, 10, 11, 0, 6]

    for i in range(len(X), 2020):
        x_last = X[i - 1]
        if X.count(x_last) == 1:
            x_new = 0
        else:
            j = 2
            while X[i - j] != x_last:
                j += 1
            x_new = j - 1
        X.append(x_new)
    return X[-1]


if __name__ == "__main__":
    print(main())
