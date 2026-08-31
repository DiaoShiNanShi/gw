#!/usr/bin/env python3
"""One-shot generator for esp32_rtos_lab.py — run once then delete."""
from pathlib import Path
import textwrap

OUT = Path(__file__).parent / "esp32_rtos_lab.py"


def ch(path, title, tag, module, body):
    return (path, title, tag, module, body)


def mk(blockquote, parts, tip, nxt_href, nxt_title):
    """parts: list of (h2, body_html)"""
    lines = [f'<blockquote><p>{blockquote}</p></blockquote>']
    for h2, body in parts:
        lines.append(f"<h2>{h2}</h2>\n{body.strip()}")
    lines.append(f'<div class="tip-box">{tip}</div>')
    lines.append(
        "<h2>小结</h2>\n"
        "<p>建议把本章表格打印或存笔记，动手实验时对照检查。"
        "遇到现象和文档不一致，先用万用表/串口确认硬件与接线。</p>"
    )
    lines.append(
        f'<p><strong>下一步：</strong> <a href="{nxt_href}">{nxt_title}</a></p>'
    )
    return "\n".join(lines)


CHAPTERS = []

# ── 硬件入门 (6) ──────────────────────────────────────────────
CHAPTERS.append(ch(
    "硬件/01-开发板与工具.html", "硬件 01：开发板与工具", "硬件入门", "硬件",
    mk(
        "学习目标：认识主流开发板形态，配齐工具链，完成第一次安全上电与 Blink 例程。",
        [
            ("1. 开发板是什么？", """
<p><strong>开发板 = MCU + 最小外围 + USB/排针</strong>，让初学者跳过 PCB 设计直接写程序。和 iPhone 主板类似，只是把「能跑 iOS 的大系统」换成「专控 GPIO 的小系统」。</p>
<table>
<thead><tr><th>类型</th><th>代表型号</th><th>适合场景</th></tr></thead>
<tbody>
<tr><td>Wi-Fi/BLE 一体</td><td>ESP32-DevKitC</td><td>IoT、对接 iOS App</td></tr>
<tr><td>工业 ARM</td><td>STM32F103 最小系统板</td><td>电机、工控、求职</td></tr>
<tr><td>超低功耗 BLE</td><td>nRF52840 DK</td><td>Beacon、可穿戴</td></tr>
</tbody>
</table>"""),
            ("2. 必备硬件清单", """
<table>
<thead><tr><th>物品</th><th>用途</th><th>必须？</th></tr></thead>
<tbody>
<tr><td>ESP32 开发板 + 数据线</td><td>主控、烧录、供电</td><td>✅</td></tr>
<tr><td>面包板、杜邦线</td><td>免焊搭电路</td><td>✅</td></tr>
<tr><td>LED、220Ω 电阻、按键</td><td>GPIO 实验</td><td>✅</td></tr>
<tr><td>数字万用表</td><td>测电压/通断</td><td>✅</td></tr>
<tr><td>CP2102 USB-TTL</td><td>无 USB 板子的串口</td><td>推荐</td></tr>
</tbody>
</table>"""),
            ("3. 软件环境（Mac 示例）", """
<pre><code>brew install --cask arduino-ide
# 附加开发板 URL（ESP32）：
# https://espressif.github.io/arduino-esp32/package_esp32_index.json

# 或专业路线：VS Code + PlatformIO 插件</code></pre>
<table>
<thead><tr><th>工具</th><th>何时用</th></tr></thead>
<tbody>
<tr><td>Arduino IDE</td><td>第一周快速点灯、跑例程</td></tr>
<tr><td>PlatformIO</td><td>多库、多板型项目管理</td></tr>
<tr><td>ESP-IDF</td><td>FreeRTOS、Wi-Fi 深度开发</td></tr>
</tbody>
</table>"""),
            ("4. 首次上电与 Blink", """
<ol>
<li>插 USB，确认板载电源灯亮</li>
<li>万用表测 3V3–GND ≈ 3.3V</li>
<li>Arduino 选板 <code>ESP32 Dev Module</code>，端口选 <code>/dev/cu.usbserial-*</code></li>
<li>上传 Blink，观察 GPIO2 板载 LED 闪烁</li>
</ol>
<pre><code>void setup() { pinMode(2, OUTPUT); }
void loop() {
  digitalWrite(2, HIGH); delay(500);
  digitalWrite(2, LOW);  delay(500);
}</code></pre>"""),
        ],
        "💡 <strong>建议</strong>：第一块板选 ESP32-DevKitC（约 30 元），Wi-Fi + BLE 一步到位，后面 iOS 联动不用换硬件。",
        "02-万用表与焊接入门.html", "02-万用表与焊接入门",
    ),
))

CHAPTERS.append(ch(
    "硬件/02-万用表与焊接入门.html", "硬件 02：万用表与焊接入门", "硬件入门", "硬件",
    mk(
        "学习目标：会用万用表排查 80% 硬件问题，掌握基础焊接与安全规范。",
        [
            ("1. 万用表三档必会", """
<table>
<thead><tr><th>档位</th><th>测什么</th><th>典型场景</th></tr></thead>
<tbody>
<tr><td>直流电压 DC V</td><td>3.3V / 5V 供电</td><td>确认 LDO 输出正常</td></tr>
<tr><td>通断蜂鸣 Ω</td><td>线路是否连通</td><td>杜邦线是否插紧</td></tr>
<tr><td>电阻 Ω</td><td>电阻阻值</td><td>限流电阻是否接错</td></tr>
</tbody>
</table>
<p>测电压时黑表笔接 GND，红表笔接测试点；测通断时先<strong>断电</strong>。</p>"""),
            ("2. 安全红线", """
<ul>
<li>⚠️ VCC 与 GND 短路 → 芯片发热、USB 口保护触发</li>
<li>⚠️ 5V 信号直接进 ESP32 GPIO → 永久损坏</li>
<li>⚠️ 带电焊接 → 虚焊 + 触电风险</li>
<li>⚠️ 人体静电 → 触摸金属壳放电后再摸芯片</li>
</ul>"""),
            ("3. 焊接五步法", """
<ol>
<li>烙铁 320°C，湿海绵清洁烙铁头</li>
<li>焊盘 + 引脚同时加热约 2 秒</li>
<li>送锡丝，焊点呈光亮圆锥形</li>
<li>先移锡丝，再停 1 秒移烙铁</li>
<li>目视 + 万用表通断档复检</li>
</ol>
<pre><code>合格焊点特征：
  ✓ 表面光亮、浸润良好
  ✗ 尖塔、虚焊、连锡（短路）</code></pre>"""),
            ("4. 常见故障速查", """
<table>
<thead><tr><th>现象</th><th>可能原因</th><th>排查</th></tr></thead>
<tbody>
<tr><td>板子发烫</td><td>电源短路</td><td>断电，万用表测 VCC–GND 电阻</td></tr>
<tr><td>无法烧录</td><td>驱动/线材/端口</td><td>换数据线、按住 BOOT 再烧录</td></tr>
<tr><td>3.3V 只有 2V</td><td>负载过大或 LDO 坏</td><td>断开外设重测</td></tr>
</tbody>
</table>"""),
        ],
        "💡 焊锡含铅版本更好焊，无铅更环保；初学者选 0.8mm 含铅锡丝 + 936 恒温烙铁即可。",
        "03-原理图阅读入门.html", "03-原理图阅读入门",
    ),
))

