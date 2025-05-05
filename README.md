to open and activate a venv
python -m venv venv
source venv/bin/activate

to install dependencies:
pip install -r requirements.txt

to run:

cd codeleap

python3 manage.py runserver



since this has login and signup implemented, this is a step by step guide:

1. signup a user by doing a POST request to /careers/auth/signup/

the body should look like this:
{
    "username": "Username",
    "password": "Password
}

2. login by doing a POST request to /careers/auth/login/

the body should look like this:
{
    "username": "Username",
    "password": "Password
}

the result of the request should look like this:
{
    "token": "your_token"
}

3. when doing a request to either create a new post or a new comment, pass the header like this in the request:
{
    "Authorization": "Token your_token"
}