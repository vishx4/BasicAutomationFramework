package Locators;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;


public class PaymentDetailsPage {
	
	public WebDriver driver;
	 
    public PaymentDetailsPage(WebDriver driver) {
		this.driver = driver;
		PageFactory.initElements(driver, this);
	}
	
	@FindBy(xpath="//a[@class='list with-promo']")
	WebElement cardPayment;
      
	@FindBy(xpath="//input[@name='cardnumber']")
	WebElement cardNumber;
	
	@FindBy(xpath="//input[@placeholder='MM / YY']")
	WebElement cardExpiryDate;
	
	@FindBy(xpath="//input[@inputmode='numeric']")
	WebElement cardCVVNumber;
	
	@FindBy(xpath="//div[@class='checkbox checkbox-left']//*[text()='Midtrans Promo']")
	WebElement checkbox;
	
	
	@FindBy(xpath="//a[@class='button-main-content']")
	WebElement payNow;
	
	@FindBy(xpath="//iframe[@style='width: 100%; height: 100%; border: 0px; position: absolute; left: 0px; top: 0px;']")
	WebElement navigateOTPPage;
	
	@FindBy(id="PaRes")
	WebElement passwordOTP;
	
	
	@FindBy(xpath="//button[@type='submit']")
	WebElement submitButton;
	
	
	
	//Need to Create New page
	


	public WebElement cardPayment() {
    	
    	return cardPayment;
    }
	
	public WebElement cardNumber() {
    	
    	return cardNumber;
    }
	
	public WebElement cardExpiryDate() {
    	
    	return cardExpiryDate;
    }
	
	
	public WebElement cardCVVNumber() {
    	
    	return cardCVVNumber;
    }
	
	public WebElement checkbox() {
    	
    	return checkbox;
    }
	
	
	public WebElement payNow() {
    	
    	return payNow;
    }
	
	public WebElement navigateOTPPage(){
		
		return navigateOTPPage;
	}
	
	public WebElement passwordOTP() {
    	
    	return passwordOTP;
    }
	
	public WebElement submitButton() {
    	
    	return submitButton;
    }
	
}	