"""
This problem requires you to calculate compounding interest and final value of a  US treasury deposit based upon
current interest rates (that will be provided). Your analysis should return the final value of the investment
after a 10-year and 20-year period. The final values should be stored in the variables "ten_year_final"
and "twenty_year_final", respectively. Perform all your calculations in this file. Do not perform the calculations by hand
and simply write in the final result.

Prompt: On October 27th, 2022, Elon Musk purchased Twitter for $44B in total, with reportedly $33B of his own money. Since
that time, it appears this investment has not worked out. If Elon has instead bought $33B of US Treasury Bonds, how much
would his investment be worth in 10-year and 20-year bonds? Assume the 10-year bonds pay 3.96%,
the 20-year bonds pay 4.32%, with each compounding annually.
Note that Elon's capital will be $33B.
"""

### all your code below ###
purchase_price = 44_000_000_000  # $44 B
elons_capital = 33_000_000_000  # $33 B

rate_10_year = 3.96  # 3.96%
rate_20_year = 4.32  # 4.32%
n1 = 10  # 10 years
n2 = 20  # 20 years

print("Elon's capital: $" + str(elons_capital))
print("10-year bond rate: " + str(rate_10_year/100))
print("Holding period: " + str(n1) + " years")

final_value_10_year = elons_capital * (1 + rate_10_year/100) ** n1

print(f"Final value of 10-year bond: ${final_value_10_year:.2f}")
# final anser for 10-year
print("20-year bond rate: " + str(rate_20_year/100))
print("Holding period: " + str(n2) + " years")
# final answer for 20-year

final_value_20_year = elons_capital * (1 + rate_20_year/100) ** n2
print(f"Final value of 20-year bond: ${final_value_20_year:.2f}")
