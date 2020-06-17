import json
#import tensorflow as tf
import numpy as np
import requests
from keras.applications.mobilenet_v2 import MobileNetV2
from keras.preprocessing import image

image_path = "./test_images/Z.png"
#image = tf.keras.preprocessing.image.load_img(image_path)
img = image.img_to_array(image.load_img(image_path, target_size=(128, 128, 3))) / 255.
img = np.expand_dims(img, axis = 0)



data = json.dumps({"signature_name": "serving_default", "instances": img.tolist()})
headers = {"content-type": "application/json"}
json_response = requests.post('http://localhost:9000/v1/models/ImageClassifier:predict', data=data, headers=headers)
#predictions = json_response.text
predictions = np.array(json.loads(json_response.text))
dic = predictions.item()         #Converting dictionary in np.ndarray to dictionary
narr = dic['predictions']
#["predictions"]
print(predictions)

MaxVal = np.amax(narr)
print("max value of accuracy : ", MaxVal)
MaxValIndx = np.where(narr == np.amax(narr))
index = MaxValIndx[1].item()
print("index of max value is: ", MaxValIndx[1])
classList = ["Cat", "Dog", "Human"]
print("Class Detected : ", classList[index])
message = "Object detected as " + str(classList[index]) + " with an accuracy of " + str("{0:.2f}".format(MaxVal*100.00)) + "%"
print(message)
#print(type(dic))
#print(dic['predictions'])






