CHAPTERS.append(ch(
    "硬件/03-原理图阅读入门.html", "硬件 03：原理图阅读入门", "硬件入门", "硬件",
    mk(
        "学习目标：能独立阅读开发板原理图，定位 LED、按键、电源、通信接口所连引脚。",
        [
            ("1. 为什么要看原理图？", """
<p>原理图是硬件的「API 文档」。不看图就接线，等于不看 Header 乱调 SDK。买模块时厂商 PDF 里一定有原理图或应用电路。</p>"""),
            ("2. 常见符号速查", """
<table>
<thead><tr><th>符号/标注</th><th>含义</th></tr></thead>
<tbody>
<tr><td>R、C、L</td><td>电阻、电容、电感</td></tr>
<tr><td>Q / U</td><td>三极管、集成电路</td></tr>
<tr><td>VCC / 3V3 / GND</td><td>电源正、3.3V、地</td></tr>
<tr><td>→|— 或 LED 图形</td><td>二极管，注意方向</td></tr>
<tr><td>XTAL / Y</td><td>晶振</td></tr>
</tbody>
</table>"""),
            ("3. 阅读四步法", """
<ol>
<li>找 MCU 芯片（引脚最多，通常在中央）</li>
<li>追电源：USB/VIN → LDO → 3V3 去耦电容 → 各模块</li>
<li>追 GPIO：LED 接哪一脚、按键是否上拉</li>
<li>追通信：I2C 的 SDA/SCL、UART 的 TX/RX 编号</li>
</ol>
<pre><code>示例（ESP32 DevKitC 常见）：
  板载 LED  → GPIO2
  按键 BOOT → GPIO0（低电平进下载模式）
  UART0     → GPIO1(TX) / GPIO3(RX)</code></pre>"""),
            ("4. 工具推荐", """
<table>
<thead><tr><th>工具</th><th>用途</th></tr></thead>
<tbody>
<tr><td>立创 EDA</td><td>免费在线看/画原理图</td></tr>
<tr><td>LCSC 商城</td><td>对照位号买元件</td></tr>
<tr><td>厂商 GitHub</td><td>下载官方 PDF 原理图</td></tr>
</tbody>
</table>"""),
        ],
        "💡 看原理图时把 PDF 和实物板<strong>对照着看</strong>，比纯读图快十倍。",
        "04-PCB与面包板实战.html", "04-PCB与面包板实战",
    ),
))

CHAPTERS.append(ch(
    "硬件/04-PCB与面包板实战.html", "硬件 04：PCB 与面包板实战", "硬件入门", "硬件",
    mk(
        "学习目标：理解面包板拓扑与 PCB 层结构，完成 LED+按键电路搭建与简单打板流程认知。",
        [
            ("1. 面包板结构", """
<p>面包板中间槽两侧<strong>不连通</strong>（适合 DIP 芯片跨接）。红色/蓝色条通常是整列电源轨。</p>
<pre><code>  +轨 ─────────────────
  a b c d e   f g h i j
  同一行 a–e 内部连通，e 与 f 不连通
  -轨 ─────────────────</code></pre>"""),
            ("2. LED 实验电路", """
<pre><code>3V3 ──[220Ω]── LED(+) ── LED(-) ── GPIO2
GPIO2 输出 LOW 时 LED 亮（灌电流接法，依板而异）</code></pre>
<table>
<thead><tr><th>元件</th><th>参数</th><th>说明</th></tr></thead>
<tbody>
<tr><td>限流电阻</td><td>220Ω–1kΩ</td><td>无电阻会烧 LED/GPIO</td></tr>
<tr><td>LED</td><td>3mm/5mm</td><td>长脚为正极</td></tr>
</tbody>
</table>"""),
            ("3. PCB 是什么？", """
<p><strong>PCB = 印刷电路板</strong>，把导线、焊盘、过孔做在 FR4 板上。双层板有 Top/Bottom 铜箔，四层板增加内电层。</p>
<table>
<thead><tr><th>术语</th><th>含义</th></tr></thead>
<tbody>
<tr><td>丝印层</td><td>白色文字、元件位号</td></tr>
<tr><td>阻焊层</td><td>绿色漆，防短路</td></tr>
<tr><td>过孔 VIA</td><td>连接不同层</td></tr>
<tr><td>飞线</td><td>手工补线，调试常用</td></tr>
</tbody>
</table>"""),
            ("4. 从原理图到 PCB（认知）", """
<ol>
<li>立创 EDA 画原理图 → ERC 电气检查</li>
<li>一键转 PCB → 布局、布线、铺铜</li>
<li>DRC 设计规则检查 → 导出 Gerber</li>
<li>嘉立创/捷配下单打样（5 片 10×10 约几十元）</li>
</ol>"""),
        ],
        "💡 实验阶段用面包板；验证稳定后再画 PCB，可省反复改板的冤枉钱。",
        "05-电源设计与LDO.html", "05-电源设计与 LDO",
    ),
))

CHAPTERS.append(ch(
    "硬件/05-电源设计与LDO.html", "硬件 05：电源设计与 LDO", "硬件入门", "硬件",
    mk(
        "学习目标：理解 LDO/DC-DC 区别，为 ESP32 设计稳定 3.3V 供电，避免 brownout 复位。",
        [
            ("1. 电源树概念", """
<pre><code>USB 5V / 锂电池 3.7V
        │
    [LDO 或 DC-DC]
        │
      3.3V ──→ ESP32 / 传感器 / OLED
      GND  ──→ 公共地</code></pre>
<p>类比 iOS：<strong>稳压器 = 给敏感外设供电的 UPS</strong>，纹波大会导致 Wi-Fi 断连、ADC 乱跳。</p>"""),
            ("2. LDO vs DC-DC", """
<table>
<thead><tr><th>类型</th><th>优点</th><th>缺点</th><th>典型芯片</th></tr></thead>
<tbody>
<tr><td>LDO</td><td>电路简单、噪声低</td><td>压差大时效率低、发热</td><td>AMS1117-3.3、XC6206</td></tr>
<tr><td>DC-DC Buck</td><td>效率高、适合电池</td><td>电路复杂、有开关噪声</td><td>MP2307、TPS62133</td></tr>
</tbody>
</table>"""),
            ("3. ESP32 供电要点", """
<ul>
<li>峰值电流 Wi-Fi 发射时可达 <strong>500mA+</strong>，USB 500mA 勉强够，建议独立 LDO 1A 能力</li>
<li>3V3 靠近芯片放 <strong>100nF + 10µF</strong> 去耦电容</li>
<li>Brownout 检测：电压低于阈值自动复位，串口可见 <code>Brownout detector was triggered</code></li>
</ul>
<pre><code>// ESP-IDF 可调 brownout 阈值（谨慎）
#include "soc/soc.h"
#include "driver/rtc_cntl.h"
// 生产环境应优先改善硬件供电而非关闭检测</code></pre>"""),
            ("4. 电池供电简图", """
<table>
<thead><tr><th>方案</th><th>适用</th></tr></thead>
<tbody>
<tr><td>18650 + TP4056 充电 + Boost 5V + LDO 3.3V</td><td>便携项目</td></tr>
<tr><td>LiPo 3.7V + 低压差 LDO（XC6206）</td><td>轻量 IoT</td></tr>
<tr><td>USB 5V 直供开发板</td><td>桌面调试</td></tr>
</tbody>
</table>"""),
        ],
        "⚠️ <strong>警告</strong>：锂电池必须加保护板（过充/过放/短路），裸 cell 充电有起火风险。",
        "06-元器件选型手册.html", "06-元器件选型手册",
    ),
))

