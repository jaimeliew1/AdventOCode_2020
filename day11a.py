import numpy as np
import matplotlib.pyplot as plt
from tqdm import trange


def iterate(a):
    N = a.shape[0] - 2
    M = a.shape[1] - 2
    a_new = np.zeros_like(a)
    a_new[:, :] = np.nan
    for i in range(1, N + 1):
        for j in range(1, M + 1):

            if np.isnan(a[i, j]):
                a_new[i, j] = np.nan

            elif a[i, j] == 0:
                occupied = np.nansum(a[i - 1 : i + 2, j - 1 : j + 2]) - a[i, j]
                if occupied == 0:
                    a_new[i, j] = 1
                else:
                    a_new[i, j] = a[i, j]

            elif a[i, j] == 1:
                occupied = np.nansum(a[i - 1 : i + 2, j - 1 : j + 2]) - a[i, j]
                if occupied >= 4:
                    a_new[i, j] = 0
                else:
                    a_new[i, j] = a[i, j]

    return a_new


def main():
    with open("data/data_11.txt", "r") as f:
        raw = f.read()

    raw = raw.split("\n")[:-1]
    N = len(raw)
    M = len(raw[0])
    in_array = np.array([list(x) for x in raw])

    a = np.zeros([N + 2, M + 2])
    a[:, :] = np.nan
    a[1:-1, 1:-1][in_array == "L"] = 0
    a[1:-1, 1:-1][in_array == "."] = np.nan

    prev_sum = -1
    for i in trange(200):
        a = iterate(a)
        if prev_sum == np.nansum(a):
            return int(prev_sum)
        prev_sum = np.nansum(a)


#
# plt.figure()
# plt.imshow(anew, vmin=0, vmax=1)
# plt.show()


if __name__ == "__main__":
    print(main())
