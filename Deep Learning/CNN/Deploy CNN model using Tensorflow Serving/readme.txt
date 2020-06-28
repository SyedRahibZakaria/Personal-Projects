

Guidelines to run Tensorflow Serving Server:

To run the Tensorflow-Serving Server:

tensorflow_model_server --model_base_path=/home/rahib/Desktop/TensorflowServing/keras-and-tensorflow-serving/my_image_classifier --rest_api_port=9000 --model_name=ImageClassifier

Note:

model_base_path is the absolute path. Change the model_base_path value according to the my_image_classifier directory of your local computer by running the pwd command while in the my_image_classifier directory.


New **

1. Change image resolution from 128 x 128 to 224 x 224 in image preprocessing
2. Remove "1" from saved_model1.pb inside my_image_classifier folder. I renamed it because I was not able to push the file
3. Add false positive class while decoding e.g: ["Cat", "Dog", "Person", "False Positive"]. Use FServer.py for reference
4. SingleBoardComputerEmulator.py is sending data to flask server (FServer.py)

