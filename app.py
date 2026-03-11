<<<<<<< HEAD
from flask import Flask, request, render_template
import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import custom_object_scope
from tensorflow.keras.layers import Layer
from tensorflow.keras.preprocessing import image
from PIL import Image
import tensorflow as tf

# === Custom Cast Layer ===
class CustomCastLayer(Layer):
    def call(self, inputs):
        return tf.cast(inputs, tf.float32)

# === Load model with custom Cast layer ===
with custom_object_scope({'Cast': CustomCastLayer}):
    model = load_model("resnet50_tf_garbage_classifier.keras")

# === Class labels (same as training) ===
class_names = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']

# === Flask app setup ===
app = Flask(__name__, template_folder='templates', static_folder='static')

# === Image preprocessing ===
def load_and_prepare_image(img_path, target_size=(224, 224)):
    img = image.load_img(img_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = tf.keras.applications.resnet50.preprocess_input(img_array)
    return img_array

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    if file:
        filepath = os.path.join('static', file.filename)
        file.save(filepath)

        preprocessed_img = load_and_prepare_image(filepath)
        predictions = model.predict(preprocessed_img)
        predicted_class = class_names[np.argmax(predictions)]

        return render_template('result.html', prediction=predicted_class, image_path=filepath)
@app.route('/performance')
def performance():
    return render_template('performance.html')


if __name__ == '__main__':
    app.run(debug=True)
=======
from flask import Flask, request, render_template
import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import custom_object_scope
from tensorflow.keras.layers import Layer
from tensorflow.keras.preprocessing import image
from PIL import Image
import tensorflow as tf

# === Custom Cast Layer ===
class CustomCastLayer(Layer):
    def call(self, inputs):
        return tf.cast(inputs, tf.float32)

# === Load model with custom Cast layer ===
with custom_object_scope({'Cast': CustomCastLayer}):
    model = load_model("resnet50_tf_garbage_classifier.keras")

# === Class labels (same as training) ===
class_names = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']

# === Flask app setup ===
app = Flask(__name__, template_folder='templates', static_folder='static')

# === Image preprocessing ===
def load_and_prepare_image(img_path, target_size=(224, 224)):
    img = image.load_img(img_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = tf.keras.applications.resnet50.preprocess_input(img_array)
    return img_array

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    if file:
        filepath = os.path.join('static', file.filename)
        file.save(filepath)

        preprocessed_img = load_and_prepare_image(filepath)
        predictions = model.predict(preprocessed_img)
        predicted_class = class_names[np.argmax(predictions)]

        return render_template('result.html', prediction=predicted_class, image_path=filepath)
@app.route('/performance')
def performance():
    return render_template('performance.html')


if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> fe98041f04fd5527ea0e009043a6455356b08b55
