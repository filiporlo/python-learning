import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

x, y = np.loadtxt('transistor.csv', delimiter=',', unpack=True)

y = 20*np.log10(y)

max = np.mean(y[18:22])

pasmo = max - 3

f = interp1d(x,y)
xnew = np.linspace(30,15000000, num = 3000000, endpoint=True)

idx = np.argwhere(np.diff(np.sign(np.full(np.shape(xnew), pasmo) - f(xnew))))

print("f_gorna=" + str(float(xnew[idx][0])) + " Hz")
print("f_dolna=" + str(float(xnew[idx][1] / 10 **6)) + " MHz")

#plt.plot(x,y, color='green')
plt.plot(xnew, f(xnew))
plt.plot(xnew[idx], f(xnew)[idx], 'ro')
plt.axhline(y=max, color='grey', linestyle='-.')
plt.axhline(y=pasmo, color='red', linestyle='-.')
plt.axvline(x=(xnew[idx])[0], color='red', linestyle='-.')
plt.axvline(x=(xnew[idx])[1], color='red', linestyle='-.')



plt.xlabel('f[Hz]')
plt.xscale('log')
plt.ylabel('Ku[dB]')
plt.title('Pasmo przenoszenia WE\n' + "f_g=" + str(float(np.round(xnew[idx][1] / 10 **6, decimals=1))) + " MHz\n" + "f_d=" + str(float(np.round(xnew[idx][0], decimals=1))) + " Hz")
#plt.legend()
plt.show()
