def ReadSignal(file_name):
    indices = []
    samples = []

    with open(file_name, 'r') as f:
        signal_type = int(f.readline().strip())
        is_periodic = int(f.readline().strip())
        n1 = int(f.readline().strip())

        for _ in range(n1):
            line = f.readline().strip()

            if not line:
                continue

            values = line.split()

            index = int(values[0])
            sample = float(values[1])

            indices.append(index)
            samples.append(sample)

    return indices, samples


def AddSignals(*signals):
    if len(signals) == 0:
        return [], []

    first_indices, first_samples = signals[0]

    result_indices = first_indices.copy()
    result_samples = first_samples.copy()

    for indices, samples in signals[1:]:
        if len(indices) != len(result_indices):
            raise ValueError("Signals must have the same length")

        if indices != result_indices:
            raise ValueError("Signals must have the same indices")

        for i in range(len(result_samples)):
            result_samples[i] += samples[i]

    return result_indices, result_samples

def MultiplySignalByConstant(signal, constant):
    indices, samples = signal

    result_indices = indices.copy()
    result_samples = []

    for sample in samples:
        result_samples.append(sample * constant)

    return result_indices, result_samples

