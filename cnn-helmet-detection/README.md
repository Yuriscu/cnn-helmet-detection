# cnn-helmet-detection
A CNN implementation of a script that detects person with/without helmets.







1- This project is developed Google Colab for GPU tesla K80 
   
       from google.colab import drive
       drive.mount('/content/drive')
       
2- Clone the repository in /content/drive/'My Drive'/cnn-helmet-detection
        
       %cd /content/drive/'My Drive'/cnn-helmet-detection
       !git clone <repo>
       
3- Install requirements.txt file for modules

       !pip install -r requirements.txt
       
4- Download negative (false) images from the ImageNet dataset via Image URLs and stores it in a 
   mounted your google drive directory. Here is the following command.
   
       !python download-negative-images.py

5- Download positive (true) images from the ImageNet dataset via Image URLs and stores it in a 
   mounted your google drive directory. Here is the following command.

       !python download-positive-images.py
       
6- Certain downloaded images may simply be empty or irrepresentative images - to improve the accuracy
   of the algorithm and time gain for download this Image URLs in ImageNet. We can use following command in
   download-negative-images.py and download-positive-images.py .
      
       import socket
       socket.setdefaulttimeout(5)
       
7- Split the downloaded images into training and test set, and sorts them into directories suitable for 
   use with Keras functions.
   
       !python sort_train_and_test.py

8-  Create and train the CNN.

       !python cnn.py
       
9- In classify.py using the parser argument -i for images path. 

       !python classify.py -i <imageFileName>