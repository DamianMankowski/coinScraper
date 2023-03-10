import argparse
from typing import List
import os
from selenium import webdriver
import pandas as pd
from CoinSites.tavex import tavex_main
from CoinSites.chojnackikwiecien import chojnackikwiecien_main
from CoinSites.flyingatom import flyingatom_main
from CoinSites.goldenmark import goldenmark_main
from CoinSites.goldon import goldon_main
from CoinSites.guldener import guldener_main
from CoinSites.mennica_gdanska import mennica_gdanska_main
from CoinSites.mennica_mazovia import mennica_mazovia_main
import datetime



def main():

    df_tavex = tavex_main()

    df_chojnackikwiecien = chojnackikwiecien_main()

    df_flyingatom = flyingatom_main()

    df_goldenmark = goldenmark_main()

    df_goldon = goldon_main()

    df_guldener = guldener_main()

    df_mennica_gdanska = mennica_gdanska_main()

    df_mennica_mazovia = mennica_mazovia_main()

    frames=[df_tavex, df_chojnackikwiecien, df_flyingatom, df_goldenmark, df_goldon,  df_guldener, df_mennica_gdanska, df_mennica_mazovia]

    result = pd.concat(frames)
    print(result)
    return result

if __name__ == '__main__':
    dane = main()
    now = datetime.datetime.utcnow()
    year_month_day_format = '%Y-%m-%d'
    today = now.strftime(year_month_day_format)
    dane.to_csv(f'Silver_coins_{today}.csv', index=False)