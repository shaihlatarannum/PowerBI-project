
# pip install lxml
import requests
from bs4 import BeautifulSoup
from lxml import html


headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.linkedin.com/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

response = requests.get('https://ticker.finology.in/company/RELIANCE', headers=headers)
print(response.status_code)
print(response.text)

with open('test.html', 'w+', encoding='utf-8') as f:
    f.write(response.text)
    
soup = BeautifulSoup(response.text, 'html.parser')

soup.find('div',{'id':'mainContent_pricesummary'}).text
tree = html.fromstring(response.text)
today_high = tree.xpath('//*[@id="mainContent_ltrlTodayHigh"]/text()')[0]
today_low = tree.xpath('//*[@id="mainContent_ltrlTodayLow"]/text()')[0]
week52High = tree.xpath('//*[@id="mainContent_ltrl52WH"]/text()')[0]
week52Low = tree.xpath('//*[@id="mainContent_ltrl52WL"]/text()')[0]

market_cap = tree.xpath('//small[text()="Market Cap"]/following-sibling::p/span/text()')[0]
enterprisevalue = tree.xpath("//span[@id='mainContent_ltrlEntValue']/span[@class='Number']/text()")[0]
No_of_shares = tree.xpath("//div[@id='mainContent_updAddRatios']//div[contains(., 'No. of Shares')]//span[@class='Number']/text()")[0]


"//tag[@class='field']"
tree.xpath('//span[@id="mainContent_ltrlTodayHigh"]/text()')

tree.xpath('//span[@id="mainContent_ltrlTodayLow"]/text()')
tree.xpath('//span[@id="mainContent_ltrlCash"]/text()')
tree.xpath('//span[@id="mainContent_ltrlCash"]//span[@class="Number"]//text()')
tree.xpath('//span[@id="mainContent_ltrl52WL"]/text()')
tree.xpath('//span[@id="mainContent_ltrlMarket Cap"]//span[@class="Number"]//text()')
tree.xpath('//span[@id="mainContent_lblDEBTCostToIncome"]/text()')
tree.xpath('//span[@id="mainContent_lblDEBTCostToIncome"]//span[@class="Number"]//text()')

tree.xpath('//span[@id="mainContent_divOwner"]/text()')
tree.xpath('//span[@id="mainContent_divOwner"]//span[@class="Number"]//text()')

tree.xpath('//span[@id="mainContent_ltrlEntValue"]/text()')
tree.xpath('//span[@id="mainContent_ltrlEntValue"]//span[@class="Number"]//text()')
ownership = tree.xpath('//div[@id="mainContent_divOwner"]//h6//span[@class="badge badge-success"]//text()')

tree.xpath('//div[@id="mainContent_divOwner"]//h6//span//text()')

# COMPANY ESSENTIALS

Market_cap = tree.xpath("//div[@id='mainContent_updAddRatios']//small[contains(text(),'Market Cap')]/following-sibling::p//span[@class='Number']/text()")[0].strip()

Enterprise_value = tree.xpath('//span[@id="mainContent_ltrlEntValue"]//span[@class="Number"]//text()')

Number_of_share = tree.xpath("//div[@id='mainContent_updAddRatios']//small[contains(text(),'No. of Shares')]/following-sibling::p//span[@class='Number']/text()")[0].strip()

PE_ratio = tree.xpath("//div[@id='mainContent_updAddRatios']//small[contains(text(),'P/E')]/following-sibling::p/text()")[0].strip() 

PB_Ratio = tree.xpath("//div[@id='mainContent_updAddRatios']//small[contains(text(),'P/B')]/following-sibling::p/text()")[0].strip() 

Face_value = tree.xpath("//div[@id='mainContent_updAddRatios']//small[contains(text(),'Face Value')]/following-sibling::p/text()")[0].strip() 

Div_Yield = tree.xpath("//div[@id='mainContent_updAddRatios']//small[contains(text(),'Div. Yield')]/following-sibling::p/text()")[0].strip() 

Book_Value_TTM = tree.xpath("//div[@id='mainContent_updAddRatios']//small[contains(text(),'Book Value (TTM)')]/following-sibling::p//span[@class='Number']/text()")[0].strip() 

Cash = tree.xpath('//span[@id="mainContent_ltrlCash"]/text()')

Debt = tree.xpath('//span[@id="mainContent_ltrlDebt"]//span[@class="Number"]//text()')

Promoter_Holding = tree.xpath("//div[@id='mainContent_updAddRatios']//small[contains(text(),'Promoter Holding')]/following-sibling::p/text()")[0].strip() 

EPS_TTM = tree.xpath("//div[@id='mainContent_updAddRatios']//small[contains(text(),'EPS (TTM)')]/following-sibling::p//span[@class='Number']/text()")[0].strip() 

Sales_Growth = tree.xpath('//span[@id="mainContent_lblSalesGrowthorCasa"]/ancestor::small/following-sibling::p/span[@class="Number"]/text()')

ROE = tree.xpath("//div[@id='mainContent_updAddRatios']//small[contains(text(),'ROE')]/following-sibling::p//span[@class='Number']/text()")[0].strip() 

ROCE = tree.xpath("//div[@id='mainContent_updAddRatios']//small[contains(text(),'ROCE')]/following-sibling::p//span[@class='Number']/text()")[0].strip() 

Profit_Growth = tree.xpath("//div[@id='mainContent_updAddRatios']//small[contains(text(),'Profit Growth')]/following-sibling::p//span[@class='Number']/text()")[0].strip() 

#  FINSTAR

ownership = tree.xpath('//div[@id="mainContent_divOwner"]//h6//span[@class="badge badge-success"]//text()')

Valueation = tree.xpath('//div[@id="mainContent_divValuation"]//h6//span[@class="badge badge-success"]//text()')

Efficiency = tree.xpath('//div[@id="mainContent_divEff"]//h6//span[@class="badge badge-success"]//text()')

Financials = tree.xpath('//div[@id="mainContent_divFinance"]//h6//span[@class="badge badge-success"]//text()')

#  RATIOS

Sales_Growth = tree.xpath('//canvas[@id="mainContent_salesChart"]/@data-chart_values')[0]
