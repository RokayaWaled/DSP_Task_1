import tkinter as tk
from tkinter import filedialog

from signal_operations import ReadSignal, AddSignals, MultiplySignalByConstant
from signal_plotting import PlotSignal, PlotTwoSignals

# Create the main window
window = tk.Tk()
window.title("Signal Processing Framework")
window.geometry("800x500")


# Read Signal
def read_signal():
    file_name = filedialog.askopenfilename(
        title="Select Signal File",
        filetypes=[("Text Files", "*.txt")]
    )

    if file_name:
        signal = ReadSignal(file_name)

        print("Signal loaded successfully")
        print("First 5 samples:", signal[1][:5])

        PlotSignal(
            signal[0],
            signal[1],
            "Signal"
        )


# Addition
def addition():
    signals = []

    while True:
        file_name = filedialog.askopenfilename(
            title="Select Signal to Add (Cancel when finished)",
            filetypes=[("Text Files", "*.txt")]
        )

        if not file_name:
            break

        signal = ReadSignal(file_name)
        signals.append(signal)

    if len(signals) < 2:
        print("Please select at least two signals.")
        return

    result = AddSignals(*signals)

    print("Addition completed successfully")
    print("First 5 samples:", result[1][:5])

    PlotSignal(
        result[0],
        result[1],
        "Addition Result"
    )

def multiplication():
    # Select a signal
    file_name = filedialog.askopenfilename(
        title="Select Signal",
        filetypes=[("Text Files", "*.txt")]
    )

    if not file_name:
        return

    signal = ReadSignal(file_name)

    # Ask for the constant
    constant_window = tk.Toplevel(window)
    constant_window.title("Multiplication")
    constant_window.geometry("300x150")

    label = tk.Label(
        constant_window,
        text="Enter the constant:"
    )
    label.pack(pady=10)

    constant_entry = tk.Entry(constant_window)
    constant_entry.pack()

    def apply_multiplication():
        try:
            constant = float(constant_entry.get())

            result = MultiplySignalByConstant(
                signal,
                constant
            )

            print("Multiplication completed successfully")
            print("First 5 samples:", result[1][:5])

            PlotSignal(
                result[0],
                result[1],
                "Multiplication Result"
            )

            constant_window.destroy()

        except ValueError:
            print("Please enter a valid number.")

    button = tk.Button(
        constant_window,
        text="Apply",
        command=apply_multiplication
    )
    button.pack(pady=10)


def display_two_signals():
    # Select first signal
    file_name1 = filedialog.askopenfilename(
        title="Select First Signal",
        filetypes=[("Text Files", "*.txt")]
    )

    if not file_name1:
        return

    signal1 = ReadSignal(file_name1)

    # Select second signal
    file_name2 = filedialog.askopenfilename(
        title="Select Second Signal",
        filetypes=[("Text Files", "*.txt")]
    )

    if not file_name2:
        return

    signal2 = ReadSignal(file_name2)

    PlotTwoSignals(
        signal1,
        signal2,
        "Signal 1",
        "Signal 2"
    )


# Create the main menu
menu_bar = tk.Menu(window)

# Signal Processing menu
signal_menu = tk.Menu(menu_bar, tearoff=0)

signal_menu.add_command(
    label="Read Signal",
    command=read_signal
)
signal_menu.add_command(
    label="Display Two Signals",
    command=display_two_signals
)

# Arithmetic Operations submenu
arithmetic_menu = tk.Menu(signal_menu, tearoff=0)

arithmetic_menu.add_command(
    label="Addition",
    command=addition
)

arithmetic_menu.add_command(
    label="Multiplication",
    command=multiplication
)

signal_menu.add_cascade(
    label="Arithmetic Operations",
    menu=arithmetic_menu
)

signal_menu.add_separator()

signal_menu.add_command(
    label="Exit",
    command=window.destroy
)

menu_bar.add_cascade(
    label="Signal Processing",
    menu=signal_menu
)


# Display the menu
window.config(menu=menu_bar)


# Start the GUI
window.mainloop()