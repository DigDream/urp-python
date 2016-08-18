##0x00    概述

本软件是urp教务系统客户端,有查看成绩,查看课表,查看学籍,一键评估等功能.

##0x01    安装与配置

克隆本项目,或者Download Zip

    git clone https://github.com/DigDream/urp-python.git

安装所需要的python库

BeautifulSoup4

或者可以通过

    pip install -r requirements.txt

##0x02    基本用法

查看成绩:

    python urpclient.py grade -no 20131613541

查看学籍:

    python urpclient.py status -no 20131613541

一键评估:

    python urpclient.py yjpg -no 20131613541

提示输入密码后

打开image.jpg,输入验证码

##0x03    查看成绩

    python urpclient.py grade -no 20131613541

##0x04    查看课表

##0x05    一键评估

    python urpclient.py yjpg -no 20131613541

##0x06    查看学籍信息

    python urpclient.py status -no 20131613541

##0x07    关于

仅为个人学习研究用.
