#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 15:50:33 2017

@author: mdubey
"""

from urllib.request import urlopen
from link_finder import LinkFinder
from domain import *
from general import *

class Spider:
    
    # Class variables (shared among all instances)
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue_set = set()
    crawled_set = set()
    
    def __init__(self, project_name, base_url, domain_name):
        super().__init__()
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('First spider', Spider.base_url)

    # Creates directory and files for project on first run and starts the spider
    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue_set = file_to_set(Spider.queue_file)
        Spider.crawled_set = file_to_set(Spider.crawled_file)
    
    # Updates user display, fills queue and updates files
    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled_set:
            print(thread_name + ' now crawling ' + page_url)
            print('Queue ' + str(len(Spider.queue_set)) + ' | Crawled  ' + str(len(Spider.crawled_set)))
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue_set.remove(page_url)
            Spider.crawled_set.add(page_url)
            Spider.update_files()

    # Converts raw response data into readable information and checks for proper html formatting
    @staticmethod
    def gather_links(page_url):
        try:
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(CustomConnection.URL(page_url))
        except:
            return set()
        return finder.page_links()
    
    # Saves queue data to project files
    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if (url in Spider.queue_set) or (url in Spider.crawled_set):
                continue
            if Spider.domain_name != get_domain_name(url):
                continue
            Spider.queue_set.add(url)
    
    @staticmethod
    def update_files():
        set_to_file(Spider.queue_set, Spider.queue_file)
        set_to_file(Spider.crawled_set, Spider.crawled_file)