def inject_card_info(page, card):
    page.fill('input[name="fullName"]', card['name'])
    page.fill('input[name="address"]', card['address'])
    page.fill('input[name="email"]', card['email'])
    page.fill('input[name="phone"]', card['tel'])
    page.fill('input[name="cardNumber"]', card['number'])
    page.fill('input[name="expiry"]', card['exp'])
    page.fill('input[name="cvv"]', card['cvv'])
    page.click('button[type="submit"]')
    page.wait_for_timeout(5000)
    if "confirmation" in page.url:
        return {"status": "success", "msg": "Order confirmed"}
    else:
        return {"status": "fail", "msg": "Check payment or anti-fraud"}
