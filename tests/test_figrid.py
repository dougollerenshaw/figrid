import pytest
import matplotlib.pyplot as plt
from figrid import place_axes_on_grid, add_label, add_labels, scalebar
from figrid.example_figures import heatmap, sinusoids, violins, scatterplot


@pytest.fixture
def figure():
    """Create a new figure for each test."""
    fig = plt.figure(figsize=(10, 10))
    yield fig
    plt.close(fig)


def test_example_layout(figure):
    """Test the complete layout example from README."""
    ax = {
        "panel_A": place_axes_on_grid(figure, xspan=[0.05, 0.3], yspan=[0.05, 0.45]),
        "panel_B": place_axes_on_grid(
            figure, xspan=[0.4, 1], yspan=[0.05, 0.45], dim=[3, 1], hspace=0.4
        ),
        "panel_C": place_axes_on_grid(figure, xspan=[0.05, 0.4], yspan=[0.57, 1]),
        "panel_D": place_axes_on_grid(figure, xspan=[0.5, 1], yspan=[0.57, 1]),
    }

    # Verify all panels exist
    assert all(key in ax for key in ["panel_A", "panel_B", "panel_C", "panel_D"])

    # Verify panel_B is a 3x1 grid
    assert len(ax["panel_B"]) == 3

    # Add example labels
    labels = [
        {
            "label_text": "A",
            "xpos": 0,
            "ypos": 0.05,
            "fontsize": 20,
            "weight": "bold",
            "ha": "right",
            "va": "bottom",
        },
        {
            "label_text": "B",
            "xpos": 0.37,
            "ypos": 0.05,
            "fontsize": 20,
            "weight": "bold",
            "ha": "right",
            "va": "bottom",
        },
        {
            "label_text": "C",
            "xpos": 0,
            "ypos": 0.55,
            "fontsize": 20,
            "weight": "bold",
            "ha": "right",
            "va": "bottom",
        },
        {
            "label_text": "D",
            "xpos": 0.45,
            "ypos": 0.55,
            "fontsize": 20,
            "weight": "bold",
            "ha": "right",
            "va": "bottom",
        },
    ]
    add_labels(figure, labels)


def test_single_axis(figure):
    """Test creating a single axis."""
    ax = place_axes_on_grid(figure)
    assert isinstance(ax, plt.Axes)


def test_multi_axis_grid(figure):
    """Test creating a multi-axis grid."""
    axes = place_axes_on_grid(figure, dim=[2, 2])
    assert len(axes) == 2
    assert len(axes[0]) == 2


def test_axis_positioning(figure):
    """Test custom axis positioning."""
    ax = place_axes_on_grid(figure, dim=[1, 1], xspan=[0.2, 0.8], yspan=[0.2, 0.8])
    bbox = ax.get_position()
    # Allow for some margin adjustment while ensuring the axis is roughly where expected
    assert 0.2 < bbox.x0 < 0.3  # Axis starts in the first third
    assert 0.7 < bbox.x1 < 0.8  # Axis ends in the last third
    assert 0.2 < bbox.y0 < 0.3  # Similar bounds for y-axis


def test_single_label(figure):
    """Test adding a single label."""
    label_text = "Test Label"
    add_label(figure, label_text, 0.5, 0.5, fontsize=12)
    all_texts = []
    for ax in figure.axes:
        all_texts.extend(ax.texts)
    assert any(text.get_text() == label_text for text in all_texts)


def test_multiple_labels(figure):
    """Test adding multiple labels."""
    labels = [
        {"label_text": "A", "xpos": 0.1, "ypos": 0.1, "fontsize": 12},
        {"label_text": "B", "xpos": 0.9, "ypos": 0.1, "fontsize": 12},
    ]
    add_labels(figure, labels)
    all_texts = []
    for ax in figure.axes:
        all_texts.extend(ax.texts)
    assert any(text.get_text() == "A" for text in all_texts)
    assert any(text.get_text() == "B" for text in all_texts)


def test_scalebar_creation(figure):
    """Test adding a scalebar to an axis."""
    ax = place_axes_on_grid(figure)
    scalebar(
        ax,
        x_pos=0.5,
        y_pos=0.5,
        x_length=1.0,
        y_length=1.0,
        x_text="1 unit",
        y_text="1 unit",
    )
    assert len(ax.lines) > 0  # Has at least one line
    assert len(ax.texts) > 0  # Has at least one text element


def test_example_heatmap(figure):
    """Test the heatmap example figure."""
    ax = place_axes_on_grid(figure)
    heatmap(ax)
    # Check that image was added
    assert len(ax.images) == 1
    # Check that scalebar was added
    assert len(ax.lines) > 0
    assert len(ax.texts) > 0


def test_example_sinusoids(figure):
    """Test the sinusoids example figure."""
    axes = place_axes_on_grid(figure, dim=[3, 1])
    sinusoids(axes)
    # Check that each subplot has the sinusoid
    for ax in axes:
        assert len(ax.lines) > 0  # At least one line exists
    # Check that scalebar was added to bottom plot
    assert len(axes[2].texts) > 0


def test_example_violins(figure):
    """Test the violin plot example figure."""
    ax = place_axes_on_grid(figure)
    violins(ax)
    # Check that violin plot elements exist
    assert len(ax.collections) > 0  # Violin shapes and points


def test_example_scatterplot(figure):
    """Test the scatter plot example figure."""
    ax = place_axes_on_grid(figure)
    scatterplot(ax)
    # Check that plot elements exist
    assert len(ax.collections) > 0  # Scatter points and contours
