from wds_astropy_table import parse_wdsweb

from astropy.io import ascii

import numpy as np
import sys

table = parse_wdsweb('wdsweb_summ2.txt')

last_date = table['last_date']
first_date = table['first_date']
last_sep = table['last_sep']
pri_mag = table['pri_mag']
sec_mag = table['sec_mag']
num_obs = table['num_obs']

delta_mag = np.abs(sec_mag-pri_mag)

neglected = (last_date < 2020) & (first_date < last_date)

observable = (last_sep>=5) & (delta_mag <=2) & (sec_mag <= 12)

orbital = num_obs>10

filtered = table[ observable ]# & orbital]

# For Enhanced Character-Separated Values (ECSV), which preserves metadata like units and data types:
# ECSV is recommended for reproducible text versions of your table.
ascii.write(filtered, sys.stdout, format='csv', overwrite=True)