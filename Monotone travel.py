def is_monotone(heights):
    #     if not heights:
    #         return True
    #     for i in range(len(heights)-1):
    #         if heights[i] > heights[i + 1]:
    #             return False
    #     else:
    #         return True

    return all(heights[i] <= heights[i + 1] for i in range(len(heights) - 1))