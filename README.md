# predictFX

## installation TA-Lib on GoogleColaborator
```
!wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
!tar -xzvf ta-lib-0.4.0-src.tar.gz
%cd ta-lib
!./configure --prefix=/usr
!make
!make install
!pip install Ta-Lib
import talib
```
ref: https://stackoverflow.com/questions/49648391/how-to-install-ta-lib-in-google-colab

## 移動平均の設定の目安

* 分足：1分足、5分足、30分足等 
* 日足：5日、25日、75日、200日 
* 週足：13週、26週、52週 
* 月足：12ヶ月、24ヶ月

ref: https://toushi-kyokasho.com/idouheikinnsenn/#11


## download links
past fx data: https://stooq.com
