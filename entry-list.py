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
entry_count = 0

for i in pub_entry_list:
    for e in i:
        # 公開日が今年のものだけ取得
        published=common.get_jst_time(e.published.text)
        if published.year!=dt_now.year:
            continue
        entry_count+=1
        entry_id=re.search(r"-(\d+)$", string=e.id.string).group(1)
        title=e.title.string
        categories={t.get('term') for t in e.find_all('category')} - {None}
        # 勉強会=1、読書=2、それ以外=0にタイプ分け
        category_type=0
        if '勉強会' in categories:
            category_type=1
        elif '読書' in categories:
            category_type=2

        print("%s,%s,%s,%s" % (entry_id,title,published.strftime("%Y/%m/%d"),category_type))

# 今年のエントリー数
print("------------------------------------")
print("total entries = %d" % entry_count)
