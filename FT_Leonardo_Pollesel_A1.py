import numpy as np
import matplotlib.pyplot as plt


def function():
    x = np.arange(0, 2*np.pi, 0.01)
    y = np.sin(x)
    z = np.cos(x)
    plt.plot(x, y, x, z)
    plt.title('One period of cos and sin')
    plt.legend(['sin(x)', 'cos(x)'])
    retunr plt.show()

if __name__ == '__main__':
    function()
