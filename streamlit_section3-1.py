from turtle import left
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image#画像を表示させるライブラリPIL
import time



#タイトルの追加
st.title('Streamlit 超入門')
#ターミナルやパワーシェル上でstreamlit run ファイル名.pyを実行
#テキストの追加
st.write('DataFrame')
#DataFrame作成
df=pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
})

#dfの表を追加する、インタラクティブなのでソートもできる
st.write(df)
#dfの表を追加する他の方法、引数をあたえられる表のサイズピクセル単位とか。
# pandasに用意されている関数、列または行の最大値をハイライトできる。axis=0は列axis=1は行
st.dataframe(df.style.highlight_max(axis=0),width=300,height=300)
#dfの表を追加する他の方法、tableは静的な表だからソートとかはできない
st.table(df.style.highlight_max(axis=0))

#テキストを書く＃の後はスペースあり
#コードを書くには```バッククォーテーション3つで```pythonでパイソンのコードをかける
"""
# 章
## 節
### 耕


```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""


#グラフを作成
#0から1で乱数を発生させる。20行3列
df=pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)
df
st.line_chart(df)
st.bar_chart(df)

#マッピング
df=pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],#新宿の緯度と経度をたしてやる
    columns=['lat','lon']#緯度、経度
)
df
st.map(df)

#画像を表示
st.write('Display Image')
img=Image.open('IMG_0852.jpg')#作業ファイルと同じ階層のファイルの場合、ファイル名のみで良い
st.image(img,caption='Maru Runa',use_column_width=True)#use_column_width=True実際の横サイズに合わせて表示

#インタラクティブ、そうほうこうのやりとりができるもので動的な変化をもたらしてくれる
#ウィジェットとはUI_ユーザーインターフェースのこと、各機能のパーツ
#スライダーやチェックボックスを用いて値を動的に変化させる
#インタラクティブなウィジェットで動的に動かす

#1_チェックボックス
# #表示可否、チェックボックスにチェックが入っていたら画像表示、入っていないと非表示
st.write('Display Image')
if st.checkbox('Show Image'):#if文を書くだけでcheckboxはTrueとFalseをかえしてくれる。入っていればTrue入ってないとFalse
    img=Image.open('IMG_0852.jpg')#作業ファイルと同じ階層のファイルの場合、ファイル名のみで良い
    st.image(img,caption='Maru Runa',use_column_width=True)#use_column_width=True実際の横サイズに合わせて表示

#2_セレクトボックス
option=st.selectbox(
    'あなたの好きな数字は',#リストで作成する必要あり、最後にカンマをわすれずに
    list(range(1,11))#1から10までのリストを作成
)
'あなたの好きな数字は、',option,'です。'#,option,の前と後ろのカンマわすれずに

#テキスト入力
st.write('Interractive Widgets')
text=st.text_input('あなたの趣味を教えてください。')
'あなたの趣味：',text,''#,option,の前と後ろのカンマわすれずに

#スライダー
condition=st.slider('あなたの今の調子は？',0,100,50)#最小と最大を書いて区切る値を最後にかく
'コンディション：',condition,

#サイドバーの追加、st.sidebar.で全てサイドバーに移動できる
st.write('Interractive Widgets')
text=st.sidebar.text_input('あなたの趣味を教えてください')
condition=st.sidebar.slider('あなたの今の調子は?？',0,100,50)#最小と最大を書いて区切る値を最後にかく
'あなたの趣味：',text,#,option,の前と後ろのカンマわすれずに
'コンディション：',condition,

#2カラムレイアウト
st.write('Interractive Widgets')
left_column,right_column=st.columns(2)#2カラムの設定
button=left_column.button('右カラムに文字を表示')#左のカラムにボタンを追加する
if button:#ボタンがTrueなら、押されたら
    right_column.write('ここは右カラム')

#expander
expander1=st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2=st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')

#プレグレスバーの表示
st.title('streamlit 入門')
st.write('プログレスバー')
'Start!!'
latest_iteration=st.empty()#空の要素を作成
bar=st.progress(0)#バーを作成

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')#イテレーションの中身をつづつ追加していく
    bar.progress(i+1)#プログレスバーをつづつ増やしていっている
    time.sleep(0.1)#0.1秒ごとに

'Done!!!!'

expander1=st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2=st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')

