#!/bin/sh
scrapy crawl armatura -o armatura.csv -L WARNING
scrapy crawl cold_list -o cold_list.csv -L WARNING
scrapy crawl hot_list -o hot_list.csv -L WARNING
scrapy crawl pipe -o pipe.csv -L WARNING
scrapy crawl angles -o angles.csv -L WARNING
scrapy crawl balka -o balka.csv -L WARNING
scrapy crawl rails -o rails.csv -L WARNING
scrapy crawl shvellers -o shvellers.csv -L WARNING

