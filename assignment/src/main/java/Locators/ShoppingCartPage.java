package Locators;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;


public class ShoppingCartPage {
	
	public WebDriver driver;
	 
    public ShoppingCartPage(WebDriver driver) {
		this.driver = driver;
		PageFactory.initElements(driver, this);
	}
	
	@FindBy(xpath="//input[@value='20000']")
	WebElement amount;
	
	@FindBy(xpath="//input[@value='Budi']")
	WebElement name;
	
	@FindBy(xpath="//input[@type='email']")
	WebElement email;
	
	@FindBy(xpath="//input[@value='081808466410']")
	WebElement phoneNo;
	
	@FindBy(xpath="//input[@value='Jakarta']")
	WebElement city;
	
	@FindBy(xpath="//textarea[@data-reactid='.0.0.1.0.3.0.0.4.1.0']")
	WebElement address;
    
	@FindBy(xpath="//input[@value='10220']")
	WebElement postalCode;
   
	@FindBy(xpath="//div[@class='cart-checkout']")
	WebElement checkout;
	
	


	public WebElement amount() {
    	
    	return amount;
    }
	
    public WebElement name() {
    	
    	return name;
    }
    
    public WebElement email() {
    	
    	return email;
    }
    
    public WebElement phoneNo() {
    	
    	return phoneNo;
    }
    
    public WebElement city() {
    	
    	return city;
    }
    
    
    public WebElement address() {
    	
    	return address;
    }
    
    
    public WebElement postalCode() {
    	
    	return postalCode;
    }
    
    
    public WebElement checkout() {
    	
    	return checkout;
    }
    
    



}
