from util.Animations import LineGraph
from util.DataCollection import DataCollection
import numpy as np

def main():
    #DataCol = DataCollection().from_txt_file('testTxt.txt')
    #data = DataCol.remove_dublicates(4)
    data = [np.sin(2 * np.pi * (1 - 0.01 * i)) for i in range(300)]
    
    graph = LineGraph(y_range=data)
    graph.set_plot_style('seaborn-darkgrid').set_figsize((17,8))
    graph.set_x_label('x axis').set_y_label('y axis')
    
    graph.run()
    
if __name__ == '__main__':
    main()
