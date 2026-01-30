tea_prices_inr = {
    "Masala Chai": 40, 
    "Lemon Chai": 50, 
    "Green Tea": 200
}

tea_prices_usd = {tea:price / 80 for tea, price in tea_prices_inr.items()}

print(tea_prices_usd)