"""
Denoise Problem
(Due date: Nov. 25, 11:59 P.M., 2019)
The goal of this task is to denoise image using median filter.

Do NOT modify the code provided to you.
Do NOT import ANY library or API besides what has been listed.
Hint: 
Please complete all the functions that are labeled with '#to do'. 
You are suggested to use utils.zero_pad.
"""
#syed rehman
#syedrehm@buffalo.edu


import utils
import numpy as np
import json


def median_filter(img):
    
    img2 = img
    img = utils.zero_pad(img, 1, 1)
    for x in range(1, len(img)-1):
        for y in range(1, len(img[0])-1):   # getting median filter. 
            arr = [img[x-1][y-1], img[x][y-1], img[x+1][y-1],  # using 3x3 median filter here. 
                   img[x-1][y],   img[x][y],   img[x+1][y],
                   img[x-1][y+1], img[x][y+1], img[x+1][y+1]]
            arr.sort()
            #img[x][y] = arr[4]  #sort and getting median value.
            img2[x-1][y-1] = arr[4]

    # for x in range(len(img2)):  
    #     for y in range(len(img2[0])):
    #         img2[x][y] = img[(x+1)][(y+1)]
    img2 = img2.astype('uint8')
    return img2

def mse(img1, img2):
    #good, filtered
    img1_ = img1.astype('float64')
    img2_ = img2.astype('float64')
    summation = 0.0
    for w in range(0, len(img1)):
        for h in range(len(img1[0])):
            val = img2_[w][h] - img1_[w][h]
            summation += val * val
    
    result = summation / (len(img1) * len(img2[0]))
    return result
    

if __name__ == "__main__":
    img = utils.read_image('noise.png')
    #gt = utils.read_image('denoise.png')

    result = median_filter(img)
    #error = mse(gt, result)

    #with open('results/task2.json', "w") as file:
    #    json.dump(error, file)
    utils.write_image(result,'results/result.jpg')


"""
previously defined median..
def getMedian2(x, y, img):
    if x == 0 :
        return getMedian2(1,y, img)
    if y == 0:
        return getMedian2(x,1, img)
    if x == len(img):
        return getMedian2(x-1, y, img)
    if y == len(img[0]):
        return getMedian2(x, y-1, img)
    #return getMedian(x, y , img)
    arr = [img[x-1][y-1], img[x][y-1], img[x+1][y-1], 
           img[x-1][y]  , img[x][y]  , img[x+1][y]  ,
           img[x-1][y+1], img[x][y+1], img[x+1][y+1]]
    arr.sort()
    # median = 
    return arr[4]

def getMedian(x,y, img):
    arr = [img[(x-1)][(y-1)], img[x][(y-1)], img[(x+1)][(y-1)], 
           img[(x-1)][y]  , img[x][y]  , img[(x+1)][y]  ,
           img[(x-1)][(y+1)], img[x][(y+1)], img[(x+1)][(y+1)]]
    
    arr.sort()
    # median = np.median(arr)
    return arr[4]

"""