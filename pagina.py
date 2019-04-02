import urllib
from io import StringIO
from io import BytesIO
import csv
import numpy as np
from datetime import datetime
import matplotlib.pylab as plt
import pandas as pd
import scipy.signal as signal

datos_2008=pd.read_csv(https://hub.mybinder.org/user/computociencias-fisi2029-201910-zgf4osv2/edit/Seccion_1/Fourier/Datos/transacciones2008.txt)
datos_2009=pd.read_csv(https://hub.mybinder.org/user/computociencias-fisi2029-201910-zgf4osv2/edit/Seccion_1/Fourier/Datos/transacciones2009.txt)
datos_2010=pd.read_csv(https://hub.mybinder.org/user/computociencias-fisi2029-201910-zgf4osv2/edit/Seccion_1/Fourier/Datos/transacciones2010.txt)

plt.plot(datos_2008)
