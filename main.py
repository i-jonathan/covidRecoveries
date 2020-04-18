from recover import *


def main(update_date, update_time):
    write_data(data, get_recovered(total_url, headers, querystring))
    print(f"New Recoveries since {data.Then[1]} : {int(data.Now[0]) - int(data.Then[0])}")
    print(f"Total Recoveries: {data.Now[0]}")
    print(f"Updated at {update_date}, {update_time} GMT")


if __name__ == "__main__":
    main(update_date, update_time)