
donation_amounts = [400, "Amir", 200, None, 100, "Keanu"]

donation_total = 0
for donation in donation_amounts:
  if isinstance(donation, int):
    donation_total += donation
donation_total