import json
import os
import datetime
import matplotlib.pyplot as plt
import numpy as np


def get_day(timestamp):
    return datetime.datetime.fromtimestamp(timestamp/1000).strftime("%Y-%m-%d")


def graph_data(data):
    # make sure the data is sorted by date
    data = dict(sorted(data.items()))

    # make a trend line of the data
    plt.plot(list(data.keys()), list(data.values()), label="Messages per day")
    # show the day with most messages and day with least messages
    plt.annotate("Max: " + str(max(data, key=data.get)) + " (" + str(max(data.values())) + ")", xy=(max(data, key=data.get),
                                                                                                    max(data.values())), xytext=(max(data, key=data.get), max(data.values()) + 10), arrowprops=dict(facecolor='black', shrink=0.05))
    plt.annotate("Min: " + str(min(data, key=data.get)) + " (" + str(min(data.values())) + ")", xy=(min(data, key=data.get), min(data.values())), xytext=(
        min(data, key=data.get), min(data.values()) - 10), arrowprops=dict(facecolor='black', shrink=0.05))
    print("Max: " + str(max(data, key=data.get)) +
          " (" + str(max(data.values())) + ")")
    print("Min: " + str(min(data, key=data.get)) +
          " (" + str(min(data.values())) + ")")
    plt.savefig("messages_per_day.png")


def main():
    path = "--path to your messages folder (should contain one or more messages.json files)--"
    files = os.listdir(path)

    day_by_day_message_count = {}

    for file in files:
        if file.endswith(".json"):
            with open(path + "/" + file) as json_file:
                data = json.load(json_file)
                for message in data["messages"]:
                    day = get_day(message["timestamp_ms"])
                    if day in day_by_day_message_count:
                        day_by_day_message_count[day] += 1
                    else:
                        day_by_day_message_count[day] = 1
            print(file + " done")

    graph_data(day_by_day_message_count)


main()
