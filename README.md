
<p align="center">
    <img src="https://raw.githubusercontent.com/HuaxinLab/briefing-generator/master/images/icon.png" 
    alt="Logo" width="128" height="128" style="max-width: 100%;">
</p>
<h1 align="center">Briefing Generator</h1>
<p align="center">简报生成器: 一个生成简报的工具</p>
<p align="center">
    <a href="https://acusp.info">
        <img src="https://badgen.net/badge/author/acusp/blue" alt="author">
    </a>
    <a href="https://github.com/scrapy/scrapy">
        <img src="https://badgen.net/badge/Scrapy/1.6.0/blue" alt="scrapy">
    </a>
    <a href="https://github.com/tornadoweb/tornado">
        <img src="https://badgen.net/badge/Tornado/6.0.2/blue" alt="tornado">
    </a>
    <a href="#">
        <img src="https://badgen.net/badge/%F0%9F%9A%80/open-in-browser/blue" alt="Live Demo">
    </a>
    <a href="LICENSE">
        <img src="https://badgen.net/github/license/HuaxinLab/briefing-generator" alt="MIT">
    </a>
</p>

## 介绍

一个自动生成简报的工具，可自动抓取并分类整理信息，最终按天提供简报内容。


目标用户每天会手动整理简报信息并发布至其它社交媒体。「简报生成器」这个产品可以替代用户手动整理信息的繁琐步骤，帮助用户快速生成简报，提高工作效率。


如果你对这个产品感兴趣，可以查看这个产品的设计历程系列文章：[《一个项目带你走进产品经理的世界》](http://www.woshipm.com/pmd/2182811.html)


## 功能列表

**支持的信息源**

- [x] [Next](http://next.36kr.com/posts?sort=hot)

- [x] [知晓程序](https://minapp.com/miniapp/)

- [ ] Readhub


**产品形态**

- [x] Web

- [ ] 小程序


**Web 界面功能列表**

- [x] 按用户设置在界面展示生成后的简报

- [ ] 一键复制

- [ ] 选择简报样式

- [ ] 简报历史

- [ ] 订阅简报（定时发送每日简报）


## 部署

```
pip install -r requirements.txt
```