CHAPTERS.append(ch(
    "硬件/06-元器件选型手册.html", "硬件 06：元器件选型手册", "硬件入门", "硬件",
    mk(
        "学习目标：按项目需求快速选 MCU、传感器、电源、接口芯片，建立可复用的 BOM 思维。",
        [
            ("1. MCU 选型矩阵", """
<table>
<thead><tr><th>需求</th><th>推荐</th><th>理由</th></tr></thead>
<tbody>
<tr><td>Wi-Fi + BLE + App</td><td>ESP32</td><td>生态、价格、例程</td></tr>
<tr><td>超低功耗传感节点</td><td>ESP32-C3 / nRF52</td><td>Deep Sleep µA 级</td></tr>
<tr><td>电机 PWM / 工业</td><td>STM32F4/G4</td><td>定时器、ADC 丰富</td></tr>
<tr><td>成本极限</td><td>ESP8266 / STM32F103</td><td>量产几元钱</td></tr>
</tbody>
</table>"""),
            ("2. 传感器与执行器", """
<table>
<thead><tr><th>功能</th><th>型号</th><th>接口</th></tr></thead>
<tbody>
<tr><td>温湿度</td><td>DHT22 / SHT30</td><td>单总线 / I2C</td></tr>
<tr><td>距离</td><td>HC-SR04 / VL53L0X</td><td>GPIO / I2C</td></tr>
<tr><td>显示屏</td><td>SSD1306 OLED</td><td>I2C</td></tr>
<tr><td>舵机</td><td>SG90</td><td>PWM 50Hz</td></tr>
</tbody>
</table>"""),
            ("3. 被动元件与接口", """
<ul>
<li>电阻：0805/0603 贴片通用；LED 限流 220Ω–1kΩ</li>
<li>电容：100nF 去耦必备；电解 10µF 储能</li>
<li>电平转换：TXS0108E（3.3V↔5V）</li>
<li>驱动：ULN2003（小继电器/步进）、DRV8833（电机）</li>
</ul>"""),
            ("4. BOM 示例（智能风扇项目）", """
<table>
<thead><tr><th>位号</th><th>型号</th><th>数量</th><th>单价参考</th></tr></thead>
<tbody>
<tr><td>U1</td><td>ESP32-DevKitC</td><td>1</td><td>¥28</td></tr>
<tr><td>Q1</td><td>IRF520 MOSFET</td><td>1</td><td>¥2</td></tr>
<tr><td>Sensor</td><td>DHT22</td><td>1</td><td>¥8</td></tr>
<tr><td>Fan</td><td>5V 小风扇</td><td>1</td><td>¥12</td></tr>
</tbody>
</table>"""),
        ],
        "💡 LCSC 搜型号 → 看「立创商城有货 + 数据手册」双确认，避免买到停产件。",
        "../入门实战/01-第一个程序点灯.html", "入门实战 01-第一个程序点灯",
    ),
))

