from recover import *
from decouple import config
import tweepy

# Twitter Ready

auth = tweepy.OAuthHandler(config('CONSUMER_KEY'), config('CONSUMER_SECRET'))
auth.set_access_token(config('ACCESS_KEY'), config('ACCESS_SECRET'))
api = tweepy.API(auth)

def main(update_date, update_time):
    write_data(data, get_recovered(total_url, headers, querystring))
    api.update_status(f"New Recoveries since {data.Then[1]} GMT: \n{(int(data.Now[0]) - int(data.Then[0])):,d} \nTotal Recoveries at {update_date}, {update_time} GMT: \n{data.Now[0]:,d}\nStay Safe Y'all.")

if __name__ == "__main__":
    main(update_date, update_time)