import os

ALLOWED_EXTENSIONS = [
    '.tif', '.tiff', '.TIF', '.TIFF', 
    '.lif', '.nd2', '.jpg', '.jpeg', 
    '.png', '.JPG', '.JPEG', '.PNG', 
    '.bmp', '.BMP', '.gif', '.GIF'
    # add other image formats here if needed
]

def list_files_recursive(directory):
    all_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in ALLOWED_EXTENSIONS):
                rel_path = os.path.relpath(os.path.join(root, file), directory)
                all_files.append(rel_path)
    return all_files

def main():
    directory = '.'  # current directory
    output_file = 'image_file_list.txt'
    
    with open(output_file, 'w') as f:
        for filepath in list_files_recursive(directory):
            f.write(f"{filepath}\n")
    print(f"Image file paths have been written to {output_file}")

if __name__ == '__main__':
    main()
