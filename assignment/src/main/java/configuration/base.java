package configuration;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Properties;
import java.util.concurrent.TimeUnit;

import org.apache.commons.io.FileUtils;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class base {
    
	public WebDriver driver;
	public Properties prop;
	public WebDriver intializeDriver() throws IOException {
		
	    prop = new Properties();
		FileInputStream fis = new FileInputStream("//Users//apple//Documents//workspace//assignment//src//main//java//configuration//testData.properties");
		prop.load(fis);
		String browserName = prop.getProperty("browser");
		
		//chromeBrowserInvoke
		if(browserName.equals("chrome")){
			System.setProperty("webdriver.chrome.driver", "//Users//apple//Downloads//chromedriver");
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
	
	public String getScreenShotPath(String testCaseName,WebDriver driver) throws IOException
	{
		TakesScreenshot ts=(TakesScreenshot) driver;
		File source =ts.getScreenshotAs(OutputType.FILE);
		String destinationFile = System.getProperty("user.dir")+"/reports/"+testCaseName+".png";
		FileUtils.copyFile(source,new File(destinationFile));
		return destinationFile;


	}
	
}