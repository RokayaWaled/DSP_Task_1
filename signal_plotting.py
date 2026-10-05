import matplotlib.pyplot as plt

def PlotSignal(indices, samples, title="Signal"):
    plt.figure()

    # Continuous representation
    plt.subplot(2, 1, 1)
    plt.plot(indices, samples)
    plt.title(title + " - Continuous")
    plt.xlabel("Index")
    plt.ylabel("Amplitude")
    plt.grid(True)

    # Discrete representation
    plt.subplot(2, 1, 2)
    plt.stem(indices, samples)
    plt.title(title + " - Discrete")
    plt.xlabel("Index")
    plt.ylabel("Amplitude")
    plt.grid(True)

    plt.tight_layout()
    plt.show()


def PlotTwoSignals(signal1, signal2, title1="Signal 1", title2="Signal 2"):
    indices1, samples1 = signal1
    indices2, samples2 = signal2

    plt.figure()

    plt.plot(indices1, samples1, label=title1)
    plt.plot(indices2, samples2, label=title2)

    plt.xlabel("Index")
    plt.ylabel("Amplitude")
    plt.title("Two Signals")
    plt.legend()
    plt.grid(True)

    plt.show()