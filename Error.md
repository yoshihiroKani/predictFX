## ValueError: could not convert string to float: 

loadtxtで読み込む場合、（a,,b）のような穴の空いたCSVを読み込むと上記のエラーとなる。
genfromtxtで読み込むことで解決。

ref: http://www.mwsoft.jp/programming/numpy/csv.html

## ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

numpy配列を比較している場合、配列の次元が異なる場合はreshape()などを使用して明示的に揃えることで解決するカノウセイあり。
