#!/bin/bash

export PATH=$PATH:/usr/local/bin
cd ~/briefing-generator/BgSpider
nohup python3 main.py > ~/log/bgSpider.log 2>&1 &