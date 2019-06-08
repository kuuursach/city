# import pandas as pd
# from pandas import DataFrame
# import matplotlib.pyplot as plt
#
#
# import matplotlib
# matplotlib.use("TkAgg")
#
# from matplotlib.backends.backend_tkagg import FigureCanvasAgg, NavigationToolbar2Tk
# from matplotlib.figure import Figure
#
#
# suffer = DataFrame()
# data_new = pd.read_csv('second.csv')
# data = pd.read_csv('one.csv')
#
# suffer = pd.merge(data, data_new, on='Key', how='left')
#
# Ass = DataFrame()
# Ass = suffer.drop_duplicates(subset=['Key'], keep='first')
#
# x = list(suffer.Town)
# y = list(suffer.Population)
#
# fig, ax = plt.subplots()
#
# ax.barh(x, y)
#
# ax.set_title('Гистограмма: Население городов России')
# ax.set_facecolor('seashell')
# ax.text(-700000, 33, 'Town',
#         rotation = 0,
#         fontsize = 10)
# ax.text(13500000, -3, 'Population',
#         rotation = 0,
#         fontsize = 10)
# fig.set_figwidth(12)    #  ширина Figure
# fig.set_figheight(6)    #  высота Figure
# fig.set_facecolor('floralwhite')
#
# f = Figure(fgsize=(5,5), dpi=100)
# a = f.add_subplot(111)
# a.plot(x, y)
#
# canvas = FigureCanvasAgg(f, self)
# canvas.show()
# canvas.get_tk_widget().pack(side=tk.TOP, fill = tk.BOTH, expand=True)
#
#
# plt.show()
# #plt.savefig('/Users/dashagaganova/Desktop/Plots.png', format='png')


import tkinter as tk
import matplotlib

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


def schart2(stock_sym):
    x = [1, 2, 3, 4]
    y = [20, 21, 20.5, 20.8]
    fig = Figure()
    axes = fig.add_subplot(111)
    axes.plot(x, y)
    return fig


class StockChart(tk.Frame):
    def __init__(self, stock_sym=''):
        tk.Frame.__init__(self, parent=None)
        self.pack(expand=tk.YES, fill=tk.BOTH)
        self.makeWidgets(stock_sym)

    def makeWidgets(self, stock_sym):
        # self.f = graphData(stock_sym,12,26)
        self.f = schart2(stock_sym)
        self.canvas = FigureCanvasTkAgg(self.f)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.canvas.show()


if __name__ == '__main__':
    StockChart('ACAD').mainloop()
