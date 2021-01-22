"""
each task  = complex n

days = 2
taks = [1, 5, 3, 2, 4]

r= 1 + 5 = 6

complex of day = task most complex

sum = complex day 1 + complex day 2

task less complex

"""

def findMinCompletixy(complexity, days):
    d = days
    tasks = complexity

    number_of_tasks = len(tasks)
    task_most_difficult = max(complexity)


    day_1 = complexity[0]
    task_most_easy = min(complexity)

    


    # number_task_day =
    # if number_of_tasks > 1:
    # rest_of_tasks = number_of_tasks % days
    #
    # for







# def set_task_to_each_day(complexity):
#     number_of_tasks = len(tasks)
#     task_most_difficult = max(complexity)
#     day_1 = complexity[0]
#     rest_of_tasks = number_of_tasks % days
#     days =
#     return




def fastestTaskSequence(tasks, n):
	frequencies = dict()
	a = []
	for ch in tasks:
		if ch in frequencies:
			frequencies[ch] += 1
		else:
			frequencies[ch] = 1
	for key, val in frequencies.iteritems():
		maxheappush(a, [val, key])
	result = ''
	while len(a):
		temp = []
		for i in range(n+1):
			if len(a):
				task = maxheappop(a)
				result += task[1]
				temp.append(task)
			else:
				break
		itemPushed = len(temp)
		while len(temp):
			task = temp.pop()
			task[0] -= 1
			if task[0] > 0:
				maxheappush(a, task)
		if len(a):
			result += '_' * (n+1-itemPushed)
	return result
