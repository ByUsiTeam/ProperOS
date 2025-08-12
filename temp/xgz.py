import os
import zipfile
import time
from datetime import datetime
import random

class BloodCoffinNovel:
    """《血棺葬》完整小说生成器"""
    
    def __init__(self):
        self.epub_structure = {
            "mimetype": "application/epub+zip",
            "META-INF/container.xml": self._container_xml(),
            "OEBPS/content.opf": self._content_opf(),
            "OEBPS/toc.ncx": self._toc_ncx(),
            "OEBPS/Styles/style.css": self._style_css(),
            "OEBPS/Text/cover.xhtml": self._cover_xhtml(),
            "OEBPS/Text/title_page.xhtml": self._title_page_xhtml(),
            "OEBPS/Text/toc.xhtml": self._toc_xhtml(),
            "OEBPS/Text/chapter01.xhtml": self._chapter_01(),
            "OEBPS/Text/chapter02.xhtml": self._chapter_02(),
            "OEBPS/Text/chapter03.xhtml": self._chapter_03(),
            "OEBPS/Text/chapter04.xhtml": self._chapter_04(),
            "OEBPS/Text/chapter05.xhtml": self._chapter_05(),
            "OEBPS/Text/chapter06.xhtml": self._chapter_06(),
            "OEBPS/Text/chapter07.xhtml": self._chapter_07(),
            "OEBPS/Text/chapter08.xhtml": self._chapter_08(),
            "OEBPS/Text/chapter09.xhtml": self._chapter_09(),
            "OEBPS/Text/chapter10.xhtml": self._chapter_10(),
            "OEBPS/Text/chapter11.xhtml": self._chapter_11(),
            "OEBPS/Text/chapter12.xhtml": self._chapter_12(),
            "OEBPS/Text/chapter13.xhtml": self._chapter_13(),
            "OEBPS/Text/chapter14.xhtml": self._chapter_14(),
            "OEBPS/Text/chapter15.xhtml": self._chapter_15(),
            "OEBPS/Text/chapter16.xhtml": self._chapter_16(),
            "OEBPS/Text/postscript.xhtml": self._postscript_xhtml(),
            "OEBPS/Images/cover.jpg": self._generate_cover_image(),
            "OEBPS/Images/blood_soil.jpg": self._generate_blood_soil_image(),
            "OEBPS/Images/coffin_sketch.jpg": self._generate_coffin_sketch()
        }
    
    def create_epub(self, output_path="blood_coffin.epub"):
        """创建完整的.epub文件"""
        # 创建临时目录
        temp_dir = "blood_coffin_temp"
        os.makedirs(temp_dir, exist_ok=True)
        
        # 创建文件结构
        for path, content in self.epub_structure.items():
            dir_path = os.path.join(temp_dir, os.path.dirname(path))
            os.makedirs(dir_path, exist_ok=True)
            
            if callable(content):
                content = content()
                
            if isinstance(content, str):
                with open(os.path.join(temp_dir, path), "w", encoding="utf-8") as f:
                    f.write(content)
            else:  # 二进制内容（图片）
                with open(os.path.join(temp_dir, path), "wb") as f:
                    f.write(content)
        
        # 打包为epub
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # 首先添加mimetype（无压缩）
            zipf.write(os.path.join(temp_dir, "mimetype"), "mimetype", compress_type=zipfile.ZIP_STORED)
            
            # 添加其他文件
            for root, _, files in os.walk(temp_dir):
                for file in files:
                    if file == "mimetype":
                        continue
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, temp_dir)
                    zipf.write(file_path, arcname)
        
        # 清理临时文件
        import shutil
        shutil.rmtree(temp_dir)
        
        return output_path

    # ================== EPUB 文件内容 ==================
    
    def _container_xml(self):
        return """<?xml version="1.0"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>"""
    
    def _content_opf(self):
        return f"""<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="bookid">urn:uuid:5e2a8d7a-f19b-11ed-a05b-0242ac120003</dc:identifier>
    <dc:title>血棺葬</dc:title>
    <dc:creator id="creator">玄枵</dc:creator>
    <dc:language>zh-CN</dc:language>
    <dc:publisher>民俗恐怖文库</dc:publisher>
    <meta property="dcterms:modified">{datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')}</meta>
    <meta name="cover" content="cover_img"/>
  </metadata>
  <manifest>
    <item id="style_css" href="Styles/style.css" media-type="text/css"/>
    <item id="cover_img" href="Images/cover.jpg" media-type="image/jpeg"/>
    <item id="blood_soil" href="Images/blood_soil.jpg" media-type="image/jpeg"/>
    <item id="coffin_sketch" href="Images/coffin_sketch.jpg" media-type="image/jpeg"/>
    <item id="cover" href="Text/cover.xhtml" media-type="application/xhtml+xml"/>
    <item id="title_page" href="Text/title_page.xhtml" media-type="application/xhtml+xml"/>
    <item id="toc" href="Text/toc.xhtml" media-type="application/xhtml+xml" properties="nav"/>
    <item id="ch01" href="Text/chapter01.xhtml" media-type="application/xhtml+xml"/>
    <item id="ch02" href="Text/chapter02.xhtml" media-type="application/xhtml+xml"/>
    <item id="ch03" href="Text/chapter03.xhtml" media-type="application/xhtml+xml"/>
    <item id="ch04" href="Text/chapter04.xhtml" media-type="application/xhtml+xml"/>
    <item id="ch05" href="Text/chapter05.xhtml" media-type="application/xhtml+xml"/>
    <item id="ch06" href="Text/chapter06.xhtml" media-type="application/xhtml+xml"/>
    <item id="ch07" href="Text/chapter07.xhtml" media-type="application/xhtml+xml"/>
    <item id="ch08" href="Text/chapter08.xhtml" media-type="application/xhtml+xml"/>
    <item id="ch09" href="Text/chapter09.xhtml" media-type="application/xhtml+xml"/>
    <item id="ch10" href="Text/chapter10.xhtml" media-type="application/xhtml+xml"/>
    <item id="ch11" href="Text/chapter11.xhtml" media-type="application/xhtml+xml"/>
    <item id="ch12" href="Text/chapter12.xhtml" media-type="application/xhtml+xml"/>
    <item id="ch13" href="Text/chapter13.xhtml" media-type="application/xhtml+xml"/>
    <item id="ch14" href="Text/chapter14.xhtml" media-type="application/xhtml+xml"/>
    <item id="ch15" href="Text/chapter15.xhtml" media-type="application/xhtml+xml"/>
    <item id="ch16" href="Text/chapter16.xhtml" media-type="application/xhtml+xml"/>
    <item id="postscript" href="Text/postscript.xhtml" media-type="application/xhtml+xml"/>
    <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
  </manifest>
  <spine>
    <itemref idref="cover"/>
    <itemref idref="title_page"/>
    <itemref idref="toc"/>
    <itemref idref="ch01"/>
    <itemref idref="ch02"/>
    <itemref idref="ch03"/>
    <itemref idref="ch04"/>
    <itemref idref="ch05"/>
    <itemref idref="ch06"/>
    <itemref idref="ch07"/>
    <itemref idref="ch08"/>
    <itemref idref="ch09"/>
    <itemref idref="ch10"/>
    <itemref idref="ch11"/>
    <itemref idref="ch12"/>
    <itemref idref="ch13"/>
    <itemref idref="ch14"/>
    <itemref idref="ch15"/>
    <itemref idref="ch16"/>
    <itemref idref="postscript"/>
  </spine>
</package>"""
    
    def _toc_ncx(self):
        return """<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
  <head>
    <meta name="dtb:depth" content="2"/>
    <meta name="dtb:totalPageCount" content="0"/>
    <meta name="dtb:maxPageNumber" content="0"/>
  </head>
  <docTitle>
    <text>血棺葬</text>
  </docTitle>
  <navMap>
    <navPoint id="cover" playOrder="1">
      <navLabel><text>封面</text></navLabel>
      <content src="Text/cover.xhtml"/>
    </navPoint>
    <navPoint id="title" playOrder="2">
      <navLabel><text>书名页</text></navLabel>
      <content src="Text/title_page.xhtml"/>
    </navPoint>
    <navPoint id="toc" playOrder="3">
      <navLabel><text>目录</text></navLabel>
      <content src="Text/toc.xhtml"/>
    </navPoint>
    
    <!-- 卷一 蜻蜓点血 -->
    <navPoint id="vol1" playOrder="4">
      <navLabel><text>卷一 蜻蜓点血</text></navLabel>
      <content src="Text/chapter01.xhtml"/>
      <navPoint id="ch01" playOrder="5">
        <navLabel><text>第一章 败落张府与深山凶穴</text></navLabel>
        <content src="Text/chapter01.xhtml"/>
      </navPoint>
      <navPoint id="ch02" playOrder="6">
        <navLabel><text>第二章 陈瞎子的三百年之咒</text></navLabel>
        <content src="Text/chapter02.xhtml"/>
      </navPoint>
      <navPoint id="ch03" playOrder="7">
        <navLabel><text>第三章 铁钉封棺，黑狗血浇土</text></navLabel>
        <content src="Text/chapter03.xhtml"/>
      </navPoint>
      <navPoint id="ch04" playOrder="8">
        <navLabel><text>第四章 夜半抬棺入血穴</text></navLabel>
        <content src="Text/chapter04.xhtml"/>
      </navPoint>
    </navPoint>
    
    <!-- 卷二 买命钱 -->
    <navPoint id="vol2" playOrder="9">
      <navLabel><text>卷二 买命钱</text></navLabel>
      <content src="Text/chapter05.xhtml"/>
      <navPoint id="ch05" playOrder="10">
        <navLabel><text>第五章 赌坊一夜千金骨</text></navLabel>
        <content src="Text/chapter05.xhtml"/>
      </navPoint>
      <navPoint id="ch06" playOrder="11">
        <navLabel><text>第六章 嫡子眼底朱砂痕</text></navLabel>
        <content src="Text/chapter06.xhtml"/>
      </navPoint>
      <navPoint id="ch07" playOrder="12">
        <navLabel><text>第七章 祖坟渗血，家犬啃尸</text></navLabel>
        <content src="Text/chapter07.xhtml"/>
      </navPoint>
      <navPoint id="ch08" playOrder="13">
        <navLabel><text>第八章 "他坟里站着呢..."</text></navLabel>
        <content src="Text/chapter08.xhtml"/>
      </navPoint>
    </navPoint>
    
    <!-- 卷三 红煞冲天 -->
    <navPoint id="vol3" playOrder="14">
      <navLabel><text>卷三 红煞冲天</text></navLabel>
      <content src="Text/chapter09.xhtml"/>
      <navPoint id="ch09" playOrder="15">
        <navLabel><text>第九章 暴雨裂坟，棺中竖影</text></navLabel>
        <content src="Text/chapter09.xhtml"/>
      </navPoint>
      <navPoint id="ch10" playOrder="16">
        <navLabel><text>第十章 长子暴毙，皮裹干骨</text></navLabel>
        <content src="Text/chapter10.xhtml"/>
      </navPoint>
      <navPoint id="ch11" playOrder="17">
        <navLabel><text>第十一章 次子疯语：血棺在吃人！</text></navLabel>
        <content src="Text/chapter11.xhtml"/>
      </navPoint>
      <navPoint id="ch12" playOrder="18">
        <navLabel><text>第十二章 火焚百年宅，灰烬生赤苔</text></navLabel>
        <content src="Text/chapter12.xhtml"/>
      </navPoint>
    </navPoint>
    
    <!-- 卷四 地脉哭坟 -->
    <navPoint id="vol4" playOrder="19">
      <navLabel><text>卷四 地脉哭坟</text></navLabel>
      <content src="Text/chapter13.xhtml"/>
      <navPoint id="ch13" playOrder="20">
        <navLabel><text>第十三章 地质队勘探赤土坡</text></navLabel>
        <content src="Text/chapter13.xhtml"/>
      </navPoint>
      <navPoint id="ch14" playOrder="21">
        <navLabel><text>第十四章 钻头带出血泥与碎棺木</text></navLabel>
        <content src="Text/chapter14.xhtml"/>
      </navPoint>
      <navPoint id="ch15" playOrder="22">
        <navLabel><text>第十五章 录音设备里的铁链拖地声</text></navLabel>
        <content src="Text/chapter15.xhtml"/>
      </navPoint>
      <navPoint id="ch16" playOrder="23">
        <navLabel><text>第十六章 "快逃！它跟着胎记回来了..."</text></navLabel>
        <content src="Text/chapter16.xhtml"/>
      </navPoint>
    </navPoint>
    
    <navPoint id="postscript" playOrder="24">
      <navLabel><text>后记</text></navLabel>
      <content src="Text/postscript.xhtml"/>
    </navPoint>
  </navMap>
</ncx>"""
    
    def _style_css(self):
        return """/* 基础样式 */
body {
  font-family: "SimSun", serif;
  line-height: 1.8;
  margin: 0;
  padding: 1em;
}

h1 {
  color: #8b0000;
  text-align: center;
  border-bottom: 1px solid #8b0000;
  margin-bottom: 1.5em;
}

h2 {
  color: #5c0000;
  text-align: center;
  margin-top: 2em;
  margin-bottom: 1em;
}

/* 章节首字下沉 */
p:first-of-type::first-letter {
  font-size: 3em;
  color: #8b0000;
  float: left;
  line-height: 0.8;
  margin-right: 0.1em;
}

/* 禁忌段落特殊样式 */
.warning {
  background-color: #ffe6e6;
  border-left: 4px solid #8b0000;
  padding: 1em;
  margin: 1em 0;
  font-style: italic;
}

/* 图片样式 */
img {
  display: block;
  margin: 1em auto;
  max-width: 80%;
  border: 1px solid #ccc;
}

/* 卷标题 */
.volume-title {
  font-size: 1.8em;
  text-align: center;
  margin: 2em 0;
  color: #8b0000;
  font-weight: bold;
}

/* 章节标题 */
.chapter-title {
  font-size: 1.4em;
  text-align: center;
  margin: 1.5em 0;
  color: #5c0000;
}"""
    
    def _cover_xhtml(self):
        return """<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>封面</title>
  <link rel="stylesheet" type="text/css" href="../Styles/style.css"/>
</head>
<body>
  <div style="text-align: center;">
    <img src="../Images/cover.jpg" alt="血棺葬封面" style="height: 80vh; width: auto;"/>
    <h1>血棺葬</h1>
    <h2>玄枵 著</h2>
  </div>
</body>
</html>"""
    
    def _title_page_xhtml(self):
        return """<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>书名页</title>
  <link rel="stylesheet" type="text/css" href="../Styles/style.css"/>
</head>
<body>
  <div style="text-align: center; margin-top: 20%;">
    <h1>血棺葬</h1>
    <h2>玄枵 著</h2>
    <p style="margin-top: 3em;">民俗恐怖文库</p>
    <p>2023年10月</p>
  </div>
</body>
</html>"""
    
    def _toc_xhtml(self):
        return """<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head>
  <title>目录</title>
  <link rel="stylesheet" type="text/css" href="../Styles/style.css"/>
</head>
<body>
  <h1>目 录</h1>
  
  <nav epub:type="toc">
    <ol>
      <li><a href="cover.xhtml">封面</a></li>
      <li><a href="title_page.xhtml">书名页</a></li>
      
      <li>
        <a href="chapter01.xhtml">卷一 蜻蜓点血</a>
        <ol>
          <li><a href="chapter01.xhtml">第一章 败落张府与深山凶穴</a></li>
          <li><a href="chapter02.xhtml">第二章 陈瞎子的三百年之咒</a></li>
          <li><a href="chapter03.xhtml">第三章 铁钉封棺，黑狗血浇土</a></li>
          <li><a href="chapter04.xhtml">第四章 夜半抬棺入血穴</a></li>
        </ol>
      </li>
      
      <li>
        <a href="chapter05.xhtml">卷二 买命钱</a>
        <ol>
          <li><a href="chapter05.xhtml">第五章 赌坊一夜千金骨</a></li>
          <li><a href="chapter06.xhtml">第六章 嫡子眼底朱砂痕</a></li>
          <li><a href="chapter07.xhtml">第七章 祖坟渗血，家犬啃尸</a></li>
          <li><a href="chapter08.xhtml">第八章 "他坟里站着呢..."</a></li>
        </ol>
      </li>
      
      <li>
        <a href="chapter09.xhtml">卷三 红煞冲天</a>
        <ol>
          <li><a href="chapter09.xhtml">第九章 暴雨裂坟，棺中竖影</a></li>
          <li><a href="chapter10.xhtml">第十章 长子暴毙，皮裹干骨</a></li>
          <li><a href="chapter11.xhtml">第十一章 次子疯语：血棺在吃人！</a></li>
          <li><a href="chapter12.xhtml">第十二章 火焚百年宅，灰烬生赤苔</a></li>
        </ol>
      </li>
      
      <li>
        <a href="chapter13.xhtml">卷四 地脉哭坟</a>
        <ol>
          <li><a href="chapter13.xhtml">第十三章 地质队勘探赤土坡</a></li>
          <li><a href="chapter14.xhtml">第十四章 钻头带出血泥与碎棺木</a></li>
          <li><a href="chapter15.xhtml">第十五章 录音设备里的铁链拖地声</a></li>
          <li><a href="chapter16.xhtml">第十六章 "快逃！它跟着胎记回来了..."</a></li>
        </ol>
      </li>
      
      <li><a href="postscript.xhtml">后记</a></li>
    </ol>
  </nav>
</body>
</html>"""
    
    # ================== 小说章节内容 ==================
    
    def _chapter_01(self):
        return """<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>第一章 败落张府与深山凶穴</title>
  <link rel="stylesheet" type="text/css" href="../Styles/style.css"/>
</head>
<body>
  <div class="volume-title">卷一 蜻蜓点血</div>
  <div class="chapter-title">第一章 败落张府与深山凶穴</div>
  
  <p>光绪二十三年秋，张家大宅的铜钱雕花门环上，第一次结出了蛛网。</p>
  
  <p>张员外攥着最后三块银元，指节发白。赌坊的打手砸碎了前厅的琉璃屏风，碎碴子溅到他缎面鞋上，像极了祖坟渗出的血泥。</p>
  
  <p>"老爷，陈瞎子到了。"管家声音发颤。</p>
  
  <div class="warning">
    <p>【血棺禁忌】血土竖葬，十族尽灭！——《葬经·凶煞卷》</p>
  </div>
  
  <p>廊下阴影里，独眼风水师拄着槐木杖，那只剩眼白的眸子正对着张员外颈后的赤痣。</p>
  
  <p>"三百里外，蜻蜓点水穴。"陈瞎子喉头滚动，"但那是血棺土..."</p>
  
  <img src="../Images/blood_soil.jpg" alt="血棺土"/>
  
  <p>张员外眼中燃起最后一丝疯狂："管它什么土！我只要三年，三年内让张家重回首富！"</p>
  
  <p>陈瞎子枯瘦的手指划过罗盘："竖葬血土，需柏木棺、无钉绳缚、脚朝下入穴，子孙三代行善，三百年后大贵..."</p>
  
  <p>"三百年？"张员外一把揪住风水师衣领，"我连三年都等不了！"</p>
  
  <p>窗外，最后一片银杏叶飘落，像极了垂死的黄蝶。</p>
</body>
</html>"""
    
    def _chapter_02(self):
        return """<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>第二章 陈瞎子的三百年之咒</title>
  <link rel="stylesheet" type="text/css" href="../Styles/style.css"/>
</head>
<body>
  <div class="volume-title">卷一 蜻蜓点血</div>
  <div class="chapter-title">第二章 陈瞎子的三百年之咒</div>
  
  <p>陈瞎子的独眼在油灯下泛着浑浊的光："张老爷，蜻蜓点水穴本是潜龙饮泉的吉兆..."</p>
  
  <p>他展开一张泛黄的舆图，指尖点向山脉褶皱处："此处土色赤红如血，乃万人坑怨气所结。若按古法竖葬，需以童子血画符封棺，待三百年怨气化尽..."</p>
  
  <div class="warning">
    <p>风水师手记：血土养尸，竖葬聚阴，此乃大凶之局，非天师不可为！</p>
  </div>
  
  <p>张员外猛地拍桌："什么三百年！我要的是速发之法！"</p>
  
  <p>陈瞎子沉默良久，从怀中摸出三枚染血的铜钱："若强行催发...需用铁钉封棺，黑狗血浇穴，可缩至三年暴富..."</p>
  
  <p>"但代价呢？"管家颤声问。</p>
  
  <p>风水师的声音似从地底传来："代价是...棺中人不入轮回，化血尸索命，三代绝嗣！"</p>
  
  <p>窗外惊雷炸响，张员外颈后赤痣突突跳动："绝嗣？呵...我连儿子都没有，怕什么绝嗣！"</p>
  
  <p>他抓起铜钱按在舆图上："就这么办！"</p>
</body>
</html>"""
    
    def _chapter_03(self):
        return """<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>第三章 铁钉封棺，黑狗血浇土</title>
  <link rel="stylesheet" type="text/css" href="../Styles/style.css"/>
</head>
<body>
  <div class="volume-title">卷一 蜻蜓点血</div>
  <div class="chapter-title">第三章 铁钉封棺，黑狗血浇土</div>
  
  <p>七日后，暴雨如注。</p>
  
  <p>张家祖坟前，八名壮汉抬着柏木棺，棺盖上赫然钉着七根三寸长的铁钉——正是北斗七星的形状。</p>
  
  <div class="warning">
    <p>《葬经》注：铁钉封棺，锁魂于尸，此乃养尸大忌！</p>
  </div>
  
  <p>"浇！"张员外嘶吼。</p>
  
  <p>三桶黑狗血泼向墓穴，血水混着雨水渗入赤土，整片山坡弥漫着腥臭。</p>
  
  <p>陈瞎子独眼圆睁："张老爷！此时收手还来得及！铁钉锁魂，黑狗血激煞，这是要化厉鬼啊！"</p>
  
  <p>张员外一脚踹开风水师："下棺！"</p>
  
  <p>棺木垂直落入三丈深的竖井，落地时发出沉闷回响。当第一铲血土盖下时，井底突然传来指甲刮擦棺板的声音——</p>
  
  <p>刺啦...刺啦...</p>
  
  <p>抬棺的壮汉们脸色煞白，张员外却仰天大笑："听见了吗？我爹答应了！张家就要发了！"</p>
  
  <p>暴雨中，陈瞎子踉跄逃下山，怀中罗盘指针疯转如轮。</p>
</body>
</html>"""
    
    def _chapter_04(self):
        return """<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>第四章 夜半抬棺入血穴</title>
  <link rel="stylesheet" type="text/css" href="../Styles/style.css"/>
</head>
<body>
  <div class="volume-title">卷一 蜻蜓点血</div>
  <div class="chapter-title">第四章 夜半抬棺入血穴</div>
  
  <p>子时，阴气最盛。</p>
  
  <p>张员外亲自举着火把，照亮峭壁上那个仅容一棺的洞穴。血红色的泥土从洞口渗出，像极了凝固的血液。</p>
  
  <img src="../Images/coffin_sketch.jpg" alt="竖葬棺示意图"/>
  
  <p>"快！把棺材竖进去！"他催促着颤抖的仆役。</p>
  
  <p>棺木被绳索吊起，缓缓送入洞穴。当棺尾触及洞底时，突然传来"咔嚓"一声脆响——</p>
  
  <div class="warning">
    <p>陈瞎子遗言：蜻蜓点水，最忌触底！棺尾需悬空三寸，触地则吉穴变煞眼！</p>
  </div>
  
  <p>张员外探头望去，只见棺尾压碎了一具白骨的头颅。那骷髅黑洞洞的眼窝正对着他，下颌骨突然"咔哒"开合。</p>
  
  <p>"老...老爷..."仆役瘫软在地，"骷髅在笑！"</p>
  
  <p>张员外一脚将他踹入深渊："废物！封洞！"</p>
  
  <p>巨石堵住洞口的瞬间，整座山体传来沉闷的呜咽。张员外颈后赤痣灼痛，他回头望去，只见峭壁上渗出无数血珠，渐渐汇成四个大字：</p>
  
  <p style="text-align: center; font-size: 1.2em; color: #8b0000;">血债血偿</p>
</body>
</html>"""
    
    def _chapter_05(self):
        return """<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>第五章 赌坊一夜千金骨</title>
  <link rel="stylesheet" type="text/css" href="../Styles/style.css"/>
</head>
<body>
  <div class="volume-title">卷二 买命钱</div>
  <div class="chapter-title">第五章 赌坊一夜千金骨</div>
  
  <p>葬父后的第七日，张员外踏进了"千金骨"赌坊。</p>
  
  <p>"哟，张老爷还有钱赌？"赌坊老板讥笑着，"您那祖传玉佩可早押给我了！"</p>
  
  <p>张员外摸出最后三个铜板："押大！"</p>
  
  <p>骰盅揭开——四五六，大！</p>
  
  <p>铜板变银锭，银锭变金条。当东方既白时，张员外脚边已堆满金砖。更诡异的是，每当他下注，骰子必定转向他押的数字。</p>
  
  <div class="warning">
    <p>赌徒日记：那夜张老爷背后总立着个红影子，骰子落地时，影子就伸手拨一下...</p>
  </div>
  
  <p>"邪门！太邪门了！"赌坊老板擦着冷汗，"张老爷，这是十万两银票，求您去别处玩吧！"</p>
  
  <p>张员外狂笑着走出赌坊，却没发现怀中的银票渐渐浮现血丝，最后汇成一张扭曲的人脸。</p>
  
  <p>当夜，赌坊老板暴毙，死时双手紧抓骰子，眼珠被挖出塞在嘴里。</p>
</body>
</html>"""
    
    def _chapter_06(self):
        return """<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>第六章 嫡子眼底朱砂痕</title>
  <link rel="stylesheet" type="text/css" href="../Styles/style.css"/>
</head>
<body>
  <div class="volume-title">卷二 买命钱</div>
  <div class="chapter-title">第六章 嫡子眼底朱砂痕</div>
  
  <p>张府重修门楣那日，管家领来个八岁男孩。</p>
  
  <p>"老爷，按您吩咐找的嗣子。"管家低声道，"生辰八字全合，只是..."</p>
  
  <p>男孩抬头，左眼底赫然有颗朱砂痣，位置竟与张员外颈后赤痣一模一样。</p>
  
  <p>"你叫什么？"张员外眯起眼。</p>
  
  <p>"张承嗣。"男孩声音清冷。</p>
  
  <p>当夜，张员外梦见父亲站在床前，浑身滴着血泥："此子...替死..."</p>
  
  <div class="warning">
    <p>解梦书：血亲托梦言替死者，乃索命替身，大凶！</p>
  </div>
  
  <p>三更时分，张员外惊醒，发现张承嗣正站在他床前，指尖离他咽喉仅三寸。</p>
  
  <p>"爹做噩梦了？"男孩微笑，眼底朱砂痣红得滴血。</p>
  
  <p>张员外惊出一身冷汗，再看时，男孩已回到偏房安睡。</p>
  
  <p>窗外，祖坟方向传来铁链拖地声。</p>
</body>
</html>"""
    
    def _chapter_07(self):
        return """<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>第七章 祖坟渗血，家犬啃尸</title>
  <link rel="stylesheet" type="text/css" href="../Styles/style.css"/>
</head>
<body>
  <div class="volume-title">卷二 买命钱</div>
  <div class="chapter-title">第七章 祖坟渗血，家犬啃尸</div>
  
  <p>清明扫墓，管家连滚带爬冲进张府："老爷！祖坟...祖坟在流血！"</p>
  
  <p>张员外赶到坟山时，只见血泥从竖葬穴的缝隙不断渗出，所到之处草木枯死。更骇人的是，渗出的血泥中混着细碎的骨渣。</p>
  
  <div class="warning">
    <p>仵作验尸录：血泥含人骨碎屑，疑为棺内尸骨自噬！</p>
  </div>
  
  <p>"慌什么！"张员外强作镇定，"这是地脉龙血！"</p>
  
  <p>当夜，张府看门黑犬突然发狂，咬死马夫后，竟趴在马尸上疯狂啃食。更诡异的是，它边吃边发出人声："饿...好饿..."</p>
  
  <p>张员外命人乱棍打死黑犬。剥皮时，家丁在狗胃里发现半截手指——戴着张员外亡父的翡翠扳指。</p>
  
  <p>张承嗣蹲在狗尸旁，轻声道："爷爷说...下面好挤..."</p>
  
  <p>一阵阴风刮过，灯笼全灭。黑暗中，啃噬声从四面八方响起。</p>
</body>
</html>"""
    
    def _chapter_08(self):
        return """<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>第八章 "他坟里站着呢..."</title>
  <link rel="stylesheet" type="text/css" href="../Styles/style.css"/>
</head>
<body>
  <div class="volume-title">卷二 买命钱</div>
  <div class="chapter-title">第八章 "他坟里站着呢..."</div>
  
  <p>守墓人老王疯了。</p>
  
  <p>他逢人便扯着嗓子喊："竖着！张老太爷在坟里竖着哩！眼睛通红！"</p>
  
  <p>张员外命人将他关进柴房。当夜，柴房传来疯狂撞门声和嘶吼："放我出去！他爬出来了！"</p>
  
  <div class="warning">
    <p>更夫证言：那夜见一红毛人形物从张家祖坟破土而出，指甲三尺长！</p>
  </div>
  
  <p>次日清晨，柴房门洞大开。老王坐在门槛上，双手捧着自己挖出的眼珠，嘴角咧到耳根："看见了...他在你背后站着呢..."</p>
  
  <p>张员外猛回头，只见张承嗣站在影壁前，正用朱砂笔在墙上画棺材。每口棺材都是竖立的，棺盖微微开启，露出半张血脸。</p>
  
  <p>"承嗣！"张员外厉喝。</p>
  
  <p>男孩转身，眼底朱砂痣已蔓延成血线，从眼角爬到脖颈："爹，爷爷让我问您..."</p>
  
  <p>"铁钉钉脑的滋味...可好受？"</p>
</body>
</html>"""
    
    def _chapter_09(self):
        return """<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>第九章 暴雨裂坟，棺中竖影</title>
  <link rel="stylesheet" type="text/css" href="../Styles/style.css"/>
</head>
<body>
  <div class="volume-title">卷三 红煞冲天</div>
  <div class="chapter-title">第九章 暴雨裂坟，棺中竖影</div>
  
  <p>三年之期将至，暴雨连下七日。</p>
  
  <p>第七夜，炸雷劈中坟山。山体裂开巨缝，露出深处竖葬的柏木棺。更骇人的是，棺盖上的七根铁钉正一根根崩出！</p>
  
  <div class="warning">
    <p>天师符咒解：七星钉尸阵破，血尸出世！</p>
  </div>
  
  <p>张员外带家丁冲上山，只见棺盖轰然掀飞，一具浑身长满红毛的尸身直立棺中。它十指乌黑，指甲已穿透棺板，颈后赫然钉着三根狗牙状的铁钉！</p>
  
  <p>"爹..."张员外腿一软跪在泥泞中。</p>
  
  <p>血尸缓缓转头，眼皮猛地睁开——没有瞳孔，只有两团跳动的血焰！</p>
  
  <p>家丁们惨叫逃窜，血尸却如鬼魅般闪到张员外面前，腐烂的手掌按在他颈后赤痣上。</p>
  
  <p>"逆子..."沙哑的声音从尸身喉中挤出，"该还债了..."</p>
</body>
</html>"""
    
    def _chapter_10(self):
        return """<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>第十章 长子暴毙，皮裹干骨</title>
  <link rel="stylesheet" type="text/css" href="../Styles/style.css"/>
</head>
<body>
  <div class="volume-title">卷三 红煞冲天</div>
  <div class="chapter-title">第十章 长子暴毙，皮裹干骨</div>
  
  <p>张员外连滚带爬逃回府邸，却发现嫡子张承嗣站在庭院井边。</p>
  
  <p>"爷爷来了。"男孩指着井口，"他说井下宽敞。"</p>
  
  <p>张员外一巴掌扇去："孽障！胡说什么！"</p>
  
  <p>张承嗣不闪不避，嘴角却诡异上扬："爹，您听——"</p>
  
  <div class="warning">
    <p>婢女口供：那夜井里传来铁链声，少爷突然自己跳了下去！</p>
  </div>
  
  <p>井底传来"噗通"落水声，随即是令人牙酸的吮吸声。当家丁打捞时，只捞上一具裹着人皮的骨架——全身血液骨髓被吸食殆尽，唯眼底朱砂痣鲜红欲滴。</p>
  
  <p>张员外抱着人皮瘫坐在地，颈后赤痣突然剧痛。他摸到痣上多了三个凸点——正是血尸在他颈后按出的指印！</p>
  
  <p>更鼓敲响三更时，井中浮起一串血泡，组成四个字：</p>
  
  <p style="text-align: center; color: #8b0000;">还有两个</p>
</body>
</html>"""
    
    def _chapter_11(self):
        return """<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>第十一章 次子疯语：血棺在吃人！</title>
  <link rel="stylesheet" type="text/css" href="../Styles/style.css"/>
</head>
<body>
  <div class="volume-title">卷三 红煞冲天</div>
  <div class="chapter-title">第十一章 次子疯语：血棺在吃人！</div>
  
  <p>张员外的小妾突然临盆，生下的男婴后背竟有七颗黑痣，排列如北斗。</p>
  
  <p>"七星伴月！大吉之兆！"产婆谄笑着。</p>
  
  <p>话音未落，婴儿突然睁眼，发出老妪般的尖笑："吉？这是索命钉啊！"</p>
  
  <div class="warning">
    <p>稳婆遗书：婴儿后背黑痣会蠕动，分明是七颗铁钉头！</p>
  </div>
  
  <p>三日后，婴儿已长成三岁孩童模样。他终日趴在窗边，指着祖坟方向尖叫："吃人了！血棺在吃人了！"</p>
  
  <p>张员外派人查看，回报说坟山裂口处发现新鲜骸骨，骨上齿痕似人非人。</p>
  
  <p>当夜，婴儿爬进祠堂，用血在族谱上涂抹。次日仆人发现时，只见张家历代祖先名讳全被划去，唯留一行血字：</p>
  
  <p style="text-align: center; font-style: italic;">贪穴者，绝嗣！</p>
  
  <p>张员外提剑冲进婴儿房，却见孩子飘在半空，背后七颗黑痣已破皮而出，竟是七根铁钉！</p>
  
  <p>"爷爷让我带话。"婴儿口吐尸臭，"下一个，是你。"</p>
</body>
</html>"""
    
    def _chapter_12(self):
        return """<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>第十二章 火焚百年宅，灰烬生赤苔</title>
  <link rel="stylesheet" type="text/css" href="../Styles/style.css"/>
</head>
<body>
  <div class="volume-title">卷三 红煞冲天</div>
  <div class="chapter-title">第十二章 火焚百年宅，灰烬生赤苔</div>
  
  <p>大火烧了三天三夜。</p>
  
  <p>百年张府在烈焰中坍塌，火中不时传出铁链拖曳声和啃骨头的脆响。乡民们躲在家中，听见张员外的惨叫划破夜空："爹！我知错了！啊——"</p>
  
  <div class="warning">
    <p>县志记载：光绪二十六年秋，张府大火，阖府俱焚，唯灰烬中生出赤色苔藓，触之如血。</p>
  </div>
  
  <p>暴雨突至，浇灭余烬。人们惊见废墟中央跪着一具焦尸，颈后钉着三根狗牙铁钉。焦尸双手插入地底，正疯狂刨挖着什么。</p>
  
  <p>胆大者近前查看，发现焦尸所刨之处，血泥翻涌如泉，渐渐汇成八个字：</p>
  
  <p style="text-align: center; color: #8b0000; font-size: 1.2em;">
    血债未偿，百年再续
  </p>
  
  <p>当夜，所有参与救火者皆暴毙家中，死状如干尸，全身血液不翼而飞。</p>
  
  <p>坟山裂缝缓缓闭合，仿佛从未开启。只有峭壁上"血债血偿"四字，在月光下流淌着新鲜的血液。</p>
</body>
</html>"""
    
    def _chapter_13(self):
        return """<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>第十三章 地质队勘探赤土坡</title>
  <link rel="stylesheet" type="text/css" href="../Styles/style.css"/>
</head>
<body>
  <div class="volume-title">卷四 地脉哭坟</div>
  <div class="chapter-title">第十三章 地质队勘探赤土坡</div>
  
  <p>2023年，省地质局第七勘探队进驻赤土坡。</p>
  
  <p>"队长，这土红得邪门啊！"实习生林远抓起一把赤土，土质黏腻如凝血。</p>
  
  <p>队长赵刚皱眉看着检测仪："铁含量超标三十倍，还混着...有机质？"</p>
  
  <div class="warning">
    <p>勘探日志：赤土坡原名张家坟，光绪年间曾发生灭门惨案。</p>
  </div>
  
  <p>林远颈后突然刺痛，他下意识摸了摸那块天生的赤痣。昨夜他又梦见自己站在竖立的棺材中，血泥淹没胸口。</p>
  
  <p>"小林子，发什么呆？"队员老陈拍他肩膀，"准备钻探了！"</p>
  
  <p>钻机轰鸣启动时，林远分明听见地底传来指甲刮擦岩层的声音——</p>
  
  <p>刺啦...刺啦...</p>
  
  <p>和他梦里的一模一样。</p>
</body>
</html>"""
    
    def _chapter_14(self):
        return """<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>第十四章 钻头带出血泥与碎棺木</title>
  <link rel="stylesheet" type="text/css" href="../Styles/style.css"/>
</head>
<body>
  <div class="volume-title">卷四 地脉哭坟</div>
  <div class="chapter-title">第十四章 钻头带出血泥与碎棺木</div>
  
  <p>钻至十五米深时，钻头突然卡死。</p>
  
  <p>"见鬼！"老陈骂骂咧咧地抽出钻杆，"这带上来什么玩意儿？"</p>
  
  <p>钻头上沾满暗红色黏土，其中混杂着黑色碎木片。更诡异的是，黏土中裹着一截指骨，骨节上套着半枚翡翠扳指。</p>
  
  <img src="../Images/blood_soil.jpg" alt="钻头带出的血泥"/>
  
  <div class="warning">
    <p>检测报告：碎木为清代柏木，含大量铁离子；指骨DNA与光绪年间张姓死者匹配。</p>
  </div>
  
  <p>林远拿起扳指，颈后赤痣突然灼痛。恍惚间，他听见有个声音在耳边嘶吼："还我...血土..."</p>
  
  <p>当夜，林远在营地帐篷里惊醒，发现手中紧握着那半枚扳指。扳指内侧刻着两个小字，在月光下泛着血光：</p>
  
  <p style="text-align: center;">承嗣</p>
</body>
</html>"""
    
    def _chapter_15(self):
        return """<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>第十五章 录音设备里的铁链拖地声</title>
  <link rel="stylesheet" type="text/css" href="../Styles/style.css"/>
</head>
<body>
  <div class="volume-title">卷四 地脉哭坟</div>
  <div class="chapter-title">第十五章 录音设备里的铁链拖地声</div>
  
  <p>赵刚队长离奇失踪了。</p>
  
  <p>他最后出现的地方是钻探井边，值班保安说看见赵队长半夜对着井口说话："...三百年...还不够吗？"</p>
  
  <p>勘探队在井边发现赵刚的录音笔，里面有一段诡异音频：</p>
  
  <div class="warning">
    <p>录音内容：铁链拖地声持续3分钟，夹杂指甲刮擦声，最后是模糊嘶吼："血...土..."</p>
  </div>
  
  <p>林远反复听着录音，颈后赤痣越来越烫。他鬼使神差地走到钻探井边，对着黑暗的井口轻声道："爷爷？"</p>
  
  <p>井底突然传来清晰的回应："承...嗣..."</p>
  
  <p>老陈跑来拉住他："你疯了？这井有古怪！"</p>
  
  <p>林远转身，眼睛在月光下泛着红光："陈叔，我背后站着几个人？"</p>
  
  <p>老陈看向他身后空荡荡的坡地，汗毛倒竖："哪...哪有人？"</p>
  
  <p>"可我肩上搭着三只手啊..."林远的声音变得沙哑，"一只干枯，一只焦黑，还有一只...长满红毛..."</p>
</body>
</html>"""
    
    def _chapter_16(self):
        return """<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>第十六章 "快逃！它跟着胎记回来了..."</title>
  <link rel="stylesheet" type="text/css" href="../Styles/style.css"/>
</head>
<body>
  <div class="volume-title">卷四 地脉哭坟</div>
  <div class="chapter-title">第十六章 "快逃！它跟着胎记回来了..."</div>
  
  <p>勘探队营地一片死寂。</p>
  
  <p>老陈醒来时，发现帐篷内壁布满血手印。他冲出帐篷，只见其他队员的床铺上只剩人形灰烬。</p>
  
  <div class="warning">
    <p>营地监控：凌晨3点17分，血红色雾气吞没所有帐篷。</p>
  </div>
  
  <p>"林远！"老陈奔向唯一完好的帐篷。</p>
  
  <p>林远背对着他，正用血在镜子上画竖立的棺材。每口棺材里都有个扭曲的人影，其中一口赫然是赵刚队长！</p>
  
  <p>"它醒了。"林远的声音重叠着三个音调，"血棺土养尸百年，该还债了。"</p>
  
  <p>老陈瞥见镜子倒影——林远背后站着三个影子：干尸、焦尸、红毛血尸！</p>
  
  <p>"快逃..."林远突然转身，双眼赤红如血，"它跟着胎记回来了...告诉所有人...远离赤痣者..."</p>
  
  <p>话音未落，三只鬼手同时插入林远后背。血雾爆开，老陈最后看见的是林远颈后赤痣裂开，变成一张嘶吼的嘴：</p>
  
  <p style="text-align: center; font-size: 1.2em; color: #8b0000;">
    血债血偿！
  </p>
  
  <p>老陈狂奔下山，背后传来铁链拖地声。他不敢回头，因为每次回头，那声音就更近一分...</p>
</body>
</html>"""
    
    def _postscript_xhtml(self):
        return """<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>后记：民俗学者手札</title>
  <link rel="stylesheet" type="text/css" href="../Styles/style.css"/>
</head>
<body>
  <h1>后记：民俗学者手札</h1>
  
  <p>血棺葬的传说在湘西、闽北、粤东等地均有变体流传，核心禁忌始终围绕三点：</p>
  
  <div class="warning">
    <p>一忌血土：赤红如血之土，多含铁质氧化成分，古人视为"地脉流血"</p>
    <p>二忌竖葬：违背"入土为安"自然法则，易致"尸立为煞"</p>
    <p>三忌速发：风水讲究"润物无声"，强求暴富必遭反噬</p>
  </div>
  
  <p>2018年，笔者在湘西凤凰县采集到一则相似传说：</p>
  
  <blockquote>
    "李姓商人将父棺倒竖于朱砂矿脉，七日后全家暴毙，唯幼子幸存却浑身长满红癣..."
  </blockquote>
  
  <p>现代科学解释：朱砂含汞，污染水土致汞中毒，红癣实为汞过敏皮疹。</p>
  
  <p>然民俗之价值，不在真假，而在警示——</p>
  
  <h3 style="text-align: center; color: #8b0000;">贪穴者，绝嗣；逆天者，天诛！</h3>
  
  <p>跋：老陈余生都在逃亡，每晚都听到铁链声。他最终自尽于精神病院，遗书仅一行字：</p>
  
  <p style="text-align: center; font-style: italic;">"它找到下一个赤痣者了。"</p>
</body>
</html>"""
    
    # ================== 图片生成函数 ==================
    # 注：实际应用中应替换为真实图片数据
    def _generate_cover_image(self):
        """生成封面图片（占位）"""
        from PIL import Image, ImageDraw, ImageFont
        img = Image.new('RGB', (800, 1200), color=(30, 0, 0))
        d = ImageDraw.Draw(img)
        
        # 绘制棺材轮廓
        d.rectangle([200, 400, 600, 900], outline=(139, 0, 0), width=5)
        
        # 添加标题
        try:
            font = ImageFont.truetype("simhei.ttf", 60)
        except:
            font = ImageFont.load_default()
        d.text((100, 200), "血棺葬", font=font, fill=(200, 0, 0))
        d.text((250, 300), "玄枵 著", font=font, fill=(150, 0, 0))
        
        # 添加血滴效果
        for _ in range(50):
            x = random.randint(100, 700)
            y = random.randint(500, 1100)
            d.ellipse([x, y, x+10, y+10], fill=(200, 0, 0))
        
        # 保存为字节流
        from io import BytesIO
        img_byte_arr = BytesIO()
        img.save(img_byte_arr, format='JPEG')
        return img_byte_arr.getvalue()
    
    def _generate_blood_soil_image(self):
        """生成血土图片（占位）"""
        from PIL import Image
        img = Image.new('RGB', (600, 400), color=(100, 0, 0))
        
        # 添加纹理
        for _ in range(1000):
            x = random.randint(0, 599)
            y = random.randint(0, 399)
            img.putpixel((x, y), (150 + random.randint(0, 50), random.randint(0, 30), random.randint(0, 30)))
        
        # 添加碎骨
        for _ in range(50):
            x = random.randint(50, 550)
            y = random.randint(50, 350)
            for i in range(5):
                for j in range(5):
                    if random.random() > 0.7:
                        img.putpixel((x+i, y+j), (220, 220, 220))
        
        from io import BytesIO
        img_byte_arr = BytesIO()
        img.save(img_byte_arr, format='JPEG')
        return img_byte_arr.getvalue()
    
    def _generate_coffin_sketch(self):
        """生成棺材示意图（占位）"""
        from PIL import Image, ImageDraw
        img = Image.new('RGB', (500, 700), color=(240, 240, 240))
        d = ImageDraw.Draw(img)
        
        # 绘制竖棺
        d.rectangle([150, 100, 350, 600], outline=(0, 0, 0), width=3)
        
        # 绘制血土
        d.rectangle([100, 600, 400, 650], fill=(100, 0, 0))
        
        # 标注
        d.text((180, 620), "血棺土", fill=(100, 0, 0))
        d.line([(250, 600), (250, 650)], fill=(0, 0, 0), width=2)
        
        from io import BytesIO
        img_byte_arr = BytesIO()
        img.save(img_byte_arr, format='JPEG')
        return img_byte_arr.getvalue()


# 创建并生成完整的.epub文件
if __name__ == "__main__":
    print("正在生成《血棺葬》完整小说...")
    start_time = time.time()
    
    novel = BloodCoffinNovel()
    epub_path = novel.create_epub()
    
    end_time = time.time()
    print(f"生成完成！文件保存至: {epub_path}")
    print(f"耗时: {end_time - start_time:.2f}秒")
    print("文件大小: {:.2f}MB".format(os.path.getsize(epub_path) / (1024 * 1024)))
