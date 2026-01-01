def control_break(records, key_fn, agg_fn, initial_value):
    current_key = None
    accumulator = initial_value

    for record in records:
        key = key_fn(record)

        if current_key is None:
            current_key = key

        if key != current_key:
            yield current_key, accumulator
            current_key = key
            accumulator = initial_value

        accumulator = agg_fn(accumulator, record)

    if current_key is not None:
        yield current_key, accumulator
