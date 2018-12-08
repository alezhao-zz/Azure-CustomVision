## Overview

The Custom Vision Service is an Azure Cognitive Service that lets you build custom image classifiers. It makes it easy and fast to build, deploy, and improve an image classifier. The Custom Vision Service provides a REST API and a web interface to upload your images and train the classifier. The Custom Vision Service works best when the item you're trying to classify is prominent in your image. Few images are required to create a classifier or detector. 50 images per class are enough to start your prototype. The methods Custom Vision Service uses are robust to differences, which allows you to start prototyping with so little data. This means Custom Vision Service is not well suited to scenarios where you want to detect subtle differences. For example, minor cracks or dents in quality assurance scenarios.

![](https://iothubstorageaccts.blob.core.windows.net/cvpic/1.jpg)

## **System requirements**

You must have the following to complete this lab:

- Azure Subscription
- Windows 10
- Microsoft Visual Code (latest update) 
- PIP library
  - `Pip install opencv-python`
  - `Pip install requests`
  - `Pip install azure-cognitiveservices-vision-customvision`
  - `Pip install matplotlib`

## **Exercises**

This Hands-on lab includes the following exercises:

1. Create Azure Service
2. Build image classify project by custom vision service
3. Build image classify project by Python with visual studio code
4. Build image object detection project by custom vision service

Estimated time to complete this lab:  **90** **minutes**.

## Exercise 1: Create Azure Service

1. Login Azure portal with provide Azure subscription

2. Create a Custom Vision Service

   - Create a new **Resource Group**, click **Add** at top panel. (remember **Resource Group Name**, please create all of services with this **Resource Group**)

   - Entry `custom vision` in Filter, you will find **Custom Vision (Preview)** in the list, choose this service and click create.

     ![](https://iothubstorageaccts.blob.core.windows.net/cvpic/2.png)

   - A new blade will open with information about the **Custom Vision (Preview)**.

     ![](https://iothubstorageaccts.blob.core.windows.net/cvpic/3.png)

   - In the **Custom Vision (Preview)** blade, provide the requested information about your service as specified in the table below image.

   - Entry **Name** of your service select default resource group in **Resource group** section. 

   - Click **Create**

## Exercise 2: Build image classify project by custom vision service

1. Open <https://customvision.ai/> by Microsoft Edge

2. Click sign in with provided azure subscription account. You will see below page once login. 

   ![](https://iothubstorageaccts.blob.core.windows.net/cvpic/4.png)

3. Click **NEW PROJECT** provide the requested information about your service as specified in the table below image.

   ![](https://iothubstorageaccts.blob.core.windows.net/cvpic/5.png)

   Entry **Name** of your project select resource group you create in **Exercise 1** in **Resource Group** section, other by default. 

   Click **Create project**

4. Click **Add images** on the top of panel, locate to folder C;\Lab\customvision\gear_images\axes\, select all of images by **Ctrl + A**, click **Open,** entry **axes** as tag at **My Tag** section

   ![](https://iothubstorageaccts.blob.core.windows.net/cvpic/6.png)

   Click **Upload 79 files**

   Do the same action for rest tags in C:\ gear_images\

   ![](https://iothubstorageaccts.blob.core.windows.net/cvpic/7.png)

5. Click **Train** at left of top panel to train the model by provide images of each tag

   ![](https://iothubstorageaccts.blob.core.windows.net/cvpic/8.png)

   Waiting for training integration complete

   ![](https://iothubstorageaccts.blob.core.windows.net/cvpic/9.png)

   You will find **Precision** and **Recall** number of your trained model. Click **Mark Default** at top of panel

6. Click **Quick Test** at left of top panel, entry 

   <https://www.alpinetrek.co.uk/1500_1500_90/002-0808/berghaus-baffin-island-shell-jacket-hardshell-jacket.jpg>

   In **Image** **URL** section, click you will see test result like below 

   ![](https://iothubstorageaccts.blob.core.windows.net/cvpic/10.png)

   Close output panel. 

7. Verify API by post URL endpoint. Click **Predictions** at top of panel, select result picture you just test, and click delete. Click **View Endpoint**

   ![](https://iothubstorageaccts.blob.core.windows.net/cvpic/11.png)

   Open **Postman** on the desktop, entry **POST URL** with first URL In above output
   panel. Entry **header** by key/value above 

   ![](https://iothubstorageaccts.blob.core.windows.net/cvpic/12.png)

   Entry **Body** with **raw** and **JSON** format with 

   {"Url": "https://www.alpinetrek.co.uk/1500_1500_90/002-0808/berghaus-baffin-island-shell-jacket-hardshell-jacket.jpg"}

   ![](https://iothubstorageaccts.blob.core.windows.net/cvpic/13.png)

   Click **Send**, you will see test result like below

   ![](https://iothubstorageaccts.blob.core.windows.net/cvpic/14.png)

## Exercise 3: Build image classify project by Python with visual studio code

1. Open **Visual Studio Code** on desktop, select Python 3.5 at left of bottom panel. 

   ![](https://iothubstorageaccts.blob.core.windows.net/cvpic/15.png)

   clicK **File** at left of top panel, click **Open File…**, locate to C;\Lab\customvision\classify.py

   click **Open**

   ![](https://iothubstorageaccts.blob.core.windows.net/cvpic/16.png)

2. Open portal <https://customvision.ai/>,
   click **sign in** if your session is expired. Click **setting icon** at left of top panel, 

   ![](https://iothubstorageaccts.blob.core.windows.net/cvpic/17.png)

   Copy **Training Key** and **Prediction Key** under resource group you created in **Exercise 1 (e.g. techsubmit not Limited trial).** Replace **training_key** and **prediction_key** in **classify.py**

   ![](https://iothubstorageaccts.blob.core.windows.net/cvpic/18.png)

   Replace project name **classifylabfreeze** with a new project name, different from project created in **Exercise 2**

   ![](https://iothubstorageaccts.blob.core.windows.net/cvpic/19.png)

   Replace `PredictionEndpoint` with **Prediction Key** above

   ![](https://iothubstorageaccts.blob.core.windows.net/cvpic/20.png)

   Click **F5,** select **Python** at output command 

   ![](https://iothubstorageaccts.blob.core.windows.net/cvpic/21.png)

   Waiting for process complete, you will see the whole project was created, image uploaded, trained and verified automatically. (you could open <https://customvision.ai> to check project status, e.g. how many images uploaded)

   ![](https://iothubstorageaccts.blob.core.windows.net/cvpic/22.png)

## Exercise 4: Build image object detection project by custom vision service

1. Open <https://customvision.ai/> by Microsoft Edge

2. Click sign in with provided azure subscription account. You will see below page once login. 

   ![](https://iothubstorageaccts.blob.core.windows.net/cvpic/23.png)

3. Click **NEW PROJECT** provide the requested information about your service as specified in the table below image.

   ![](https://iothubstorageaccts.blob.core.windows.net/cvpic/24.png)

   Entry **Name** of your project select resource group you create in **Exercise 1** in **Resource Group** section, select **Object Detection (preview)** in **Project Type** section. 

   Click **Create project**

4. Click **Add images** on the top of panel, locate to folder C;\Lab\customvision\gear_images_detection\, select all of images by **Ctril + A**, click **Open**

   ![](https://iothubstorageaccts.blob.core.windows.net/cvpic/26.png)

   Click **Upload 251 files**

5. After uploaded all files, click first picture, select boundary of helmets in the picture and add tag **helmets** like below. 

   ![](https://iothubstorageaccts.blob.core.windows.net/cvpic/27.png)

   Entry **helmets** in **Add Region Tag** section first time. 

   ![](https://iothubstorageaccts.blob.core.windows.net/cvpic/28.png)

   Click next icon and do same action of rest of all pictures, it might take couple minutes. (you don’t need tag all of pictures, but at least 30 tagged pictures need)

6. Click **Train** at left of top panel to train model by provide images of each tag.

   ![](https://iothubstorageaccts.blob.core.windows.net/cvpic/29.png)

7. You will find **Precision**, **Recall** and **M.A.P** number of your trained model. Click **Mark Default** at top of panel 

8. Click **Quick Test** at left of top panel, entry. In **Image** **URL** section, click -> you will see test result like below 

   ![](https://iothubstorageaccts.blob.core.windows.net/cvpic/30.png)

9. Verify API by post URL endpoint. 

   Click **Predictions** at top of panel, select result picture you just test, and click delete. 

   Click **View Endpoint**

   ![](https://iothubstorageaccts.blob.core.windows.net/cvpic/31.png)

   Open **Postman** on the desktop, entry **POST URL** with first URL In above output panel. Entry **header** by key/value above 

   ![](https://iothubstorageaccts.blob.core.windows.net/cvpic/32.png)

   Entry **Body** with **raw** and **JSON** format with 

   ```json
   {"Url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Cologne_Germany_Industrial-work-with-Personal-Protective-Equipment-04.jpg/1200px-Cologne_Germany_Industrial-work-with-Personal-Protective-Equipment-04.jpg"}
   ```

   ![](https://iothubstorageaccts.blob.core.windows.net/cvpic/33.png)

   Click **Send**, you will see test result like below

   ![](https://iothubstorageaccts.blob.core.windows.net/cvpic/34.png)