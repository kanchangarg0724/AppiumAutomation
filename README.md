# AppiumAutomation
This project will verify basic login functionality of the mobile app. Like Download, Launch, Login etc.

# Prerequisites
- python interpreter [3.6 or above](https://www.python.org/downloads/release/python-360/)
- python modules

```
pip install -r requirements.txt
```

# Installation
1. Clone the repo

``` 
git clone https://github.com/kanchangarg0724/AppiumAutomation.git
```

2. XML file for test case input [testdata.xml](https://github.com/kanchangarg0724/AppiumAutomation/blob/main/testdata.xml)
```
<?xml version="1.0"?>
<DataSource xmlns="http://xmlns.oracle.com/weblogic/jdbc-data-source" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<?xml-stylesheet type="text/xsl" href="TestData.xslt"?>
<TestData>
	<TestCases ExecuteAllTestCases="Yes" suite="P1">
		<downloadApp>Yes</downloadApp>
		<verifyTwitterIcon>Yes</verifyTwitterIcon>
		<verifyTwitterLogin>Yes</verifyTwitterLogin>
		<verifyGoogleLogin>No</verifyGoogleLogin>
		<verifyLoginSuccess>Yes</verifyLoginSuccess>
	</TestCases>
</TestData>
</DataSource>
```
5. Enter your Twitter credentials in config.js
```
useremail = "Enter your email"
userpassword = "Enter your password"
```

# License
This is an open source project

# Contact
Kanchan Garg - [kanchangarg0724@gmail.com](mailto:email@kanchangarg0724@gmail.com)
