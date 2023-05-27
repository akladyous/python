def car_listing(car_prices):
  result = ""
  for key in car_prices.keys():
    prezzo=car_prices[key]
    result += "{} costs {} dollars".format(key, prezzo) + "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))