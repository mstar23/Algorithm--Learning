def solution(n, m, section):
    # Create a list to mark the sections that need to be repainted
    needs_paint = [False] * (n + 1)
    for s in section:
        needs_paint[s] = True
    
    # The count of painting actions needed
    paint_count = 0
    
    # Iterate over each segment to determine if it needs painting
    i = 1
    while i <= n:
        if needs_paint[i]:
            # Find the rightmost start point where the roller can start to cover this segment
            start = max(i, (i + m - 1) - (m - 1))
            
            # Update the start position based on the furthest possible to minimize roller uses
            start = min(start, n - m + 1) if i + m - 1 > n else start
            
            # Mark all covered segments as painted
            for j in range(start, start + m):
                if j > n:
                    break
                needs_paint[j] = False
            
            # Increment the paint counter
            paint_count += 1
        
        # Move to the next segment
        i += 1
    
    return paint_count