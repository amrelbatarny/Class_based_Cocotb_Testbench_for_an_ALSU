def max(signal):
    signal_width = len(signal)  # Get the bit width of the signal
    max_value = (1 << signal_width) - 1  # Calculate the maximum value: 2^width - 1
    return max_value