import requests
from bs4 import BeautifulSoup

def scrape_amazon_deals(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all product containers
        products = soup.find_all('div', class_='a-section a-spacing-none')
        
        # Loop through each product container to extract information
        for product in products:
            # Find mobile name
            name = product.find('span', class_='a-size-base-plus a-text-normal').text.strip()
            
            # Find price
            price = product.find('span', class_='a-offscreen').text.strip()
            
            # Find discounted price
            discounted_price = product.find('span', class_='a-price')
            if discounted_price:
                discounted_price = discounted_price.find('span', class_='a-offscreen').text.strip()
            else:
                discounted_price = "No discount available"
            
            # Print the information
            print(f"Mobile Name: {name}")
            print(f"Price: {price}")
            print(f"Discounted Price: {discounted_price}")
            print("-" * 30)
    else:
        print("Failed to fetch the page")

# URL of the Amazon Egypt deals page
url = "https://www.amazon.eg/-/en/deal/190728fc/?_encoding=UTF8&_encoding=UTF8&ref_=dlx_gate_sd_dcl_tlt_190728fc_dt_pd_gw_unk&pd_rd_w=QEknB&content-id=amzn1.sym.f5b727f8-fd8e-4981-84ba-3457ff0dea8f&pf_rd_p=f5b727f8-fd8e-4981-84ba-3457ff0dea8f&pf_rd_r=QNNXJR57HG4B2SQXTXJM&pd_rd_wg=xLrqq&pd_rd_r=7bf46c2b-0ba5-40ce-931d-32066d521772"

# Call the function with the provided URL
scrape_amazon_deals(url)
