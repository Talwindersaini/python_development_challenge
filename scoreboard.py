import json
import pprint
from operations import scoreboard, accept_input


def main():
    start_date, sd = accept_input("start date")
    end_date, ed = accept_input("end date")
    diff =  ed - sd

    if diff.days <= 7:
        result = scoreboard(start_date, end_date)
        pprint.pprint(result)
        return json.dumps(result)
    else:
        print('Date range must a maximum of 7 days for sports other than MMA, Boxing and AutoRacing and a maximum of 1 month for MMA, Boxing and AutoRacing.')

if __name__ == "__main__":
    main()
