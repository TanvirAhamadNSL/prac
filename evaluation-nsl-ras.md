# Evaluation Question for NSL Reaserch Assistants

## Index
- [Instructions](https://github.com/NSLabTeam/nslraevaluation/blob/master/evaluation-nsl-ras.md#instructions)
- [A. Unix commands](https://github.com/NSLabTeam/nslraevaluation/blob/master/evaluation-nsl-ras.md#a-unix-commands)
- [B. Python basic](https://github.com/NSLabTeam/nslraevaluation/blob/master/evaluation-nsl-ras.md#b-python-basic)
- [C. Python OOP](https://github.com/NSLabTeam/nslraevaluation/blob/master/evaluation-nsl-ras.md#c-python-oop)
- [D. Data structure & algorithm](https://github.com/NSLabTeam/nslraevaluation/blob/master/evaluation-nsl-ras.md#d-data-structure--algorithm)
- [E. Numpy](https://github.com/NSLabTeam/nslraevaluation/blob/master/evaluation-nsl-ras.md#e-numpy)
- [F. Deep learning](https://github.com/NSLabTeam/nslraevaluation/blob/master/evaluation-nsl-ras.md#f-deep-learning)

## Instructions
1. Numbers placed at the end of each question represents the points for that specific question/problem.

2. Total time for this evaluation is: `4 hr`.

3. Create a directory named `ra_evaluation_<name>`. Write your answers in .docx file and use `.py` files where necessary. Put all the files inside the `ra_evaluation_<name>` directory.

4. You need to upload the directory to your NSL github repository immediately after the evaluation time ended.

## A. Unix commands
### A1. Suppose we have three paths like bellow- `[3]`
```bash
/tmp/data/images/
tmp/data/images/
./tmp/data/images/
```
what are the differences among these paths?

### A2. What is the meaning of `~` in linux system and what will the bellow command print? `[1]`
```bash
>>> echo ~
```

### A3. What will the bellow command do in linux system? `[1]`
```bash
>>> mkdir {1..10}
```
### A4. What are the differences between these two commands? `[2]`
```bash
>>> mkdir data
>>> mkdir -p data
```
Between the above commands which one can be used as the best practice?

### A5. Suppose you have an image directory that contains `10000000` images. Now there is a problem with image file `10000.png`. So you need to check it. But the problem is when you open the image directory from your file manager, your file manager gets hang. What should you do in this situtation to check image file `10000.png`? `[2.5]`

### A6. Suppose you have a log file written from one of your training operations. The problem is that- the log file is of very large size that you can not open in a text editor, it gets stuck. Now you need to search for a specific log message in that log file. What unix command will you use to confirm if that specific message exists in your log file and how will you extract the line containing relevent info of that log message? `[2.5]`

## B. Python basic

### B1. Suppose we have two python variables *arg **args like bellow. `[2]`
```python
def method_name(*arg, **args):
    pass
```
what is the differrence between these two veriables in python? 

### B2. We have code like bellow `[2]`
```python
def iterator(start, end):
    pass

iterator(10, 10)
iterator(start=10, 20)
iterator(10, end=10)
iterator(start=10, end=20)
```
What will happen in the above 4 different calls of the same method `iterator()`?

### B3. Suppose we have a string object as following, `[2]`
```python
lab_name = "NSLab"
```
Can we do the bellow operations? Yes or not, explain.
```python
lab_name[0] = 'n'
lab_name[1] = 's'
lab_name[2] = 'l'
lab_name[3] = 'A'
lab_name[4] = 'b'
```
### B4. Suppose you have a method named `get_info()` and it return two values `name` and `address` like bellow- `[3]`
```python
def get_info():
    name = get_name()
    address = get_address()
    return name, address
```
We can get info by calling, 
```python
name, address = get_info()
```
Let's say, we do not need to use variable `address` then what should be the best way to call `get_address()` method?

### B5. Suppose you are given the bellow method for doing a specific mathematical operation. Can you find out the breaking point of the method and how can you fix that if any? `[5]`

```python
def do_math(number1, number2):
    return number1 / number2

# lets call the method with x, y where x and y are two numbers
do_math(x, y)
```

## C. Python OOP
### C1. Meaning of underscors in python `[3]`
- `_variable_name`
- `__variable_name`
- `variable_name_`

What are the meanings of these three different undrescores in python language?


### C2. Implement the required built in method to get access list like data. `[5]`
For example we have custom class `LaptopBrand` and it’s object `laptopBrand`.

```python
class LaptopBrand:
    def __init__(self, name):
        self.name = name
```
How do we get feature like bellow from `LaptoopBrand` class?
```python
# we can do this
laptopBrand = Laptop("Lenovo")

# but how can i do this
laptopBrand[0] = 'DELL'
laptopBrand[1] = 'HP'

print(laptopBrand[0])
```

### C3. We have two methods with same name in class A & B. If we inherite both A, B in class C which method will be called? `[2]`

```python
class A: 
    def f(self):
        print(‘f from class A’) 

class B:
    def f(self):
        print(‘f from class B’)

class C(A, B): 
   pass 

# create object of C()
obj = C()
# lets call the f() method
obj.f() 
```
what will `obj .f()` print?

### C4. How to make a python object callable? `[5]`

```python
class Layer:
    def __init__(self, name):
        self.name = name
    
    def ... (self):
        pass 

layer = Layer("custom layer name")

y = layer(image)
```
what method do we need to implement to get feature like `y = layer(image)` in our custom `Layer` object? Implement the right method

#### C5. How to initialize super class ```__init__()``` from child class `[3]`
```
# super class
class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height

# child class
class FlowerImage(Image):
    def __init__(self, width, height, flower_name):
        pass
```
How to call `Image` class `__init__()` method from `FlowerImage` class?

## D. Data structure & algorithm
### D1. Suppose you have data like `Bangladesh voter ID card`. We all know it has the attribues like `name, id card number, address, date of brith` and so on. What python data structure will you use to store this kinds of data and why? `[4]`

### D2. We have a `test` directory like bellow- `[8]`
```bash
test
├── A
│   ├── a1.txt
│   ├── a2.txt
│   └── K
├── B
│   └── L
│       ├── l1.txt
│       └── l2.txt
└── C
    └── c1.txt
```
Write a function that resursively visit each file and directory and print the name of file and directory. You can not use python built in function to do this. But you can only use `os.listdir('test')` to get listing file and folder names in the current directory. 

### D3. Do you know about fibonacci numbers? If not please check [wiki](https://en.wikipedia.org/wiki/Fibonacci_number). Now your task is to write a python function that will generate all the `i`<sup>`th`</sup> fibonacci sequence for `0 < i <= N`. `[6]`

```python
Inputs:
1, 2, 5, 10

Outpus:
0
0, 1
0, 1, 2, 3, 5
0, 1, 2, 3, 5, 8, 13, 21, 34, 55
```
NB: You must have to use python `generator` in your implementatoin.

### D4. Let's assume we have built a model (`translator`) that translates `bangla` text to `english`. In the prediction `API` we have the following code- `[4]`
```python
def predict_bangla_text_to_english_text(bangla_text):
    english_text = translator.predict(bangla_text)
    return english_text
```
Is there any way to improve the speed for frequently searched translations for the above `predict_bangla_text_to_english_text()` method?

## E. Numpy

### E1. Let's assume, you have an array or numbers like below- `[6]`
```python
A = [[ 0,  1,  2,  3],
[ 4,  5,  6,  7],
[ 8,  9, 10, 11],
[12, 13, 14, 15]]
```
a. Write a statement with slice notation that will select center elements from the array `A`. The resultant array might look like below- 
```python
[[ 5,  6],
[ 9, 10]]
```
b. Pick all values from `A` except the last column. The resultant array might look like below.
```python
[[ 0,  1,  2],
[ 4,  5,  6],
[ 8,  9, 10],
[12, 13, 14]]
```
c. Pick all values from `A` except the first row. The resultant array might look like below.
```python
[[ 4,  5,  6,  7],
[ 8,  9, 10, 11],
[12, 13, 14, 15]]
```

### E2. Suppose you are given a numpy array like bellow-  `[3]`
```python
A = [[[[ 0,  1,  2],
        [ 3,  4,  5]],

        [[ 6,  7,  8],
        [ 9, 10, 11]]],


        [[[12, 13, 14],
        [15, 16, 17]],

        [[18, 19, 20],
        [21, 22, 23]]]]
```
Calculate the row wise sum of the array without using explicit loop.
See the output for clarification-

```python
Row_sum =   [[[ 3, 12],
            [21, 30]],

            [[39, 48],
            [57, 66]]]
```


## F. Deep learning
### F1. Suppose you have a polynomial equation `y = 5x`<sup>`2`</sup>` + 7x + 9`. Now, you want to learn this equation by a neural network. Write the possible solution in python and tensorflow. To be more specefic we have below input and target. `[25]`

```python
x_train = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_train = np.array([5*i**2 + 7*i + 9 for i in x_train])
```
Input / Output:
```python
If we input to our model 0 it should print 9
If we input to our model 1 it should print 21
If we input to our model 2 it should print 43
...
for 9 it should print 477
```
### F2. Solving model overfitting issue `[25]`
You are given a code snipt for training a neural network model for classifying cats and dogs. Run the training in a python environment. It seems that the model will overfit in the learning process. Can you fix the overfitting issue so that the distance in between training accuracy and validation accuracy curve is closer as much as possible.
```python
# Download dataset
wget --no-check-certificate \
    https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip \
    -O /tmp/cats_and_dogs_filtered.zip
  
import os
import zipfile
import tensorflow as tf
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator

local_zip = '/tmp/cats_and_dogs_filtered.zip'
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall('/tmp')
zip_ref.close()

base_dir = '/tmp/cats_and_dogs_filtered'
train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'validation')

# Directory with our training cat pictures
train_cats_dir = os.path.join(train_dir, 'cats')

# Directory with our training dog pictures
train_dogs_dir = os.path.join(train_dir, 'dogs')

# Directory with our validation cat pictures
validation_cats_dir = os.path.join(validation_dir, 'cats')

# Directory with our validation dog pictures
validation_dogs_dir = os.path.join(validation_dir, 'dogs')

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(150, 150, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(loss='binary_crossentropy',
              optimizer=RMSprop(lr=1e-4),
              metrics=['accuracy'])

# All images will be rescaled by 1./255
train_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

# Flow training images in batches of 20 using train_datagen generator
train_generator = train_datagen.flow_from_directory(
        train_dir,  # This is the source directory for training images
        target_size=(150, 150),  # All images will be resized to 150x150
        batch_size=20,
        # Since we use binary_crossentropy loss, we need binary labels
        class_mode='binary')

# Flow validation images in batches of 20 using test_datagen generator
validation_generator = test_datagen.flow_from_directory(
        validation_dir,
        target_size=(150, 150),
        batch_size=20,
        class_mode='binary')

history = model.fit(
      train_generator,
      steps_per_epoch=100,  # 2000 images = batch_size * steps
      epochs=100,
      validation_data=validation_generator,
      validation_steps=50,  # 1000 images = batch_size * steps
      verbose=2)
```
Model result shold look like bellow
```python
import matplotlib.pyplot as plt
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(len(acc))

plt.plot(epochs, acc, 'bo', label='Training accuracy')
plt.plot(epochs, val_acc, 'b', label='Validation accuracy')
plt.title('Training and validation accuracy')

plt.figure()

plt.plot(epochs, loss, 'bo', label='Training Loss')
plt.plot(epochs, val_loss, 'b', label='Validation Loss')
plt.title('Training and validation loss')
plt.legend()

plt.show()
```
![image](./images/overfitting.png)
