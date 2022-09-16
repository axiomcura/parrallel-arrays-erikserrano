import matplotlib.pyplot as plt

def make_box_plot(data, output_file):
  fig, ax = plt.subplots()
  ax.boxplot(data)
  fig.savefig(output_file)
