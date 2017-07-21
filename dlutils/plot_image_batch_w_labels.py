"""
Module to plot a batch of images along w/ their corresponding label(s)/annotations and save the plot to disc.

Use cases:
Plot images along w/ their corresponding ground-truth label & model predicted label,
Plot images generated by a GAN along w/ any annotations used to generate these images,
Plot synthetic, generated, refined, and real images and see how they compare as training progresses in a GAN,
etc...
"""

import os

import matplotlib
import numpy as np

matplotlib.use('Agg')  # b/c matplotlib is such a great piece of software ;) - needed to work on ubuntu
from matplotlib import pyplot as plt

matplotlib.rcParams.update({'axes.titlesize': 1})


def plot_batch(image_batch, figure_path, label_batch=None, vmin=0, vmax=255, scale=True):
    """
    Plots a batch of images and their corresponding label(s)/annotations, saving the plot to disc.

    :param image_batch: Batch of images to be plotted.
    :param figure_path: Full path of the filename the plot will be saved as.
    :param label_batch: Batch of labels corresponding to `image_batch`.
       Labels will be displayed along w/ their corresponding image.
    """
    if label_batch is not None:
        assert len(image_batch) == len(label_batch), 'Their must be a label for each image to be plotted.'

    batch_size = len(image_batch)
    assert batch_size >= 1

    assert isinstance(image_batch, np.ndarray), 'image_batch must be an np array.'

    # for gray scale images if image_batch.shape == (img_height, img_width, 1) plt requires this to be reshaped
    if image_batch.shape[-1] == 1:
        image_batch = np.reshape(image_batch, newshape=image_batch.shape[:-1])

    # plot images in rows and columns
    # `+ 2` prevents plt.subplots from throwing: `TypeError: 'AxesSubplot' object does not support indexing` when batch_size < 10
    nb_rows = batch_size // 10 + 2  # each row will have 10 images, last row will have the rest of images in the batch
    nb_columns = 10
    
    _, ax = plt.subplots(nb_rows, nb_columns, sharex=True, sharey=True)

    for i in range(nb_rows):
        for j in range(nb_columns):
            try:
                x = image_batch[i * nb_columns + j]
                if scale:
                    x = x + max(-np.min(x), 0)
                    x_max = np.max(x)
                    if x_max != 0:
                        x /= x_max
                    x *= 255

                ax[i][j].imshow(x.astype('uint8'), vmin=vmin, vmax=vmax, interpolation='lanczos')
                if label_batch is not None:
                    ax[i][j].set_title(label_batch[i * nb_columns + j])
                ax[i][j].set_axis_off()
            except IndexError:
                break

    plt.savefig(os.path.join(figure_path), dpi=600)
    plt.close()
