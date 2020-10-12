#!/usr/bin/env python3

class Configuration:
  connectionStrings =	{    
    "ExcelConn":"Driver={Microsoft Excel Driver (*.xls, *.xlsx, *.xlsm, *.xlsb)};DBQ=[ControlFileName];",
  }

  appSettings =	{
    "ControlFileName": "\\Resources\\TestData\\ControlFile.xlsx",
    "Browser.DefaultTimeout": "10",
    "ChromeDriverPath": "\\Resources\\ChromeDriver\\chromedriver.exe",
    "FirFoxDriverPath": "\\Resources\\FireFoxDriver\\geckodriver.exe",
    "IEedgeDriverPath": "\\Resources\\IEedgeDriver\\MicrosoftWebDriver.exe",
    "ReportPath":"\\Reports"
  }


