### System Referral RESTful API

### next update
    update expired link
    update beautiful API

### deploy on docker

    run : docker-compose up --build

### list api => testing POSTMAN

    POST ==> http://localhost:5000/login
    POST ==> http://localhost:5000/signup
    GET ==> http://localhost:5000/referral_code
    GET ==> http://localhost:5000/statement

<!-- -->
### -----------------------------------------------

### API Login
Params Request
```
{
    "email": "user2@email.com",
    "password": "123456"
}
```
Response
```
{
    "email": "user2@email.com",
    "id": 2,
    "password": "hIhOzmS8VgxPHWXNIgQbTDgcKggZ6CZ/lLXeZg1DM6M=",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJSZWZlcnJhbCBQcm9ncmFtIEFQSSIsImFjY251bSI6IjQwMTAzNTQ0MTIiLCJpYXQiOjE2NDYyMTM0ODQuMCwiZXhwIjoxNjQ2MjI0Mjg0LjAsInN1YiI6IlVzZXIyX1JlZmZlcmFsIn0.p48apLyDdbJrvne21s5iMg8jYdpHa3ZgntLmDyfmfyY"
}
```

### -----------------------------------------------

### API Signup
Params Request
```
{
    "name": "User4_Refferal",
    "email": "user4@email.com",
    "password": "123456",
    "referralCode": ""
}
```
Response
```
{
    "email": "user4@email.com",
    "id": 4,
    "name": "User4_Refferal",
    "password": "atioJdA+ZYROIGs9nbSmvjTUx1UB6vzrP8IZdS7D7ok="
}
```

### -----------------------------------------------

### API Refferal Code

Params Request

get Bearer token from login account
```
{
    "bearer_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJVc2VyMSIsImlzcyI6IlJlZmVycmFsIFByb2dyYW0gQVBJIiwiZXhwIjoxNjQ2MjIzNDIzLjAsImFjY251bSI6IjQwNzU4Mjc2MjgiLCJpYXQiOjE2NDYyMTI2MjMuMH0gX_0qAuYLncii9gR1QVA-0zub-H6ugQ8DhmE_ZTQi48"
}
```
Response
```
{
    "code": "7ZDP8NMVCZ",
    "link": "http://localhost:5000/signup?code=7ZDP8NMVCZ"
}
```

### -----------------------------------------------

### API Statement

Params Request

get Bearer token from login account with signup with referral code
```
{
    "bearer_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJVc2VyMl9SZWZmZXJhbCIsImlzcyI6IlJlZmVycmFsIFByb2dyYW0gQVBJIiwiZXhwIjoxNjQ2MjIzNDY0LjAsImFjY251bSI6IjQwMTAzNTQ0MTIiLCJpYXQiOjE2NDYyMTI2NjQuMH0.mqWAoJ116gQG1MpO0BMdoRwdTXbdynm_Jn8Tn4tdvV0"
}
```
Response
```
[
    {
        "account": "4010354412",
        "date": "2022-03-02T09:15:43.653132",
        "description": "User signup using a referral code",
        "name": "User2_Refferal",
        "status": "Contributor"
    }
]
```
