times = pd.DataFrame(full_data, index=range(len(full_data), 0, -1))
times['Time'] = pd.to_datetime(list(times['Time']))
times = times.sort_values(by='Time')
times
right = times['Time'][1] + pd.Timedelta(30, unit='m')
mask_main = (times['Time'] < right)

mask_neg = mask_main & (times['Assessment'] > 0)

times.loc[mask_neg]