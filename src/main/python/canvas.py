from typing import List

import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QVBoxLayout, QWidget

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

        # list of colors to be used when plotting (5 colors x 3 different linestyles)
        colors = [
            "#648FFF",
            "#785EF0",
            "#DC267F",
            "#FE6100",
            "#FFB000",
        ]
        colors = colors + colors + colors

        # linestyle to be applied to the supplied distributions
        line_styles = [
            "-",
            "-",
            "-",
            "-",
            "-",
            ":",
            ":",
            ":",
            ":",
            ":",
            "--",
            "--",
            "--",
            "--",
            "--",
        ]

        # Array containing all the lines plotted on the graph
        lines = []

        # set the Axes
        axes = self.canvas.axes

        # If the "new" flag is set to true clear the graph before drawing
        if new == True:
            axes.cla()

        # Draw a line for every distribution passed to the function
        # Store the line object into lines list
        for i, label in enumerate(labels):
            (line,) = axes.plot(
                x[i], y[i], ls=line_styles[i], color=colors[i], label=label
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
