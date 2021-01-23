import numpy as np


def iterate(X):
    Y = np.zeros_like(X)
    nx, ny, nz, na = X.shape
    for i in range(1, nx - 1):
        for j in range(1, ny - 1):
            for k in range(1, nz - 1):
                for l in range(1, na - 1):
                    state = X[i, j, k, l]
                    active_neighbors = (
                        X[
                            i - 1 : i + 2, j - 1 : j + 2, k - 1 : k + 2, l - 1 : l + 2
                        ].sum()
                        - state
                    )
                    if state == 1:
                        if active_neighbors in [2, 3]:
                            Y[i, j, k, l] = 1
                        else:
                            Y[i, j, k, l] = 0
                    elif state == 0:
                        if active_neighbors == 3:
                            Y[i, j, k, l] = 1
                        else:
                            Y[i, j, k, l] = 0

    return Y


def main(N=7):
    input = []
    with open("data/data_17.txt", "r") as f:
        for line in f:
            input.append([1 if x == "#" else 0 for x in line[:-1]])

    # X = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]]) # example input
    X = np.array(input)
    X = np.expand_dims(X, 0)
    X = np.expand_dims(X, 0)
    X = np.pad(X, N)

    for i in range(6):
        X = iterate(X)

    return X.sum()


if __name__ == "__main__":
    print(main())
