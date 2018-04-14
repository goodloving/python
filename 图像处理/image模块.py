import PIL
import numpy as np
import jieba
from wordcloud import WordCloud, ImageColorGenerator

# 1、读入txt文本数据
text = open('1.txt', "r", encoding='utf-8').read()

# 2、结巴分词:cut_all参数可选, True为全模式，False为精确模式,默认精确模式
cut_text = jieba.cut(text, cut_all=False)
result = "/".join(cut_text)  # 必须给个符号分隔开分词结果,否则不能绘制词云

# 3、初始化自定义背景图片
image = PIL.Image.open(r'F:\meizitu\382011a-12-36\04.jpg')
graph = np.array(image)

# 4、产生词云图
# 有自定义背景图：生成词云图由自定义背景图像素大小决定
wc = WordCloud(font_path='STXINWEI.TTF', background_color='white', max_font_size=50, mask=graph)
wc.generate(result)

# 5、绘制文字的颜色以背景图颜色为参考
image_color = ImageColorGenerator(graph)  # 从背景图片生成颜色值
wc.recolor(color_func=image_color)
wc.to_file('词云图.jpg')  # 按照背景图大小保存绘制好的词云图，比下面程序显示更清晰