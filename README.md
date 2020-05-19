# ProblemStatement
Problem Statement 1
Please investigate https://demo.midtrans.com/ website and write UI automation framework covering
the below scenarios:
Must have
1. Create an automation test script to test end to end checkout flow for purchasing “Pillow” using
Credit Card as payment method. This should be a SUCCESSFUL payment flow.
2. Create the second script to test end to end checkout flow for purchasing “Pillow” using Credit
Card as payment method. This should be FAILED payment flow.
3. Implement a reporting framework of your choice to display the test results
4. The above tests should be cross-browser compatible on Chrome and Firefox
Test data:
Payment Type Card Number Expiry Date CVV Number Bank’s OTP
Success Credit Card Payment 4811 1111 1111 1114 05/20 123 112233
Failed Credit Card Payment 4911 1111 1111 1113 05/20 123 112233


Automation For Problem Statement1 :

Configuration & Setup: 
Automation Tool : Selenium 
Programming Language : Java Jdk
Framework : TestNG 
Design : Page Object & Page Factory
Build Automation Tool : Maven
Log Maintain : Lo4j2 
Reporting & continuous integration : Jenkins 


Framework Design

Project: Assignment

Folder :  src/main/java

Package : configuration-It contains all setup files
          Locators-It contains all locators of every page
          
Folder :  src/test/java

Package : Scenario-It contains all test files

Folder   : Logs - print.logs

Folder  :  Report - Jenkins 

