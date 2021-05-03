import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
ALPHAVANTAGE_API_KEY = 'alphavantage api key'
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = 'news api key'
yesterday_date = ''

twilio_id = 'twilio ACCOUNT SID'
auth_token = 'auth token'
twilio_trail_number = 'twilio phone number'
my_phone = '+123456789'

parameter = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': ALPHAVANTAGE_API_KEY
}

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def check_stock_price():
    global yesterday_date
    # TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
    # TODO 2. - Get the day before yesterday's closing stock price
    response = requests.get(STOCK_ENDPOINT, params=parameter)
    response.raise_for_status()
    yesterday_date = response.json()['Meta Data']['3. Last Refreshed']
    print(yesterday_date)
    daily_price_dict = response.json()['Time Series (Daily)']
    daily_price_list = [value for (key, value) in daily_price_dict.items()]
    # print(daily_price_list)
    yesterday_close = float(daily_price_list[0]['4. close'])
    yes_yesterday_close = float(daily_price_list[1]['4. close'])

    # TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
    # TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
    # print(yesterday_close, yes_yesterday_close)
    difference = yesterday_close - yes_yesterday_close
    def_percentage = difference / yesterday_close * 100
    # print(def_percentage)
    up_down = None
    if difference > 0:
        up_down = '⬆️'
    elif difference < 0:
        up_down = '⬇️'

    # TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
    if def_percentage > 1 or def_percentage < -1:
        print('get news')
        ## STEP 2: https://newsapi.org/
        # Instead of printing ("Get News"), actually get the first 3 news_list pieces for the COMPANY_NAME.
        new_params = {
            'q': COMPANY_NAME,
            'from': yesterday_date,
            'sortBy': 'publishedAt',
            'apiKey': NEWS_API_KEY
        }
        # 'https://newsapi.org/v2/everything?q=tesla&from=2021-04-30&sortBy=publishedAt&apiKey=971e7e6b33d541b1b71a865308f94f99'

        #TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
        #TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
        response = requests.get(NEWS_ENDPOINT, params=new_params)
        response.raise_for_status()

        ## STEP 3: Use twilio.com/docs/sms/quickstart/python
        #to send a separate message with each article's title and description to your phone number.

        #TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
        news_articles = response.json()['articles'][:3]
        news_list = [[item['title'], item['description']] for item in news_articles]

        #TODO 9. - Send each article as a separate message via Twilio.
        for new in news_list:
            client = Client(twilio_id, auth_token)
            message = client.messages \
                .create(
                body=f'{STOCK_NAME}: {up_down} {int(def_percentage)}%\nHeadline: {new[0]}\nBrief: {new[1]}',
                from_=twilio_trail_number,
                to=my_phone
            )
            print(message.status)

check_stock_price()

#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
