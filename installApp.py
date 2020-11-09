from appium import webdriver
import config
import time


class InstallAppFromGooglePlayStore:

    def __init__(self):
        self.desired_cap = {"platformName": "Android",
                        "platformVersion": "7.0",
                        "deviceName": "32793457",
                        "automationName": "UiAutomator1",
                        "appPackage": "tv.game", # com.android.vending
                        "appActivity": "tv.game.MainActivity" # com.android.vending.AssetBrowserActivity
                    }

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',self.desired_cap)

    def verifyAppLaunch(self):

        time.sleep(10)
        isVisibleHome = self.driver.find_element_by_xpath("//android.view.View[@content-desc='Enter your phone number']").is_enabled()

        if isVisibleHome:
            print("Test Case 1: Pass")
        else:
            print("Test Case 1: Fail, Unable to launch application.")

    def verifyTwitterIcon(self):

        time.sleep(10)
        isVisibleTwitterIcon = self.driver.find_element_by_xpath(
            "//android.widget.ImageView[@content-desc='AuthoriseWithTwitter_593']").is_enabled()

        if isVisibleTwitterIcon:
            print("Test Case 2: Pass")
        else:
            print("Test Case 2: Fail, Twitter Icon not visible on Login Screen")


    def verifyLogin(self):

        time.sleep(10)

        isVisibleGoogleIcon = self.driver.find_element_by_xpath(
            "/ hierarchy / android.widget.FrameLayout / android.widget.LinearLayout / android.widget.FrameLayout / android.widget.FrameLayout / android.widget.FrameLayout / android.view.View / android.view.View / android.view.View / android.view.View / android.widget.ImageView / android.view.View / \
          android.widget.ImageView[2]").is_enabled()

        if isVisibleGoogleIcon:
            self.driver.find_element_by_id('com.google.android.gms:id/add_account_chip_title').click()
            time.sleep(10)
            self.driver.find_element_by_id('com.android.settings:id/password_entry').send_keys('0724')

            self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[3]/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View').send_keys('test1.auto1@gmail.com')

            self.driver.find_element_by_id('identifierNext').click()

            self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[3]/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[3]').send_keys('game@twitter')

        else:
            print("Test Case 3: Fail, Unable to login using google")



gtv = InstallAppFromGooglePlayStore()

gtv.verifyAppLaunch()
gtv.verifyTwitterIcon()
gtv.verifyLogin()
