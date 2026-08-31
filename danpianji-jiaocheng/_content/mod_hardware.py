"""Chapter content definitions."""

from .helpers import chapter

CHAPTERS = {
    "硬件/01-开发板与工具.html": chapter(
        '硬件 01：开发板与工具',
        '硬件入门',
        '硬件',
        """<blockquote><p>认识开发板组成，配齐工具，完成 Blink。</p></blockquote><hr>
<h2>1. 开发板是什么</h2>
<p>MCU + 最小外围（晶振、LDO、USB-UART、LED/按键）+ 排针。降低入门门槛。</p>
<h2>2. 类型对比</h2>
<table><thead><tr><th>类型</th><th>代表</th><th>特点</th></tr></thead><tbody><tr><td>Wi-Fi/BLE</td><td>ESP32-DevKitC</td><td>IoT 首选</td></tr><tr><td>工业</td><td>STM32 Nucleo</td><td>外设全+ST-Link</td></tr><tr><td>BLE</td><td>nRF52840 DK</td><td>低功耗</td></tr><tr><td>极简</td><td>Arduino Uno</td><td>16MHz 8bit</td></tr></tbody></table>
<h2>3. 工具清单</h2>
<table><thead><tr><th>工具</th><th>必须</th><th>用途</th></tr></thead><tbody><tr><td>ESP32 开发板</td><td>✅</td><td>主平台</td></tr><tr><td>面包板+线</td><td>✅</td><td>免焊实验</td></tr><tr><td>万用表</td><td>✅</td><td>测电压通断</td></tr><tr><td>烙铁</td><td>可选</td><td>焊接</td></tr><tr><td>逻辑分析仪</td><td>可选</td><td>协议解码</td></tr></tbody></table>
<h2>4. 第一次 Blink</h2>
<pre><code class="language-c">void setup(){ pinMode(2,OUTPUT); Serial.begin(115200);}
void loop(){ digitalWrite(2,!digitalRead(2)); delay(500); Serial.println("blink");}</code></pre>
<div class="tip-box">💡 ESP32-DevKitC 约30元，IoT+iOS 一块板够用。</div>
<h2>常见问题</h2>
<h3>开发板=芯片?</h3><p>板=芯片+外围+USB。</p>
<h3>Mac?</h3><p>完全支持。</p>
<h3>兼容板?</h3><p>可以，查驱动。</p>
<h2>本章小结</h2><ul>
<li>开发板降门槛</li>
<li>ESP32 IoT首选</li>
<li>万用表必备</li>
<li>Blink 第一步</li>
</ul>
<p><strong>下一步：</strong> <a href="02-万用表与焊接入门.html">02-万用表</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "硬件/02-万用表与焊接入门.html": chapter(
        '硬件 02：万用表与焊接入门',
        '硬件入门',
        '硬件',
        """<blockquote><p>万用表三板斧，焊接安全，排查短路。</p></blockquote><hr>
<h2>1. 万用表三档</h2>
<table><thead><tr><th>档位</th><th>用途</th><th>ESP32 期望</th></tr></thead><tbody><tr><td>DC V</td><td>测电压</td><td>3.3V/5V</td></tr><tr><td>通断</td><td>测连线</td><td>蜂鸣</td></tr><tr><td>Ω</td><td>测电阻</td><td>220Ω LED</td></tr></tbody></table>
<h2>2. 安全红线</h2>
<ul><li>短路 VCC-GND 烧芯片</li><li>5V 进 3.3V GPIO 永久损坏</li><li>锂电池必须保护板</li><li>220V 继电器用合规模块</li></ul>
<h2>3. 焊接五步</h2>
<pre><code class="language-text">1.烙铁350°C 2.加热焊盘 3.送锡 4.停2秒 5.移烙铁</code></pre>
<h2>4. 虚焊排查</h2>
<p>通断档测焊点；LED 不亮先测 GPIO 电压。</p>
<div class="tip-box">💡 先练废板再焊项目。</div>
<div class="tip-box" style="border-color:#ff6b6b;background:rgba(255,107,107,.08)">⚠️ 锂电池必须保护板，勿短路。</div>
<h2>常见问题</h2>
<h3>表笔接法?</h3><p>黑GND红测点。</p>
<h3>虚焊?</h3><p>通断档+晃动看阻值。</p>
<h3>焊锡?</h3><p>0.8mm 含铅易上手。</p>
<h2>本章小结</h2><ul>
<li>万用表三板斧</li>
<li>ESP32仅3.3V</li>
<li>安全红线牢记</li>
<li>焊接需练习</li>
</ul>
<p><strong>下一步：</strong> <a href="03-原理图阅读入门.html">03-原理图</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "硬件/03-原理图阅读入门.html": chapter(
        '硬件 03：原理图阅读入门',
        '硬件入门',
        '硬件',
        """<blockquote><p>读原理图定位引脚，符号识别，四步阅读法。</p></blockquote><hr>
<h2>1. 为何重要</h2>
<p>原理图 = 硬件 API 文档。不知道 GPIO2 接什么，代码写对也白搭。</p>
<h2>2. 符号</h2>
<table><thead><tr><th>符号</th><th>含义</th></tr></thead><tbody><tr><td>R</td><td>电阻</td></tr><tr><td>C</td><td>电容</td></tr><tr><td>D/LED</td><td>二极管/LED</td></tr><tr><td>U</td><td>芯片</td></tr><tr><td>VCC/GND</td><td>电源地</td></tr></tbody></table>
<h2>3. 四步阅读</h2>
<pre><code class="language-text">1.找MCU芯片 2.看电源树(LDO/去耦) 3.跟GPIO到外围 4.看通信(UART/I2C)</code></pre>
<h2>4. 获取途径</h2>
<p>厂商 GitHub/Wiki、立创EDA 开源、DevKit PDF 随板附赠。</p>
<div class="tip-box">💡 PDF 对照实物板最快建立空间感。</div>
<h2>常见问题</h2>
<h3>哪下载?</h3><p>乐鑫/ST 官网 GitHub。</p>
<h3>GPIO2=LED?</h3><p>以原理图为准。</p>
<h3>立创EDA?</h3><p>免费在线画/看。</p>
<h2>本章小结</h2><ul>
<li>原理图是硬件API</li>
<li>先MCU后电源</li>
<li>GPIO查图不猜</li>
<li>立创EDA开源多</li>
</ul>
<p><strong>下一步：</strong> <a href="04-PCB入门.html">04-PCB</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "硬件/04-PCB入门.html": chapter(
        '硬件 04：PCB 入门',
        '硬件入门',
        '硬件',
        """<blockquote><p>面包板拓扑，PCB 术语，打样流程。</p></blockquote><hr>
<pre><code class="language-c">// 本章配套：在 DevKit 上验证所学概念
void setup() { Serial.begin(115200); }
void loop() { /* 实验代码 */ }</code></pre>
<h2>1. 面包板</h2>
<p>中间槽两侧不通，上下轨连通。适合 MHz 以下原型。</p>
<h2>2. PCB 术语</h2>
<table><thead><tr><th>术语</th><th>含义</th></tr></thead><tbody><tr><td>丝印</td><td>白色文字标识</td></tr><tr><td>铜箔</td><td>走线导电</td></tr><tr><td>过孔</td><td>层间连接</td></tr><tr><td>焊盘</td><td>元件焊接点</td></tr></tbody></table>
<h2>3. 设计流程</h2>
<ol><li>原理图</li><li>PCB 布局</li><li>DRC 检查</li><li>嘉立创打样</li></ol>
<h2>4. 何时上 PCB</h2>
<p>面包板验证功能后；频率>1MHz 或要量产时。</p>
<div class="tip-box">💡 验证后 PCB，几十元打样 5 片。</div>
<h2>常见问题</h2>
<h3>面包板极限?</h3><p>高频/大电流需PCB。</p>
<h3>打样费?</h3><p>5片几十元包邮。</p>
<h3>飞线?</h3><p>调试补线技巧。</p>
<h2>本章小结</h2><ul>
<li>面包板做实验</li>
<li>验证后PCB</li>
<li>懂丝印过孔焊盘</li>
<li>嘉立创打样便宜</li>
</ul>
<p><strong>下一步：</strong> <a href="05-电源设计.html">05-电源</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "硬件/05-电源设计.html": chapter(
        '硬件 05：电源设计',
        '硬件入门',
        '硬件',
        """<blockquote><p>LDO/DC-DC，ESP32 供电，去耦与 Brownout。</p></blockquote><hr>
<h2>1. 电源树</h2>
<pre><code class="language-text">USB 5V → LDO(AMS1117-3.3) → 3.3V → ESP32
         → 100nF+10µF 去耦</code></pre>
<h2>2. LDO vs DC-DC</h2>
<table><thead><tr><th>类型</th><th>优点</th><th>缺点</th></tr></thead><tbody><tr><td>LDO</td><td>简单低纹波</td><td>效率低发热</td></tr><tr><td>DC-DC</td><td>高效</td><td>纹波/EMI复杂</td></tr></tbody></table>
<h2>3. ESP32 峰值</h2>
<p>Wi-Fi 发射瞬间可达 500mA+，USB 500mA 够用但 LDO 需散热，建议 1117-1A 以上。</p>
<h2>4. Brownout</h2>
<p>电压过低芯片复位。电池项目注意放电曲线+低压检测。</p>
<div class="tip-box">💡 供电不稳表现为 Wi-Fi 断连、ADC 跳变、随机复位。</div>
<div class="tip-box" style="border-color:#ff6b6b;background:rgba(255,107,107,.08)">⚠️ 锂电池必须保护板。</div>
<h2>常见问题</h2>
<h3>Brownout?</h3><p>低压自动复位保护。</p>
<h3>电池方案?</h3><p>LiPo+保护板+LDO。</p>
<h3>纹波影响?</h3><p>干扰 Wi-Fi/ADC。</p>
<h2>本章小结</h2><ul>
<li>供电是基础</li>
<li>Wi-Fi峰值500mA</li>
<li>去耦电容必须</li>
<li>电池加保护板</li>
</ul>
<p><strong>下一步：</strong> <a href="06-元件选型.html">06-选型</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "硬件/06-元件选型.html": chapter(
        '硬件 06：元件选型',
        '硬件入门',
        '硬件',
        """<blockquote><p>MCU/传感器/被动件 BOM 选型，LCSC 供货。</p></blockquote><hr>
<pre><code class="language-c">// 本章配套：在 DevKit 上验证所学概念
void setup() { Serial.begin(115200); }
void loop() { /* 实验代码 */ }</code></pre>
<h2>1. MCU 选型</h2>
<table><thead><tr><th>需求</th><th>推荐</th></tr></thead><tbody><tr><td>IoT+App</td><td>ESP32-S3</td></tr><tr><td>工业</td><td>STM32F407</td></tr><tr><td>超低功耗</td><td>nRF52840</td></tr></tbody></table>
<h2>2. 传感器</h2>
<table><thead><tr><th>功能</th><th>型号</th><th>接口</th></tr></thead><tbody><tr><td>温湿度</td><td>DHT22/BME280</td><td>单总线/I2C</td></tr><tr><td>距离</td><td>HC-SR04</td><td>GPIO</td></tr><tr><td>光照</td><td>BH1750</td><td>I2C</td></tr><tr><td>屏</td><td>SSD1306</td><td>I2C</td></tr></tbody></table>
<h2>3. BOM 示例</h2>
<table><thead><tr><th>位号</th><th>型号</th><th>说明</th></tr></thead><tbody><tr><td>U1</td><td>ESP32-WROOM</td><td>主控</td></tr><tr><td>U2</td><td>AMS1117-3.3</td><td>LDO</td></tr><tr><td>R1</td><td>220Ω</td><td>LED限流</td></tr></tbody></table>
<h2>4. 模块 vs 芯片</h2>
<p>原型用模块（DHT 模块、继电器模块）快；量产用芯片降 BOM。</p>
<div class="tip-box">💡 LCSC 查库存+下载 datasheet 是工程师日常。</div>
<h2>常见问题</h2>
<h3>LCSC?</h3><p>立创商城元器件。</p>
<h3>0805?</h3><p>贴片封装尺寸。</p>
<h3>模块优势?</h3><p>免焊接快速验证。</p>
<h2>本章小结</h2><ul>
<li>先列需求再选型</li>
<li>原型用模块</li>
<li>LCSC查库存</li>
<li>BOM留20%余量</li>
</ul>
<p><strong>下一步：</strong> <a href="../入门实战/01-第一个程序点灯.html">入门实战</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
}
