package Locators;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;


public class LandingPage {
	
	public WebDriver driver;
	 
    public LandingPage(WebDriver driver) {
		this.driver = driver;
		PageFactory.initElements(driver, this);
	}
	
	@FindBy(xpath="//a[@class='btn buy']")
	WebElement buyNow;
    
	@FindBy(xpath="//span[@data-reactid='.0.0.0.2.0.1.0.0:0']")
	WebElement successfulOrder;
    


	public WebElement buyNow() {
    	
    	return buyNow;
    }
	
	public WebElement successfulOrder() {
    	
    	return successfulOrder;
    }

}
