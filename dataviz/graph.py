import tkinter as tk
from collections import Counter
import csv
import matplotlib.pyplot as plt
import numpy as np
import parse

def visualize_days():
	"""Visualize data by day of week"""

	data = parse.parse(parse.MY_FILE, delimiter = ",")

	counter = Counter(item["DayOfWeek"] for item in data)

	data_list = [
		counter["Monday"],
		counter["Tuesday"],
		counter["Wednesday"],
		counter["Thursday"],
		counter["Friday"],
		counter["Saturday"],
		counter["Sunday"]]
	day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

	plt.plot(data_list)
	plt.xticks(range(len(day_tuple)), day_tuple)
	plt.savefig("Days.png")
	plt.clf()


def visualize_type():
	"""Visualize data by type of incident"""

	data = parse.parse(parse.MY_FILE, delimiter = ",")

	counter = Counter(item["Category"] for item in data)

	labels = tuple(counter.keys())
	xlocation = np.arange(len(labels)) + 0.5

	width = 0.5

	plt.bar(xlocation, counter.values(), width=width)
	plt.xticks(xlocation + width / 2, labels, rotation=90)
	plt.subplots_adjust(bottom=0.4)
	plt.rcParams['figure.figsize'] = 12, 8
	plt.savefig("Type.png")
	plt.clf()

def main():
	visualize_days()
	visualize_type()

if __name__ == "__main__":
	main()


