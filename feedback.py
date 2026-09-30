def evaluate(target, guess):
    result = ["gray"] * len(guess)
    remaining = {}

    # First pass: mark exact matches (green)
    for i, ch in enumerate(guess):
        if ch == target[i]:
            result[i] = "green"
        else:
            target_ch = target[i]
            remaining[target_ch] = remaining.get(target_ch, 0) + 1

    # Second pass: mark misplaced letters (yellow)
    for i, ch in enumerate(guess):
        if result[i] == "green":
            continue

        if remaining.get(ch, 0) > 0:
            result[i] = "yellow"
            remaining[ch] -= 1

    return result