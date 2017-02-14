# deep-learning-utils
A clean and general implementation of some common utils and tools required by various deep learning projects.

## Installing
> $ pip install -U git+https://github.com/wayaai/deep-learning-utils.git  

or  

> $ git clone https://github.com/wayaai/deep-learning-utils.git  
> $ python setup.py install develop

## Usage

`plot_image_batch_w_labels.py`
```python
from dlutils import plot_image_batch_w_labels

# where `image_batch` is the batch of images to be plotted
# `label_batch` is a batch of true labels corresponding to each image in `image_batch`
# `predicted_labels` is a batch of labels predicted by our model for each image in `image_batch`

label_batch_strings = []
    for true_label, predicted_label in zip(label_batch, predicted_labels):
        label_batch_strings.append('True: {}, Predicted: {}'.format(true_label, predicted_label))
        
plot_image_batch_w_labels.plot_batch(image_batch, os.path.join(path, 'test.png'), label_batch=label_batch_strings)
```
