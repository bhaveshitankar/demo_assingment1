# This is an assignment to for rotation of PEB image file.

## The code can rotate PEB images by 90, 180, 270 ... or -90, -180, ... degrees 

## inputs:
- 1. file path of image to be rotated
- 2. angle at which image has to be rotated. code rounds of any angle to closest multiple of 90.

## output:
- 1. Console shows matrix of inputs image and output image.
- 2. a file is written at the same folder where input file is present with a new tage _output at the end.

## Cases when this code can panic
- 1. when PEB file does not have "P1" string.
- 2. image file is not present at the location.
- 3. I have tried to meet all the formatings of PEB Image, Known errors for formating are raised. Source (https://en.wikipedia.org/wiki/Netpbm)
### My development environment is linux. Code is made general for windows and linux but not tested on windows. 
