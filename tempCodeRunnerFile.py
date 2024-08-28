    if (x1 >= x2 and x1 < x2 + sizeX) and (y1 >= y2 and y1 < y2 + sizeY):
            return True
        # Check if snake's head is outside the playable area
        if x1 < 0 or x1 >= 1400 or y1 < 0 or y1 >= 750:
            return True
        return False
