from tqdm import trange


def main():
    # X = [0, 3, 6]
    X = [2, 1, 10, 11, 0, 6]
    N = len(X)
    x_last = X[-1]
    X = {val: [pos, None] for pos, val in enumerate(X)}
    print(X)

    for i in trange(N, 30000000):

        if X[x_last][1] == None:
            x_last = 0
            X[x_last] = [i, X[x_last][0]]

        else:
            x_new = X[x_last][0] - X[x_last][1]
            if x_new not in X.keys():
                X[x_new] = [i, None]
            else:
                X[x_new] = [i, X[x_new][0]]
            x_last = x_new

    return x_last


if __name__ == "__main__":
    print(main())
