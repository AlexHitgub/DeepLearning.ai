import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import ndimage
from course1.week_02.Test.logistic_regression_with_a_neural_network_mindset.lr_utils import load_dataset
from course1.week_02.Test.logistic_regression_with_a_neural_network_mindset.helper_functions import predict
from course1.week_02.Test.logistic_regression_with_a_neural_network_mindset.train import train

# Loading the data (cat/non-cat)
train_set_x_orig, _, test_set_x_orig, _, classes = load_dataset()
num_px = train_set_x_orig.shape[1]

d = train()

## START CODE HERE ## (PUT YOUR IMAGE NAME)
my_image = "my_image.jpg"   # change this to the name of your image file
## END CODE HERE ##

# We preprocess the image to fit your algorithm.
fname = "images/" + my_image
image = np.array(ndimage.imread(fname, flatten=False))
my_image = scipy.misc.imresize(image, size=(num_px,num_px)).reshape((1, num_px*num_px*3)).T
my_predicted_image = predict(d["w"], d["b"], my_image)

plt.imshow(image)
print("y = " + str(np.squeeze(my_predicted_image)) + ", your algorithm predicts a \"" + classes[int(np.squeeze(my_predicted_image)),].decode("utf-8") +  "\" picture.")