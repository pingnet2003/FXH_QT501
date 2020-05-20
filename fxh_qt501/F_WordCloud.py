import wordcloud   #pip install wordcloud
import jieba     #pip install jieba
import imageio    #pip install imageio

# 词云都是句子 显示
# f = open('14.txt','r',encoding='gbk')
# # with f 
# txt=f.read()
# # print(txt)

# w = wordcloud.WordCloud(width=1000,height=700,background_color='white',font_path="C:/Windows/Fonts/STFANGSO.TTF")
# w.generate(txt)
# w.to_file('14.png')
# f.close()

# 词云都是词语 显示
f = open('14.txt','r',encoding='gbk')
# with f 
txt=f.read()
# print(txt)

mk = imageio.imread('love2.png')

w = wordcloud.WordCloud(width=1000,height=700,background_color='white',mask=mk,contour_width=1,font_path="C:/Windows/Fonts/STFANGSO.TTF")
txt_list = jieba.lcut(txt)
string = "".join(txt_list)
# print(string)
w.generate(string)
w.to_file('18.png')
f.close()

