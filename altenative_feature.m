city = 'Beijing';

X2 = csvread(['convert1/', city, '_x.csv']);

Y2 = csvread(['convert1/', city, '_y.csv']);


% MAPE = zeros(25,1);


tres2 = floor(size(X2,1)*0.7);

X2_train = X2(1:tres2, 1:24);
Y2_train = Y2(1:tres2, 1);
X2_test = X2(tres2+1:size(X2,1), 1:24);
Y2_test = Y2(tres2+1:size(Y2,1), 1);

    % B = regress(Y_train, X_train);

    % C = X_test * B;
    % MAPE(dim) = mean(abs(C - Y_test)./C);