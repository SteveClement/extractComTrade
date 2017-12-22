#!/usr/bin/env python3

import json
from pprint import pprint

SITC1c="7317 7326 7327 7328 73292 73312 7197 7333 73492 7199 8121 8123 7191 7222 723 7192 7231 722 7232 7111 7112 7113 7115 7116 7117 7291 7293 7294 7118 7193 95103 95106 7311 7312 7313 7314 7315 7316 7321 7322 7323 7324 7325 7195 7196 73291 73311 7198 7334 7341 73491 7351 7353 7358 7359 695 696 6981 6982 7221 7143 7149 715 717 718 8213 7142 724 7241 7242 7249 72501 72502 7114 7194 72503 72504 72505 726 7292 7297 7295 7296 7299 7121 7122 7123 7125 7129 7141 81242 81243 861 864 8911 8914 8918 8919 894 8951 95101 95102 95104 95105 9610 89999"

countries="Austria,Belgium,Belgium-Luxembourg,Bulgaria,Cyprus,Czechoslovakia,Czech Republic,Slovakia,Denmark,Estonia,Finland,France,Germany,Greece,Hungary,Ireland,Italy,Latvia,Lithuania,Luxembourg,Malta,Netherlands,Poland,Portugal,Romania,Slovenia,Spain,Sweden,United Kingdom"

# https://comtrade.un.org/data/cache/reporterAreas.json
# https://comtrade.un.org/data/cache/partnerAreas.json

reporterAreas = json.load(open('reporterAreas.json'))
partnerAreas = json.load(open('partnerAreas.json'))

def countryToComtrade(country):
    for res in reporterAreas["results"]:
        if country in res["text"]:
            print("The corresponding code to {} is {}".format(country, res['id']))

##pprint(partnerAreas)
##pprint(reporterAreas)

for country in countries.split(','):
    countryToComtrade(country)
