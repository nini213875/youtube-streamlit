import streamlit as st
import time

#タイトルの追加
st.title('Streamlit 超入門')

#プレグレスバーの表示
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

