id = 'IAD'
location = 'Dulles Intl Airport'
max_temp = 32
min_temp = 13
precipitation = 0.4

print(f'{id:<5s} : {location:19s} : {max_temp:^9d} / {min_temp:3d} /'
      f' {precipitation:<6.3f}')

value = 2 ** 12 - 1
print(f'{value=} {2**7+1=}')

data = dict(
    id=id, location=location, max_temp=max_temp,
    min_temp=min_temp, precipitation=precipitation
)

# using format_map
s = '{id:<5s} : {location:19s} : {max_temp:^9d} / {min_temp:3d} / {precipitation:6.2f}'.format_map(data)
print(s)
