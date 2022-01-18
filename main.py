
import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os

header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "Accept-Language":"en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get("https://www.amazon.in/gp/product/B08697KLZP/ref=s9_acss_bw_cg_Budget_2a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-8&pf_rd_r=E43AABHGYASBJ9M546F9&pf_rd_t=101&pf_rd_p=3ef9a16f-7c76-4743-91bd-2aa2f631bb2f&pf_rd_i=1389401031&th=1", headers=header)

soup = BeautifulSoup(response.text, "lxml")
selected = soup.select(selector="span.a-offscreen")

price = float(selected[0].string.replace("₹", "").replace(",", ""))
print(price)

if price<10000:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user="120.koshanqari@gmail.com", password=os.environ.get("password"))
        connection.sendmail(from_addr="120.koshanqari@gmail.com", to_addrs="koshanqari@hotmail.com", msg=f"the prize for your product is ={price}")
        print("email sent")