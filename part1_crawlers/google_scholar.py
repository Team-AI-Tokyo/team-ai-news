######## Google Scholar 

import scholarly

search_query_2 = scholarly.search_keyword('thermodynamics')
keyword = next(search_query_2).fill()
title2 = [pub.bib['title'] for pub in keyword.publications]


title3 = [pub for pub in keyword.publications]




################################################################################

import gscholar

gscholar.query("thermodynamics")

