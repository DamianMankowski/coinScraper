import argparse
from typing import List
import os
from selenium import webdriver
import pandas as pd
from CoinSites.tavex import tavex_main
from CoinSites.chojnackikwiecien import chojnackikwiecien_main
from CoinSites.flyingatom import flyingatom_main
from CoinSites.goldenmark import goldenmark_main


def main():

    # df = pd.DataFrame(columns=['Nazwa', 'Sprzedaż', 'Kupno'])

    df_tavex = tavex_main()

    df_chojnackikwiecien = chojnackikwiecien_main()

    df_flyingatom = flyingatom_main()

    df_goldenmark = goldenmark_main()

    frames=[df_tavex, df_chojnackikwiecien, df_flyingatom, df_goldenmark]

    result = pd.concat(frames)
    print(result)

if __name__ == '__main__':
    dane = main()
    print(dane)