#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 17:10:21 2017

@author: mdubey
"""

# Set the working directory
import os
os.chdir('/Users/mdubey/Desktop/Crawler')

import threading
from queue import Queue
from spider_new import Spider
from domain import *
from general import *
from Library import Requirement_Manager

# This method gets all requirements from the user
# This file module was created because it takes up
# more lines to be in this main.py python module
Requirement_Manager.Initiate()

PROJECT_NAME = Requirement_Manager.getPath() + Requirement_Manager.getProjectName()
DOMAIN_NAME = get_domain_name(Requirement_Manager.getHomePage())
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = Requirement_Manager.getPath() + PROJECT_NAME + '/crawled.txt'
queue = Queue()
Spider(PROJECT_NAME, Requirement_Manager.getHomePage(), DOMAIN_NAME)

print(Requirement_Manager.getCores())
# Create worker threads (will die when main exits)
def create_workers():
    for _ in range(Requirement_Manager.getCores()):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

# Do the next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()

# Each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()

# Check if there are items in the queue, if so crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()

create_workers()
crawl()