# ── 入门实战 (10) ─────────────────────────────────────────────
_practice = [
    ("入门实战/01-第一个程序点灯.html", "入门实战 01：第一个程序点灯", "01-第一个程序点灯",
     "学习目标：写出嵌入式 Hello World——控制 GPIO 点亮 LED，理解 setup/loop 与引脚模式。",
     [
         ("1. 程序结构", """<p>Arduino 框架把 <code>main()</code> 藏起来了，你只写：</p>
<pre><code>void setup() { /* 上电执行一次 */ }
void loop()  { /* 反复执行 */ }</code></pre>
<p>类比 iOS：<code>setup</code> ≈ <code>application(_:didFinishLaunchingWithOptions:)</code>，<code>loop</code> ≈ 永不退出的 runloop。</p>"""),
         ("2. 接线", """<pre><code>ESP32 GPIO4 ──[220Ω]── LED+ ── LED- ── GND</code></pre>
<table><thead><tr><th>引脚模式</th><th>函数</th></tr></thead>
<tbody>
<tr><td>输出</td><td><code>pinMode(pin, OUTPUT)</code></td></tr>
<tr><td>写高/低</td><td><code>digitalWrite(pin, HIGH/LOW)</code></td></tr>
</tbody></table>"""),
         ("3. 完整代码", """<pre><code>const int LED = 4;
void setup() {
  pinMode(LED, OUTPUT);
  Serial.begin(115200);
  Serial.println("LED demo start");
}
void loop() {
  digitalWrite(LED, HIGH);
  delay(1000);
  digitalWrite(LED, LOW);
  delay(1000);
}</code></pre>"""),
         ("4. 排错", """<table><thead><tr><th>问题</th><th>检查</th></tr></thead>
<tbody>
<tr><td>不亮</td><td>LED 方向、电阻、GPIO 号</td></tr>
<tr><td>常亮不灭</td><td>代码是否上传成功</td></tr>
<tr><td>微亮</td><td>是否浮空输入，确认 OUTPUT 模式</td></tr>
</tbody></table>"""),
     ], "💡 改 delay 为 100ms，肉眼仍像常亮——为后面 PWM 呼吸灯埋伏笔。", "02-按键与中断.html", "02-按键与中断"),
    ("入门实战/02-按键与中断.html", "入门实战 02：按键与中断", "02-按键与中断",
     "学习目标：用内部上拉读按键，理解轮询 vs 中断，实现防抖。",
     [
         ("1. 按键电路", """<pre><code>GPIO15 ── 按键 ── GND
pinMode(15, INPUT_PULLUP);  // 未按下=HIGH，按下=LOW</code></pre>"""),
         ("2. 轮询方式", """<pre><code>void loop() {
  if (digitalRead(15) == LOW) {
    digitalWrite(2, !digitalRead(2));
    delay(200);  // 简单防抖
  }
}</code></pre>"""),
         ("3. 中断方式（ESP32 Arduino）", """<pre><code>void IRAM_ATTR onBtn() {
  // 中断里只做标志，别 Serial.println
}
void setup() {
  pinMode(15, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(15), onBtn, FALLING);
}
volatile bool flag = false;
void loop() {
  if (flag) { flag = false; /* 处理 */ }
}</code></pre>"""),
         ("4. 对比", """<table><thead><tr><th>方式</th><th>CPU</th><th>适用</th></tr></thead>
<tbody>
<tr><td>轮询</td><td>占用高</td><td>简单实验</td></tr>
<tr><td>中断</td><td>事件驱动</td><td>低功耗、快速响应</td></tr>
</tbody></table>"""),
     ], "💡 中断服务函数越短越好；复杂逻辑放到 loop 里用标志位处理。", "03-串口调试.html", "03-串口调试"),
    ("入门实战/03-串口调试.html", "入门实战 03：串口调试", "03-串口调试",
     "学习目标：用 UART 打印日志、接收 PC 命令，建立嵌入式「 NSLog 」习惯。",
     [
         ("1. 接线", """<pre><code>ESP32 TX(GPIO1) → USB-TTL RX
ESP32 RX(GPIO3) ← USB-TTL TX
GND ──────────── GND</code></pre>"""),
         ("2. 打印与格式化", """<pre><code>void setup() {
  Serial.begin(115200);
  while (!Serial) { ; }
  Serial.printf("Chip model: %s\\n", ESP.getChipModel());
}
void loop() {
  Serial.println("heartbeat");
  delay(2000);
}</code></pre>"""),
         ("3. 接收命令", """<pre><code>if (Serial.available()) {
  String cmd = Serial.readStringUntil('\\n');
  cmd.trim();
  if (cmd == "on")  digitalWrite(2, HIGH);
  if (cmd == "off") digitalWrite(2, LOW);
}</code></pre>"""),
         ("4. Mac 终端看串口", """<pre><code>ls /dev/cu.*
screen /dev/cu.usbserial-XXXX 115200
# Ctrl+A K 退出</code></pre>
<table><thead><tr><th>波特率</th><th>场景</th></tr></thead>
<tbody><tr><td>115200</td><td>ESP32 默认首选</td></tr>
<tr><td>921600</td><td>大量日志时</td></tr></tbody></table>"""),
     ], "💡 发布固件前用 <code>#ifdef DEBUG</code> 关掉冗长日志，省 Flash 也防泄露信息。", "04-PWM控制舵机.html", "04-PWM 控制舵机"),
    ("入门实战/04-PWM控制舵机.html", "入门实战 04：PWM 控制舵机", "04-PWM 控制舵机",
     "学习目标：理解 PWM 占空比，用 50Hz 信号驱动 SG90 舵机指定角度。",
     [
         ("1. 舵机信号", """<p>SG90 用 <strong>50Hz</strong> PWM，脉宽 1ms≈0°，1.5ms≈90°，2ms≈180°。</p>
<table><thead><tr><th>角度</th><th>脉宽</th></tr></thead>
<tbody>
<tr><td>0°</td><td>1000 µs</td></tr>
<tr><td>90°</td><td>1500 µs</td></tr>
<tr><td>180°</td><td>2000 µs</td></tr>
</tbody></table>"""),
         ("2. ESP32 LEDC PWM", """<pre><code>#include &lt;ESP32Servo.h&gt;
Servo myservo;
void setup() {
  myservo.attach(18);
  myservo.write(90);
}
void loop() {
  for (int a = 0; a &lt;= 180; a++) {
    myservo.write(a);
    delay(15);
  }
}</code></pre>"""),
         ("3. 供电注意", """<ul>
<li>舵机电流大，<strong>不要</strong>只从 ESP32 3V3 取电</li>
<li>独立 5V 供电，GND 与 ESP32 共地</li>
</ul>"""),
         ("4. 应用", """<p>云台、阀门、机械臂关节——配合 BLE 可从 iOS App 发角度值。</p>"""),
     ], "💡 舵机抖动时加 100µF 电容在 5V 旁，并检查 GND 是否共地。", "05-温湿度传感器.html", "05-温湿度传感器"),
    ("入门实战/05-温湿度传感器.html", "入门实战 05：温湿度传感器", "05-温湿度传感器",
     "学习目标：读取 DHT22 单总线数据，校验失败重试，串口输出温湿度。",
     [
         ("1. 选型", """<table><thead><tr><th>型号</th><th>精度</th><th>接口</th></tr></thead>
<tbody>
<tr><td>DHT11</td><td>低</td><td>单总线</td></tr>
<tr><td>DHT22</td><td>±0.5°C</td><td>单总线</td></tr>
<tr><td>SHT30</td><td>高</td><td>I2C</td></tr>
</tbody></table>"""),
         ("2. 接线与库", """<pre><code>DATA → GPIO4，VCC 3.3V，GND
#include &lt;DHT.h&gt;
DHT dht(4, DHT22);
void setup() { dht.begin(); Serial.begin(115200); }</code></pre>"""),
         ("3. 读取代码", """<pre><code>void loop() {
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  if (isnan(h) || isnan(t)) {
    Serial.println("DHT read fail, retry");
    return;
  }
  Serial.printf("T=%.1fC H=%.1f%%\\n", t, h);
  delay(2000);
}</code></pre>"""),
         ("4. 扩展", """<p>超阈值控制继电器/风扇——后面综合练习会用到。</p>"""),
     ], "💡 DHT 读数间隔建议 ≥2s，连续读会返回 NaN。", "06-OLED显示屏.html", "06-OLED 显示屏"),
    ("入门实战/06-OLED显示屏.html", "入门实战 06：OLED 显示屏", "06-OLED 显示屏",
     "学习目标：I2C 驱动 SSD1306 128×64 OLED，显示文字与简单图形。",
     [
         ("1. I2C 接线", """<pre><code>OLED SDA → GPIO21
OLED SCL → GPIO22
VCC 3.3V, GND</code></pre>"""),
         ("2. 初始化与文字", """<pre><code>#include &lt;Wire.h&gt;
#include &lt;Adafruit_SSD1306.h&gt;
Adafruit_SSD1306 display(128, 64, &amp;Wire, -1);
void setup() {
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  display.clearDisplay();
  display.setTextSize(1);
  display.setCursor(0, 0);
  display.println("Hello ESP32!");
  display.display();
}</code></pre>"""),
         ("3. 刷新策略", """<table><thead><tr><th>方式</th><th>说明</th></tr></thead>
<tbody>
<tr><td>全屏刷新</td><td><code>display.display()</code> 较慢</td></tr>
<tr><td>局部更新</td><td>只改变化区域省 CPU</td></tr>
</tbody></table>"""),
         ("4. 显示传感器数据", """<pre><code>display.clearDisplay();
display.printf("T: %.1f C", temp);
display.printf("\\nH: %.1f %%", hum);
display.display();</code></pre>"""),
     ], "💡 I2C 地址常见 0x3C 或 0x3D，扫描程序：<code>Wire.begin(); for(byte i=1;i&lt;127;i++) Wire.beginTransmission(i);</code>", "07-EEPROM存储.html", "07-EEPROM 存储"),
    ("入门实战/07-EEPROM存储.html", "入门实战 07：EEPROM 存储", "07-EEPROM 存储",
     "学习目标：用 Preferences/NVS 掉电保存配置，类比 iOS UserDefaults。",
     [
         ("1. 为什么需要？", """<p>Wi-Fi SSID、亮度档位、校准参数——重启后仍要保留。Flash 寿命有限，需减少擦写次数。</p>"""),
         ("2. Arduino Preferences", """<pre><code>#include &lt;Preferences.h&gt;
Preferences prefs;
void setup() {
  prefs.begin("myapp", false);
  int count = prefs.getInt("boot", 0);
  count++;
  prefs.putInt("boot", count);
  Serial.printf("Boot count: %d\\n", count);
}</code></pre>"""),
         ("3. 键值设计", """<table><thead><tr><th>Key</th><th>类型</th><th>示例</th></tr></thead>
<tbody>
<tr><td>wifi_ssid</td><td>String</td><td>家庭路由名</td></tr>
<tr><td>target_temp</td><td>float</td><td>风扇启动温度</td></tr>
</tbody></table>"""),
         ("4. 注意", """<ul>
<li>写入前 <code>prefs.begin(namespace, false)</code>，只读用 <code>true</code></li>
<li>大量数据用 SPIFFS/LittleFS 文件系统</li>
</ul>"""),
     ], "💡 同一 namespace 下 key 勿过长；频繁变化的数据放 RAM，定时批量写 Flash。", "08-ADC读取电位器.html", "08-ADC 读取电位器"),
    ("入门实战/08-ADC读取电位器.html", "入门实战 08：ADC 读取电位器", "08-ADC 读取电位器",
     "学习目标：用 ADC 读模拟电压，映射为 0–100 百分比控制 LED 亮度。",
     [
         ("1. ESP32 ADC 特性", """<p>ESP32 ADC1 在 Wi-Fi 工作时可用通道：GPIO32–39。分辨率默认 12bit（0–4095）。</p>"""),
         ("2. 电位器接线", """<pre><code>3V3 ── 电位器一端
GND ── 电位器另一端
GPIO34 ── 电位器中间抽头（仅输入脚）</code></pre>"""),
         ("3. 代码", """<pre><code>const int POT = 34;
void setup() {
  analogReadResolution(12);
  pinMode(2, OUTPUT);
}
void loop() {
  int raw = analogRead(POT);
  int duty = map(raw, 0, 4095, 0, 255);
  analogWrite(2, duty);
  Serial.printf("ADC=%d duty=%d\\n", raw, duty);
  delay(50);
}</code></pre>"""),
         ("4. 校准", """<p>ESP32 ADC 非线性，量产产品需 <code>esp_adc_cal</code> 或查表校准。</p>"""),
     ], "💡 GPIO34–39 只能输入，不能 <code>pinMode OUTPUT</code>。", "09-蜂鸣器播放旋律.html", "09-蜂鸣器播放旋律"),
    ("入门实战/09-蜂鸣器播放旋律.html", "入门实战 09：蜂鸣器播放 melody", "09-蜂鸣器播放旋律",
     "学习目标：无源蜂鸣器用 tone 产生方波，播放简单旋律。",
     [
         ("1. 有源 vs 无源", """<table><thead><tr><th>类型</th><th>特点</th></tr></thead>
<tbody>
<tr><td>有源</td><td>给电就响固定音，GPIO 高低即可</td></tr>
<tr><td>无源</td><td>需 PWM/方波驱动不同频率</td></tr>
</tbody></table>"""),
         ("2. 频率与音符", """<pre><code>#define NOTE_C4 262
#define NOTE_E4 330
#define NOTE_G4 392
int melody[] = { NOTE_C4, NOTE_E4, NOTE_G4 };
int duration[] = { 200, 200, 400 };</code></pre>"""),
         ("3. 播放循环", """<pre><code>void setup() { pinMode(25, OUTPUT); }
void loop() {
  for (int i = 0; i &lt; 3; i++) {
    tone(25, melody[i], duration[i]);
    delay(duration[i] + 50);
    noTone(25);
  }
  delay(1000);
}</code></pre>"""),
         ("4. 非阻塞思路", """<p>用 <code>millis()</code> 状态机代替 <code>delay</code>，以便同时处理按键/Wi-Fi。</p>"""),
     ], "💡 无源蜂鸣器别长时间满占空比，加 100Ω 限流或 NPN 驱动。", "10-综合练习智能风扇.html", "10-综合练习智能风扇"),
    ("入门实战/10-综合练习智能风扇.html", "入门实战 10：综合练习智能风扇", "10-综合练习智能风扇",
     "学习目标：整合 DHT22 + MOSFET 风扇 + OLED + NVS，完成温控小项目。",
     [
         ("1. 功能需求", """<ul>
<li>读取温湿度，OLED 显示</li>
<li>温度 &gt; 阈值 → PWM 加速风扇</li>
<li>阈值存 NVS，按键可调</li>
</ul>"""),
         ("2. 硬件", """<pre><code>DHT22 → GPIO4
风扇 5V ← MOSFET(IRF520) ← GPIO25 PWM
OLED I2C 21/22</code></pre>"""),
         ("3. 核心逻辑", """<pre><code>float target = prefs.getFloat("target", 28.0);
float t = dht.readTemperature();
int speed = (t > target) ? map(t, target, target+5, 80, 255) : 0;
speed = constrain(speed, 0, 255);
analogWrite(FAN_PIN, speed);</code></pre>"""),
         ("4. 验收", """<table><thead><tr><th>项</th><th>标准</th></tr></thead>
<tbody>
<tr><td>显示</td><td>OLED 实时温湿度</td></tr>
<tr><td>控制</td><td>升温风扇转速上升</td></tr>
<tr><td>记忆</td><td>重启阈值保留</td></tr>
</tbody></table>"""),
     ], "💡 做完可拍视频放作品集，并加 BLE 让 iOS 调阈值——衔接 ESP32 专题。", "../ESP32/01-ESP32双核架构.html", "ESP32 01-双核架构"),
]

