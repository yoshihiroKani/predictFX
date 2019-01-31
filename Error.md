## ValueError: could not convert string to float: 

loadtxtで読み込む場合、（a,,b）のような穴の空いたCSVを読み込むと上記のエラーとなる。
genfromtxtで読み込むことで解決。

ref: http://www.mwsoft.jp/programming/numpy/csv.html

## ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

numpy配列を比較している場合、配列の次元が異なる場合はreshape()などを使用して明示的に揃えることで解決する可能性あり。

## /usr/local/lib/python3.6/dist-packages/sklearn/neural_network/multilayer_perceptron.py:1316: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().

fit()に渡している引数yの次元が原因の可能性あり。y.ravel()などして渡す。
