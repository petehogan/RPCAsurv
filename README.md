# RPCAsurv
Robust PCA for use in surveillance footage
### Dependencies:
  - Python version >3.X
  - OpenCv
  - Numpy
  - Sufficent storage ~ 1.5 GB
  - VLC video player to view output with mp4v codec
### How to use:
  - First put .py and mp4 into your working directory
  - Run security.py to save M.csv, L.csv, and S.csv
  - Note M = L + S per Robust PCA
  - Num frames = 100 and other dimension choices are hardcoded, you can change this as you see fit 
    - num iters and $\epsilon$ thresh are set to 10 and 1.7e-10 * l2(data) respectivley   
  - Run playsparse.py to output and save the video containing the sparse noise at 20 fps to your WD
  - Reccomended to open output video in VLC or other 3rd party video player, out of box windows/mac players may not support relevant codec
