city = 'Beijing';

X_c = csvread(['classification/', city, '_x.csv']);

Y_c = csvread(['classification/', city, '_y.csv']);

test = zeros(size(Y_c,1),3);

for i = 1:size(test,1)
    test(i,Y_c(i)) = 1;
end