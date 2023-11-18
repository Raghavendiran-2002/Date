import datetime
timestamp = datetime.datetime.strptime(
    '2023-09-15T08:00:00Z', "%Y-%m-%dT%H:%M:%S%fZ")
print(timestamp)
