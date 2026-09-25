import math

def calculate_polygon_perimeter():
    print("Calculate the perimeter of a polygon.")
    
    try:
        first_x_str = input("Enter the first x-coordinate: ").strip()
        if not first_x_str:
            print("No polygon points provided.")
            return
        first_x = float(first_x_str)
        first_y = float(input("Enter the first y-coordinate: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    perimeter = 0.0
    prev_x = first_x
    prev_y = first_y

    while True:
        next_x_str = input("Enter the next x-coordinate (blank to quit): ").strip()
        if next_x_str == "":
            break
            
        try:
            next_x = float(next_x_str)
            next_y = float(input("Enter the next y-coordinate: "))
            distance = math.sqrt((next_x - prev_x)**2 + (next_y - prev_y)**2)
            perimeter += distance
            prev_x = next_x
            prev_y = next_y
            
        except ValueError:
            print("Invalid input. Please enter valid numeric coordinates.")
    final_closing_distance = math.sqrt((first_x - prev_x)**2 + (first_y - prev_y)**2)
    perimeter += final_closing_distance

    print(f"The perimeter of that polygon is {perimeter}")

if __name__ == "__main__":
    calculate_polygon_perimeter()
