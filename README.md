# backend
<h1 align="center" >
<img src = "https://drive.google.com/uc?export=view&id=1B09xe3rZvdkPybAF5BMYF1_L4RuU6FDJ" >
</h1>

## Inital setup for project 
    - git clone <url>
    - pip install virtualenv
    - cd oasis
    - virtualenv venv
    - venv\Scripts\activate (windows)
    - source venv/bin/activate (UNIX systems)
    - pip install -r requirements.txt
    - python manage.py makemigrations authenticate commissions content feed subscriptions
    - python manage.py migrate
    - python manage.py runserver

## Or simply
    - git clone <url>
    - cd oasis
    - source scripts/setup_unix.sh (UNIX)
    - scripts\setup_win.sh (windows)

## Subsequent updations
    - git pull
    - venv\Scripts\activate (windows)
    - source venv/bin/activate (UNIX systems)
    - pip install -r requirements.txt
    - python manage.py makemigrations
    - python manage.py migrate
    - python manage.py runserver

## Configuration for Social auth


### Google
    name: google_login

    client id: 355429657096-erletokt235ok76vgb6v3l7tsv6240en.apps.googleusercontent.com

    secret_key: bZ6YsmnzY7XNe0RCD6AmwTvB

    choosen site : 127.0.0.1:8000


### Facebook
    name: fb_login

    client id: 2739355959611383

    secret_key: d495756c9d094fccd065e8cbcf845d74

    choosen site: 127.0.0.1:8000
___
## rest-auth registration 
    method : POST
    url: /authenticate/rest-auth/registration/
    body: {
            "email":"",
            "first_name":"",
            "last_name": "",
            "username":"",
            "password":"",
            "password2": "",
            "login_type": "manual"
    }
    response : {
            "detail": "Verification e-mail sent."
        }
___
## rest-auth login 
    method : POST
    url: /authenticate/rest-auth/login/
    body: {
            "email": "anshul19023@gmail.com",
            "password": "memboro@123"
        }
    response : {
            "key": "b3b7a756d27e49c29d4ae37b4c1c5782af085354",
            "user_id": 1,
            "is_creator": true
    }


# End Points

### For registrations
    - /authenticate/rest-auth/registration/ (POST)
    - /authenticate/rest-auth/login/ (POST)
    - /authenticate/rest-auth/logout/ (POST)
    - /authenticate/rest-auth/password/change/ (POST)
        - body :{
            old_password : <string>,
            new_password1 : <string>,
            new_password2 : <string>
        }
___
### For content Posts
    - /content/api/tiers/ (POST, GET, PATCH, DELETE)
    - /content/api/content/ (POST, GET, PATCH, DELETE)
    - /content/api/likes/ (POST, GET, PATCH, DELETE)
    - /content/api/comment/ (POST, GET, PATCH, DELETE)
    - /content/api/remove-tiers/<int:pk>/ (DELETE)
        - body:{
            tiers: [1,2,...]
        }
