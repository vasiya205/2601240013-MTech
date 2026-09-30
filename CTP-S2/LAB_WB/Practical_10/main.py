def calculate_area(length: float, width: float) -> float:
    """Calculate the area of a rectangle with type hints."""
    if length < 0 or width < 0:
        raise ValueError("Dimensions must be non-negative.")
    return length * width

if __name__ == "__main__":
    rect_length: float = 10.5
    rect_width: float = 5.0
    area = calculate_area(rect_length, rect_width)
    print(f"Calculated Area: {area}")
