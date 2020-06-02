package config;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Properties;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class BrowserSetup {
    
	public WebDriver driver;
	public Properties prop;
	public WebDriver intializeDriver() throws IOException {
		
	    prop = new Properties();
		FileInputStream fis = new FileInputStream("C:\\Users\\VISHAL\\git\\BasicAutomationFramework\\assignment\\src\\main\\java\\config\\testData.properties");
		prop.load(fis);
		String browserName = prop.getProperty("browser");
		
		//chromeBrowser 
		if(browserName.equals("chrome")){
			System.setProperty("webdriver.chrome.driver", "C:\\Users\\VISHAL\\Desktop\\chromedriver.exe");
			driver = new ChromeDriver();
		}
		//firefoxBrowser
		else if (browserName.equals("firefox")){
			System.setProperty("webdriver.firefox.driver", "//Users//apple//Downloads//firefoxdriver");
			driver = new FirefoxDriver();
			
		}
	
		driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);
		return driver;
		
	}
	
}