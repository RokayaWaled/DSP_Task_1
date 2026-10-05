import os

from signal_operations import (
    ReadSignal,
    AddSignals,
    MultiplySignalByConstant
)


# =========================
# Project folders
# =========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INPUT_FOLDER = os.path.join(BASE_DIR, "input_signals")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "output_signals")


# =========================
# Read expected signal
# =========================

def ReadSignalFile(file_name):

    expected_indices = []
    expected_samples = []

    with open(file_name, "r") as f:

        # Skip first 3 header lines
        f.readline()
        f.readline()
        f.readline()

        line = f.readline()

        while line:

            parts = line.strip().split()

            if len(parts) == 2:

                index = int(parts[0])
                sample = float(parts[1])

                expected_indices.append(index)
                expected_samples.append(sample)

            line = f.readline()

    return expected_indices, expected_samples


# =========================
# Compare signals
# =========================

def SignalSamplesAreEqual(
        task_name,
        output_file,
        your_indices,
        your_samples):

    try:

        expected_indices, expected_samples = ReadSignalFile(
            output_file
        )

        # Check length
        if (
            len(expected_indices) != len(your_indices)
            or
            len(expected_samples) != len(your_samples)
        ):

            print(
                task_name +
                " Test case failed: different length"
            )

            return False

        # Check indices
        for i in range(len(your_indices)):

            if your_indices[i] != expected_indices[i]:

                print(
                    task_name +
                    " Test case failed: different indices"
                )

                return False

        # Check samples
        for i in range(len(your_samples)):

            if abs(
                your_samples[i] - expected_samples[i]
            ) >= 0.01:

                print(
                    task_name +
                    " Test case failed: different values"
                )

                print(
                    "Sample:",
                    i
                )

                print(
                    "Your value:",
                    your_samples[i]
                )

                print(
                    "Expected value:",
                    expected_samples[i]
                )

                return False

        print(
            task_name +
            " Test case passed successfully"
        )

        return True

    except Exception as error:

        print(
            task_name +
            " Test Error:"
        )

        print(error)

        return False


# =========================
# Find output files
# =========================

def find_output_file(keyword):

    for file_name in os.listdir(OUTPUT_FOLDER):

        if keyword.lower() in file_name.lower():

            return os.path.join(
                OUTPUT_FOLDER,
                file_name
            )

    return None


# =========================
# Read input signals
# =========================

signal1 = ReadSignal(
    os.path.join(
        INPUT_FOLDER,
        "Signal1.txt"
    )
)

signal2 = ReadSignal(
    os.path.join(
        INPUT_FOLDER,
        "Signal2.txt"
    )
)

signal3 = ReadSignal(
    os.path.join(
        INPUT_FOLDER,
        "Signal3.txt"
    )
)


# =========================
# TEST 1
# Signal1 + Signal2
# =========================

result = AddSignals(
    signal1,
    signal2
)

output_file = find_output_file(
    "Signal1+signal2"
)

if output_file:

    SignalSamplesAreEqual(
        "Signal1 + Signal2",
        output_file,
        result[0],
        result[1]
    )

else:

    print(
        "Signal1 + Signal2: output file not found"
    )


# =========================
# TEST 2
# Signal1 + Signal3
# =========================

result = AddSignals(
    signal1,
    signal3
)

output_file = find_output_file(
    "Signal1+signal3"
)

if output_file:

    SignalSamplesAreEqual(
        "Signal1 + Signal3",
        output_file,
        result[0],
        result[1]
    )

else:

    print(
        "Signal1 + Signal3: output file not found"
    )


# =========================
# TEST 3
# Signal1 × 5
# =========================

result = MultiplySignalByConstant(
    signal1,
    5
)

output_file = find_output_file(
    "Signal1"
)

# Find the multiplication file specifically
if output_file:

    for file_name in os.listdir(OUTPUT_FOLDER):

        if (
            "multiplybyconstant" in file_name.lower()
            and
            "signal1" in file_name.lower()
            and
            "5" in file_name
        ):

            output_file = os.path.join(
                OUTPUT_FOLDER,
                file_name
            )

            break

if output_file:

    SignalSamplesAreEqual(
        "Signal1 × 5",
        output_file,
        result[0],
        result[1]
    )

else:

    print(
        "Signal1 × 5: output file not found"
    )

# =========================
# TEST 4
# Signal2 × 10
# =========================

result = MultiplySignalByConstant(
    signal2,
    10
)

output_file = None

for file_name in os.listdir(OUTPUT_FOLDER):

    lower_name = file_name.lower()

    if (
        "constant" in lower_name
        and
        "signal2" in lower_name
        and
        "10" in lower_name
    ):

        output_file = os.path.join(
            OUTPUT_FOLDER,
            file_name
        )

        break

if output_file:

    SignalSamplesAreEqual(
        "Signal2 × 10",
        output_file,
        result[0],
        result[1]
    )

else:

    print("Signal2 × 10: output file not found")