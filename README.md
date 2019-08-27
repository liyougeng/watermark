# watermark
add transparent text overlay the jpg. 给图片打文字水印，支持角度、重复、透明度等，全网最简单的实现方式.

# Sample Images
https://raw.githubusercontent.com/jingle1267/watermark/master/output/weixiaobao.jpg
<img style="width:450px;height:450px" src="https://raw.githubusercontent.com/jingle1267/watermark/master/output/weixiaobao.jpg"  alt="真棒" align=center />

# Similar Repo
https://github.com/jingle1267/watermark
本Repo独立实现，我实现完了去pypi找了一下发现有这个repo，看了代码太多了，懒得看。

# Repo method
本Repo思路就是： 读取要加水印的原图，创建一张巨大的水印空白RGBA图，在空白水印图上重复绘制文字，旋转空白水印图，按照目标图扣取水印图，两图叠加，输出。
