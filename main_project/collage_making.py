import matplotlib.pyplot as plt
from PIL import Image # Used to open image files
import os

image_files = [
    'Hist_1_AQI.png',  
    'Hist_2_NO2.png',  
    'Hist_3_CO.png',  
    'Hist_4_SO2.png', 
    'Hist_5_O3.png', 
    'Hist_6_Toluene.png',  
    'Hist_7_PM10.png',  
    'Hist_8_NH3.png'   
]

# Create a figure and a grid of subplots for the collage
# We'll use a 3x3 grid, which gives us 9 slots. With 8 images, one will be empty.
fig, axes = plt.subplots(3, 3, figsize=(15, 15))
axes = axes.flatten() # Flatten the 2D array of axes for easy iteration

# Loop through the image files and place them on the subplots
for i, img_path in enumerate(image_files):
    if i < len(axes): # Ensure we don't try to plot more images than we have subplots
        try:
            # Open the image using PIL (Image.open)
            img = Image.open(img_path)
            axes[i].imshow(img)
            axes[i].axis('off') # Turn off axis labels and ticks for a cleaner look

            # Optional: Add a title for each subplot, derived from the filename
            # This makes it clear which pollutant each histogram represents
            title_text = os.path.basename(img_path).replace('.png', '').replace('image', '').upper()
            axes[i].set_title(title_text if title_text else f'Image {i+1}', fontsize=12)

        except FileNotFoundError:
            print(f"Warning: The image file '{img_path}' was not found. Skipping this subplot.")
            axes[i].axis('off') # Ensure the empty subplot doesn't show axes
        except Exception as e:
            print(f"Error processing image '{img_path}': {e}")
            axes[i].axis('off') # Ensure the empty subplot doesn't show axes
    else:
        break # Stop if we've filled all our desired subplot slots

# Turn off any remaining empty subplots (e.g., the 9th slot if you have 8 images)
for j in range(len(image_files), len(axes)):
    axes[j].axis('off')

# Add a main title for the entire collage
plt.suptitle('Histograms of Pollutant Distributions', y=1.02, fontsize=20) # y adjusts title position

# Adjust layout to prevent titles/labels from overlapping
plt.tight_layout(rect=[0, 0.03, 1, 0.98]) # Adjust rect if main title is cut off

# Save the collage to a file
output_filename = 'histograms_collage.png'
plt.savefig(output_filename, dpi=300, bbox_inches='tight') # Save with high resolution
print(f"\nCollage saved successfully as '{output_filename}'")
plt.close(fig) # Close the figure to free up memory