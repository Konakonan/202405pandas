#　pandas　自分用まとめ　＃df_^_^は変数
import pandas as pd
# pandasにはSeries（シリアス）とDateFrameがある。
# Seriesは一次元の表
# DateFrameはSeriesをまとめたもの
# index（行ラベル）、columns（列ラベル）

#　・Seriesの生成
df_a=pd.Series([1,2,3],index=["a","b","c"],dtype=np.int64)
# ・seriesのデータへのアクセス、indexは指定しなかったら0〜
df_aa=df_a.a
df_aa=df["a"]


# ・DateFrameの生成
date={"カラム名1":[1,2,3],"カラム名2":["a","b","c"]}
df_b=pd.DateFrame(date,index=[1,2,3])
#　・DateFrameのデータへのアクセス
df_b["カラム名"]
df_b.カラム名　
df_b.カラム名.index名
#列データの更新
b=[10,12,23,55]
df_b["カラム名"]=pd.Series(b,index="index名") #indexが同じである必要です。
#行データの取得
df_b.loc[index名]
df_b.iloc[index番号]　#位置を表す整数でアクセスできる、ilocは抽出する行、列を番号で指定
#行データの更新
df_d=pd.Series([13,12],index=["index名","index名"])
df_b.loc["index名"]=df_d
#列も行も指定して取得
df_b.loc["index名","カラム名""]


#　・CSVファイルなどのファイルに対しての入出力、SQLへのアクセス、実行できるがリレーションデータベースの理解が必要（まだあんまり分かってない）
df_c=pd.read.csv("ファイルパス",index_col="index名")　#入力、index_colはindexを指定するもの
df_c=pd.to_csv("ファイル名") #出力 行番号、列名を削除して出力したいときは、index=None,header=Noneをつける

# ・読み込んだCSVファイルやDateFrameのデータを表示させる
df_c.head() #上から表示
df_c.tail() #下から表示
df_c[5:10]  #5~9番目を表示
df_c[5:10][["カラム名","カラム名"]] #5~10番目の指定カラムに該当するものを表示

#　・条件による行を抽出する
df_c[df_c["カラム名"]=="データ名"]　#カラム名がデータ名に該当するもの抽出
df_c[df_c["カラム名"] >= 100]     #カラム名が100より大きいものを抽出
df_c[(df_c["カラム名"]=="データ名") & (df_c[] >= 100)]　#andは"&"、orは"|"
df_c.query("カラム名=='カラム内の要素名'& カラム名=='カラム内の要素名'")#こんな感じで抽出もできる、『"』の使い方に気を付けること!!


#　・並び変え
df_c.sort_values("カラム名",ascending=False) #カラム名でソート、Falseで大きい順
df_c.sort_values(["カラム名1","カラム名2"]) #カラム1を並び変え、かつ、カラム2も並び変える


#　・データの集計
df_c.describe() #要素、平均、標準偏差、最小値、中央値、最大値
df_c.sum(numeric_only=True) # numeric_only=Trueで数字データのみ
df_c.groupby("カラム名").mean() #カラム名でまとめて、平均値を抽出
df_c.groupby("カラム名").mean()["カラム名"]#上記のもののカラム名のみ抽出
df_c.groupby(["カラム名","カラム名"]).mean()[["カラム名"]]#リスト二重で表記が変わる　


#　・データクレンジング
df_c.duplicated() #全てのカラムに重複あるものはTureが返ってくる。
#
df_c.drop_duplicates(keep=False)#keep=Trueで重複がどちらも消える、Falseで片方消える。
df_c.drop_duplicates(subset="カラム名")#カラムで重複を制御
df_c.drop_duplicates(subset=["カラム名","カラム名"])

#欠損値の処理
df_c.dropna(subset="カラム名") #nullがある場所全てを消す
df_c.fillna("文字列など")　#欠損値(null)に文字列など入れる
df_c.fillna({"カラム名":"文字列など","カラム": df_c.mean()["カラム名"]})　#こんな表現も

df_a.isnull().sum()#null値の数をカラム別に合計して調べる


# ・データ結合

#joinによる結合
df_p.join(df_q) #左外部結合
#join( ,how="right")右外部結合
#join( ,how="inner")内部結合
#join( how="outer")外部結合

#mergeによる結合
#onでkey設定、複数をkeyにできる
#mergeは内部結合が標準
pd.merge(df_p,df_q, on=["カラム名","カラム名"],how="inner")

#concatによる結合、これはデータを縦に繋げる
pd.concat([df_p,df_q]) #リストを忘れないでね。
pd.concat([df_1,df_2],axis=1)#axis=1を指定することで横に繋げることができる


#コピーを作る
"""
df_copy = dfはdf_copyはdfを参照している、df側の値を変えると、df_copy側の値も変わる
df_copy = df.copy()は、df側に変更があっても、df.copy()には反映されない^^
"""

#列のカラム名を参照する
print(df_a.dtypes)#型を確認する
print(df_a["カラム名"].dtypes)#これは指定したカラム名の型が表示される
print(type(df_a))#これはデータフレームかシリーズかを確認できる

#行数を表示
len(df_a)

#行の中の欠損値の有無を確認
print(df_a.info())

#カラムの列に含まれる要素の種類を列挙
print(df_a["sex"].unique())#この場合(カラム名を性別にしているので)["男","女"]などと出力される
df_a.nunique()#これはカラム列一つ一つに要素がいくつあるかを表示させる
df_a["カラム名"].value_counts()#これは指定したカラム名の出現回数を表示する？
df_a["sex"].value_counts()#"男"＝~回、"女"=~回と表示された!^^

#列のカラム名をリストで表示
df_a.columns.tolist()

df.columns.values#これはndarray型で表示

#行のインデックス名を表示
df_a.index.tolist()
df_a.index.values#上記同様

#複数のカラム名を指定して表示
df_a[["name","age"]]#名前と年齢にカラム名を絞って表示する




#df_aの中で文字列(object型)の列のみを表示させる
df_a.select_dtypes(inclue="object")#数値型の列を表示させたければ(exclude="object")とする?

#小数点を丸める
df_a["カラム名"].round()#これは指定したカラム名の要素の全ての小数を四捨五入している、()内の数字で丸める位置を変更できる
df["カラム名"].round(-1)#など

#型変換？
df["age"].astype(str)#多分かたをobjectに変換しています^^

#列や行を削除する
df.drop("カラム名",axis=1)#指定カラムの列を削除、列を削除する場合はaxis=1を記述
df.drop("index名",axis=0)#指定indexの行を削除、行を削除する場合はaxis=0を記述

del df_a["カラム名"]　#これでも一応消える

#カラム名を一括変更（要素の内容は変わらない？）
df_a.columns=["カラム名","カラム名","カラム名"]
df.rename(columns={"元カラム名":"変更したいカラム名","元カラム名2":"変更したいカラム名2"})#このように変更することもできる？
df_a.rename("変更後の名称") #シリーズの場合はこのように変更できる？

#行(index)名を変更する
df_a=df_a.rename(index={1:10})#index(1)がindex(10)に変更している

df_a.reindex(index=["","",""],method="ffill")#imdex名を変更する、methodにffillを指定することで、欠損値が前方と同じになる。

#列の値をまとめて変更する
df['sex'][df['sex'] == 'male'] = 0 #ここではカラム名（性別）=maleを0に変更している
df['sex'] = df['sex'].replace({'male': 0, 'female': 1}) #replace関数を利用しても同様の結果

#列の値を結合する
df["カラム名"]=df["カラム名1"].str.cat(df["カラム名2"],sep="_")　
df['test'] = df['cabin'] + '_' + df['embarked']#上と同様結果

df["カラム名"]=df["カラム名"].astype(型).str.cat(df["カラム名2"],sep="_")#型がちゃう場合はastype()を利用

#データをランダムに抽出する
df.sampel(frac=1) #(ftac=1)で行をランダムに抽出
df.sample(frac=1).reset_index() #reset_index()でindexを振りなおす


#大文字、小文字に変換
df_a["カラム名"].str.upper()#大文字
df_a["カラム名"].str.lower()#小文字


#データフレームの行と列を入れ替える
df_a=df_a.transpose()
df_a.T


#検索
staetswith("検索文字列")
endswith("検索文字列")
contains()#検索文字が含まれるかどうか

#時系列データの扱い
shift()
-------
pd.to_datetime(df_aa)#datedimeに変換
pd.to_datetime(df_aa,unit="sなど")
"""pandasでのunit='s'は、timestampやdatetimeのデータを秒単位で扱うことを指定するオプションです。例えば、Unixエポック（1970年1月1日 00:00:00 UTC）からの経過時間を秒単位で表す数値を、pandas.to_datetime()関数で日付形式に変換する際に使用されます。"""


pd.to_datetime().dt.day#dayのみ取り出し
pd.to_datetime()dt.strftime("%mなどのフォーマットを選択")#自動的に0埋めなどを行ってくれる

#ピポットテーブルの作成
pd.picot_table(テーブル名,index="",columns="",values-"",aggfunc=sumなど)


#
stack()


#文字の選択？抽出みないなの
df_aa["カラム名"].str[0:3]#0~3文字目を抽出


#ダミー変数
dummie=pd.get_dummies(df_a,prefix='category',columns=['カラム名'])
""""
prefixで生成されるカラム名を編集できる。columns=で指定したカラムに対してダミーを作れます
""""

#データフレームからarrayリスト型へ
df_a.to_numpy()


#apply()とagg()
df_a.apply(def,axis=0)#列に対してdefの処理を行う
df_a["カラム名"].map(def)#カラム名を指定するなら上記と同じことなのでは

df_a.groupby("").agg({"":sum,})#aggは集約したものに対して処理を行う？
