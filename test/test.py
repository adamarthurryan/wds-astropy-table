last_date = table['last_date']
first_date = table['first_date']
last_sep = table['last_sep']
pri_mag = table['pri_mag']
sec_mag = table['sec_mag']
num_obs = table['num_obs']

delta_mag = np.abs(sec_mag-pri_mag)

neglected = (last_date < 2020) & (first_date < last_date)

observable = (last_sep>=5) & (delta_mag <=2) & (sec_mag <= 12)

orbital = num_obs>100

filtered = table[ observable & orbital]

# For Enhanced Character-Separated Values (ECSV), which preserves metadata like units and data types:
# ECSV is recommended for reproducible text versions of your table.
csv=filtered.write('wdsweb_filtered.csv', format='ascii.csv', overwrite=True)

print(csv)
