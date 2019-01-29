import random
import time
import traceback

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import instabot.navigation as navigation


class InstaBot:

    def __init__(self, followed_accounts, unfollowed_accounts, username, password):
        self.driver = webdriver.Chrome()

        # driver = webdriver.Remote(command_executor='http://127.0.0.1:50776', desired_capabilities={})
        # driver.session_id = 'e01fb575-e36f-f546-84d4-cf8131bf47aa'

        print(self.driver.command_executor._url)
        print(self.driver.session_id)
        self.followed_accounts = followed_accounts
        self.unfollowed_accounts = unfollowed_accounts
        self.hashtags = (
            "#potd", "#photooftheday", "#naturephotography", "#follow", "#beachlife", "#instapic", "#instatravel",
            "#andaman", "#"
                        "", "#beach" "#like", "#friendship", "#hitchhiking", "#trekking", "#worldtour",
            "#motivation", "#travel", "#wanderlust")

        self.firefox_comments = (
            "Love ❤️",
            "😍",
            "WOW!!! Great click 📷. I wish you could give me some photography lessons 😛",
            "loved your insta feed 😘",
            "impressive enough for me to follow you 😛",
            "let me just say... Merry Christmas 🎄🎅. haha 😛",
            "Awe 😮",
            "it's adorable..ain't it ❤️❤️😘",
            "nice click.. 📷 ☺️️",
            "☺️😊", "what a click 😍",
            "Merry Christmas 🎄🎅 😛",
            "its beautiful ❤️",
            "amazing 😮",
            "stunning 😮"
        )

        self.chrome_comments = (
            "Love <3",
            ":) :)",
            "WOW!!! Great click :). I wish you could give me some photography lessons :P",
            "loved your insta feed :o",
            "impressive enough for me to follow you :P",
            "let me just say... Merry Christmas. haha :P",
            "awe!!! :O",
            "it's adorable..ain't it? :)",
            "nice click... :D",
            ":) :D",
            "what a click <3",
            "Merry Christmas :)",
            "its beautiful",
            "amazing...",
            "stunning :o"
        )
        self.current_follow_count = 0
        self.current_unfollow_count = 0
        self.login(username, password)

    def login(self, username, pwd):
        self.driver.get("https://www.instagram.com/accounts/login/")
        assert "Instagram" in self.driver.title
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.NAME, "username")))
        username_elem = self.driver.find_element_by_name('username')
        username_elem.clear()
        username_elem.send_keys(username)

        pwd_elem = self.driver.find_element_by_name('password')
        pwd_elem.clear()
        pwd_elem.send_keys(pwd, Keys.ENTER)

        navigation.hide_notification_popup(self.driver)

    def like(self):
        try:
            WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, "button.coreSpriteHeartOpen")))

            self.driver.find_element_by_css_selector("button.coreSpriteHeartOpen").click()

        except Exception:
            traceback.print_exc()

    def follow(self, insta_username):
        try:
            WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                (By.XPATH, "//button[contains(text(), 'Follow')]")))
            self.driver.find_element_by_xpath("//button[contains(text(), 'Follow')]").click()

            self.current_follow_count += 1
            print("followed: {0}, current score: {1}".format(insta_username, self.current_follow_count))
            self.followed_accounts.add(insta_username)

        except Exception:
            traceback.print_exc()

    def unfollow(self, insta_username):
        print("unfollowing username: {}".format(insta_username))
        self.followed_accounts.discard(insta_username)

        if insta_username not in self.unfollowed_accounts:

            try:
                self.driver.get("https://www.instagram.com/" + insta_username + "/")

                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, "//button[contains(text(), 'Following')]")))
                self.driver.find_element_by_xpath("//button[contains(text(), 'Following')]").click()

                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, "//button[contains(text(), 'Unfollow')]")))
                self.driver.find_element_by_xpath("//button[contains(text(), 'Unfollow')]").click()

                self.unfollowed_accounts.add(insta_username)
                self.current_unfollow_count += 1
                print("unfollowed: {0}, current score: {1}".format(insta_username, self.current_unfollow_count))

            except Exception:
                traceback.print_exc()

    def unfollow_people(self, count):
        i = 0

        while i < min(count, len(self.followed_accounts)):
            unfollow_insta_username = self.followed_accounts[0]
            self.unfollow(unfollow_insta_username)
            time.sleep(2)
            i += 1

    def comment(self, insta_username):
        try:
            WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(
                (By.CSS_SELECTOR, "span[aria-label='Comment']")))
            self.driver.find_element_by_css_selector("span[aria-label='Comment']").click()

            WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, "textarea[placeholder='Add a comment…']")))

            comment_textarea = self.driver.find_element_by_css_selector("textarea[placeholder='Add a comment…']")
            comment_textarea.click()
            comment_textarea.send_keys("@" + insta_username + " " + self.chrome_comments[random.randint(0, 14)],
                                       Keys.ENTER)

        except Exception:
            traceback.print_exc()

    def search_hashtag(self, hashtag):
        to_be_liked = set()
        self.driver.get("https://www.instagram.com/")
        WebDriverWait(self.driver, 20).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Search']")))

        searchbox = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search']")
        searchbox.clear()
        searchbox.send_keys(hashtag)
        searchbox.send_keys(Keys.ENTER)

        WebDriverWait(self.driver, 20).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.fuqBx')))

        self.driver.find_element_by_css_selector('.fuqBx').find_element_by_css_selector('a').click()

        tile_class = 'KL4Bh'
        WebDriverWait(self.driver, 20).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.Saeqz')))

        tiles = self.driver.find_elements_by_class_name(tile_class)

        tiles = tiles[9:] if len(tiles) > 9 else tiles

        for i, tile in enumerate(tiles):
            try:

                # if i % 3 == 0:
                #     navigation.scroll_element(self.driver, tile)

                time.sleep(random.randint(0, 2))
                ActionChains(self.driver).move_to_element(tile).click().perform()

                WebDriverWait(self.driver, 20).until(
                    expected_conditions.presence_of_element_located((By.CSS_SELECTOR, 'h2.BrX75 a')))

                insta_username = self.driver.find_element_by_css_selector('h2.BrX75 a').get_attribute('text')

                if insta_username not in self.followed_accounts:
                    to_be_liked.add(insta_username)
                    # self.like()
                    # self.comment(insta_username)
                    # self.follow(insta_username)
                    # time.sleep(random.randint(0, 1))

            except Exception:
                traceback.print_exc()

            self.close_pic()

        self.follow_like_profiles(to_be_liked)

    def follow_like_profiles(self, to_be_liked):
        for insta_username in to_be_liked:
            self.driver.get("https://www.instagram.com/" + insta_username + "/")
            WebDriverWait(self.driver, 20).until(
                expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "img._6q-tv")))

            #self.follow(insta_username)

            tiles = self.driver.find_elements_by_css_selector(".v1Nh3.kIKUG._bz0w a")

            i = 0

            while i < min(1, len(tiles)):
                time.sleep(random.randint(1, 3))
                tile = tiles[i]

                ActionChains(self.driver).move_to_element(tile).click().perform()
                self.like()

                # if i == 0:
                #     self.comment(insta_username)
                self.close_pic()
                i += 1

    def close_pic(self):
        try:
            self.driver.find_element_by_class_name('ckWGn').click()
        except Exception:
            pass

    def follow_people(self):
        for hashtag in self.hashtags:
            try:
                self.search_hashtag(hashtag)
            except Exception:
                traceback.print_exc()

        input("Press Enter to continue...")

    def shutdown(self):
        try:
            self.driver.close()
        except Exception:
            traceback.print_exc()
