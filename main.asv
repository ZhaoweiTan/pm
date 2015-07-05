city = 'Beijing';

X = csvread(['convert/', city, '_x.csv']);

Y = csvread(['convert/', city, '_y.csv']);


MAPE = zeros(25,1);

for dim = 1:25

    tres = floor(size(X,1)*0.7);

    X_train = X(1:tres, 1:dim);
    Y_train = Y(1:tres, 1);
    X_test = X(tres+1:size(X,1), 1:dim);
    Y_test = Y(tres+1:size(Y,1), 1);

    B = regress(Y_train, X_train);

    C = X_test * B;
    MAPE(dim) = mean(abs(C - Y_test)./C);
end
