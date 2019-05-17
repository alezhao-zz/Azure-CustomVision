
# coding: utf-8

# In[1]:


get_ipython().system(' /anaconda/envs/py35/bin/python -m pip freeze')
get_ipython().system(' /anaconda/envs/py35/bin/python -m pip --version')


# In[1]:


import sys
sys.version


# In[2]:


import time 
import requests
import cv2
import operator
import numpy as np
import json

# Import compatibility libraries (python 2/3 support)
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

# Python 3
try:
    from urllib.request import urlopen, Request
    from urllib.parse import urlparse, urlencode
    from http.client import HTTPSConnection
# Python 2.7
except ImportError:
    from urlparse import urlparse
    from urllib import urlencode
    from urllib2 import Request, urlopen
    from httplib import HTTPSConnection

# Import library to display results
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
# Display images within Jupyter


# In[12]:


# !conda install --no-deps -c menpo opencv=2.4.11 --yes


# In[14]:


# ! pip uninstall matplotlib --yes


# In[16]:


# ! pip install matplotlib -q


# In[3]:


from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageUrlCreateEntry

ENDPOINT = "https://westus2.api.cognitive.microsoft.com"

# Replace with a valid key
training_key = ""
prediction_key = ""


# In[4]:


trainer = CustomVisionTrainingClient(training_key, endpoint=ENDPOINT)

# Create a new project
print ("Creating project...")
project = trainer.create_project("ohcv")


# In[5]:


hardshell_jackets_tag = trainer.create_tag(project.id, "hardshell jackets")
insulated_jackets_tag = trainer.create_tag(project.id, "insulated jackets")


# In[6]:


import os.path
hardshell_jackets_path = './gear_images/hardshell_jackets'
hardshell_jackets_count = len([f for f in os.listdir(hardshell_jackets_path) if os.path.isfile(os.path.join(hardshell_jackets_path, f))])
print ("hardshell_jackets_count has " + str(hardshell_jackets_count))

insulated_jackets_path = './gear_images/insulated_jackets'
insulated_jackets_count = len([f for f in os.listdir(insulated_jackets_path) if os.path.isfile(os.path.join(insulated_jackets_path, f))])
print ("insulated_jackets_count has " + str(insulated_jackets_count))


# In[7]:


import os
print ("Adding images...")
for image in os.listdir(os.fsencode(hardshell_jackets_path)):
    with open(hardshell_jackets_path + "/" + os.fsdecode(image), mode="rb") as img_data: 
        trainer.create_images_from_data(project.id, img_data, [ hardshell_jackets_tag.id ])
        
for image in os.listdir(os.fsencode(insulated_jackets_path)):
    with open(insulated_jackets_path + "/" + os.fsdecode(image), mode="rb") as img_data: 
        trainer.create_images_from_data(project.id, img_data, [ insulated_jackets_tag.id ])
        
print ("Done!")


# In[ ]:


import time

print ("Training...")
iteration = trainer.train_project(project.id)
print (iteration)
while (iteration.status != "Completed"):
    iteration = trainer.get_iteration(project.id, iteration.id)
    print ("Training status: " + iteration.status)
    time.sleep(1)


# In[27]:


# The iteration is now trained. Make it the default project endpoint
trainer.update_iteration(project.id, iteration.id, is_default=True, name="Iteration 1")
print ("Done!")


# In[31]:


print(iteration)


# In[32]:


from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO
import matplotlib.patches as patches
# Now there is a trained endpoint that can be used to make a prediction

predictor = CustomVisionPredictionClient(prediction_key, endpoint=ENDPOINT)

test_img_url = "http://cdn.gearpatrol.com/wp-content/uploads/2014/01/best-hard-shells-gear-patrol-lead.jpg"
results = predictor.classify_image_url(project.id, 'alecv', url=test_img_url)

# Alternatively, if the images were on disk in a folder called Images alongside the sample.py, then
# they can be added by using the following.
#
# Open the sample image and get back the prediction results.
# with open("Images\\test\\test_image.jpg", mode="rb") as test_data:
#     results = predictor.predict_image(project.id, test_data, iteration.id)

# Display the results.

for prediction in results.predictions:
    print ("\t" + prediction.tag_name + ": {0:.2f}%".format(prediction.probability * 100))


# In[33]:


import requests 
import json 


# In[35]:


# importing the requests library 
import requests 
import json  
# api-endpoint 
URL = "https://westus2.api.cognitive.microsoft.com/customvision/v3.0/Prediction/d3398cdf-77ec-41da-995c-2954e586a1ed/classify/iterations/alecv/url?"
headers = {'content-type': 'application/json', 'Prediction-Key': '285654d7051e448ca2dcf121be88dbeb'}
data = json.dumps({"Url":"http://cdn.gearpatrol.com/wp-content/uploads/2014/01/best-hard-shells-gear-patrol-lead.jpg"})
# sending get request and saving the response as response object 
r = requests.post(url = URL, data = data, headers = headers) 

result = r.text 
print("Result is:%s"%result) 


# In[36]:


visual_box = []
visual_label = []
for single_result in json.loads(result)['predictions']:
    if (single_result["probability"] > 0.15):
        visual_label.append(single_result["tagName"])


# In[37]:


response = requests.get(test_img_url)
img = Image.open(BytesIO(response.content))
plt.figure()
# Create figure and axes
fig,ax = plt.subplots(1)
ax.imshow(img)
i = 0
for visual_box_single in visual_box:
    left = visual_box_single["left"] * img.size[0]
    top =  visual_box_single["top"] * img.size[1]
    width = visual_box_single["width"] * img.size[0]
    height = visual_box_single["height"] * img.size[1]
    rect = patches.Rectangle((left,top),width, height,linewidth=3,edgecolor='r',facecolor='none')
    ax.add_patch(rect)
    ax.annotate(visual_label[i], xy = (left,top))
    i= i+1

plt.title(visual_label[0])
plt.show()

