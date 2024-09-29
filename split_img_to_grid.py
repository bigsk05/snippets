import os

from PIL import Image

def split_image_to_grid(image_path, output_folder):
    img = Image.open(image_path)
    basename = os.path.basename(image_path).split(".")[0]

    width, height = img.size
    if width != height:
        raise ValueError("The picture must be square!")

    grid_size = width // 3

    for row in range(3):
        for col in range(3):
            left = col * grid_size
            top = row * grid_size
            right = left + grid_size
            bottom = top + grid_size

            grid_img = img.crop((left, top, right, bottom))
            os.makedirs(output_folder, exist_ok=True)
            grid_img.save(f"{output_folder}/{basename}_{row}_{col}.png")

    print("Success!")

def main():
    image_path = input("Please type in input file path:\n").replace("'", "")
    output_folder = input("Please type in output dir path:\n").replace("'", "")
    split_image_to_grid(image_path, output_folder)

if __name__ == "__main__":
    main()