---
title: "AppleTrace dance with MonkeyDev"
excerpt: tracing any apps
categories:
  - Tool
tags:
  - Tool
comments: true
---

{% include toc %}

# 结果演示：

![appletrace](http://everettjf.github.io/stuff/appletrace/appletrace.gif)


# 环境：
arm64（仅在arm64环境下）

# 工具：

- MonkeyDev https://github.com/AloneMonkey/MonkeyDev
- AppleTrace https://github.com/everettjf/AppleTrace

# 步骤：

1. 首先使用MonkeyDev创建MonkeyApp
2. 新建Podfile

    ```
    #source 'https://github.com/AloneMonkey/MonkeyDevSpecs.git'
    source 'https://github.com/everettjf/MonkeyDevSpecs.git'
    use_frameworks!
    target 'WeChatAppleTraceDylib' do
         pod 'AppleTrace','1.0.1'
    end
    ```
3. 运行

# 结果

https://github.com/everettjf/Yolo/raw/master/WeChatAppleTrace/Result/WeChatStartup.zip

w a s d 就像在玩 CS，是吧。

