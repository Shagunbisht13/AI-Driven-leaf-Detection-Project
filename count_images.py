import os

dataset_path = "Leaf Disease Dataset/Train"

total = 0

for folder in os.listdir(dataset_path):
    folder_path = os.path.join(dataset_path, folder)
    if os.path.isdir(folder_path):
        images = [
            f for f in os.listdir(folder_path)
            if f.lower().endswith(('.png', '.jpg', '.jpeg'))
        ]
        print(f"{folder}: {len(images)} images")
        total += len(images)

print("\nTotal images:", total)
