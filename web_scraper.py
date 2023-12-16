from bs4 import BeautifulSoup
import requests

# get the URL i want to scrape 
url = requests.get("https://www.amazon.eg/-/en/deal/190728fc/?_encoding=UTF8&_encoding=UTF8&ref_=dlx_gate_sd_dcl_tlt_190728fc_dt_pd_gw_unk&pd_rd_w=QEknB&content-id=amzn1.sym.f5b727f8-fd8e-4981-84ba-3457ff0dea8f&pf_rd_p=f5b727f8-fd8e-4981-84ba-3457ff0dea8f&pf_rd_r=QNNXJR57HG4B2SQXTXJM&pd_rd_wg=xLrqq&pd_rd_r=7bf46c2b-0ba5-40ce-931d-32066d521772").text

#bring the beautiful soap to interact with DOM to handle the page HTML 
#lxml parser is better than HTML parser as it can handle broken html code
soap = BeautifulSoup(url, "lxml")


# find all the mobile cards in the page 

mobile_cards = soap.find_all("span", class_="a-list-item")

#print a headline 
print ("Here are some Black Friday Discounts From Amazon Egypt")
print()


# Iterate over the mobile cards to pull specific info

for mobile_card in mobile_cards:
    # the condition is to only get the mobile cards with discounts
    if mobile_card.find("span", class_="a-text-strike"):
        # get the mobile name 
        mobile_card_name = mobile_card.find("a", class_="a-size-base").text.strip()

        #get the mobile real price with the strikout , and the discounted price

        mobile_real_price = mobile_card.find("span", class_="a-text-strike").text.strip() #returns str
        mobile_discount_price = mobile_card.find("span", class_= "a-offscreen").text #returns str


        #filtering out the all the non digit characters by filter method 
        # Removing commas and decimals, keeping only first part of the digit
        #to be joined and stored in the variable as str data 
        real_price = ''.join(filter(str.isdigit, mobile_real_price.replace(",","").split(".")[0]))
    
        discount_price = ''.join(filter(str.isdigit, mobile_discount_price.replace(",","").split(".")[0]))

        #converting all str into int and calculate the discount
        saved_amount = int(real_price) - int(discount_price)
                     


   
        print(f"Mobile : {mobile_card_name}")
        print("Real Price VS. Discount Price")
        print(f"{mobile_real_price} VS. {mobile_discount_price}")
        print(f"You Saved EGP {saved_amount}")
        print ("#" *100)
        print()
        

    
