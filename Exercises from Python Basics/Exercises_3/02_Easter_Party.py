THRESHOLD_TEN=10
THRESHOLD_FIFTEEN=15
THRESHOLD_TWENTY=20
THRESHOLD_TWENTY_FIVE=25
DISCOUNT_TEN=0.10
DISCOUNT_FIFTEEN_=0.15
DISCOUNT_TWENTY=0.20
DISCOUNT_TWENTY_FIVE=0.25

amount_guests=int(input())
price_reservation=float(input())
budget=float(input())

price_cake=budget*DISCOUNT_TEN

if THRESHOLD_TEN <= amount_guests <= THRESHOLD_FIFTEEN:
    price_reservation -= price_reservation*DISCOUNT_FIFTEEN_
elif THRESHOLD_FIFTEEN < amount_guests <= THRESHOLD_TWENTY:
    price_reservation-=price_reservation*DISCOUNT_TWENTY
elif amount_guests > THRESHOLD_TWENTY:
    price_reservation-=price_reservation*DISCOUNT_TWENTY_FIVE

total_price=(amount_guests*price_reservation)+price_cake

if budget >= total_price:
    print(f'It is party time! {budget-total_price:.2f} leva left.')
else:
    print(f'No party! {total_price- budget:.2f} leva needed.')