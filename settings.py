# coding: UTF-8
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

HATENA_ID = os.environ.get("HATENA_ID") 
BLOG_ID = os.environ.get("BLOG_ID")
API_KEY = os.environ.get("API_KEY")
