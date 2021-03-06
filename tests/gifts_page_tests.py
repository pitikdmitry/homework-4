# -*- coding: utf-8 -*-
import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from src.pages.gift_page import GiftPage
from src.pages.self_gift_page import SelfGiftPage
from src.pages.gift_dialog_page import GiftDialogPage

import time


class GiftsPageTests(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', os.environ['BROWSER'])

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.gift_page = GiftPage(self.driver)
        self.self_gift = SelfGiftPage(self.driver)
        self.gift_dialog_page = GiftDialogPage(self.driver)
        self.gift_page.open()

        self.gift_page.open_self_gifts()
        if not self.gift_page.check_gift_exist():
            self.gift_page.create_new_gift()

        self.gift_page.open_without_auth()

    def tearDown(self):
        self.driver.quit()

    #pitikdmitry
    #   Отправка подарка другу обычно
    def test_send_gift_usual(self):
        gift_page = self.gift_page.send_gift_usual()
        ok = gift_page.is_gift_sent()
        self.assertTrue(ok)

    #    Отправка подарка по имени друга(такой друг есть)
    def test_send_gift_by_receivers_name(self):
        gift_page = self.gift_page.send_gift_by_receivers_name()
        ok = gift_page.is_gift_sent()
        self.assertTrue(ok)

    #   Отправка подарка по имени друга(такого друга нет)
    def test_send_gift_by_receivers_name_not_exists(self):
        gift_page = self.gift_page.send_gift_by_receivers_name_not_exists()
        ok = gift_page.is_gift_not_sent()
        self.assertTrue(ok)

    #   Отправка подарка по имени друга(очень большая строка)
    def test_send_gift_by_receivers_name_big_str(self):
        gift_page = self.gift_page.send_gift_by_receivers_name_big_str()
        ok = gift_page.is_gift_not_sent()
        self.assertTrue(ok)

    #    Отправка подарка другу приватно
    def test_send_gift_private(self):
        gift_page = self.gift_page.send_gift_private()
        ok = gift_page.is_gift_sent()
        self.assertTrue(ok)

    #    Отправка подарка приватно по имени друга(такой друг есть)
    def test_send_gift_private_by_receivers_name(self):
        gift_page = self.gift_page.send_gift_private_by_receivers_name()
        ok = gift_page.is_gift_sent()
        self.assertTrue(ok)

    #   Отправка подарка приватно по имени друга(такого друга нет)
    def test_send_gift_private_by_receivers_name_not_exists(self):
        gift_page = self.gift_page.send_gift_private_by_receivers_name_not_exists()
        ok = gift_page.is_gift_not_sent()
        self.assertTrue(ok)

    #   Отправка подарка приватно по имени друга(очень большая строка)
    def test_send_gift_private_by_receivers_name_big_str(self):
        gift_page = self.gift_page.send_gift_private_by_receivers_name_big_str()
        ok = gift_page.is_gift_not_sent()
        self.assertTrue(ok)

    #   Отправка подарка другу тайно
    def test_send_gift_secretly(self):
        gift_page = self.gift_page.send_gift_secretly()
        ok = gift_page.is_gift_sent()
        self.assertTrue(ok)

    #   Поиск подарка по названию(такой подарок есть)
    def test_search_gift(self):
        gift_page = self.gift_page.search_gift()
        ok = gift_page.is_search_done()
        self.assertTrue(ok)

    #   Поиск подарка по названию(такой такой подарок отстуствует)
    def test_search_gift_not_exists(self):
        gift_page = self.gift_page.search_gift_not_exists()
        ok = gift_page.is_search_not_done()
        self.assertTrue(ok)

    #   Поиск подарка по названию и отправка
    def test_search_gift_and_send(self):
        gift_page = self.gift_page.search_gift_and_send()
        ok = gift_page.is_gift_sent()
        self.assertTrue(ok)

    #    Переход на страницу акуальных подарков
    def test_open_actual_gifts(self):
        actual_gift_page = self.gift_page.open_actual_gifts()
        ok = actual_gift_page.is_loaded()
        self.assertTrue(ok)

    #    Переход на страницу акуальных подарков и отправка подарка
    def test_open_actual_gifts_and_send_gift(self):
        actual_gift_page = self.gift_page.open_actual_gifts_and_send()
        ok = actual_gift_page.is_gift_sent()
        self.assertTrue(ok)

    #    Переход на страницу авторских подарков
    def test_open_authors_gifts(self):
        authors_gift_page = self.gift_page.open_authors_gifts()
        ok = authors_gift_page.is_loaded()
        self.assertTrue(ok)

    #    Переход на страницу акуальных подарков и отправка подарка
    def test_open_authors_gifts_and_send_gift(self):
        authors_gift_page = self.gift_page.open_authors_gifts_and_send()
        ok = authors_gift_page.is_gift_sent()
        self.assertTrue(ok)

    #   Переход на страницу открыток
    def test_open_postcards(self):
        postcards_page = self.gift_page.open_postcards()
        ok = postcards_page.is_loaded()
        self.assertTrue(ok)

    #   Переход на страницу открыток и отправка открытки
    def test_open_postcards_and_send(self):
        postcards_page = self.gift_page.open_postcards_and_send()
        ok = postcards_page.is_gift_sent()
        self.assertTrue(ok)

    #   Переход на страницу VIP-подарков
    def test_open_vip_gifts(self):
        vip_gift_page = self.gift_page.open_vip_gifts()
        ok = vip_gift_page.is_loaded()
        self.assertTrue(ok)

    #   Переход на страницу VIP-подарков и отправка подарка
    def test_open_vip_gifts_and_send(self):
        vip_gift_page = self.gift_page.open_vip_gifts()
        ok = vip_gift_page.is_gift_sent()
        self.assertTrue(ok)

    #   Переход на страницу "Создать свой подарок"
    def test_oepn_create_gift(self):
        create_gift_page = self.gift_page.open_create_gift()
        ok = create_gift_page.is_loaded()
        self.assertTrue(ok)

    #   Переход на страницу "Создать свой подарок" и создание подарка
    def test_create_gift(self):
        create_gift_page = self.gift_page.create_gift()
        ok = create_gift_page.is_gift_created()
        self.assertTrue(ok)

    #   Создание собсвенного подарка и его отправка
    def test_create_gift_and_send(self):
        create_gift_page = self.gift_page.create_gift_and_send()
        ok = create_gift_page.is_gift_sent()
        self.assertTrue(ok)

    # ZubAnt
    def test_open_feed_page_by_logo(self):
        feed_page = self.gift_page.open_feed_page_by_logo()
        ok = feed_page.is_loaded()
        self.assertTrue(ok)

    def test_open_feed_page_by_nav_menu(self):
        feed_page = self.gift_page.open_feed_page_by_nav_menu()
        ok = feed_page.is_loaded()
        self.assertTrue(ok)

    def test_open_friends_page_by_nav_menu(self):
        friends_page = self.gift_page.open_friends_page_by_nav_menu()
        ok = friends_page.is_loaded()
        self.assertTrue(ok)

    def test_open_photo_page_by_nav_menu(self):
        photo_page = self.gift_page.open_photo_page_by_nav_menu()
        ok = photo_page.is_loaded()
        self.assertTrue(ok)

    def test_open_groups_page_by_nav_menu(self):
        groups_page = self.gift_page.open_groups_page_by_nav_menu()
        ok = groups_page.is_loaded()
        self.assertTrue(ok)

    def test_open_games_page_by_nav_menu(self):
        games_page = self.gift_page.open_games_page_by_nav_menu()
        ok = games_page.is_loaded()
        self.assertTrue(ok)

    def test_open_notes_page_by_nav_menu(self):
        notes_page = self.gift_page.open_notes_page_by_nav_menu()
        ok = notes_page.is_loaded()
        self.assertTrue(ok)

    def test_open_inventories_page_by_nav_menu(self):
        inventories_page = self.gift_page.open_inventories_page_by_nav_menu()
        ok = inventories_page.is_loaded()
        self.assertTrue(ok)

    def test_open_own_gifts_page_by_nav_menu(self):
        own_gifts_page = self.gift_page.open_own_gifts()
        ok = own_gifts_page.is_loaded()
        self.assertTrue(ok)

        ok = own_gifts_page.is_loaded_own_gifts()
        self.assertTrue(ok)

    def test_add_music(self):
        music_editor = self.gift_page.open_add_music_editor()
        gift_page = music_editor.select_sound()
        ok = gift_page.is_added_music()
        self.assertTrue(ok)

    def test_send_usual_gift_with_music(self):
        self.gift_page.add_music()
        gift_page = self.gift_page.send_gift_usual()
        ok = gift_page.is_gift_sent()
        self.assertTrue(ok)

    def test_send_private_gift_with_music(self):
        self.gift_page.add_music()
        gift_page = self.gift_page.send_gift_private()
        ok = gift_page.is_gift_sent()
        self.assertTrue(ok)