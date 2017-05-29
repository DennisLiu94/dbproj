import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

def draw(x,y,name):
	plt.plot(y)
	plt.savefig('{}.png'.format(name))
