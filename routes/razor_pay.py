from fastapi import APIRouter, HTTPException
from utils.payment import create_payment, get_payment_methods

razor_pay_api_fake = APIRouter()

@razor_pay_api_fake.post("/pay/for_strip", tags=["Razor Pay Payment"])
def new_payment(payment_method:int, amount:float):
   return create_payment(payment_method_id=payment_method, amount=amount)


@razor_pay_api_fake.get("/pay/payments-mehtods", tags=["Razor Pay Payment"])
def get_methods():
    return get_payment_methods()