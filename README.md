# Pic In Pic by python
One of the most popular domain for fun is image domain. By this code you can generate your mosaic style image. By this code, you replace some pix of master image to the best sub image (master and sub image are picture that you introduced to algorithm as them. Certainly, they are described In the steps of implementation). By some a littele changes, you can inject this code to your server side and extend features of your application.


# Implementation:
This usage code has main 8 steps. For acheiveing to your mosaic image, you should follow these.

#### Step 1:
First of all, put your sub image in “data/raw/”. They should have .jpg format. If it’s not, jump to code and set the correct format (in 0_preprocess).
#### Step 2:
Make sure that your python has these libraries: 
  - cv2
  - csv
  - sklearn.externals

#### Step 3: 
Run 0_preprocess.py. It’ll build rgb_file.csv in clusters folder. 
#### Step 4: 
If you want to use all of your sub image to create master image (mosaic image), set k to number of sub images. This parameter is in 1_clustering.py file (line 8). 
#### Step 5:
If everything is ok, you shoud put your master image that you want to make it mosaic style, in pic folder. It is necessary to rename this image to “input.jpg” 
#### Step 6: 
Set size of each sub image in line 7 of 2_create_master.py file (suggested size is 150). Then run 2_create_master.py. 
#### Step 7: 
Waiting… In this step you can drinke some cup of cofee until the generation will be compeleted.
#### Step 8: 
Done! Your mosaic image is ready in “pic/output.png”

**warning :** Don’t remove or rename the path directories. If you want to remove them, you should find that dir in the code and substitiut that.
