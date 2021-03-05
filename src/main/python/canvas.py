import itertools
from typing import List

import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QSizePolicy

matplotlib.use("Qt5Agg")


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi, tight_layout=True)
        super(MplCanvas, self).__init__(fig)
        self.axes = fig.add_subplot(111)


class WidgetPlot(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.setLayout(QVBoxLayout())
        self.canvas = MplCanvas(self)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.layout().addWidget(self.toolbar)
        self.layout().addWidget(self.canvas)

        # Code to keep the graph aspect ratio square
        self.ratio = 1
        self.adjusted_to_size = (-1, -1)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored))

    def resizeEvent(self, event):
        size = event.size()
        if size == self.adjusted_to_size:
            # Avoid infinite recursion.
            return
        self.adjusted_to_size = size

        full_width = size.width()
        full_height = size.height()
        width = min(full_width, full_height * self.ratio)
        height = min(full_height, full_width / self.ratio)

        h_margin = round((full_width - width) / 2)
        v_margin = round((full_height - height) / 2)

        self.setContentsMargins(h_margin, v_margin, h_margin, v_margin)

    def plot(
        self,
        x: List,
        y: List,
        labels: List[str],
        xlabel: str,
        ylabel: str,
        title: str,
        new=False,
    ):
        """
        Plots new data into the widget deleting any previous plot
        """

        def onpick(event):
            """
            Handles show/hide events when clicking on the corresponding line in the legend
            """
            # on the pick event, find the orig line corresponding to the
            # legend proxy line, and toggle the visibility
            legline = event.artist
            origline = lined[legline]
            vis = not origline.get_visible()
            origline.set_visible(vis)
            # Change the alpha on the line in the legend so we can see what lines
            # have been toggled
            if vis:
                legline.set_alpha(1.0)
            else:
                legline.set_alpha(0.2)
            self.canvas.draw()

        # list of colors to be used when plotting
        colormap = matplotlib.cm.Dark2.colors

        # linestyles to be applied to the supplied distributions
        l_styles = [
            "-",
            "--",
            ":",
            "-.",
        ]

        # markers to be applied
        m_styles = ["", ".", "o", "^", "*"]

        # Array containing all the lines plotted on the graph
        lines = []

        # set the Axes
        axes = self.canvas.axes

        # If the "new" flag is set to true clear the graph before drawing
        if new == True:
            axes.cla()

        # Draw a line for every distribution passed to the function
        # Store the line object into lines list
        for (i, label), (marker, linestyle, color) in zip(
            enumerate(labels), itertools.product(m_styles, l_styles, colormap)
        ):
            (line,) = axes.plot(
                x[i], y[i], label=label, color=color, ls=linestyle, marker=marker
            )
            lines.append(line)
        # Set labels, titles and draw legend
        axes.set_ylabel(ylabel)
        axes.set_xlabel(xlabel)
        axes.set_title(title)
        leg = axes.legend()

        # take note of corresponding lines in the plot and in the legend
        lined = dict()
        for legline, origline in zip(leg.get_lines(), lines):
            legline.set_picker(5)  # 5 pts tolerance
            lined[legline] = origline

        # Onclick hide/show line
        self.canvas.mpl_connect("pick_event", onpick)
        self.canvas.draw()