for path, title, slug, bq, parts, tip, nxt, nxt_t in _practice:
    CHAPTERS.append(ch(path, title, "入门实战", "入门实战", mk(bq, parts, tip, nxt, nxt_t)))

# ── ESP32 专题 (8) ────────────────────────────────────────────
_esp32 = [
    ("ESP32/01-ESP32双核架构.html", "ESP32 01：ESP32 双核架构", "01-ESP32 双核架构",
     "学习目标：理解 ESP32 双核 Xtensa LX6、PRO CPU / APP CPU 分工与核间通信基础。",
     [
         ("1. 双核概览", """<p>ESP32 有两颗 240MHz Xtensa LX6：<strong>PRO_CPU（核0）</strong>通常跑 Wi-Fi/BT 协议栈，<strong>APP_CPU（核1）</strong>跑用户任务（可配置）。</p>
<table><thead><tr><th>核心</th><th>默认职责</th></tr></thead>
<tbody>
<tr><td>CPU0</td><td>Wi-Fi、蓝牙、部分系统任务</td></tr>
<tr><td>CPU1</td><td>Arduino loop 默认在此（IDF 可绑核）</td></tr>
</tbody></table>"""),
         ("2. 为何需要双核？", """<p>Wi-Fi 栈实时性高，若与用户代码同核，<code>delay</code> 或长计算会导致断连。双核 = 协议栈与用户逻辑物理隔离。</p>"""),
         ("3. 查看当前核", """<pre><code>// ESP-IDF
printf("Running on core %d\\n", xPortGetCoreID());

// FreeRTOS 创建任务时可 xTaskCreatePinnedToCore</code></pre>"""),
         ("4. 与 iOS 对照", """<table><thead><tr><th>ESP32</th><th>iOS</th></tr></thead>
<tbody>
<tr><td>双核分工</td><td>性能核 + 能效核</td></tr>
<tr><td>Wi-Fi 栈任务</td><td>系统网络守护进程</td></tr>
</tbody></table>"""),
     ], "💡 Arduino 层不必手动绑核；上 ESP-IDF + FreeRTOS 后再精细分配。", "02-Arduino框架开发.html", "02-Arduino 框架开发"),
    ("ESP32/02-Arduino框架开发.html", "ESP32 02：Arduino 框架开发", "02-Arduino 框架开发",
     "学习目标：掌握 ESP32 Arduino 核心库、板型选择、库管理与迁移到 IDF 的路径。",
     [
         ("1. 框架层次", """<pre><code>你的 sketch (.ino)
    ↓
Arduino-ESP32 核心
    ↓
ESP-IDF + FreeRTOS + Wi-Fi/BT 栈</code></pre>"""),
         ("2. 常用 API", """<table><thead><tr><th>功能</th><th>头文件/API</th></tr></thead>
<tbody>
<tr><td>GPIO</td><td><code>pinMode/digitalWrite</code></td></tr>
<tr><td>Wi-Fi</td><td><code>WiFi.h</code></td></tr>
<tr><td>BLE</td><td><code>BLEDevice.h</code></td></tr>
<tr><td>多任务</td><td><code>xTaskCreate</code>（需 include）</td></tr>
</tbody></table>"""),
         ("3. 库管理", """<pre><code>// platformio.ini 示例
[env:esp32dev]
platform = espressif32
board = esp32dev
framework = arduino
lib_deps = adafruit/DHT sensor library</code></pre>"""),
         ("4. 局限", """<p>Arduino 隐藏细节，适合原型；量产或低功耗深度优化建议转 ESP-IDF。</p>"""),
     ], "💡 复杂项目用 PlatformIO，`.ino` 可拆成 `.cpp` 模块化。", "03-ESP-IDF原生开发.html", "03-ESP-IDF 原生开发"),
    ("ESP32/03-ESP-IDF原生开发.html", "ESP32 03：ESP-IDF 原生开发", "03-ESP-IDF 原生开发",
     "学习目标：搭建 ESP-IDF 环境，理解 app_main、menuconfig、组件化工程结构。",
     [
         ("1. 安装 IDF", """<pre><code># macOS
mkdir -p ~/esp && cd ~/esp
git clone -b v5.2 --recursive https://github.com/espressif/esp-idf.git
./esp-idf/install.sh esp32
. ./esp-idf/export.sh</code></pre>"""),
         ("2. 工程结构", """<pre><code>my_project/
  CMakeLists.txt
  main/
    CMakeLists.txt
    main.c
  sdkconfig</code></pre>"""),
         ("3. app_main 入口", """<pre><code>void app_main(void) {
    esp_log_level_set("*", ESP_LOG_INFO);
    xTaskCreate(blink_task, "blink", 2048, NULL, 5, NULL);
}</code></pre>"""),
         ("4. 构建烧录", """<pre><code>idf.py set-target esp32
idf.py menuconfig
idf.py build flash monitor</code></pre>"""),
     ], "💡 第一次编译较慢，用国内镜像或代理；<code>idf.py monitor</code> 等价于串口调试。", "04-WiFi配网SmartConfig.html", "04-WiFi 配网 SmartConfig"),
    ("ESP32/04-WiFi配网SmartConfig.html", "ESP32 04：WiFi 配网 SmartConfig", "04-WiFi 配网 SmartConfig",
     "学习目标：实现 SmartConfig / SoftAP 配网，设备无屏也能连路由器。",
     [
         ("1. 配网方式对比", """<table><thead><tr><th>方式</th><th>体验</th><th>适用</th></tr></thead>
<tbody>
<tr><td>硬编码 SSID</td><td>差</td><td>仅开发</td></tr>
<tr><td>SoftAP 网页</td><td>中</td><td>有浏览器</td></tr>
<tr><td>SmartConfig</td><td>好</td><td>ESP Touch App</td></tr>
<tr><td>BLE 配网</td><td>好</td><td>自有 iOS App</td></tr>
</tbody></table>"""),
         ("2. SmartConfig 流程", """<ol>
<li>ESP32 进入混杂模式监听</li>
<li>手机 App 编码 SSID/密码到 UDP 包</li>
<li>设备解析后连 AP，可回调通知 App</li>
</ol>"""),
         ("3. 代码片段", """<pre><code>#include "esp_smartconfig.h"
esp_smartconfig_set_type(SC_TYPE_ESPTOUCH);
smartconfig_start_config_t cfg = SMARTCONFIG_START_CONFIG_DEFAULT();
esp_smartconfig_start(&cfg);</code></pre>"""),
         ("4. 存储凭据", """<p>配网成功后写入 NVS，下次 <code>esp_wifi_start</code> 自动连接。</p>"""),
     ], "💡 量产推荐自有 App BLE 配网，比 ESPTouch 更可控、可品牌化。", "05-BLE-NimBLE开发.html", "05-BLE NimBLE 开发"),
    ("ESP32/05-BLE-NimBLE开发.html", "ESP32 05：BLE NimBLE 开发", "05-BLE NimBLE 开发",
     "学习目标：用 NimBLE 栈创建 GATT 服务，与 iOS CoreBluetooth 读写互通。",
     [
         ("1. NimBLE vs Bluedroid", """<p>ESP-IDF 5 默认 NimBLE，RAM 占用更小，适合 IoT 从机。</p>"""),
         ("2. GATT 结构", """<pre><code>Service UUID: 0xFFE0
  Characteristic 0xFFE1  (READ | WRITE | NOTIFY)</code></pre>
<table><thead><tr><th>BLE</th><th>CoreBluetooth</th></tr></thead>
<tbody>
<tr><td>Peripheral</td><td>CBPeripheral / 外设端</td></tr>
<tr><td>Notify</td><td>setNotifyValue(true)</td></tr>
</tbody></table>"""),
         ("3. 广播与连接", """<pre><code>// Arduino BLE 简化
BLEServer *pServer = BLEDevice::createServer();
BLEService *pSvc = pServer->createService("FFE0");
BLECharacteristic *pChar = pSvc->createCharacteristic(
  "FFE1", BLECharacteristic::PROPERTY_WRITE);
pSvc->start();
BLEDevice::startAdvertising();</code></pre>"""),
         ("4. iOS 联调", """<p>Info.plist 添加蓝牙权限；真机扫描服务 UUID，写入 1 字节控制 LED。</p>"""),
     ], "💡 MTU 协商后可用更长包；iOS 默认 185 字节 ATT MTU 左右。", "06-Deep-Sleep低功耗.html", "06-Deep Sleep 低功耗"),
    ("ESP32/06-Deep-Sleep低功耗.html", "ESP32 06：Deep Sleep 低功耗", "06-Deep Sleep 低功耗",
     "学习目标：配置 Deep Sleep + 定时/GPIO 唤醒，电池项目续航数月。",
     [
         ("1. 睡眠模式", """<table><thead><tr><th>模式</th><th>电流</th><th>唤醒源</th></tr></thead>
<tbody>
<tr><td>Modem sleep</td><td>mA 级</td><td>Wi-Fi 活动时</td></tr>
<tr><td>Light sleep</td><td>~0.8mA</td><td>定时/触摸</td></tr>
<tr><td>Deep sleep</td><td>~10µA</td><td>RTC GPIO/定时器</td></tr>
</tbody></table>"""),
         ("2. 定时唤醒", """<pre><code>esp_sleep_enable_timer_wakeup(20 * 1000000ULL); // 20s
esp_deep_sleep_start();</code></pre>"""),
         ("3. 注意", """<ul>
<li>Deep Sleep 后 RAM 丢失，变量用 RTC_DATA_ATTR 或 NVS</li>
<li>GPIO33 等 RTC 脚才能做 ext0 唤醒</li>
</ul>"""),
         ("4. 测量", """<p>用万用表 µA 档串在电池正极，确认睡眠电流达标。</p>"""),
     ], "💡 Wi-Fi 连上再睡：典型模式是唤醒→读传感器→MQTT→Deep Sleep。", "07-NVS与分区表.html", "07-NVS 与分区表"),
    ("ESP32/07-NVS与分区表.html", "ESP32 07：NVS 与分区表", "07-NVS 与分区表",
     "学习目标：理解 Flash 分区表 nvs/ota/app，安全读写 NVS 与 OTA 预留。",
     [
         ("1. 默认分区", """<pre><code># Name,   Type, SubType, Offset,  Size
nvs,      data, nvs,     0x9000,  0x6000
phy_init, data, phy,     0xf000,  0x1000
factory,  app,  factory, 0x10000, 1M</code></pre>"""),
         ("2. NVS API", """<pre><code>nvs_handle_t h;
nvs_open("storage", NVS_READWRITE, &h);
nvs_set_i32(h, "counter", 42);
nvs_commit(h);
nvs_close(h);</code></pre>"""),
         ("3. 自定义分区", """<p>OTA 需要 <code>ota_0/ota_1</code> 双 app 分区，在 <code>partitions.csv</code> 定义。</p>"""),
         ("4. 坑", """<ul>
<li>NVS 满需擦除命名空间</li>
<li>频繁写 wear — 批量提交</li>
</ul>"""),
     ], "💡 改分区表后需 <code>idf.py fullclean</code>，否则 offset 错乱烧录失败。", "08-双核任务分配.html", "08-双核任务分配"),
    ("ESP32/08-双核任务分配.html", "ESP32 08：双核任务分配", "08-双核任务分配",
     "学习目标：用 xTaskCreatePinnedToCore 分配 CPU 密集型与 I/O 任务，避免 Wi-Fi 饿死。",
     [
         ("1. 绑核 API", """<pre><code>xTaskCreatePinnedToCore(
    heavy_task, "heavy", 4096, NULL, 5, NULL, 1);  // 核1
xTaskCreatePinnedToCore(
    wifi_worker, "wifi", 8192, NULL, 6, NULL, 0); // 核0</code></pre>"""),
         ("2. 优先级", """<table><thead><tr><th>任务</th><th>建议优先级</th><th>核心</th></tr></thead>
<tbody>
<tr><td>Wi-Fi 相关</td><td>高（系统设）</td><td>0</td></tr>
<tr><td>传感器采样</td><td>中</td><td>1</td></tr>
<tr><td>日志/UI</td><td>低</td><td>1</td></tr>
</tbody></table>"""),
         ("3. 核间通信", """<p>用 FreeRTOS 队列在核间传数据，<strong>不要</strong>跨核直接共享无锁全局变量。</p>"""),
         ("4. 调试", """<pre><code>vTaskList(buffer);
printf("%s\\n", buffer);  // 看各任务 CPU 占用</code></pre>"""),
     ], "💡 双核不是万能，瓶颈常在 Flash /cache 争用；大算力考虑 ESP32-S3。", "../进阶/01-FreeRTOS任务与调度.html", "进阶 01-FreeRTOS 任务与调度"),
]

