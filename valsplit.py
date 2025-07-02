import os
import random
import shutil

# Paths
image_dir = 'dataset/images'
label_dir = 'dataset/labels'
output_base = 'dataset'

train_img_dir = os.path.join(output_base, 'images/train')
val_img_dir = os.path.join(output_base, 'images/val')
train_lbl_dir = os.path.join(output_base, 'labels/train')
val_lbl_dir = os.path.join(output_base, 'labels/val')

for d in [train_img_dir, val_img_dir, train_lbl_dir, val_lbl_dir]:
    os.makedirs(d, exist_ok=True)

image_files = [f for f in os.listdir(image_dir) if f.lower().endswith('.jpg')]
random.shuffle(image_files)

# Split ratio
split_ratio = 0.8
split_index = int(len(image_files) * split_ratio)

train_files = image_files[:split_index]
val_files = image_files[split_index:]

# Copy function
def copy_files(file_list, img_dest, lbl_dest):
    for filename in file_list:
        src_img = os.path.join(image_dir, filename)
        src_lbl = os.path.join(label_dir, filename.replace('.jpg', '.txt'))

        dst_img = os.path.join(img_dest, filename)
        dst_lbl = os.path.join(lbl_dest, filename.replace('.jpg', '.txt'))

        if os.path.exists(src_lbl):  # Only copy if label exists
            shutil.copy2(src_img, dst_img)
            shutil.copy2(src_lbl, dst_lbl)
        else:
            print(f"⚠️ Warning: Label file not found for {filename}, skipping.")

# Perform copy
copy_files(train_files, train_img_dir, train_lbl_dir)
copy_files(val_files, val_img_dir, val_lbl_dir)

print(f"✅ Done! {len(train_files)} images in train, {len(val_files)} in val.")
