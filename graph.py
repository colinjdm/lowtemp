from bokeh.io import curdoc
from bokeh.plotting import figure, show


def line_graph(x, y):
    # x = [1,2,3,4,5,6]
    # y = [65, 68, 72, 60, 63, 65]

    p = figure(title="Example", x_axis_label = 'x', y_axis_label = 'y')

    p.line(x, y, legend_label = "Temp.", line_width = 2)

    show(p)


if __name__ == "__main__":
    line_graph()