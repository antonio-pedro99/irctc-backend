from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Payment(BaseModel):
    payment_method:int
    amount:float
    date:Optional[str] = datetime.now()

class PaymentCreate(Payment):
    pass

class PaymentInDB(Payment):
    paymentID:int
