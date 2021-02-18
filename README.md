# mpl_figure_formatter
Utilities for formatting matplotlib figures

# sample use:

    import mpl_figure_formatter as ff
    from example_figures import *

    def make_fig_ax():
        fig = plt.figure(figsize=(11,8.5))
        ax = {
            'panel_A': ff.place_axes_on_grid(fig, xspan=[0, 0.3], yspan=[0, 0.45]),
            'panel_B': ff.place_axes_on_grid(fig, xspan=[0.4, 1], yspan=[0, 0.45], dim=[3, 1], hspace=0.4),
            'panel_C': ff.place_axes_on_grid(fig, xspan=[0, 0.4], yspan=[0.55, 1]),
            'panel_D': ff.place_axes_on_grid(fig, xspan=[0.5, 1], yspan=[0.55, 1])
        }
        
        return fig, ax

    fig, ax = make_fig_ax()
    heatmap(ax['panel_A'])
    sinusoids(ax['panel_B'])
    violins(ax['panel_C'])
    scatterplot(ax['panel_D'])

![Alt text](examples/sample_figure.png?raw=true "Sample Figure")