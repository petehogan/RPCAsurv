# RPCAsurv
Robust PCA for use in surveillance footage
### Contains: 
  - security.py
    - contains call to rpca via svt and creates data matrices from video   
  - securitypcp.py
    - same as security except solves nuclear norm min via PCP and not svt per alternating optimization   
  - pcp.py
    - algorithm for pricipal component pursuit from https://github.com/dfm/pcp 
  - playsparse.py
    - take result of rpca, either m, l or s (from m = l + s) and output to video in WD 
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
