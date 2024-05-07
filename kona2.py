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
df_b.iloc[index番号]　#位置を表す整数でアクセスできる
#行データの更新
df_d=pd.Series([13,12],index=["index名","index名"])
df_b.loc["index名"]=df_d
#列も行も指定して取得
dh_b.at["index名","カラム名""]


#　・CSVファイルなどのファイルに対しての入出力、SQLへのアクセス、実行できるがリレーションデータベースの理解が必要（まだあんまり分かってない）
df_c=pd.read.csv("ファイルパス",index_col="index名")　#入力、index_colはindexを指定するもの
df_c=pd.to_csv("ファイル名") #出力

# ・読み込んだCSVファイルやDateFrameのデータを表示させる
df_c.head() #上から表示
df_c.tail() #下から表示
df_c[5:10]  #5~9番目を表示
df_c[5:10][["カラム名","カラム名"]] #5~10番目の指定カラムに該当するものを表示

#　・条件による行を抽出する
df_c[df_c["カラム名"]=="データ名"]　#カラム名がデータ名に該当するもの抽出
df_c[df_c["カラム名"] >= 100]     #カラム名が100より大きいものを抽出
df_c[(df_c["カラム名"]=="データ名") & (df_c[] >= 100)]　#andは"&"、orは"|"

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
df_c.dropna(subset="カラム名") #nullがあるを消す
df_c.fillna("文字列など")　#欠損値(null)に文字列など入れる
df_c.fillna({"カラム名":"文字列など","カラム": df_c.mean()["カラム名"]})　#こんな表現も


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
