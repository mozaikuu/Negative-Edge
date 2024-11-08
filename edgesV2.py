import os
import cv2

# specify the folder path
folder_path = './images'
save_path_edges = './edges'
save_path_grey = './grey'
save_path_gaussianblur = './gaussianblur'

# list all image files in the folder
image_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg') or f.endswith('.png')]

#Variables
low = 50 # 100
high = 50 # 150

# loop over the image files
for image_file in image_files:
    # read the image
    image_path = os.path.join(folder_path, image_file)
    image = cv2.imread(image_path)

    # check if the image was read successfully
    if image is None:
        print(f"Error: Could not read image file {image_path}")
        continue

    # apply the Canny edge detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    GB = cv2.GaussianBlur(gray, (9, 9), 0)
    edges = cv2.Canny(GB, low, high) 
    
    # # apply the Canny edge detection V2
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # GB = cv2.GaussianBlur(gray, (5, 5), 0)
    # _, mask = cv2.threshold(GB, 255, 255, cv2.THRESH_BINARY_INV)
    # result = cv2.bitwise_and(GB, mask)
    # edges = cv2.Canny(result, low, high) 

    # do something with the edges (e.g., save them)
    # cv2.imwrite(os.path.join(save_path_grey, 'GS_' + image_file), gray)
    # cv2.imwrite(os.path.join(save_path_gaussianblur, 'GB_' + image_file), GB)
    cv2.imwrite(os.path.join(save_path_edges, 'edges_' + image_file), edges)
print('Done!')