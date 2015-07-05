import csv

city = 'beijing'

X = []
Y = []

pm = []

def generate_data(n, k):
	for i in range(n, len(pm)):
		if pm[i] < 0:
			continue
		temp = []
		if pm[i-48] < 0:
			continue
		else:
			temp.append(pm[i-48])
		if pm[i-72] < 0:
			continue
		else:
			temp.append(pm[i-72])	

		for j in range(1, n + 1):
			if pm[i-j] < 0:
				break
			temp.append(pm[i-j])
			if j == n:
				X.append(temp)
				Y.append([pm[i]])
	# print X[0], X[1], X[2], Y[1], Y[2]





for k in range(2008, 2015):
	miss = 0 
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
			miss = miss + 1
		else:
			pm.append(int(line[7]))
	print float(miss)/len(pm)
	print miss
	print len(pm)
	generate_data(24, k)












pmd = [-100]
X_c = []
Y_c = []

def tolevel(x):
	if (x<=50):
		return 1
	if (x<=100):
		return 2
	if (x<=150):
		return 3
	if (x<=200):
		return 4
	if (x<=300):
		return 5
	if (x<=500):
		return 6
	return 7



def generate_classification():
	for i in range(7, len(pmd)):
		if pmd[i] < 0:
			continue
		temp = []

		for j in range(1, 7):
			if pmd[i - j] < 0:
				break
			temp.append(pmd[i - j])
			if j == 2:
				X_c.append(temp)
				Y_c.append([tolevel(pmd[i])])
	#print X_c[0], X_c[1], X_c[2], Y_c[1], Y_c[2]




for k in range(2008, 2015):
	miss = 0 
	pmd = [-100]
	reader = csv.reader(file('PM2.5/'+ city + '_' + str(k)+'.csv', 'rb'))
	i = 0
	day = -1

	nd = 1
	for line in reader:
		# print i
		i = i + 1
		if i <= 4:
			continue
		if (int(line[5])!=day):
			day = int(line[5])
			#print nd
			pmd[-1] = float(pmd[-1])/nd
			pmd.append(0)
			nd = 1
		else:
			nd = nd + 1

		if (line[10] == 'Missing' or int(line[7]) < 0):
			pmd[-1]=-999999
		else:
			pmd[-1]=pmd[-1]+int(line[7])
	pmd[-1] = float(pmd[-1]) / nd
	#print pmd[0], pmd[1], pmd[2], pmd[-2], pmd[-1]
	generate_classification()




with open('convert2/'+city+'_x.csv', 'wb') as csvfile:
	writer = csv.writer(csvfile, delimiter=',')
	writer.writerows(X)
with open('convert2/'+city+'_y.csv', 'wb') as csvfile:
	writer = csv.writer(csvfile, delimiter=',')
	writer.writerows(Y)



with open('classification/'+city+'_x.csv', 'wb') as csvfile:
	writer = csv.writer(csvfile, delimiter=',')
	writer.writerows(X_c)
with open('classification/'+city+'_y.csv', 'wb') as csvfile:
	writer = csv.writer(csvfile, delimiter=',')
	writer.writerows(Y_c)


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



