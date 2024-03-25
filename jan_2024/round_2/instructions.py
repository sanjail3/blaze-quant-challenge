"""
For round 2, you have to predict ETH price in USD between Feb 4th and Feb 10th 2024 (inclusive).
Each team will have to make 7 predictions; one for each day. The prediction has to be
within a range. Each range is inclusive of the lower bound and exclusive of the higher bound.
E.g. pr_2000_2025 is [2000, 2025).

Note: the price ranges might be updated closer to Feb 4th.
Please copy the example to add your predictions.
We will call the predictions function on Feb 4th 12:00 AM PST. After that, the predictions
will not be altered. 

We will take the closing price on the day as the correct price. The source for the closing
price will be https://coinmarketcap.com/currencies/ethereum/. Coin market cap provides
prices at 5 min intervals. We will take the price at 11:55 pm PST as the closing price.
"""
from enum import Enum


class ETHPriceRanges(Enum):
    pr_2000_2025 = 1
    pr_2025_2050 = 2
    pr_2050_2075 = 3
    pr_2075_2100 = 4
    pr_2100_2125 = 5
    pr_2125_2150 = 6
    pr_2150_2175 = 7
    pr_2175_2200 = 8
    pr_2200_2225 = 9
    pr_2225_2250 = 10
    pr_2250_2275 = 11
    pr_2275_2300 = 12
    pr_2300_2325 = 13
    pr_2325_2350 = 14
    pr_2350_2375 = 15
    pr_2375_2400 = 16
    pr_2400_2425 = 17
    pr_2425_2450 = 18
    pr_2450_2475 = 19
    pr_2475_2500 = 20
    pr_2500_2525 = 21
    pr_2525_2550 = 22
    pr_2550_2575 = 23
    pr_2575_2600 = 24
