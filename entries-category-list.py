# coding: UTF-8
import settings
import common

import requests
import bs4
import re
import datetime

collection_uri = common.get_collection_uri(settings.HATENA_ID, settings.BLOG_ID, settings.API_KEY)
pub_entry_list = common.get_published_entry_list(collection_uri, settings.HATENA_ID, settings.API_KEY)

dt_now = datetime.datetime.now()
category = {}

print("category,count")

for i in pub_entry_list:
    for e in i:
        # 公開日が今年のものだけ取得
        published=common.get_jst_time(e.published.text)
        if published.year!=dt_now.year:
            continue
        for t in e.find_all('category'):
            category_name=t.get('term')
            categories={category_name} - {None}
            if category_name not in category:
                category[category_name]=0
            category[category_name]+=1

# カテゴリーごとの集計
for c in category:
    print("%s,%d" % (c, category[c]))


