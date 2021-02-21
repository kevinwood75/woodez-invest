import yahoo_fin.options as ops

expiration_dates = ops.get_expiration_dates("sq")
print(expiration_dates)

ops_data = ops.get_options_chain("sq", "02/26/2021")

print(ops_data)
