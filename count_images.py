import os
import random
from PIL import Image
import matplotlib.pyplot as plt

# 🔹 Main dataset folder
DATASET_PATH = r"C:\Users\Shagun\OneDrive\Desktop\leaf disease project\image data"


folders = ["train", "test", "validation"]

# ----------------------------------
# Function to analyze image sizes
# ----------------------------------
def analyze_folder(folder_path):
    sizes = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png")):
                img_path = os.path.join(root, file)
                try:
                    with Image.open(img_path) as img:
                        sizes.append(img.size)
                except:
                    continue

    if sizes:
        min_size = min(sizes)
        max_size = max(sizes)
        avg_width = sum([s[0] for s in sizes]) / len(sizes)
        avg_height = sum([s[1] for s in sizes]) / len(sizes)

        print(f"\n📂 {folder_path}")
        print(f"Total Images: {len(sizes)}")
        print(f"Minimum Size: {min_size}")
        print(f"Maximum Size: {max_size}")
        print(f"Average Size: ({int(avg_width)}, {int(avg_height)})")
    else:
        print(f"No images found in {folder_path}")


# ----------------------------------
# Function to show 9 random images
# ----------------------------------
def show_random_images(folder_path):
    all_images = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png")):
                all_images.append(os.path.join(root, file))

    random_images = random.sample(all_images, min(9, len(all_images)))

    plt.figure(figsize=(10, 10))

    for i, img_path in enumerate(random_images):
        img = Image.open(img_path)
        disease = os.path.basename(os.path.dirname(img_path))

        plt.subplot(3, 3, i+1)
        plt.imshow(img)
        plt.title(disease)
        plt.axis("off")

    plt.tight_layout()
    plt.show()


# ----------------------------------
# Run Analysis
# ----------------------------------
for folder in folders:
    analyze_folder(os.path.join(DATASET_PATH, folder))

# Show 9 random images from train
show_random_images(os.path.join(DATASET_PATH, "train"))
