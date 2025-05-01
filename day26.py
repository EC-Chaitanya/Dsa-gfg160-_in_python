def eraseOverlapIntervals(intervals):
    # Step 1: Sort intervals by their end times
    intervals.sort(key=lambda x: x[1])
    
    e = float('-inf')
    c = 0

    # Step 2: Iterate and count overlaps
    for i in intervals:
        if i[0] >= e:
            # No overlap, keep the interval
            e = i[1]
        else:
            # Overlap, need to remove this interval
            c += 1

    return c
