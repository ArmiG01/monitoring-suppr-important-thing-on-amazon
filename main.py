from bs4 import BeautifulSoup
import requests
import smtplib
url = "https://www.amazon.com/August-Smart-Lock-Connect-technology/dp/B0752V8D8D/ref=lp_21216824011_1_3?s=specialty-aps"
req = requests.get(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,hy;q=0.6"
})
soup = BeautifulSoup(req.text, "html.parser")
price = float(soup.find("span", id="priceblock_dealprice").getText().split("$")[1])
name = soup.find("span", id="productTitle").getText().split("\n")[8]
if price <= 100:
    message = f"The '{name} is now ${price}!'"
    with smtplib.SMTP("smtp.gmail.com") as conect:
        conect.starttls()
        conect.login("sberrusmoscow@gmail.com", "00ls0002002123")
        conect.sendmail(from_addr="sberrusmoscow@gmail.com",
                        to_addrs="arman009.cooll@gmail.com",
                        msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}")
