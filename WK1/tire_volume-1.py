# Ehijie Omijie
import datetime
import math

# Function to calculate tire volume
def calculate_tire_volume(width, aspect_ratio, wheel_diameter):
    radius = (wheel_diameter * 2.54) / 2  # Convert diameter from inches to cm
    volume = math.pi * width * aspect_ratio * (width + (2 * aspect_ratio * radius))
    return volume

# Function to determine the tire volume category
def categorize_tire_volume(volume):
    if volume < 2000:
        return "small"
    elif 2000 <= volume <= 4000:
        return "medium"
    else:
        return "large"

# Get current date
current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Get tire specifications from the user
width = float(input("Enter the width of the tire in cm: "))
aspect_ratio = float(input("Enter the aspect ratio of the tire: "))
wheel_diameter = float(input("Enter the diameter of the wheel in inches: "))

# Calculate the tire volume
volume = calculate_tire_volume(width, aspect_ratio, wheel_diameter)

# Categorize the tire volume
volume_category = categorize_tire_volume(volume)

# Append data to the volumes.txt file
with open("volumes.txt", "a") as file:
    file.write(f"{current_date}, {width}, {aspect_ratio}, {wheel_diameter}, {volume}, {volume_category}\n")

# Display a message based on the tire volume category
print(f"Tire volume: {volume} cubic cm")
print(f"Tire volume category: {volume_category.capitalize()}")

# Creative Feature: Display a message based on the tire volume category
if volume_category == "small":
    print("This tire has a small volume. Consider inflating it for better performance.")
elif volume_category == "medium":
    print("This tire has a medium volume. It's in good condition.")
else:
    print("This tire has a large volume. Ensure it's not overinflated for safety.")
