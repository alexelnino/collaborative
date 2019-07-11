# collaborative filtering

import numpy as np
import pandas as pd

df = pd.read_excel('dataTV.xlsx', index_col=0)
df.fillna(0, inplace=True)      #buat ngisi value NaN menjadi 0
print(df)
#  produk_a  produk_b  produk_c  produk_d  produk_e  produk_f
# user_`1       1.0       4.0       5.0         3       0.0         2
# user_2        5.0       3.0       3.0         2       2.0         2
# user_3        1.0       0.0       0.0         4       5.0         4
# user_4        0.0       2.0       1.0         4       0.0         3
# user_5        1.0       0.0       2.0         3       3.0         5
# correlation

dfCorr = df.corr(method='pearson')
print(dfCorr)
#  produk_a  produk_b  produk_c  produk_d  produk_e  produk_f
# produk_a  1.000000  0.329785  0.293359 -0.858395  0.120913 -0.452461
# produk_b  0.329785  1.000000  0.813733 -0.467707 -0.790569 -0.943242
# produk_c  0.293359  0.813733  1.000000 -0.652438 -0.612679 -0.618025
# produk_d -0.858395 -0.467707 -0.652438  1.000000  0.140859  0.412514
# produk_e  0.120913 -0.790569 -0.612679  0.140859  1.000000  0.632714
# produk_f -0.452461 -0.943242 -0.618025  0.412514  0.632714  1.000000

# parson : standard correlation coefficient
# kendall : kendall tau correlation coefficient
# spearman : spearman rank correlation

saya=[
    ('doraemon',5),('tersanjung',3)
]

# print=dfCorr['produk_a'] * (1-2.5)
# x= x.sort_values(ascending = False)
# print(x)

skorSama=pd.DataFrame()


for produk, rating in saya:
    skor=dfCorr[produk] * (rating - 2.5)
    skor=skor.sort_values(ascending=False)
    skorSama=skorSama.append(skor, ignore_index=False)

print(skorSama)
print(skorSama.sum().sort_values(ascending=False))


# 