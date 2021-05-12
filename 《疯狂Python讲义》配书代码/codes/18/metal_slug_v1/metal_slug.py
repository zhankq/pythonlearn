# coding: utf-8
#########################################################################
# 网站: <a href="http://www.crazyit.org">疯狂Java联盟</a>               #
# author yeeku.H.lee kongyeeku@163.com                                  #
#                                                                       #
# version 1.0                                                           #
#                                                                       #
# Copyright (C), 2001-2018, yeeku.H.Lee                                 #
#                                                                       #
# This program is protected by copyright laws.                          #
#                                                                       #
# Program Name:                                                         #
#                                                                       #
# <br>Date:                                                             #
#########################################################################
import pygame
import sys
from view_manager import ViewManager
import game_functions as gf
import monster_manager as mm

def run_game():
    # 初始化游戏
    pygame.init()
    # 创建ViewManager对象
    view_manager = ViewManager()
    # 设置显示屏幕，返回Surface对象
    screen = pygame.display.set_mode((view_manager.screen_width, 
        view_manager.screen_height))
    # 设置标题
    pygame.display.set_caption('合金弹头')

    while(True):
        # 处理游戏事件
        gf.check_events(screen, view_manager)
        # 更新游戏屏幕
        gf.update_screen(screen, view_manager, mm)
run_game()
