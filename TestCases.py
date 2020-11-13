from appium import webdriver
import config
import time
import XMLFunction
from datetime import datetime, timedelta


class InstallAppFromGooglePlayStore:


    def __init__(self):
        self.desired_cap = { "platformName": config.platformName,
                        "platformVersion": config.platformVersion,
                        "deviceName": config.deviceName,
                        "automationName": config.automationName,
                        "appPackage": config.appPackage,
                        "appActivity":config.appActivity
                    }

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',self.desired_cap)

    def downloadApp(self):

        """
            downloadApp(): This function will download app from play store.
            >> Open play store and search for app
            >> Open the app profile on play store
            >> Install the app on the device
            >> Open the app to verify its successfully launched
        """
        try:

            time.sleep(20)
            # Click on search box view
            searchView = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView')
            searchView.click()

            time.sleep(10)
            # Click app name in search
            searchBox = self.driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.EditText")
            searchBox.send_keys("game.tv")

            time.sleep(10)
            # Click on first occurrences of the suggested list
            suggestList = self.driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]")
            suggestList.click()

            time.sleep(10)
            # Click on first occurrences of the app list
            searchList = self.driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]")
            searchList.click()

            time.sleep(10)
            # Click on Install
            istallBtn = self.driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.Button")
            istallBtn.click()

            time.sleep(60)

            # Click on open
            openBtn = self.driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.Button[2]")
            openBtn.click()

            self.verifyAppLaunch()

            self.driver.closeApp()

            config.TCResultDict[config.currentTestCase] = "Pass"

        except Exception as err:
            print("Error: " % str(err))
            config.TCResultDict[config.currentTestCase] = "Fail," + str(err)


    def verifyAppLaunch(self):

        """
            verifyAppLaunch(): This function will verify that the user is able to launch the application and login
            screen is visible.
            >> Open the app to verify its successfully launched
        """

        try:

            time.sleep(10)
            isVisibleHome = self.driver.find_element_by_xpath("//android.view.View[@content-desc='Enter your phone number']").is_enabled()

            if isVisibleHome:
                config.TCResultDict[config.currentTestCase] = "Pass"
            else:
                config.TCResultDict[config.currentTestCase] = "Fail, Unable to launch application."

        except Exception as err:
            print("Error: " % str(err))
            config.TCResultDict[config.currentTestCase] = "Fail," + str(err)

    def verifyTwitterIcon(self):

        """
            verifyTwitterIcon(): This function will verify that Twitter Icon should be visible on the login screen
            >> Open the app to verify its successfully launched
        """
        try:

            time.sleep(10)
            isVisibleTwitterIcon = self.driver.find_element_by_xpath(
                "//android.widget.ImageView[@content-desc='AuthoriseWithTwitter_593']").is_enabled()

            if isVisibleTwitterIcon:
                config.TCResultDict[config.currentTestCase] = "Pass"
            else:
                config.TCResultDict[config.currentTestCase] = "Fail, Twitter Icon not visible on Login Screen"

        except Exception as err:
            print("Error: " % str(err))
            config.TCResultDict[config.currentTestCase] = "Fail," + str(err)


    def verifyTwitterLogin(self):

        """
            verifyTwitterLogin(): This function will verify that user should be able to login to Game.tv through the
            twitter option.
            >> Find the twitter icon on the page and click on the twitter icon.
            >> Enter the user credentials and click on submit
        """

        try:

            time.sleep(10)

            twitterIcon = self.driver.find_element_by_xpath("//android.widget.ImageView[@content-desc='AuthoriseWithTwitter_593']")

            if twitterIcon.is_enabled():
                twitterIcon.click()

                # Verify the twitter login page is visible
                tiwtterLoginPage = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View[1]")

                if tiwtterLoginPage.is_enabled():

                    username = self.driver.find_element_by_id("username_or_email")
                    username.send_keys(config.useremail)

                    userpass = self.driver.find_element_by_id("password")
                    userpass.send_keys(config.userpassword)

                    self.driver.hide_keyboard()

                    submitBtn = self.driver.find_element_by_id("allow")
                    submitBtn.click()
                    time.sleep(10)

                    config.TCResultDict[config.currentTestCase] = "Pass"

                else:
                    config.TCResultDict[config.currentTestCase] = "Fail, Unable to open twitter login page"


        except Exception as err:
            print("Error: " % str(err))
            config.TCResultDict[config.currentTestCase] = "Fail," + str(err)

    def verifyGoogleLogin(self):

        try:

            time.sleep(10)

            GoogleIcon = self.driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView/android.view.View/android.widget.ImageView[2]")

            isVisibleGoogleIcon = GoogleIcon.is_enabled()

            if isVisibleGoogleIcon:
                # Select login with google
                GoogleIcon.click()
                time.sleep(10)

                # Check if the Choose account window appears
                if self.driver.find_element_by_id('com.google.android.gms:id/main_title').is_enabled():
                    # Tab on add another account
                    self.driver.find_element_by_id('com.google.android.gms:id/add_account_chip_title').click()
                    time.sleep(20)

                    self.driver.find_element_by_id('identifierId').send_keys(config.useremail)
                    self.driver.find_element_by_id('identifierNext').click()
                    time.sleep(5)

                    self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[3]/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[1]/android.widget.EditText').send_keys(config.userpassword)
                    self.driver.find_element_by_id('headingText').click()
                    self.driver.find_element_by_id('passwordNext').click()
                    time.sleep(10)

                    signinconsentNext = self.driver.find_element_by_id('signinconsentNext')
                    if signinconsentNext.is_enabled():
                        signinconsentNext.click()
                        time.sleep(10)

                config.TCResultDict[config.currentTestCase] = "Pass"
            else:
                config.TCResultDict[config.currentTestCase] = "Fail, Unable to login using google"

        except Exception as err:
            print("Error: " % str(err))
            config.TCResultDict[config.currentTestCase] = "Fail," + str(err)


    def verifyLoginSuccess(self):

        """
            verifyLoginSuccess(): This function verify that you are on Home Page.
            >> Find some text visible on the home page and verifies that user is on Home Page.

        """
        try:

            time.sleep(20)

            if self.driver.find_element_by_id('//android.view.View[@content-desc="edit_profile_title What should we call you?"]').is_enabled():
                config.TCResultDict[config.currentTestCase] = "Pass"

            else:
                config.TCResultDict[config.currentTestCase] = "Fail, Unable to login"

        except Exception as err:
            print("Error: " % str(err))
            config.TCResultDict[config.currentTestCase] = "Fail," + str(err)


if __name__=="__main__":

    gtv = InstallAppFromGooglePlayStore()

    # Calling Test Cases from XML
    for suite, tclist in XMLFunction.ExecuteTestcases().items():
        for tc, val in tclist.items():
            config.currentTestCase = tc
            print("Calling ",config.currentTestCase)
            config.TCResultDict[config.currentTestCase] = None
            str(eval("gtv." + tc + "()"))

        # Generating result logs
        timestamp = (datetime.today() - timedelta(days=0)).strftime("%Y%m%d-%H%M%S")
        OutputFilePath = "result_" + suite + "_" + timestamp + ".xml"
        XMLFunction.RecodLogsXML(OutputFilePath, config.TCResultDict)
        config.TCResultDict.clear()


