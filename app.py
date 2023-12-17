import os
from PIL import Image

def list_images_in_current_directory():
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']  # Add more extensions if needed

    image_list = []

    try:
        current_directory = os.getcwd()  # Get the current working directory
        for filename in os.listdir(current_directory):
            file_extension = os.path.splitext(filename)[1].lower()
            if file_extension in image_extensions:
                image_path = os.path.join(current_directory, filename)
                image_list.append(image_path)

        return image_list

    except Exception as e:
        print(f"Error: {e}")
        return []

def convert_images_to_cmyk(image_paths, output_folder):
    try:
        for image_path in image_paths:
            get_image_info(image_path)
            # Open the RGB image
            rgb_image = Image.open(image_path)

            # Convert to CMYK
            cmyk_image = rgb_image.convert('CMYK')

            # Get the original image filename (without extension)
            filename = os.path.splitext(os.path.basename(image_path))[0]

            # Construct the output path for the CMYK image
            output_image_path = os.path.join(output_folder, f"{filename}_cmyk.jpg")

            # Save the CMYK image
            cmyk_image.save(output_image_path)
            get_image_info(output_image_path)

            print(f"Image converted to CMYK and saved as {output_image_path}")
            print("=================")
    except Exception as e:
        print(f"Error: {e}")



def get_image_info(image_path):
    try:
        # Open the image
        img = Image.open(image_path)

        # Get image format (JPEG, PNG, BMP, etc.)
        image_format = img.format

        # Get image size (width x height)
        width, height = img.size

        # Get color mode (RGB, CMYK, grayscale, etc.)
        color_mode = img.mode

        # Print the image information
        print("Image Information:")
        print(f"Format: {image_format}")
        print(f"Size: {width} x {height}")
        print(f"Color Mode: {color_mode}")
        print("-------------")

    except Exception as e:
        print(f"Error: {e}")
        
        
if __name__ == "__main__":
    image_paths = list_images_in_current_directory()

    if image_paths:
        output_folder = "./output"  # Replace with the path to the output folder
        os.makedirs(output_folder, exist_ok=True)  # Create the output folder if it doesn't exist

        convert_images_to_cmyk(image_paths, output_folder)
    else:
        print("No images found in the current directory.")
        
