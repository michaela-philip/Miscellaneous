import pandas as pd
import numpy as np

#let's read in the data

county_vars = pd.read_stata("C:/EITC Replication/Replication/Data/county_vars.dta")

eitc = pd.read_stata("C:/EITC Replication/Replication/Data/eitc.dta")

ruralcounty_vars = pd.read_stata("C:/EITC Replication/Replication/Data/ruralcounty_vars.dta")

#creating eitc categories
eitc['eitc'] = np.where(eitc['eitc_pct'] > 0, 1, 0)

eitc['eitcp'] = np.where(eitc['eitc_pct'] > 0, eitc['eitc_pct'], np.nan)

eitc['refund'] = np.where((eitc['eitc'] == 1) & (eitc['refund'] == 1), 1, np.where((eitc['eitc'] == 1) & (eitc['refund'] == 0), 0, np.nan))