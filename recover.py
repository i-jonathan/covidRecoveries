import requests, datetime, pytz, pandas as df, time

total_url = "https://covid-19-data.p.rapidapi.com/totals"

headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "7748ae5db9msh74a199cdb6bb845p146c3ajsna91e5c5ee1ad"
} 

querystring = {"format":"json"}
update_time = time.strftime("%H:%M", time.gmtime())
update_date = time.strftime("%d %B, %Y", time.gmtime())
data = df.read_csv('data.csv', index_col='Index')

def get_recovered(url, headers, parameters):
    return (requests.request("GET", url, headers=headers, params=parameters)).json()[0]["recovered"]


def write_data(data, recovered):
    data.Then[0] = data.Now[0]
    data.Now[0] = recovered
    data.Then[1] = data.Now[1]
    data.Now[1] = f"{update_date}, {update_time}"
    data.to_csv('data.csv')
