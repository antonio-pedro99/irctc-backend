from fastapi import APIRouter, HTTPException
from schemas.payment import PaymentCreate
from utils.payment import create_payment, get_payment_methods

razor_pay_api_fake = APIRouter()

@razor_pay_api_fake.post("/pay/for_strip", tags=["Razor Pay Payment"])
def new_payment(payment:PaymentCreate):
   return create_payment(payment_method_id=payment.payment_method, amount=payment.amount)


@razor_pay_api_fake.get("/pay/payments-mehtods", tags=["Razor Pay Payment"])
def get_methods():
    return get_payment_methods()