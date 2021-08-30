import datetime
import webbrowser
import random

links = ['https://youtu.be/3AbM4exnEIc', 'https://youtu.be/fpQHabt6e-w', 'https://youtu.be/3u-Pp7IMebA']
link = random.choice(links)


def date(alarm):
    while True:
        current_time = datetime.datetime.now()
        hour = current_time.strftime('%H:%M')
        if hour == alarm:
            print("Alarm brr")
            webbrowser.open_new(link)
            break


def set_alarm():
    hour1 = input("Hey enter Hour of the Alarm: ")
    minute = input("Hey enter minute of the Alarm: ")
    alarm = f'{hour1}:{minute}'
    print(f'Alarm will ring at {alarm}')
    date(alarm)


set_alarm()