for path, title, slug, bq, parts, tip, nxt, nxt_t in _esp32:
    CHAPTERS.append(ch(path, title, "ESP32 专题", "ESP32", mk(bq, parts, tip, nxt, nxt_t)))

# ── FreeRTOS 进阶 (8) ─────────────────────────────────────────
_rtos = [
    ("进阶/01-FreeRTOS任务与调度.html", "进阶 01：FreeRTOS 任务与调度", "01-FreeRTOS 任务与调度",
     "学习目标：创建任务、理解优先级抢占式调度，对比 iOS GCD。",
     [
         ("1. 为何 RTOS？", """<p>同时读传感器、刷屏幕、发 MQTT——单 loop 难维护。FreeRTOS 提供多任务 + 阻塞 API。</p>"""),
         ("2. 概念对照", """<table><thead><tr><th>FreeRTOS</th><th>iOS</th></tr></thead>
<tbody>
<tr><td>Task</td><td>DispatchQueue / Thread</td></tr>
<tr><td>vTaskDelay</td><td>Task.sleep</td></tr>
<tr><td>Priority</td><td>QoS / queue priority</td></tr>
</tbody></table>"""),
         ("3. 创建任务", """<pre><code>void sensor_task(void *arg) {
  while (1) {
    read_and_publish();
    vTaskDelay(pdMS_TO_TICKS(1000));
  }
}
xTaskCreate(sensor_task, "sensor", 4096, NULL, 5, NULL);
vTaskStartScheduler();</code></pre>"""),
         ("4. 调度规则", """<ul>
<li>高优先级就绪 → 立即抢占</li>
<li>同优先级时间片轮转</li>
<li>阻塞态任务不占 CPU</li>
</ul>"""),
     ], "💡 栈大小单位是字（ESP32 为 4 字节），4096 = 16KB 栈，溢出会 Guru Meditation。", "02-队列与消息传递.html", "02-队列与消息传递"),
    ("进阶/02-队列与消息传递.html", "进阶 02：队列与消息传递", "02-队列与消息传递",
     "学习目标：用 Queue 在任务间传结构体，解耦生产者与消费者。",
     [
         ("1. 队列模型", """<pre><code>传感器任务 ──Queue──► Wi-Fi 任务 ──► MQTT
             （缓冲 N 条）</code></pre>"""),
         ("2. API", """<pre><code>QueueHandle_t q = xQueueCreate(10, sizeof(sensor_data_t));
xQueueSend(q, &data, pdMS_TO_TICKS(100));
xQueueReceive(q, &data, portMAX_DELAY);</code></pre>"""),
         ("3. 结构体消息", """<pre><code>typedef struct {
  float temp;
  float hum;
  uint32_t ts;
} sensor_data_t;</code></pre>"""),
         ("4. 注意", """<table><thead><tr><th>问题</th><th>处理</th></tr></thead>
<tbody>
<tr><td>队列满</td><td>超时丢弃或增大深度</td></tr>
<tr><td>大对象</td><td>传指针 + 内存池</td></tr>
</tbody></table>"""),
     ], "💡 中断里用 xQueueSendFromISR，不能调用普通 Send。", "03-信号量与互斥量.html", "03-信号量与互斥量"),
    ("进阶/03-信号量与互斥量.html", "进阶 03：信号量与互斥量", "03-信号量与互斥量",
     "学习目标：Binary/Counting Semaphore 同步事件，Mutex 保护共享资源。",
     [
         ("1. 二进制信号量", """<p>任务 A 完成 → <code>give</code>，任务 B <code>take</code> 阻塞等待。适合一次事件通知。</p>"""),
         ("2. 互斥量 Mutex", """<pre><code>SemaphoreHandle_t mux = xSemaphoreCreateMutex();
if (xSemaphoreTake(mux, portMAX_DELAY)) {
  // 访问共享 SPI 总线
  xSemaphoreGive(mux);
}</code></pre>"""),
         ("3. 对比", """<table><thead><tr><th>机制</th><th>用途</th></tr></thead>
<tbody>
<tr><td>Mutex</td><td>保护资源，谁 take 谁 give</td></tr>
<tr><td>Binary Sem</td><td>同步信号，可跨任务</td></tr>
<tr><td>Counting Sem</td><td>资源计数（缓冲池）</td></tr>
</tbody></table>"""),
         ("4. 死锁", """<p>禁止嵌套 take 不同顺序的多个 Mutex；设置超时 take。</p>"""),
     ], "💡 优先级反转：用 Mutex 的 priority inheritance（ESP-IDF 默认支持）。", "04-事件组与通知.html", "04-事件组与通知"),
    ("进阶/04-事件组与通知.html", "进阶 04：事件组与通知", "04-事件组与通知",
     "学习目标：Event Group 等多位标志，Task Notification 轻量通知。",
     [
         ("1. 事件组", """<pre><code>#define BIT_WIFI  (1&lt;&lt;0)
#define BIT_SENSOR (1&lt;&lt;1)
EventGroupHandle_t eg = xEventGroupCreate();
xEventGroupSetBits(eg, BIT_WIFI);
xEventGroupWaitBits(eg, BIT_WIFI|BIT_SENSOR, pdTRUE, pdTRUE, portMAX_DELAY);</code></pre>"""),
         ("2. 任务通知", """<p>比队列更轻：<code>xTaskNotifyGive</code> / <code>ulTaskNotifyTake</code>，适合单消费者。</p>"""),
         ("3. 场景", """<table><thead><tr><th>场景</th><th>选择</th></tr></thead>
<tbody>
<tr><td>多条件就绪</td><td>Event Group</td></tr>
<tr><td>单任务唤醒</td><td>Task Notification</td></tr>
</tbody></table>"""),
         ("4. ISR 版本", """<pre><code>xEventGroupSetBitsFromISR(eg, BIT_SENSOR, &hpw);</code></pre>"""),
     ], "💡 Event Group 最多 24 个 bit（configUSE_16_BIT_TICKS 相关），规划位含义文档化。", "05-内存管理与堆栈.html", "05-内存管理与堆栈"),
    ("进阶/05-内存管理与堆栈.html", "进阶 05：内存管理与堆栈", "05-内存管理与堆栈",
     "学习目标：理解 heap_4、栈溢出检测、静态 vs 动态任务创建。",
     [
         ("1. ESP32 内存布局", """<p>内部 SRAM ~520KB，部分用于 Wi-Fi；大缓冲可用 PSRAM（若板载）。</p>"""),
         ("2. 栈溢出", """<pre><code>// menuconfig 开启
CONFIG_FREERTOS_CHECK_STACKOVERFLOW_CANARY=y
// 任务列表看高水位
uxTaskGetStackHighWaterMark(NULL);</code></pre>"""),
         ("3. 分配策略", """<table><thead><tr><th>方式</th><th>适用</th></tr></thead>
<tbody>
<tr><td>栈上小数组</td><td>&lt; 几百字节</td></tr>
<tr><td>malloc</td><td>运行时大小未知</td></tr>
<tr><td>静态 Global</td><td>大缓冲、DMA</td></tr>
</tbody></table>"""),
         ("4. 碎片", """<p>长期 malloc/free 碎片化 → 启动阶段分配，或内存池。</p>"""),
     ], "💡 Wi-Fi 缓冲在 heap，留 50KB+ 余量；PSRAM 需配置 <code>CONFIG_SPIRAM</code>。", "06-中断与临界区.html", "06-中断与临界区"),
    ("进阶/06-中断与临界区.html", "进阶 06：中断与临界区", "06-中断与临界区",
     "学习目标：ISR 规则、FromISR API、临界区 portENTER_CRITICAL。",
     [
         ("1. ISR 原则", """<ul>
<li>短小、无阻塞、无 printf</li>
<li>仅置标志或 FromISR 发队列</li>
</ul>"""),
         ("2. 临界区", """<pre><code>portENTER_CRITICAL(&mux);
shared_counter++;
portEXIT_CRITICAL(&mux);</code></pre>"""),
         ("3. FromISR", """<pre><code>BaseType_t hpw = pdFALSE;
xQueueSendFromISR(q, &item, &hpw);
if (hpw) portYIELD_FROM_ISR();</code></pre>"""),
         ("4. 优先级", """<table><thead><tr><th>层级</th><th>说明</th></tr></thead>
<tbody>
<tr><td>中断优先级</td><td>高于所有任务</td></tr>
<tr><td>configMAX_SYSCALL</td><td>高于此优先级 ISR 不能调 FreeRTOS API</td></tr>
</tbody></table>"""),
     ], "⚠️ 在 ISR 里调用非 FromISR 的 API 会导致崩溃或死锁。", "07-低功耗与Tickless.html", "07-低功耗与 Tickless"),
    ("进阶/07-低功耗与Tickless.html", "进阶 07：低功耗与 Tickless", "07-低功耗与 Tickless",
     "学习目标：configUSE_TICKLESS_IDLE 让空闲任务进 light sleep，配合 ESP32 PM。",
     [
         ("1. Tickless", """<p>无任务就绪时暂停 SysTick，睡到最后一个 wake 时间点，省 CPU 空转。</p>"""),
         ("2. ESP-IDF PM", """<pre><code>esp_pm_config_t pm = {
  .max_freq_mhz = 240,
  .min_freq_mhz = 80,
  .light_sleep_enable = true
};
esp_pm_configure(&pm);</code></pre>"""),
         ("3. 与 RTOS", """<table><thead><tr><th>模式</th><th>RTOS 行为</th></tr></thead>
<tbody>
<tr><td>Idle hook</td><td>进入 sleep 前关外设</td></tr>
<tr><td>Tickless</td><td>动态调整 tick</td></tr>
</tbody></table>"""),
         ("4. 测量", """<p>对比开启前后平均电流；注意 UART 调试时 sleep 会丢日志。</p>"""),
     ], "💡 BLE 连接间隔内可 sleep；Wi-Fi 常连时 tickless 收益有限。", "08-OTA固件升级.html", "08-OTA 固件升级"),
    ("进阶/08-OTA固件升级.html", "进阶 08：OTA 固件升级", "08-OTA 固件升级",
     "学习目标：双分区 OTA 流程、HTTPS 下载、失败回滚与版本校验。",
     [
         ("1. OTA 架构", """<pre><code>Flash: [bootloader][partition table][ota_0][ota_1][nvs]
运行 ota_0 → 下载到 ota_1 → 切换 boot → 重启</code></pre>"""),
         ("2. ESP-IDF OTA API", """<pre><code>esp_ota_handle_t handle;
const esp_partition_t *update = esp_ota_get_next_update_partition(NULL);
esp_ota_begin(update, OTA_SIZE_UNKNOWN, &handle);
// esp_https_ota 或 esp_ota_write 循环
esp_ota_end(handle);
esp_ota_set_boot_partition(update);
esp_restart();</code></pre>"""),
         ("3. 安全", """<ul>
<li>HTTPS + 证书校验</li>
<li>固件签名（Secure Boot）</li>
<li>失败回滚 <code>esp_ota_mark_app_valid_cancel_rollback</code></li>
</ul>"""),
         ("4. iOS 协同", """<p>App 检查云端版本 → 通知设备 MQTT OTA URL → 进度 Notify 给 App。</p>"""),
     ], "💡 第一次 OTA 前留 UART 线，变砖可 serial 烧录救回。", "../README.html", "返回教程首页"),
]

