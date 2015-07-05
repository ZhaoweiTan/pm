import csv

city = 'Shenyang'

X = []
Y = []

pm = []
# miss = 0

def generate_data(n, k):
	print n
	for i in range(n, len(pm)):
		if pm[i] < 0:
			continue
		temp = [1]
		for j in range(1, n + 1):
			if pm[i-j] < 0:
				break
			temp.append(pm[i-j])
			if j == n:
				X.append(temp)
				Y.append([pm[i]])
	# print X[0], X[1], X[2], Y[1], Y[2]


for k in range(2013, 2015):
	pm = []
	reader = csv.reader(file('PM2.5/'+ city + '_' + str(k)+'.csv', 'rb'))
	i = 0
	for line in reader:
		# print i
		i = i + 1
		if i <= 4:
			continue
		# print line
		# print i,k
		if (line[10] == 'Missing' or int(line[7]) < 0):
			pm.append(-999)
			# miss = miss + 1
		else:
			pm.append(int(line[7]))
	generate_data(24, k)



with open('convert/'+city+'_x.csv', 'wb') as csvfile:
	writer = csv.writer(csvfile, delimiter=',')
	writer.writerows(X)
with open('convert/'+city+'_y.csv', 'wb') as csvfile:
	writer = csv.writer(csvfile, delimiter=',')
	writer.writerows(Y)



print len(X), len(Y)





# print float(miss)/(len(pm)-1)
# print miss
# print (len(pm)-1)



# for i in range (1,870):
# 	print pm[i]


# with open('csv/Shanghai_2014.csv', 'w') as csvfile:
# 	fieldnames = ['pm']
# 	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# 	writer.writeheader()
# 	for i in range(1, len(pm)):
# 		writer.writerow({'pm':pm[i]})



