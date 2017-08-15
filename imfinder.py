import numpy as np
import cv2
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')


# The function below takes an input image, the logo, and returns that logo in the image using a convolutional filter
# 
#  - turn this into a neural network that can find logos, period

# In[141]:

def logo_finder(scene, logo):
    
    # load image and logo
    full_image = cv2.imread(scene)
    gray_full_image = cv2.cvtColor(full_image, cv2.COLOR_BGR2GRAY)
    logo_0 = cv2.imread(logo)
    logo = cv2.cvtColor(logo_0, cv2.COLOR_BGR2GRAY)
    (logo_height, logo_width) = logo.shape[:2]

    # show image and logo
    plt.figure()
    plt.axis("off")
    plt.imshow(cv2.cvtColor(full_image, cv2.COLOR_BGR2RGB))
    
    plt.figure()
    plt.axis("off")
    plt.imshow(cv2.cvtColor(logo_0, cv2.COLOR_BGR2RGB))

    # find logo position in image
    result = cv2.matchTemplate(gray_full_image,logo,cv2.TM_CCOEFF_NORMED)
    (_, _, minLoc, maxLoc) = cv2.minMaxLoc(result)

    # grab the bounding box of the logo and crop from the image
    top_left = maxLoc
    bottom_right = (top_left[0] + logo_width, top_left[1] + logo_height)
    crop = full_image[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]

    plt.figure()
    plt.axis("off")
    plt.imshow(cv2.cvtColor(crop, cv2.COLOR_BGR2RGB))
    
    return crop


# Apple examples (all using the same logo image)

# In[142]:

apple = logo_finder("apple1_full.jpg", "apple1.jpg")


# In[143]:

apple = logo_finder("apple5_full.jpg", "apple1.jpg")


# In[144]:

apple = logo_finder("apple10_full.jpg", "apple1.jpg")


# Adidas Examples (all using the same logo image)

# In[145]:

adidas = logo_finder("adidas1_full.jpg", "adidas1.jpg")


# In[146]:

adidas = logo_finder("adidas3_full.jpg", "adidas1.jpg")


# In[147]:

adidas = logo_finder("adidas10_full.jpg", "adidas1.jpg")


# In[148]:

dunkindonuts1 = logo_finder("dunk1_full3.jpg", "dunk1.jpg")


# In[152]:

starbucks = logo_finder("starbucks1_full4.jpg", "starbucks1.jpg")


# In[153]:

starbucks = logo_finder("starbucks1_full5.jpg", "starbucks1.jpg")


# In[155]:

starbucks = logo_finder("starbucks1_full6.jpg", "starbucks1.jpg")