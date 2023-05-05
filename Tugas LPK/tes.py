from chempy import Reaction
from chempy.kinetics.ode import get_odesys
import numpy as np
import matplotlib.pyplot as plt

# Mendefinisikan reaksi kimia
reaction = Reaction.from_string('A + B -> C', k=1.23)

# Mendefinisikan kondisi awal
c0 = {'A': 1.0, 'B': 2.0, 'C': 0.0}

# Mendefinisikan waktu
t = np.linspace(0, 10, 100)

# Mendapatkan sistem persamaan diferensial
odesys, extra = get_odesys(reaction, c0)

# Menyelesaikan persamaan diferensial
c, info = odesys.integrate(t, c0, atol=1e-12, rtol=1e-12)

# Membuat plot kecepatan reaksi
plt.plot(t, -reaction.rate(c) / reaction.stoichiometry[0])
plt.xlabel('Waktu')
plt.ylabel('Kecepatan reaksi')
plt.show()
