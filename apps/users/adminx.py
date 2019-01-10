#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Time    : 2019/1/10 12:08 AM
# @Author  : LiJinzhou
# @File    : adminx.py


import xadmin
from xadmin import views
from .models import EmailVerifyRecord, Banner, UserProfile


class UserProfileAdmin(object):
    list_display = ("id", "username", "email", "is_staff","is_superuser", "is_active", "address")
    search_fields = ("username", "email", "address", "nick_name", "mobile", "image")
    list_filter = ("is_staff", "is_active", "is_superuser", "birthday", "create_time", "update_time", "date_joined")


class EmailVerifyRecordAdmin(object):
    list_display = ("code", "email", "send_type", "send_time")
    search_fields = ("code", "email")
    list_filter = ("send_type", "send_time")


class BannerAdmin(object):
    list_display = ("title", "image", "url", "index", "create_time")
    search_fields = ("title", "image", "url", "index")
    list_filter = ("create_time", "update_time")


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = "慕雪后台管理系统"
    site_footer = "慕雪在线"
    # 菜单样式字段：收起
    menu_style = "accordion"


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile, UserProfileAdmin)
# xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)