for path, title, slug, bq, parts, tip, nxt, nxt_t in _rtos:
    CHAPTERS.append(ch(path, title, "FreeRTOS 进阶", "FreeRTOS", mk(bq, parts, tip, nxt, nxt_t)))

# ── Validate & write ──────────────────────────────────────────
errors = []
for i, (path, title, tag, module, body) in enumerate(CHAPTERS):
    n = len(body)
    if n < 1500 or n > 3500:
        errors.append(f"  [{i+1}] {path}: {n} chars")
    for req in ("<blockquote>", "<h2>", "<table", "<pre><code>", "tip-box", "下一步"):
        if req not in body:
            errors.append(f"  [{i+1}] {path}: missing {req}")
    h2_count = body.count("<h2>")
    if h2_count < 5:  # 4+ sections + 小结
        errors.append(f"  [{i+1}] {path}: only {h2_count} h2")

if errors:
    print("VALIDATION ERRORS:")
    print("\n".join(errors))
    raise SystemExit(1)

lines = [
    '"""ESP32 + FreeRTOS 实验教程章节内容。"""',
    "",
    "# Each tuple: (path, title, tag, module, body_html)",
    "CHAPTERS = [",
]
for path, title, tag, module, body in CHAPTERS:
    lines.append("    (")
    lines.append(f'        {path!r},')
    lines.append(f'        {title!r},')
    lines.append(f'        {tag!r},')
    lines.append(f'        {module!r},')
    lines.append('        """')
    lines.append(body)
    lines.append('        """,')
    lines.append("    ),")
lines.append("]")
lines.append("")

OUT.write_text("\n".join(lines), encoding="utf-8")
print(f"Wrote {OUT} with {len(CHAPTERS)} chapters")
for path, title, tag, module, body in CHAPTERS:
    print(f"  {path}: {len(body)} chars")

PYEOF
python3 /Users/xion/Projects/gw/danpianji-jiaocheng/_content/_gen_esp32_rtos_lab.py