def non_empty_truths(val: list) -> list:
    if not isinstance(val, list):
        return val

    return [x for x in map(non_empty_truths, val) if x]
