# coding: UTF-8
import settings
import common

import requests
import bs4
import re
import datetime

from wordcloud import WordCloud

collection_uri = common.get_collection_uri(settings.HATENA_ID, settings.BLOG_ID, settings.API_KEY)
pub_entry_list = common.get_published_entry_list(collection_uri, settings.HATENA_ID, settings.API_KEY)

dt_now = datetime.datetime.now()
category_list = []

for i in pub_entry_list:
    for e in i:
        # 公開日が今年のものだけ取得
        published=common.get_jst_time(e.published.text)
        if published.year!=dt_now.year:
            continue
        for t in e.find_all('category'):
            category_name=t.get('term')
            categories={category_name} - {None}
            # 勉強会と読書はほとんどどちらかを設定するので除外する
            if not '勉強会' in category_name and not '読書' in category_name:
                category_list.append(category_name)

# TODO:フォントのあるパスを指定する
wordcloud = WordCloud(background_color="white",
    font_path="/System/Library/Fonts/ヒラギノ角ゴシック W0.ttc",
    width=800,height=600,collocations = False).generate(' '.join(category_list))

wordcloud.to_file("./wordcloud_hatena_blog.png")

