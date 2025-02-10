import leafmap
#m = leafmap.Map(center=(40, -100), zoom=4) # イギリス
m = leafmap.Map(center=(30, 135), zoom=4) # 日本
#m
m.to_html("./map.html") # generate an HTML file

#Traceback (most recent call last):
#   File "f:\211220_nakagawa\test_python\N2_leafmap\hello_leafmap.py", line 1, in <module>
#    import leafmap
#ModuleNotFoundError: No module named 'leafmap'
#
# pip3 insall leafmap
#
# Leafmapを使用してデータを地図上に可視化 #Python - Qiita
# https://qiita.com/wooooo/items/f905899654e551daaf19

