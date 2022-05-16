from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure 
fig = Figure()
canvas = FigureCanvas(fig)

import numpy as np
x = np.random.randn(10000)


ax = fig.add_subplot(111)

ax.hist(x,100)
ax.set_title("Normal distribution")
fig.savefig("test.png")
fig.show()
