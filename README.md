# Hawaii Weather Analysis

## Purpose
Manipulate Python dataframes, containing weather data, to determine if O'ahu is a good location to open a surf shop.
- Use SQLalchemy with pandas to query data from a SQLite database
- Use Flask to showcase results

## Differences between June and December Weather
Temperature: 
On average June is warmer than December, but the difference is less than it would be at latitudes further from the equator.
- The average temperature is higher in June (74.9F) than in December (71.0F) by 3.9F.
- The minimum temperature is lower in December (56.0F) than in June (64.0F).
- The maximum temperature is higher in June (85.0) than in December (83.0F).

Precipitation:
On average it rains more in December than in June, but only by 0.08in.
- The average precipitation is higher in December (0.22in) than in June (0.14in) by 0.08in.
- The maximum precipitation is higher in December (6.42in) than in June (4.43in) by 1.99in.

## Reccomendations for Further Analysis
- O'ahu is a large island with several coastal towns and mountainous regions. Weather stations from the mountains are likley skewing our data. It would be better to only use data from the nearest weather stations.

- It would be good to gather data on where the tourists live. Tourist are more likely to rent surf boards, so we want to place our shop near them.

- It would be good to gather data on where the best places to surf are. This way we can place our shop near the best waves.

- We should gather data on how good our customers will be at surfing, are they beginners/professionals? This would allow us to better decide where to place our shop. We wouldn't want beginners tackling 30ft waves.

## O'ahu June Weather Analysis
![June Stats and Histograms](https://github.com/Calistic/surfs_up/blob/master/Pictures/June1.PNG)
![December Box Plot](https://github.com/Calistic/surfs_up/blob/master/Pictures/June2.PNG)

## O'ahu December Weather Analysis
![December Stats and Histograms](https://github.com/Calistic/surfs_up/blob/master/Pictures/December1.PNG)
![December Box Plot](https://github.com/Calistic/surfs_up/blob/master/Pictures/December2.PNG)


