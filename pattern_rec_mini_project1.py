import wfdb
import numpy as np
import matplotlib.pyplot as plt
record = wfdb.rdrecord('100')
print(record.p_signal.shape)
plt.plot(record.p_signal[: 1000 , 0])
plt.title('EGG Signal')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.show()

