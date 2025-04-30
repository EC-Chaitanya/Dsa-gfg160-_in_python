def insert_interval(intervals, newInterval):
    result = []
    inserted = False

    for interval in intervals:
        if interval[1] < newInterval[0]:
            # No overlap, current interval ends before new starts
            result.append(interval)
        elif interval[0] > newInterval[1]:
            # No overlap, current interval starts after new ends
            if not inserted:
                result.append(newInterval)
                inserted = True
            result.append(interval)
        else:
            # Overlap - merge intervals
            newInterval[0] = min(newInterval[0], interval[0])
            newInterval[1] = max(newInterval[1], interval[1])

    # If newInterval hasn't been inserted yet
    if not inserted:
        result.append(newInterval)

    return result
