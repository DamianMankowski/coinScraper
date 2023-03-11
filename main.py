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
from CoinSites.mennicaskarbowa import mennicaskarbowa_main
from CoinSites.metalmarket import metalmarket_main
from CoinSites.srebnamennica import srebnamennica_main
from CoinSites.szlachetneinwestycje import szlachetneinwestycje_main

from CoinSites.element79 import element79_main
from CoinSites.spotprice import spotprice_main
from CoinSites.numizmatyczny import numizmatyczny_main



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

    df_mennicaskarbowa = mennicaskarbowa_main()

    df_metalmarket = metalmarket_main()

    df_srebnamennica = srebnamennica_main()

    df_szlachetneinwestycje = szlachetneinwestycje_main()

    df_element79 = element79_main()

    df_spotprice = spotprice_main()

    df_numizmatyczny = numizmatyczny_main()

    frames=[df_tavex, df_chojnackikwiecien, df_flyingatom, df_goldenmark, df_goldon,  df_guldener, df_mennica_gdanska,
            df_mennica_mazovia, df_mennicaskarbowa, df_metalmarket, df_srebnamennica, df_szlachetneinwestycje,
            df_element79, df_spotprice, df_numizmatyczny]

    result = pd.concat(frames)
    print(result)
    return result

if __name__ == '__main__':
    dane = main()
    now = datetime.datetime.utcnow()
    year_month_day_format = '%Y-%m-%d'
    today = now.strftime(year_month_day_format)
    dane.to_csv(f'Silver_coins_{today}.csv', index=False)