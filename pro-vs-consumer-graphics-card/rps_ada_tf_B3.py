import os
import tensorflow as tf
import requests 
import py7zr
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

# function for downloading the image files from a URL
def download_file(url, filename, chunk_size=128):
    response = requests.get(url, stream=True)
    with open(f'./{filename}', 'wb') as new_file:
        for chunk in response.iter_content(chunk_size=chunk_size):
            new_file.write(chunk)

# define folders and filenames
dl_file_1 = 'rps.7z.001'
dl_file_2 = 'rps.7z.002'
filenames = [dl_file_1, dl_file_2]
output_file = 'rps.7z'
root_folder = './rps'
file_part1 = 'https://github.com/thetestspecimen/notebooks/raw/main/datasets/rock_paper_scissors/rock_paper_scissors_712.7z.001'
file_part2 = 'https://github.com/thetestspecimen/notebooks/raw/main/datasets/rock_paper_scissors/rock_paper_scissors_712.7z.002'

# download files
download_file(url=file_part1, filename=dl_file_1)
download_file(url=file_part2, filename=dl_file_2)

# concatenate files
with open(output_file, 'ab') as outfile: 
    for filename in filenames:
        with open(filename, 'rb') as infile:      
            outfile.write(infile.read())

# unzip concatenated file
with py7zr.SevenZipFile("rps.7z", "r") as archive:
    archive.extractall(path=root_folder)

# delete archives
for f in filenames:
    os.remove(f)
os.remove(output_file)

# print files and folders
for root, dirs, files in os.walk(root_folder):
    print(f"{len(dirs)} directories and {len(files)} files in '{root}'")

# constants
IMAGE_HEIGHT = 300
IMAGE_WIDTH = 300
IMAGE_SIZE = (IMAGE_HEIGHT,IMAGE_WIDTH)
BATCH_SIZE = 128
DATA_DIR = f"{root_folder}/"
SEED = 12

# create datasets from the directories
train_data, val_data = tf.keras.utils.image_dataset_from_directory(DATA_DIR, 
                                                                   labels='inferred',
                                                                   label_mode='categorical',
                                                                   batch_size=BATCH_SIZE,
                                                                   image_size=IMAGE_SIZE,
                                                                   shuffle=True, 
                                                                   seed=SEED,
                                                                   validation_split=0.2,
                                                                   subset='both') 

# get the class names generated from the dataset
class_names = train_data.class_names
num_classes = len(class_names)

# augment the image files
# the image files are PNG, and therefore already sit beween 0 and 1.
# typically a rescaling layer would be required if they were JPG
# however EfficientNet has an inbuilt scaling layer so even then it isn't required
data_augmentation = Sequential([
                                layers.RandomRotation(0.2),
                                layers.RandomFlip('horizontal'),
                                layers.RandomZoom(0.2)
], name='data_augmentation')

# create and compile model
base_model = tf.keras.applications.EfficientNetB3(include_top=False, weights="imagenet")
base_model.trainable = True
inputs = layers.Input(shape=(IMAGE_SIZE + (3,)), name="input_layer")
x = data_augmentation(inputs)
x = base_model(x)
x = layers.GlobalAveragePooling2D(name="global_avg_pool_layer")(x)
outputs = layers.Dense(units=num_classes, activation='softmax', name='output_layer')(x)
model = tf.keras.Model(inputs, outputs)
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
          loss=tf.keras.losses.CategoricalCrossentropy(),
          metrics=['accuracy'])

# print model summary
model.summary()

# run training and validation
history = model.fit(train_data,
                    epochs=2,
                    validation_data=val_data,
                    verbose=1)

# print the peak GPU usage in GB for each GPU
for i, gpu in enumerate(tf.config.list_physical_devices('GPU')):
  # Returns a dict in the form {'current': <current mem usage>,
  #                             'peak': <peak mem usage>}
    mem_usage = tf.config.experimental.get_memory_info(f'GPU:{i}').get('peak')/1e9
    print(f'GPU Peak Memory Usage: {mem_usage:.2f}GB')