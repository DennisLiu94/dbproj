import matplotlib
matplotlib.use('Agg')
testx=[1,2,3,4]
testy=[1,2,3,4]

from matplotlib import pyplot as plt
plt.plot(testy)
plt.savefig('test.png')
