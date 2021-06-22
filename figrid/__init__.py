import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

__version__ = '0.1.6'

def place_axes_on_grid(
        fig,
        dim=[1, 1],
        xspan=[0, 1],
        yspan=[0, 1],
        wspace=None,
        hspace=None,
        sharex=False,
        sharey=False,
        frameon=True):
    '''
    Takes a figure with a gridspec defined and places an array of sub-axes on a portion of the gridspec
    
    Takes as arguments:
        fig: figure handle - required
        dim: number of rows and columns in the subaxes - defaults to 1x1
        xspan: fraction of figure that the subaxes subtends in the x-direction (0 = left edge, 1 = right edge)
        yspan: fraction of figure that the subaxes subtends in the y-direction (0 = top edge, 1 = bottom edge)
        wspace and hspace: white space between subaxes in vertical and horizontal directions, respectively
    returns:
        subaxes handles
    '''

    outer_grid = gridspec.GridSpec(100, 100)
    inner_grid = gridspec.GridSpecFromSubplotSpec(
        dim[0],
        dim[1],
        subplot_spec=outer_grid[int(100 * yspan[0]):int(100 * yspan[1]), int(100 * xspan[0]):int(100 * xspan[1])],
        wspace=wspace,
        hspace=hspace
    )

    # NOTE: A cleaner way to do this is with list comprehension:
    # inner_ax = [[0 for ii in range(dim[1])] for ii in range(dim[0])]
    inner_ax = dim[0] * [dim[1] * [fig]]  # filling the list with figure objects prevents an error when it they are later replaced by axis handles
    inner_ax = np.array(inner_ax)
    idx = 0
    for row in range(dim[0]):
        for col in range(dim[1]):
            if row > 0 and sharex == True:
                share_x_with = inner_ax[0][col]
            else:
                share_x_with = None

            if col > 0 and sharey == True:
                share_y_with = inner_ax[row][0]
            else:
                share_y_with = None

            inner_ax[row][col] = plt.Subplot(
                fig,
                inner_grid[idx],
                sharex=share_x_with,
                sharey=share_y_with,
                frameon=frameon,
            )

            if row == dim[0] - 1 and sharex == True:
                inner_ax[row][col].xaxis.set_ticks_position('bottom')
            elif row < dim[0] and sharex == True:
                plt.setp(inner_ax[row][col].get_xtick)

            if col == 0 and sharey == True:
                inner_ax[row][col].yaxis.set_ticks_position('left')
            elif col > 0 and sharey == True:
                plt.setp(inner_ax[row][col].get_yticklabels(), visible=False)

            fig.add_subplot(inner_ax[row, col])
            idx += 1

    inner_ax = np.array(inner_ax).squeeze().tolist()  # remove redundant dimension
    return inner_ax


def add_label(fig, label_text, xpos, ypos, **kwargs):
    '''
    add a single label to a figure canvas using the place_axes_on_grid infrastructure
    inputs:
        fig: figure handle
        label_text : text of label, 
        xpos, ypos: floats from 0 to 1 defining where on the canvas the label should be
        kwargs: additional keyword arguments for matplotlib text()
    ''' 
    label_axis = place_axes_on_grid(
        fig, 
        xspan=[xpos,xpos + 0.01],
        yspan=[ypos,ypos + 0.01],
    )
    label_axis.text(0, 0, label_text, **kwargs)
    label_axis.axis('off')


def add_labels(fig, labels):
    '''
    add multiple labels to a figure canvas using the place_axes_on_grid infrastructure
    inputs:
        fig: figure handle
        labels: a list of dictionaries with the following key/value pairs (keys must be named as follows):
            * label_text (required): text of label
            * xpos (required): float from 0 to 1 defining horizontal position of label (0 = left, 1 = right)
            * ypos (required): float from 0 to 1 defining vertical position of label (0 = top, 1 = bottom)
            * any additional keyword arguments that can be passed to the matplotib text function (e.g., fontsize, weight, etc)
    '''
    for label in labels:
        add_label(fig, **label)


def scalebar(axis, x_pos, y_pos, x_length=None, y_length=None, x_text=None, y_text=None, x_buffer=0.25, y_buffer=0.25, scalebar_color='black', text_color='black', fontsize=10, linewidth=3):
    '''
    add a scalebar
    input params:
        axis: axis on which to add scalebar
        x_pos: x position, in pixels
        y_pos: y position, in pixels
    '''
    if x_length is not None:
        axis.plot(
            [x_pos,x_pos + x_length],
            [y_pos,y_pos],
            color = scalebar_color,
            linewidth = linewidth
        )
        axis.text(
            x_pos + x_length/2, 
            y_pos - y_buffer,
            x_text,
            color = text_color,
            fontsize = fontsize,
            ha = 'center',
            va = 'top'
        )
    
    if y_length is not None:
        axis.plot(
            [x_pos,x_pos],
            [y_pos,y_pos + y_length],
            color = scalebar_color,
            linewidth = linewidth
        )
    
        axis.text(
            x_pos - x_buffer, 
            y_pos + y_length/2,
            y_text,
            color = text_color,
            fontsize = fontsize,
            ha='right',
            va='center'
        )