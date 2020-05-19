package Scenario;

import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

import Locators.LandingPage;
import Locators.OrderSummaryPage;
import Locators.PaymentDetailsPage;
import Locators.ShoppingCartPage;
import configuration.base;

import org.testng.annotations.Test;
import org.testng.annotations.Test;
import org.testng.annotations.Test;
import org.testng.annotations.Test;
import org.testng.annotations.Test;
import org.testng.annotations.Test;
import org.testng.annotations.Test;
import org.testng.annotations.Test;
import org.testng.annotations.Test;
import java.io.IOException;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.testng.annotations.Test;


import junit.framework.Assert;




public class SuccessCreditCardPaymentTest extends base{
	public WebDriver driver;
	private static Logger log =LogManager.getLogger(base.class.getName());
	
	@BeforeTest
	public void initialize() throws IOException
	{
		
		driver = intializeDriver();
	    driver.get(prop.getProperty("url"));
		driver.manage().window().maximize();
	}
	
	@Test
	public void successPaymentFlow() throws IOException, InterruptedException {
		
	
		
	
		
		LandingPage lp = new LandingPage(driver);
		lp.buyNow().click();
		log.trace("Buy Now Selected");
		
		ShoppingCartPage  scp = new ShoppingCartPage(driver);
		scp.amount().clear();
		scp.amount().sendKeys(prop.getProperty("totalAmount"));
		scp.name().clear();
		scp.name().sendKeys(prop.getProperty("customerName"));
		log.trace("testing again");
		scp.email().clear();
		scp.email().sendKeys(prop.getProperty("customerEmailId"));
		scp.phoneNo().clear();
		scp.phoneNo().sendKeys(prop.getProperty("customerPhoneNo"));
		scp.city().clear();
		scp.city().sendKeys(prop.getProperty("customerCity"));
		scp.address().clear();
		scp.address().sendKeys(prop.getProperty("customerAddress"));
		scp.postalCode().clear();
		scp.postalCode().sendKeys(prop.getProperty("customerPostalCode"));
		scp.checkout().click();
		log.trace("Customer Details Submitted");
		
		OrderSummaryPage  osp = new OrderSummaryPage(driver);
		driver.switchTo().frame(osp.navigateSummaryPage());
		osp.continueButton().click();
		PaymentDetailsPage pdp =  new PaymentDetailsPage(driver);
		pdp.cardPayment().click();
		pdp.cardNumber().sendKeys(prop.getProperty("cardNumber"));
		pdp.cardExpiryDate().sendKeys(prop.getProperty("cardExpiryDate"));
		pdp.cardCVVNumber().sendKeys(prop.getProperty("cardCVVNumber"));
		pdp.checkbox().click();
		pdp.payNow().click();
		Thread.sleep(3000);
		log.trace("Payment Details Submitted");
		
		driver.switchTo().frame(pdp.navigateOTPPage());
		pdp.passwordOTP().click();
		pdp.passwordOTP().sendKeys(prop.getProperty("passwordOTP"));
		pdp.submitButton().click();
		Thread.sleep(10000);
		System.out.println(lp.successfulOrder().getText());
		Assert.assertTrue(lp.successfulOrder().isDisplayed());
		log.trace("Payment Succesfully Done");
		
			
	}
	
	@AfterTest
	public void endTest()
	{
		driver.close();
	}
		
		
	

}
