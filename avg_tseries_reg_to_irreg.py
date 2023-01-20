import pandas as pd


"""Average a regular time series to an irregular time base
    From my question on stackoverflow here
    https://stackoverflow.com/questions/75183869/resample-from-regular-to-irregular-time-series-in-pandas/75183913?noredirect=1#comment132672845_75183913
"""



import numpy as np
import pandas as pd
import datetime as dt

reg_data = pd.Series(
    np.arange(25),
    index=pd.date_range(start='2018-01-01', end='2018-01-02', freq='H')
    )
new_start_times = [
    dt.datetime(2018,1,1,2,5,12),
    dt.datetime(2018,1,1,6,0,0),
    dt.datetime(2018,1,1,12,7,58)
    ]
new_end_times = [
    dt.datetime(2018,1,1,3,7,28),
    dt.datetime(2018,1,1,7,0,0),
    dt.datetime(2018,1,1,19,55,22)
    ]

#If you want you can also round the new_start_times and new_end_times to the nearest hour
irreg_data = [reg_data.loc[start.round('H'):end.round('H')].mean() 
     for start, end in zip(pd.to_datetime(new_start_times), pd.to_datetime(new_end_times))]