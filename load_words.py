from IPython.display import display
import pandas
import sys

def load_data_from_csv(file):
    return pandas.read_csv(file, header=0)

if __name__ == '__main__':
    la = load_data_from_csv('./data/wordle-la.txt')
    ta = load_data_from_csv('./data/wordle-ta.txt')

    la.append(ta)
    display(la)

    la.to_csv(sys.stdout,index=True)