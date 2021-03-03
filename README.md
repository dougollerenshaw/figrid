# figrid
A wrapper for the matplotlib gridspec function.  Designed to make it easy to place axes on a pre-defined grid on a figure canvas. For example, maybe you want to lay out axes like this:

<img src="examples/sample_figure_layout.png?raw=true " alt="Example Layout" style="zoom:40%;" />

## how it works
The fundamental function to use is `place_axes_on_grid`. This will generate an evenly spaced 100x100 grid on the desired figure canvas. You can then specify how much of the figure canvas a given axis (or set of axes) will span.  

## what it's good for
Maybe it's just me, but I've always found matplotlib's gridspec function to be confusing. And simple NxM subplots can be too limiting. This makes it easy to place any number of axes at arbitrary locations on a figure. It's handy for making figures for publication.

## a sample workflow
1) Make some functions to generate the various subplots you want to display on a figure. Those functions should take an axis handle as an input.
2) Define a figure canvas of the desired size.
3) Define your axes, specifying their locations using `figrid.place_axes_on_grid()` (a dictionary is a handy data structure for storing your axis handles).
4) Call your plotting functions with the axes as inputs.
5) Add some axis labels that you can refer to from your figure legend.

## installation:

    pip install figrid

## syntax
`figrid.place_axes_on_grid` takes the following inputs:
* fig - the figure handle on which the axis will be placed
* xspan - a two-element list or tuple defining the left and right edges of the axis, respectively. Numbers should be floats ranging from 0 to 1 and will be rounded to 2 decimal places.
* yspan - a two-element list or tuple defining the top and bottom edges of the axis, respectively. Numbers should be floats ranging from 0 to 1 and will be rounded to 2 decimal places.
* dim - a two-element tuple defining the number of rows/columns of the axis. Default = [1, 1], giving a single axis.
* hspace = a float defining the horizontal space between subplots (if dim is specified)
* vspace = a float defining the vertical space between subplots (if dim is specified)

## sample use:

some imports:

    # import the package as fg
    import figrid as fg

    # import example figure code
    import example_figures

    # import maptlotlib
    import matplotlib.pyplot as plt

define a function to lay out the axes on a figure

    # define function to set up figure and axes
    def make_fig_ax():
        fig = plt.figure(figsize=(11,8.5))
        ax = {
            'panel_A': fg.place_axes_on_grid(fig, xspan=[0.05, 0.3], yspan=[0.05, 0.45]),
            'panel_B': fg.place_axes_on_grid(fig, xspan=[0.4, 1], yspan=[0.05, 0.45], dim=[3, 1], hspace=0.4),
            'panel_C': fg.place_axes_on_grid(fig, xspan=[0.05, 0.4], yspan=[0.57, 1]),
            'panel_D': fg.place_axes_on_grid(fig, xspan=[0.5, 1], yspan=[0.57, 1])
        }
        
        return fig, ax

make the figure

    # call function to make figure and axes
    fig, ax = make_fig_ax()

    # call individual plotting functions, with axes as inputs
    example_figures.heatmap(ax['panel_A'])
    example_figures.sinusoids(ax['panel_B'])
    example_figures.violins(ax['panel_C'])
    example_figures.scatterplot(ax['panel_D'])

add some labels

    labels = [
        {'label_text':'A', 'xpos':0,    'ypos':0.05, 'fontsize':20, 'weight': 'bold', 'ha': 'right', 'va': 'bottom'},
        {'label_text':'B', 'xpos':0.37, 'ypos':0.05, 'fontsize':20, 'weight': 'bold', 'ha': 'right', 'va': 'bottom'},
        {'label_text':'C', 'xpos':0,    'ypos':0.55, 'fontsize':20, 'weight': 'bold', 'ha': 'right', 'va': 'bottom'},
        {'label_text':'D', 'xpos':0.45, 'ypos':0.55, 'fontsize':20, 'weight': 'bold', 'ha': 'right', 'va': 'bottom'},
    ]
    fg.add_labels(fig, labels)

Then we have this:

<img src="examples/sample_figure.png?raw=true " alt="Example Figure" style="zoom:100%;" />