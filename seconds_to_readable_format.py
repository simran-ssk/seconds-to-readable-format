import datetime

def seconds_to_readable_format(seconds):
    """
    Converts seconds to a detailed time format.
    :param seconds: Int
    :return: String
    """
    time_to_convert = str(datetime.timedelta(seconds=seconds)).split(':')
    if 'days' in time_to_convert[0]:
        time_to_convert = time_to_convert[0].split(', ') + time_to_convert[1:]
        return '{days} {hours} hours {minutes} minutes {seconds} seconds'.format(
            days=time_to_convert[0], hours=int(time_to_convert[1]), minutes=int(time_to_convert[2]), seconds=int(time_to_convert[3])
        )
    elif int(time_to_convert[0]) > 0:
        return '{hours} hours {minutes} minutes {seconds} seconds'.format(
            hours=time_to_convert[0], minutes=int(time_to_convert[1]), seconds=int(time_to_convert[2])
        )
    elif int(time_to_convert[1]) > 0:
        return '{minutes} minutes {seconds} seconds'.format(
            minutes=int(time_to_convert[1]), seconds=int(time_to_convert[2])
        )
    else:
        return '{seconds} seconds'.format(
            seconds=int(time_to_convert[2])
        )
