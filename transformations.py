import numpy as np
import matplotlib.pyplot as plt
import cv2

def translate(img, x_shift, y_shift):
    rows, cols, dim = img.shape
    # transformation matrix for translation
    M = np.float32([[1, 0, x_shift],
                    [0, 1, y_shift],
                    [0, 0, 1]])
    # apply a perspective transformation to the image
    return cv2.warpPerspective(img, M, (cols, rows))
    

def scale(img, x_scale, y_scale):
    # get the image shape
    rows, cols, dim = img.shape
    #transformation matrix for Scaling
    M = np.float32([[x_scale, 0  , 0],
                    [0,   y_scale, 0],
                    [0,   0,   1]])
    #apply a perspective transformation to the image
    return cv2.warpPerspective(img,M,(cols*2,rows*2))
    

def shear(img, x_shear, y_shear):
    # get the image shape
    rows, cols, dim = img.shape
    # transformation matrix for Shearing
    # shearing applied to x-axis
    M = np.float32([[1, x_shear, 0],
                    [y_shear, 1  , 0],
                    [0, 0  , 1]])
    # apply a perspective transformation to the image                
    return cv2.warpPerspective(img,M,(int(cols*1.5),int(rows*1.5)))
    

def reflect(img, axis):
    # get the image shape
    rows, cols, dim = img.shape
    # transformation matrix for x-axis reflection 
    if(axis == "x"):
        M = np.float32([[1,  0, 0   ],
                        [0, -1, rows],
                        [0,  0, 1   ]])
    # transformation matrix for y-axis reflection
    else:
        M = np.float32([[-1, 0, cols],
                         [ 0, 1, 0   ],
                         [ 0, 0, 1   ]])
    # apply a perspective transformation to the image
    return cv2.warpPerspective(img,M,(int(cols),int(rows))) 

def rotate(img, angle):
    # get the image shape
    rows, cols, dim = img.shape
    #angle from degree to radian
    angle = np.radians(angle)
    #transformation matrix for Rotation
    M = np.float32([[np.cos(angle), -(np.sin(angle)), 0],
                    [np.sin(angle), np.cos(angle), 0],
                    [0, 0, 1]])
    # apply a perspective transformation to the image
    return cv2.warpPerspective(img, M, (int(cols),int(rows)))

#fname = input("Enter the file name: ")
#suffix = input("Enter the file type: ")
cmd = input("Enter the desired transformation: ")

# read the input image
img = cv2.imread("dunk.jpeg")
# convert from BGR to RGB so we can plot using matplotlib
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
new_img = None

if(cmd == "translate"):
    x_shift = float(input("Enter x_shift: "))
    y_shift = float(input("Enter y_shift: "))
    new_img = translate(img, x_shift, y_shift)
elif(cmd == "scale"):
    x_scale = float(input("Enter x_scale: "))
    y_scale = float(input("Enter y_scale: "))
    new_img = scale(img, x_scale, y_scale)
elif(cmd == "shear"):
    x_shear = float(input("Enter x_shear: "))
    y_shear = float(input("Enter y_shear: "))
    new_img = shear(img, x_shear, y_shear)
elif(cmd == "reflect"):
    axis = input("x-axis or y-axis? ")
    new_img = reflect(img, axis)
    cmd = axis + cmd
elif(cmd == "rotate"):
    angle = float(input("Enter desired angle of rotation: "))
    new_img = rotate(img, angle)
    cmd = cmd + str(angle)
else:
    print("Error, invalid translation!")
    exit(1)

# disable x & y axis
plt.axis('off')
# show the resulting image
plt.imshow(new_img)
plt.show()
# save the resulting image to disk
plt.imsave("dunk_" + cmd + ".jpeg", new_img)