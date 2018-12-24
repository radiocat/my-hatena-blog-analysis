# coding: UTF-8
import requests
import bs4
import time

def get_collection_uri(hatena_id, blog_id, password):
    service_doc_uri = "https://blog.hatena.ne.jp/{hatena_id:}/{blog_id:}/atom".format(hatena_id=hatena_id, blog_id=blog_id)
    res_service_doc = requests.get(url=service_doc_uri, auth=(hatena_id, password))
    if res_service_doc.ok:
        soup_servicedoc_xml = bs4.BeautifulSoup(res_service_doc.content, features="xml")
        collection_uri = soup_servicedoc_xml.collection.get("href")
        return collection_uri

    return False

def get_published_entry_list(collection_uri, hatena_id, password):
    MAX_ITERATER_NUM = 50
    pub_entry_list = []
    for i in range(MAX_ITERATER_NUM):
        #print(collection_uri)
        # Basic認証で記事一覧を取得
        res_collection = requests.get(collection_uri, auth=(hatena_id, password))
        if not res_collection.ok:
            print("faild")
            continue
        # Beatifulsoup4でDOM化
        soup_collectino_xml = bs4.BeautifulSoup(res_collection.content, features="xml")
        # entry elementのlistを取得
        entries = soup_collectino_xml.find_all("entry")
        # 下書きを無視
        pub_entry_list.append(list(filter(lambda e: e.find("app:draft").string != "yes", entries)))
    
        # next
        link_next = soup_collectino_xml.find("link", rel="next")
        if not link_next:
            break
        collection_uri = link_next.get("href")
        if not collection_uri:
            break
        time.sleep(0.01)# 10ms

    return pub_entry_list
