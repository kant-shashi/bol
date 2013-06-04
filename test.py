#!/usr/bin/env python

from couchbase import Couchbase
from pprint import pprint

cb=Couchbase.connect(bucket="beer-sample")
result = cb.get('new_holland_brewing_company-sundog')

pprint(result.value,indent=4)

new_beer = {
    'name': 'Old yankee ale',
    'abv':5.00,
    'srm':0,
    'upc':0,
    'type':'beer',
    'brewery_id':'cottrell_brewing_co',
    'updated':'2012-08-o30',
    'description':'.A medium_bodied Amber Ale',
    'style':'American-Style Amber',
    'category':'North American Ale'
}


key = '{0}-{1}'.format(
    new_beer['brewery_id'],
    new_beer['name'].replace(' ','_').lower()
)

result = cb.set(key,new_beer)
print result

# cb.delete(key)














