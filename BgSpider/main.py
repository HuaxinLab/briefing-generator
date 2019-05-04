#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

def main():
    setting = get_project_settings()
    process = CrawlerProcess(setting)
    didntWorkSpider = ['sample']

    for spider_name in process.spider_loader.list():
        if spider_name in didntWorkSpider :
            continue
        print("[+] Running spider %s" % (spider_name))
        process.crawl(spider_name)
    process.start()

if __name__ == "__main__":
    main()
