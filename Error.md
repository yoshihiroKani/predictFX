### ValueError: could not convert string to float: 

loadtxtで読み込む場合、（a,,b）のような穴の空いたCSVを読み込むと上記のエラーとなる。
genfromtxtで読み込むことで解決。

ref: http://www.mwsoft.jp/programming/numpy/csv.html
