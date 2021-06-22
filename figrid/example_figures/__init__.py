import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

import figrid as fg

def heatmap(axis):
    '''
    plot a random pixel image
    input: a single axis handle
    '''
    axis.imshow(np.random.randn(100,100),cmap='gray')
    axis.set_title('An image')
    axis.axis('off')
    
    # add a scalebar
    fg.scalebar(
        axis = axis,
        x_pos = 10,
        y_pos = 85,
        x_length = 30, 
        x_text = '60 um',
        scalebar_color='white',
        text_color='white',
        fontsize=12,
        y_buffer = -2,
    )
    
def sinusoids(axis):
    '''
    plot 3 sinusoids plus a scalebar
    input: a 3 row by 1 column array of axis handles
    '''
    t = np.arange(0,10,0.01)
    for row in range(3):
        f = 0.8*(row + 1)
        axis[row].plot(t, np.sin(2*np.pi*f*t), color='black',linewidth=2)
        axis[row].axis('off')
        axis[row].set_xlim(-0.5,10.5)
        axis[row].set_ylim(-1.35,1.05)
        axis[row].set_title('frequency = {:0.1f} Hz'.format(f))
    
    # add a scalebar
    fg.scalebar(
        axis = axis[2],
        x_pos = -0.25, 
        y_pos = -1.25, 
        x_length = 1, 
        y_length = 1, 
        x_text = '1 s', 
        y_text = '1 u'
    )
    
def violins(axis):
    '''
    violinplot example from https://seaborn.pydata.org/examples/simple_violinplots.html
    '''
    # Create a random dataset across several variables
    rs = np.random.default_rng(0)
    n, p = 40, 8
    d = rs.normal(0, 2, (n, p))
    d += np.log(np.arange(1, p + 1)) * -5 + 10

    # Show each distribution with both violins and points
    sns.violinplot(data=d, palette="light:g", inner="points", orient="h", ax=axis)
    sns.despine()
    
def scatterplot(axis):
    '''
    scatterplot example from https://seaborn.pydata.org/examples/layered_bivariate_plot.html
    '''
    # Simulate data from a bivariate Gaussian
    n = 10000
    mean = [0, 0]
    cov = [(2, .4), (.4, .2)]
    rng = np.random.RandomState(0)
    x, y = rng.multivariate_normal(mean, cov, n).T

    # Draw a combo histogram and scatterplot with density contours
    sns.scatterplot(x=x, y=y, s=5, color=".15", ax=axis)
    sns.kdeplot(x=x, y=y, levels=5, color="w", linewidths=1, ax=axis)