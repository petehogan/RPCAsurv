import cv2
import numpy as np
import time


start_load = time.time()

# uncomment to read the noiseless low rank matrix L, or the original clip M, these are big so they take a while, beware

# L = np.loadtxt('L.csv',delimiter= ',')
S = np.loadtxt('S.csv', delimiter=',')
# M = np.loadtxt('M.csv',delimiter= ','

fin_load = time.time()
print(f'cpu load time: {fin_load-start_load}')
# begin writing video. convert to bone so its a 3 channel, easier for std mp4 codec. choice of 20 frames is arbitrary
m, n = 360, 640
fps = 20
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
vout = cv2.VideoWriter()
# writes to WD
success = vout.open('outputSPARSE.mp4', fourcc, fps, (n, m), True)
# I chose 100 frames in security.py just to reduce runtime, we can do the whole video later
for i in range(100):
    frame = np.reshape(S[i], (m, n)).astype(np.uint8)
    frame_bone = cv2.applyColorMap(frame, cv2.COLORMAP_BONE)
    vout.write(frame_bone)
vout.release()



