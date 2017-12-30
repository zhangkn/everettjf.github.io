---
layout: post
title: "AppleTrace dance with MonkeyDev"
excerpt: tracing any apps
categories:
  - Tool
tags:
  - Tool
comments: true
---



(关联文章：http://everettjf.com/2017/09/21/appletrace/ )

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
    source 'https://github.com/AloneMonkey/MonkeyDevSpecs.git'
    use_frameworks!
    target 'WeChatAppleTraceDylib' do
         pod 'AppleTrace'
    end
    ```
3. 把第三方App的ipa放入 MonkeyDev指定的Target目录中。
4. 运行
5. 从沙盒 Library目录中复制出 appletracedata目录
6. 按照 https://github.com/everettjf/AppleTrace README中的步骤可生成 trace.html

# 结果

https://github.com/everettjf/Yolo/raw/master/WeChatAppleTrace/Result/WeChatStartup.zip

解压上面的zip文件，打开trace.html，按快捷键 w a s d 可缩放移动，就像在玩 CS，是吧。

