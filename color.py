import matplotlib.pyplot as plt
import matplotlib.patches as patches

def rgb_to_hsv(r, g, b):
    r_normalized = r / 255.0
    g_normalized = g / 255.0
    b_normalized = b / 255.0

    max_val = max(r_normalized, g_normalized, b_normalized)
    min_val = min(r_normalized, g_normalized, b_normalized)

    v = max_val

    if max_val == min_val:
        s = 0
    else:
        s = (max_val - min_val) / max_val

    if max_val == r_normalized:
        h = (g_normalized - b_normalized) / (max_val - min_val)
    elif max_val == g_normalized:
        h = 2 + (b_normalized - r_normalized) / (max_val - min_val)
    else:
        h = 4 + (r_normalized - g_normalized) / (max_val - min_val)

    h = (h * 60) % 360  # Convert hue to degrees

    return h, s, v

# Get RGB input from the user
try:
    r = int(input("Enter the red component (0-255): "))
    g = int(input("Enter the green component (0-255): "))
    b = int(input("Enter the blue component (0-255): "))

    if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
        h, s, v = rgb_to_hsv(r, g, b)
        
        # Display the color using a color patch
        color_rgb = (r / 255, g / 255, b / 255)
        color_hsv = (h, s, v)

        fig, ax = plt.subplots()
        rect = patches.Rectangle((0, 0), 1, 1, linewidth=1, edgecolor='none', facecolor=color_rgb)
        ax.add_patch(rect)
        ax.axis('off')

        # Add the message below the color patch with larger and bold font
        plt.text(0.5, -0.1, "Thank you, If you have any questions,please let me know.",
                 horizontalalignment='center', verticalalignment='center', transform=ax.transAxes,
                 fontsize=12, fontweight='bold', color='black')
        
        plt.title(f'RGB Color: ({r}, {g}, {b})\nHSV Color: ({h:.2f}, {s:.2f}, {v:.2f})')
        
        plt.show()
    else:
        print("RGB values should be in the range 0-255.")
except ValueError:
    print("Invalid input. Please enter valid integers for RGB components.")
