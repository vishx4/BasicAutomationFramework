package Locators;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class OrderSummaryPage {
	
	public WebDriver driver;
	 
    public OrderSummaryPage(WebDriver driver) {
		this.driver = driver;
		PageFactory.initElements(driver, this);
	}
	
	@FindBy(xpath="//a[@class='button-main-content']")
	WebElement continueButton;
	
	@FindBy(id="snap-midtrans")
	WebElement navigateSummaryPage;

    
   
	public WebElement continueButton() {
    	
    	return continueButton;
    }
	
    public WebElement navigateSummaryPage() {
    	
    	return navigateSummaryPage;
    }


}
