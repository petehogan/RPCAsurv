from __future__ import division, print_function
import numpy as np
import cv2
import numpy as np
import time
from matplotlib import pyplot as plt
from PIL import Image
from pcp import pcp


## same as security except calls the data from pcp.py, this is probably redundant but serves as an example for how to call pcp.pcp()

f = 'securitylong_trim.mp4'
cap = cv2.VideoCapture(f)
num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
cnt = 0
# dim m,n | n = width * height = 360 * 640
matrix = np.zeros((1,230400))
start = time.time()
while (cap.isOpened()) and cnt <100:
    try:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cropped = gray[360:,640:]
        #cv2.imshow('frame', cropped)
        #print(cropped)
        cnt+=1
        #print(cropped.reshape(-1,360*640).shape)
        matrix = np.append(matrix,cropped.reshape(1, 360 * 640),axis = 0)
        #print(cropped.reshape(-1, 360 * 640).shape)
        #cv2.waitKey(1)
    except:
        break
finish = time.time()

L, S, (u, s, v) = pcp(matrix, maxiter=50, verbose=True, svd_method="exact")

start_write = time.time()
np.savetxt('LPCP.csv',L, delimiter= ',')
np.savetxt('SPCP.csv',S, delimiter= ',')
np.savetxt('MPCP.csv',matrix, delimiter= ',')
fin_write = time.time()
print(f'write time: {fin_write-start_write}')