___
### For subscriptions (Razorpay)
    - /subscriptions/create (POST) 
        - body : {
            tierID : <tierID>
        }
        -> {
            'SubscriptionID' : client_subscription_id,
            'public_key' : RAZOR_PAY_PUBLIC
        }
    
    - /subscriptions/create_onetime/ (POST) 
        - body : {
            tierID : <tierID>,
            currency: <currency>,
        }
        -> {
            'SubscriptionID' : client_subscription_id,
            'public_key' : RAZOR_PAY_PUBLIC
        }
    
    - /subscriptions/save (POST)
        - body : {
            tierID : <tierID>,
            razor_payment_id : <id>,
            razorpay_signature : <signature>,
            razorpay_subscription_id : <id>
        }
        -> {
            'details': 'Subscription created'
        }
    - /subscriptions/save_order (POST)
        - body : {
            name : <string>
            message : <string>
            amount : <int>
            razorpay_payment_id : <id>
            razorpay_signature : <signature>
            razorpay_subscription_id : <id>
        }
        -> {
            'details': 'Subscription created'
        }
    - /subscriptions/create_order (POST)
        - body : {
            amount : <int>,
            currency : <string>,
        }
        -> {
            'SubscriptionID' : <client_order_id>,
            'public_key' : RAZOR_PAY_PUBLIC
        }
    - /subscriptions/list_message/<creator_id>
        - body : {

        }
        -> {
            messages : [ (singlePayments)
                {    
                    name : <string>,
                    message : <string>,
                    amount : <int>,
                    profile_pic : <string>,
                    dateTime : <string>
                },
            ]
        }
    - /subscriptions/subscribe_to_public_tier
    - /subscriptions/list (GET)
    - /subscriptions/list_tips/<userID>
        - body : {

        }
        -> {
            tips : [
                {
                    'Creator_username':<string>,
                    'Creator_profile_pic':<string>,
                    'message':<string>,
                    'amount':<int>,
                    'dateCreated':<date>
                }
            ]
        }
    - /subscriptions/api/bankdetails (GET, POST, PATCH, DELETE)
        - body : {
            'ifscCode' : String,
            'accountNumber': String,
            'BankName': String,
            'accountHolderName':String
        }
    - /subscriptions/end/ (POST)
        - body : {
            'tier' : <id>,
            'end_type' : 1 or 0 
        }
        - end_type = 1 (end on the next cycle) or 0 (end immediately)
        - Response -> {
            'status' : 'Success'
        } or {
            'status' : 'Failed',
            'message' : 'Subscription does not exist'
        }

    - /subscriptions/get_ghost_user/ (POST)
        - body : {
            'email': <string>,
            'phone': <string>,
            'password':<string>,
            'payment_type':"recurring" or "oneTime" or "commission",
            if (payment_type == "recurring) then 
                'tierID':<int>
            if (payment_type == "oneTime") then
                'tierID':<int>
                'currency':"INR" or "USD",
            if (payment_type == "commission") then
                'currency':"INR" or "USD",
                'commissionID':<int>
        }

        - Response -> {
            'email': <string>,
            'phone': <string>,
            'username':<string>
            'SubscriptionID': <string>,
            'public_key':<string>
        }
___
### For feed
    - /feed/api/feed?page=<int> (GET) (Pagination)
    - /feed/api/user-profile/<id>?page=<int> (GET) (Pagination)
    - /feed/api/search?q=<query> (GET)
    - /feed/api/get-posts (GET)
    - /feed/api/follow/<creator_id> (GET, POST)
        - GET to check if the logged in user follows the creator
        - POST to make the user follow the creator
        - DELETE to make the current user UnFollow the creator whose pk is passed in the URL
    - /feed/api/stats (GET) -> To get creator's dashboard stats
    - /feed/api/userstats (GET) -> To get normal user's dashboard stats
___
### to remove migrations
    - python -m scripts.delete
___
### notifications api
    pip install django-notifications-hq
    First run - python manage.py migrate
    - /feed/api/notifications/?max=100 (GET)
        Reponse:
            {
                'unread_count' :<int>,
                'unread_list':[
                    {
                        'sulg': <id>,
                        'actor': <creator>,
                        'target': <user>,
                        'action_object': <string>,
                        'data': <string>
                    },
                ],
                'all_count' :<int>,
                'all_list':[
                    {
                        'sulg': <id>,
                        'actor': <creator>,
                        'target': <user>,
                        'action_object': <string>,
                        'data': <string>
                    },
                ]
            }

___
### commission
    - commissions/api/commission-creator (POST)
    - commissions/api/commission-user (POST)
    - commissions/api/get-commissions (GET) 
        - like commission-creator but with username and profile-pic of creator
    - commissions/list/<int:id> (GET)
        - id = creator id
    - commissions/api/get-commissions-user (GET)
        - to get user commissions for creator profile
    - commissions/api/deletable/<commissionID> (GET)
        - to know if a particular commission is deletable or not

### Follow-Unfollow a creator
    - content/api/user-creator (PATCH)
___
### TODO
    - razorpay in commissions
___
### auth token (if ever need)
    - from django.apps import apps
        apps.get_models()
        apps.get_model('authtoken', 'Token')
    - from rest_framework.authtoken.models import Token

# On changes to code How to update AWS

    - git checkout development
    - git pull
    - git checkout aws
    - git pull
    - Login to AWS SSH using credentials
    - source env/bin/activate
    - cd oasis/
    - git pull
    - python manage.py makemigrations
    - python manage.py migrate

    $ sudo service nginx restart
    $ sudo supervisorctl reload

# JWT GUIDE
> Endpoints
> 
    - /authenticate/api/token/ (POST)
            
        body : {
            'username' : <username>,
            'email' : <email>, (if email provided)
            'password' : <password> (anything random for google login)
        }
    - /authenticate/api/token/refresh/ (POST)
        body : {
            'refresh': <refresh token>
        }
> access token expires in 5 minutes
>
> encrypt all the data with private key and send in body under the key **payload**

References : 
    
- https://dev.to/subhamuralikrishna/deploying-django-application-to-aws-ec2-instance-2a81

Razorpay Refs:

- https://razorpay.com/docs/api/subscriptions/#fetch-subscription-by-id

JWT References:
- https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html


error on aws

    - cat /var/log/gunicorn/gunicorn.err.log
    - cat /var/log/gunicorn/gunicorn.out.log


Commission Data for webhook

    change notes values for successful request
    razorpay/webhooks/save_onetime_order/

## Recurring Subscription payload
{
  "entity": "event",
  "account_id": "acc_F5Motm2sJ5Fomd",
  "event": "subscription.authenticated",
  "contains": [
    "subscription"
  ],
  "payload": {
    "subscription": {
      "entity": {
        "id": "sub_F5aa7VaVXtXh80",
        "entity": "subscription",
        "plan_id": "plan_F5Zu0nrXVhHV2m",
        "customer_id": "cust_Hqv4jKULwAykog",
        "status": "authenticated",
        "current_start": null,
        "current_end": null,
        "ended_at": null,
        "quantity": 1,
        "notes": {
            "userID":"anshulyadav",
            "tierID":4
        },
        "charge_at": 1593109800,
        "start_at": 1593109800,
        "end_at": 1598380200,
        "auth_attempts": 0,
        "total_count": 3,
        "paid_count": 0,
        "customer_notify": true,
        "created_at": 1592811228,
        "expire_by": null,
        "short_url": null,
        "has_scheduled_changes": false,
        "change_scheduled_at": null,
        "source": "api",
        "offer_id":"offer_JHD834hjbxzhd38d",
        "remaining_count": 3
      }
    }
  },
  "created_at": 1592811255
}

## Subscription Payload

{"entity":"event","account_id":"acc_FlI5o3qjKOncPY","event":"payment.authorized","contains":["payment"],"payload":{"payment":{"entity":{"id":"pay_Gs7H4cAY5zRubS","entity":"payment","amount":34800,"currency":"INR","status":"authorized","order_id":"order_Gs7Gk7vBhrievW","invoice_id":null,"international":false,"method":"upi","amount_refunded":0,"refund_status":null,"captured":false,"description":"2","card_id":null,"bank":null,"wallet":null,"vpa":"success@razorpay","email":"lad.naitik301@gmail.com","contact":"+919725214538","notes":{"type": "subscription", "username": "usingla78", "tierID":"7"},"fee":null,"tax":null,"error_code":null,"error_description":null,"error_source":null,"error_step":null,"error_reason":null,"acquirer_data":{"rrn":"785396808883","upi_transaction_id":"61284802FCF29B9835F49EF57CD430D2"},"created_at":1616943771}}},"created_at":1616943771}

## Cheer payload

{"entity":"event","account_id":"acc_FlI5o3qjKOncPY","event":"payment.authorized","contains":["payment"],"payload":{"payment":{"entity":{"id":"pay_Gs7H4cAY5zRubS","entity":"payment","amount":34800,"currency":"INR","status":"authorized","order_id":"order_Gs7Gk7vBhrievW","invoice_id":null,"international":false,"method":"upi","amount_refunded":0,"refund_status":null,"captured":false,"description":"2","card_id":null,"bank":null,"wallet":null,"vpa":"success@razorpay","email":"lad.naitik301@gmail.com","contact":"+919725214538","notes":{"type": "cheer", "creatorID": "11","username":"usingla78", "name":"Utsav", "message":"check"},"fee":null,"tax":null,"error_code":null,"error_description":null,"error_source":null,"error_step":null,"error_reason":null,"acquirer_data":{"rrn":"785396808883","upi_transaction_id":"61284802FCF29B9835F49EF57CD430D2"},"created_at":1616943771}}},"created_at":1616943771}


## Commission Payload

{"entity":"event","account_id":"acc_FlI5o3qjKOncPY","event":"payment.authorized","contains":["payment"],"payload":{"payment":{"entity":{"id":"pay_Gs7H4cAY5zRubS","entity":"payment","amount":34800,"currency":"INR","status":"authorized","order_id":"order_Gs7Gk7vBhrievW","invoice_id":null,"international":false,"method":"upi","amount_refunded":0,"refund_status":null,"captured":false,"description":"2","card_id":null,"bank":null,"wallet":null,"vpa":"success@razorpay","email":"lad.naitik301@gmail.com","contact":"+919725214538","notes":{"type": "commission", "creatorID": "11","username":"usingla78", "commissionID":1, "description":"Utsav", "contactDetails":"somedetails", "status":"ordered","mode_of_delivery":"1"},"fee":null,"tax":null,"error_code":null,"error_description":null,"error_source":null,"error_step":null,"error_reason":null,"acquirer_data":{"rrn":"785396808883","upi_transaction_id":"61284802FCF29B9835F49EF57CD430D2"},"created_at":1616943771}}},"created_at":1616943771}


apt package needed for installing psycopg2
sudo apt install libpq-dev

pyenv should be used to install python in ubuntu
