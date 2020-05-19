package dkatalis.assignment;

import org.testng.annotations.Test;
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
import org.apache.logging.log4j.*;
import org.openqa.selenium.By;
import org.testng.annotations.Test;

import Locators.LandingPage;
import Locators.OrderSummaryPage;
import Locators.PaymentDetailsPage;
import Locators.ShoppingCartPage;
import config.BrowserSetup;



public class HomePageTest extends BrowserSetup{

	private static Logger log =LogManager.getLogger(BrowserSetup.class.getName());
	@Test
	public void basePageNavigation() throws IOException, InterruptedException {
		
		driver = intializeDriver();
		log.info("driver is initialize");
		driver.get(prop.getProperty("url"));
		driver.manage().window().maximize();
		LandingPage lp = new LandingPage(driver);
		lp.buyNow().click();
		ShoppingCartPage  scp = new ShoppingCartPage(driver);
		scp.amount().clear();
		scp.amount().sendKeys(prop.getProperty("totalAmount"));
		scp.name().clear();
		scp.name().sendKeys(prop.getProperty("customerName")); 
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
		driver.switchTo().frame(pdp.navigateOTPPage());
		pdp.passwordOTP().click();
		pdp.passwordOTP().sendKeys(prop.getProperty("passwordOTP"));
		pdp.submitButton().click();
		Thread.sleep(10000);
		System.out.println(lp.successfulOrder().getText());
		log.info("Purchase Done Successfully");
		driver.close();
		
		
		
	}

}
