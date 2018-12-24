# coding: UTF-8
import settings
import common

import requests
import bs4
import re
import time
import datetime
import dateutil.parser

collection_uri = common.get_collection_uri(settings.HATENA_ID, settings.BLOG_ID, settings.API_KEY)
pub_entry_list = common.get_published_entry_list(collection_uri, settings.HATENA_ID, settings.API_KEY)

dt_now = datetime.datetime.now()
entry_count = 0

for i in pub_entry_list:
    for e in i:
        # 公開日が今年のものだけ取得
        published=dateutil.parser.parse(e.published.text) + datetime.timedelta(hours=9)
        if published.year!=dt_now.year:
            continue
        entry_count+=1
        entry_id=e.id.string
        title=e.title.string
        print("%s,%s,%s" % (entry_id,title,published.strftime("%Y/%m/%d")))


