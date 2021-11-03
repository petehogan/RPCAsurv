import cv2
import numpy as np
import time
from matplotlib import pyplot as plt

#
def shrink(X,tau):
    return np.sign(X) * np.maximum(np.abs(X) - tau, 0)

def svt(X,tau):
    U,S,Vt = np.linalg.svd(X,full_matrices=False)
    S = np.diag(S)
    return np.matmul(np.matmul(U,shrink(S,tau)),Vt)

def rpca(X):
    n, p = X.shape
    mu = n*p/(4*np.sum(np.abs(X.flatten())))
    lam = 1/np.sqrt(max(n,p))
    thresh = (1e-7)*np.linalg.norm(X)

    L = np.zeros_like(X)
    S = np.zeros_like(X)
    Y = np.zeros_like(X)

    count = 0
    err = np.inf
    while (err > thresh) and (count < 10):
        start = time.clock()
        L = svt(X - S + (1/mu)*Y, 1/mu)
        S = shrink(X - L + (1/mu)*Y, lam/mu)
        Y = Y + mu*(X - L - S)
        count += 1
        err = np.linalg.norm(X-L-S)
        finish = time.clock()

        print(f'iter num: {count}')
        print(f'cpu clock time: {finish - start}')
        print(f'thresh: {thresh}')
        print(f'L2 error: {err}')

    return L, S

f = 'securitylong_trim.mp4'
cap = cv2.VideoCapture(f)
num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
cnt = 0
# dim m,n | n = width * height = 360 * 640
matrix = np.zeros((1,230400))
start = time.clock()
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
finish = time.clock()
#print(finish - start)
#print(matrix.T.shape)
#print(matrix.T)
#print(matrix)
#choice = 50
L,S = rpca(matrix)
choice = 25
m,n = 360,640
fig, axs = plt.subplots(1,3)
axs[0].imshow(np.reshape(matrix[choice],(m,n)),cmap=plt.cm.bone)
axs[0].set_title("Original Image")
axs[0].axis("off")
axs[1].imshow(np.reshape(L[choice],(m,n)),cmap=plt.cm.bone)
axs[1].set_title("Low Rank Reconstruction")
axs[1].axis("off")
axs[2].imshow(np.reshape(S[choice],(m,n)),cmap=plt.cm.bone)
axs[2].set_title("Sparse 'Noise'")
axs[2].axis("off")
plt.tight_layout()
plt.savefig("robust_person{}.png".format(choice),dpi=200)
plt.show()

width = 360
height = 640
channel = 2
fps = 30
sec = 10
# comment this out to write matrices to csv, only need to do this once per set of params/ num frames
start_write = time.time()
np.savetxt('L.csv',L, delimiter= ',')
np.savetxt('S.csv',S, delimiter= ',')
np.savetxt('M.csv',matrix, delimiter= ',')
fin_write = time.time()
print(f'write time: {fin_write-start_write}')
