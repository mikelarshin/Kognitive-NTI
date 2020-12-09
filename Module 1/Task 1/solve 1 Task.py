import numpy as np
from numpy.fft import rfft, rfftfreq

def main():
    signal = np.array(input().split())

    def getFureier():
        N = signal.size
        return np.uint8(signal)

    def furFur():
        N = signal.size
        return rfft(signal)

    def pwer():
        N = signal.size
        return rfftfreq(N, 1 / 256)

    aklsjddsd = np.abs(furFur())
    asdkjl = pwer()

    asklj = np.where(np.isin(aklsjddsd, sorted(aklsjddsd)[-3:]))

    asklj = asdkjl[asklj]
    asklj = asklj[(asklj != 0) & (asklj != 1)]
    asklj = int(asklj)

    print(asklj)

main()