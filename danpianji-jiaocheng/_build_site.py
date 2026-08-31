#!/usr/bin/env python3
"""Generate 单片机/嵌入式学习教程 HTML pages."""
from pathlib import Path

ROOT = Path(__file__).parent

NAV = [
    {"id": "home", "title": "教程首页", "href": "README.html"},
    {"id": "base", "title": "基础", "items": [
        ("01 单片机是什么", "基础/01-单片机是什么.html"),
        ("02 iOS开发者视角", "基础/02-从iOS开发者视角看嵌入式.html"),
        ("03 开发板怎么选", "基础/03-开发板怎么选.html"),
        ("04 C语言速成", "基础/04-C语言速成-Swift开发者版.html"),
        ("05 GPIO与点灯", "基础/05-GPIO与点灯原理.html"),
        ("06 通信协议入门", "基础/06-常见通信协议入门.html"),
        ("07 应用场景与方向", "基础/07-应用场景与赚钱方向.html"),
        ("08 环境搭建", "基础/08-工具链与环境搭建.html"),
    ]},
    {"id": "hw", "title": "硬件入门", "items": [
        ("01 开发板与工具", "硬件/01-开发板与工具.html"),
        ("02 万用表与焊接", "硬件/02-万用表与焊接入门.html"),
        ("03 原理图阅读", "硬件/03-原理图阅读入门.html"),
    ]},
    {"id": "start", "title": "入门实战", "items": [
        ("01 第一个程序点灯", "入门实战/01-第一个程序点灯.html"),
        ("02 按键与中断", "入门实战/02-按键与中断.html"),
        ("03 串口调试", "入门实战/03-串口调试.html"),
        ("04 PWM与舵机", "入门实战/04-PWM控制舵机.html"),
        ("05 温湿度传感器", "入门实战/05-温湿度传感器.html"),
    ]},
    {"id": "adv", "title": "进阶", "items": [
        ("01 STM32入门", "进阶/01-STM32入门.html"),
        ("02 FreeRTOS基础", "进阶/02-FreeRTOS基础.html"),
        ("03 低功耗设计", "进阶/03-低功耗设计.html"),
        ("04 OTA固件升级", "进阶/04-OTA固件升级.html"),
    ]},
    {"id": "ios", "title": "iOS 联动", "items": [
        ("01 BLE与iOS通信", "iOS联动/01-BLE蓝牙与iOS通信.html"),
        ("02 WiFi与MQTT", "iOS联动/02-WiFi-MQTT与App联动.html"),
        ("03 智能硬件全栈", "iOS联动/03-智能硬件全栈方案.html"),
        ("04 CoreBluetooth实战", "iOS联动/04-CoreBluetooth实战代码.html"),
    ]},
    {"id": "proj", "title": "项目实战", "items": [
        ("01 智能台灯", "项目实战/01-智能台灯.html"),
        ("02 远程开关", "项目实战/02-远程开关.html"),
        ("03 环境检测仪", "项目实战/03-环境检测仪.html"),
    ]},
    {"id": "scene", "title": "应用场景", "items": [
        ("01 行业应用全景", "应用场景/01-行业应用全景.html"),
        ("02 如何接单赚钱", "应用场景/02-如何接单赚钱.html"),
    ]},
    {"id": "practice", "title": "练习", "items": [
        ("01 入门采购清单", "练习/01-入门采购清单.html"),
        ("02 自测题", "练习/02-自测题.html"),
    ]},
    {"id": "interview", "title": "面试题", "items": [
        ("嵌入式面试题精选", "面试题/嵌入式面试题精选.html"),
    ]},
]

CHAPTERS = {
    "基础/01-单片机是什么.html": {
        "title": "基础 01：单片机是什么",
        "tag": "基础模块",
        "module": "基础",
        "body": """
<blockquote><p>学习目标：10 分钟搞懂单片机是啥、能干啥，不再被一堆缩写吓到。</p></blockquote>
<h2>1. 一句话说清单片机</h2>
<p><strong>单片机（MCU）= 一块集成了 CPU、内存、定时器、GPIO 的「迷你电脑芯片」。</strong>它没有 macOS，没有 UI 界面，但能通过引脚控制 LED、读传感器、发 Wi-Fi/BLE 信号。</p>
<p>大白话：<strong>你 iPhone 里的 A 系列芯片是「超级大脑」；单片机是「小脑」</strong>——专门干一件小事：控灯、测温、开门锁、转电机。</p>
<h2>2. 核心比喻：单片机 = 永远在线的 while 循环</h2>
<p>写 iOS App 时，系统是事件驱动的（点按钮 → 回调）。单片机程序通常是：</p>
<pre><code>int main() {
    初始化硬件();
    while (1) {          // 永远跑，不会退出
        读传感器();
        控制输出();
        延时(10ms);
    }
}</code></pre>
<p>没有 <code>UIApplication</code>，没有 <code>viewDidLoad</code>，就是<strong>一个死循环 + 硬件寄存器</strong>。</p>
<h2>3. 单片机 vs iPhone（帮你建立对照）</h2>
<table>
<thead><tr><th>对比</th><th>iPhone / iOS</th><th>单片机 / 嵌入式</th></tr></thead>
<tbody>
<tr><td>算力</td><td>极强，多核 GHz</td><td>弱，几十～几百 MHz</td></tr>
<tr><td>内存</td><td>GB 级</td><td>KB～MB 级</td></tr>
<tr><td>操作系统</td><td>iOS</td><td>裸机 / FreeRTOS</td></tr>
<tr><td>语言</td><td>Swift / ObjC</td><td>C / C++</td></tr>
<tr><td>调试</td><td>Xcode + 模拟器</td><td>串口 + 示波器 + J-Link</td></tr>
<tr><td>功耗</td><td>瓦级</td><td>毫瓦～微瓦（可电池跑几年）</td></tr>
<tr><td>成本</td><td>几千元</td><td>芯片 2～50 元</td></tr>
</tbody>
</table>
<h2>4. 常见芯片家族（2026 年入门推荐）</h2>
<table>
<thead><tr><th>芯片</th><th>特点</th><th>适合谁</th></tr></thead>
<tbody>
<tr><td><strong>ESP32</strong></td><td>自带 Wi-Fi + BLE，资料超多</td><td>小白首选、IoT、对接 iOS</td></tr>
<tr><td><strong>Arduino (ATmega)</strong></td><td>最简单，生态成熟</td><td>纯入门体验</td></tr>
<tr><td><strong>STM32</strong></td><td>工业标准，外设丰富</td><td>求职嵌入式岗位</td></tr>
<tr><td><strong>nRF52</strong></td><td>低功耗 BLE 王者</td><td>可穿戴、Beacon</td></tr>
</tbody>
</table>
<h2>5. 单片机在生活中的样子</h2>
<ul>
<li>空调遥控器里的芯片 → 发红外信号</li>
<li>小米台灯 → ESP32 控亮度 + App 联动</li>
<li>充电桩 → STM32 控继电器 + 计量</li>
<li>Apple Watch 里也有 MCU 协处理器（常低功耗跑传感器）</li>
</ul>
<h2>小结</h2>
<ol>
<li>单片机 = <strong>便宜、省电、专干一件事</strong>的小电脑</li>
<li>程序结构 = <strong>初始化 + 死循环</strong></li>
<li>入门推荐 <strong>ESP32</strong>（能联网，和你 iOS 背景绝配）</li>
</ol>
<p><strong>下一步：</strong> <a href="02-从iOS开发者视角看嵌入式.html">02-从 iOS 开发者视角看嵌入式</a></p>
""",
    },
    "基础/02-从iOS开发者视角看嵌入式.html": {
        "title": "基础 02：从 iOS 开发者视角看嵌入式",
        "tag": "基础模块",
        "module": "基础",
        "body": """
<blockquote><p>你有 iOS 基础，学嵌入式不是从零开始——很多概念有「一一对应」。</p></blockquote>
<h2>1. 概念对照表（背这张表就省一半时间）</h2>
<table>
<thead><tr><th>iOS / Swift</th><th>嵌入式 / C</th><th>说明</th></tr></thead>
<tbody>
<tr><td><code>UIView</code></td><td>GPIO 引脚</td><td>对外接口，一个管脚高/低电平</td></tr>
<tr><td><code>Button target-action</code></td><td>外部中断</td><td>事件触发回调</td></tr>
<tr><td><code>Timer</code></td><td>硬件定时器</td><td>周期性任务</td></tr>
<tr><td><code>URLSession</code></td><td>UART / SPI / I2C</td><td>和别的芯片「说话」的协议</td></tr>
<tr><td><code>CoreBluetooth</code></td><td>BLE 协议栈</td><td>手机 ↔ 设备无线通信</td></tr>
<tr><td><code>UserDefaults</code></td><td>Flash / EEPROM</td><td>掉电保存小数据</td></tr>
<tr><td><code>DispatchQueue</code></td><td>FreeRTOS 任务</td><td>多任务调度</td></tr>
<tr><td><code>Instruments</code></td><td>逻辑分析仪 / 示波器</td><td>性能与信号调试</td></tr>
<tr><td><code>App Store 审核</code></td><td>CE / 3C / 车规认证</td><td>产品合规</td></tr>
</tbody>
</table>
<h2>2. 你的优势</h2>
<ul>
<li><strong>产品思维</strong>：嵌入式很多人只会写驱动，不懂用户体验——你会做 App</li>
<li><strong>蓝牙/Wi-Fi 联调</strong>：CoreBluetooth、Network 框架经验直接复用</li>
<li><strong>架构能力</strong>：MVVM、模块化在固件里同样适用</li>
<li><strong>全栈交付</strong>：MCU + App + 云端 = 完整智能硬件产品</li>
</ul>
<h2>3. 你需要补的短板</h2>
<ul>
<li><strong>C 语言</strong>：指针、位操作、内存管理（没有 ARC）</li>
<li><strong>电路基础</strong>：能看懂简单原理图（VCC、GND、上拉电阻）</li>
<li><strong>示波器/万用表</strong>：硬件调试必备</li>
<li><strong>耐心</strong>：接线松了、电源接反了——硬件 bug 比软件难查</li>
</ul>
<div class="tip-box">💡 <strong>建议</strong>：不要先啃 500 页 STM32 手册。买一块 ESP32 开发板（约 30 元），先点亮 LED，再连 iPhone 蓝牙——有成就感才能坚持。</div>
<h2>4. 推荐学习路径（有 iOS 背景版）</h2>
<pre><code>第 1 周：C 语言速成 + 点灯（Arduino/ESP32）
第 2 周：按键/串口/传感器
第 3 周：BLE 通信 + iOS CoreBluetooth 联调
第 4 周：做一个「手机控灯」完整项目
第 2 月：STM32 + FreeRTOS（求职向）
第 3 月：选一个行业项目（台灯/检测仪/工控）</code></pre>
<p><strong>下一步：</strong> <a href="03-开发板怎么选.html">03-开发板怎么选</a></p>
""",
    },
    "基础/03-开发板怎么选.html": {
        "title": "基础 03：开发板怎么选",
        "tag": "基础模块",
        "module": "基础",
        "body": """
<h2>1. 入门三板斧（按推荐顺序）</h2>
<table>
<thead><tr><th>开发板</th><th>价格</th><th>推荐理由</th></tr></thead>
<tbody>
<tr><td><strong>ESP32-DevKitC</strong></td><td>25～40 元</td><td>Wi-Fi + BLE，Arduino/ESP-IDF 双生态，和 iOS 联动最佳</td></tr>
<tr><td><strong>Arduino Uno R3</strong></td><td>20～35 元</td><td>最简单，教程最多，适合第一天点灯</td></tr>
<tr><td><strong>STM32F103 最小系统板</strong></td><td>10～15 元</td><td>求职必备，便宜到离谱</td></tr>
</tbody>
</table>
<h2>2. 必买配件（200 元以内搞定）</h2>
<ul>
<li>面包板 + 杜邦线</li>
<li>LED、电阻（220Ω）、按键</li>
<li>DHT11 温湿度模块（练传感器）</li>
<li>USB 数据线（注意 ESP32 很多要 Type-C）</li>
<li>可选：逻辑分析仪（20 元，淘宝一堆）</li>
</ul>
<h2>3. 不要一上来就买</h2>
<ul>
<li>❌ 树莓派（那是 Linux 小电脑，不是单片机入门）</li>
<li>❌ 几十种传感器大礼包（吃灰）</li>
<li>❌ 没文档的国产冷门板子</li>
</ul>
<h2>4. Mac 开发环境</h2>
<p>你用的是 Mac，完美支持：</p>
<ul>
<li><strong>Arduino IDE</strong> 或 <strong>PlatformIO</strong>（VS Code 插件，推荐）</li>
<li><strong>ESP-IDF</strong>（乐鑫官方，终端安装）</li>
<li><strong>STM32CubeIDE</strong>（ST 官方，免费）</li>
<li>串口工具：<strong>screen</strong>、<strong>Serial Studio</strong></li>
</ul>
<p><strong>下一步：</strong> <a href="04-C语言速成-Swift开发者版.html">04-C语言速成</a></p>
""",
    },
    "基础/04-C语言速成-Swift开发者版.html": {
        "title": "基础 04：C 语言速成（Swift 开发者版",
        "tag": "基础模块",
        "module": "基础",
        "body": """
<blockquote><p>嵌入式 90% 用 C。有 Swift 基础，学 C 只要抓住差异点。</p></blockquote>
<h2>1. 语法对照</h2>
<table>
<thead><tr><th>Swift</th><th>C</th></tr></thead>
<tbody>
<tr><td><code>var x = 10</code></td><td><code>int x = 10;</code></td></tr>
<tr><td><code>let pi = 3.14</code></td><td><code>const float pi = 3.14f;</code></td></tr>
<tr><td><code>func add(a: Int, b: Int) -> Int</code></td><td><code>int add(int a, int b)</code></td></tr>
<tr><td><code>if / for / while</code></td><td>几乎一样，但每行末尾要 <code>;</code></td></tr>
<tr><td>ARC 自动内存</td><td><strong>手动管理</strong>，<code>malloc</code>/<code>free</code></td></tr>
<tr><td>可选类型 <code>Int?</code></td><td>没有，用特殊值或指针 NULL</td></tr>
</tbody>
</table>
<h2>2. 嵌入式必学：指针与位操作</h2>
<pre><code>// 读寄存器：把地址 0x4001080C 当作 int 指针，写入 1 点亮 LED
*(volatile unsigned int *)0x4001080C = 0x01;

// 位操作：置位第 5 位
GPIOA-&gt;ODR |= (1 &lt;&lt; 5);   // 点亮
GPIOA-&gt;ODR &amp;= ~(1 &lt;&lt; 5);  // 熄灭</code></pre>
<p>Swift 里你很少碰指针，嵌入式里<strong>每天都在碰</strong>。</p>
<h2>3. 头文件与编译</h2>
<pre><code>// main.c
#include "driver.h"   // 类似 Swift 的 import

int main(void) {
    gpio_init();
    while (1) { }
}</code></pre>
<h2>4. 练手题（5 分钟）</h2>
<ol>
<li>写一个函数判断数字是否为偶数</li>
<li>用 for 循环计算 1～100 的和</li>
<li>定义一个结构体 <code>SensorData { float temp; float humi; }</code></li>
</ol>
<p><strong>下一步：</strong> <a href="05-GPIO与点灯原理.html">05-GPIO与点灯</a></p>
""",
    },
    "基础/05-GPIO与点灯原理.html": {
        "title": "基础 05：GPIO 与点灯原理",
        "tag": "基础模块",
        "module": "基础",
        "body": """
<h2>1. GPIO 是什么？</h2>
<p><strong>GPIO = General Purpose Input/Output</strong>，芯片上的一根「可编程的电线」。</p>
<ul>
<li><strong>输出模式</strong>：MCU 控制引脚高电平（3.3V）或低电平（0V）→ 点亮/熄灭 LED</li>
<li><strong>输入模式</strong>：MCU 读取引脚电压 → 检测按键是否按下</li>
</ul>
<h2>2. 点灯电路（必背）</h2>
<pre><code>ESP32 GPIO2 ──→ LED长脚(+) ──→ LED短脚(-) ──→ 220Ω电阻 ──→ GND</code></pre>
<p>电流路径：引脚输出高电平 → 电流流过 LED → 发光。电阻防止电流过大烧 LED。</p>
<h2>3. 代码逻辑（伪代码）</h2>
<pre><code>pinMode(LED_PIN, OUTPUT);      // 配置为输出
digitalWrite(LED_PIN, HIGH);   // 点亮
delay(1000);                   // 等 1 秒
digitalWrite(LED_PIN, LOW);    // 熄灭</code></pre>
<p>对应 iOS：就像设置某个 <code>UIView.backgroundColor</code>，只不过你操作的是硬件引脚。</p>
<h2>4. 常见坑</h2>
<ul>
<li>LED 接反 → 不亮</li>
<li>没加电阻 → LED 烧掉</li>
<li>GPIO 编号搞错 → 看开发板丝印，不是随便写</li>
</ul>
<p><strong>下一步：</strong> <a href="06-常见通信协议入门.html">06-通信协议入门</a></p>
""",
    },
    "基础/06-常见通信协议入门.html": {
        "title": "基础 06：常见通信协议入门",
        "tag": "基础模块",
        "module": "基础",
        "body": """
<h2>1. 协议速查表</h2>
<table>
<thead><tr><th>协议</th><th>线数</th><th>距离</th><th>典型场景</th></tr></thead>
<tbody>
<tr><td><strong>UART</strong>（串口）</td><td>2（TX/RX）</td><td>短</td><td>调试打印、GPS 模块</td></tr>
<tr><td><strong>I2C</strong></td><td>2（SDA/SCL）</td><td>短</td><td>温湿度、OLED 屏</td></tr>
<tr><td><strong>SPI</strong></td><td>4+</td><td>短</td><td>Flash、高速传感器</td></tr>
<tr><td><strong>BLE</strong></td><td>无线</td><td>10m 内</td><td>手环、iOS 联动 ⭐</td></tr>
<tr><td><strong>Wi-Fi</strong></td><td>无线</td><td>远</td><td>智能家居、MQTT</td></tr>
<tr><td><strong>MQTT</strong></td><td>基于 TCP</td><td>互联网</td><td>设备 ↔ 云端 ↔ App</td></tr>
</tbody>
</table>
<h2>2. 和 iOS 的关系</h2>
<ul>
<li><strong>BLE</strong> → <code>CoreBluetooth</code>（你最该先学的）</li>
<li><strong>Wi-Fi + MQTT</strong> → App 通过云端控制设备</li>
<li><strong>HTTP</strong> → ESP32 开 Web Server，App 直接请求</li>
</ul>
<h2>3. 大白话记忆</h2>
<ul>
<li>UART = 两个人面对面说话（调试必备）</li>
<li>I2C = 一条总线挂多个设备（像 USB Hub）</li>
<li>BLE = 蓝牙，和 iPhone 配对</li>
</ul>
<p><strong>下一步：</strong> <a href="07-应用场景与赚钱方向.html">07-应用场景与赚钱方向</a></p>
""",
    },
    "基础/07-应用场景与赚钱方向.html": {
        "title": "基础 07：应用场景与赚钱方向",
        "tag": "基础模块",
        "module": "基础",
        "body": """
<h2>1. 高需求行业</h2>
<table>
<thead><tr><th>行业</th><th>典型产品</th><th>薪资感受</th></tr></thead>
<tbody>
<tr><td>消费电子 / IoT</td><td>台灯、插座、门锁</td><td>8K～20K</td></tr>
<tr><td>工业控制</td><td>PLC、电机驱动</td><td>10K～25K，稳定</td></tr>
<tr><td>汽车电子</td><td>ECU、BMS</td><td>15K～35K+</td></tr>
<tr><td>医疗器械</td><td>血压计、监护仪</td><td>12K～25K</td></tr>
<tr><td>新能源</td><td>充电桩、储能 BMS</td><td>热门，缺口大</td></tr>
</tbody>
</table>
<h2>2. 副业/接单方向</h2>
<ul>
<li>智能硬件原型开发（MCU + App 一体化）</li>
<li>工业设备改造（老设备加传感器上云）</li>
<li>毕业设计辅导（单片机类）</li>
</ul>
<h2>3. iOS + 嵌入式组合拳（你的差异化）</h2>
<pre><code>传感器采集（MCU）→ BLE/Wi-Fi → iOS App 展示控制 → 云端 AI 分析</code></pre>
<p>纯嵌入式工程师不会做 App，纯 iOS 不会硬件——<strong>你会两者就是稀缺人才</strong>。</p>
<p><strong>下一步：</strong> <a href="08-工具链与环境搭建.html">08-环境搭建</a></p>
""",
    },
    "基础/08-工具链与环境搭建.html": {
        "title": "基础 08：工具链与环境搭建",
        "tag": "基础模块",
        "module": "基础",
        "body": """
<h2>1. ESP32 路线（推荐首选）</h2>
<pre><code># 安装 Arduino IDE 或 VS Code + PlatformIO
# Mac 串口查看
ls /dev/cu.*          # 找到 usbserial 设备
screen /dev/cu.usbserial-xxx 115200   # 看串口输出</code></pre>
<h2>2. STM32 路线（求职向）</h2>
<ol>
<li>下载 <strong>STM32CubeIDE</strong>（免费）</li>
<li>用 ST-Link 连接电脑</li>
<li>CubeMX 图形化配置引脚 → 生成代码</li>
</ol>
<h2>3. 调试工具箱</h2>
<table>
<thead><tr><th>工具</th><th>用途</th></tr></thead>
<tbody>
<tr><td>串口监视器</td><td>看 <code>printf</code> 调试信息</td></tr>
<tr><td>万用表</td><td>测电压、通断</td></tr>
<tr><td>逻辑分析仪</td><td>看 I2C/SPI 波形</td></tr>
<tr><td>示波器</td><td>看信号质量（进阶）</td></tr>
</tbody>
</table>
<div class="tip-box">💡 第一天的目标：环境装好 → 例程编译通过 → 串口看到 "Hello" → LED 闪起来。搞定这四步就算入门。</div>
<p><strong>下一步：</strong> <a href="../入门实战/01-第一个程序点灯.html">入门实战 01-第一个程序点灯</a></p>
""",
    },
}

# Add more chapters - I'll use a helper to add remaining with good content
MORE = {
    "入门实战/01-第一个程序点灯.html": ("入门实战 01：第一个程序——点灯", "入门实战", "入门实战", """
<h2>目标</h2><p>让 LED 每秒闪一次——嵌入式界的 Hello World。</p>
<h2>Arduino 代码（ESP32）</h2>
<pre><code>#define LED_PIN 2

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(115200);
  Serial.println("Hello Embedded!");
}

void loop() {
  digitalWrite(LED_PIN, HIGH);
  delay(500);
  digitalWrite(LED_PIN, LOW);
  delay(500);
}</code></pre>
<h2>步骤</h2>
<ol>
<li>板子选 <strong>ESP32 Dev Module</strong></li>
<li>按 GPIO 接线图接 LED</li>
<li>上传 → 看 LED 闪烁 + 串口输出</li>
</ol>
<p><strong>下一步：</strong> <a href="02-按键与中断.html">02-按键与中断</a></p>
"""),
    "入门实战/02-按键与中断.html": ("入门实战 02：按键与中断", "入门实战", "入门实战", """
<h2>轮询 vs 中断</h2>
<ul>
<li><strong>轮询</strong>：<code>while(1)</code> 里不断读按键——费 CPU</li>
<li><strong>中断</strong>：按键按下 → 硬件自动跳转到处理函数——像 iOS 的 <code>target-action</code></li>
</ul>
<pre><code>void IRAM_ATTR onButton() {
  // 中断服务函数：尽量短！
  flag_pressed = true;
}

void setup() {
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(BUTTON_PIN), onButton, FALLING);
}</code></pre>
<p><strong>下一步：</strong> <a href="03-串口调试.html">03-串口调试</a></p>
"""),
    "入门实战/03-串口调试.html": ("入门实战 03：串口调试", "入门实战", "入门实战", """
<h2>串口 = 嵌入式的 NSLog</h2>
<pre><code>Serial.begin(115200);
Serial.printf("温度: %.1f°C\\n", temp);</code></pre>
<p>没有 Xcode 断点时，<code>printf</code> 是最好的朋友。复杂问题用逻辑分析仪看波形。</p>
<p><strong>下一步：</strong> <a href="04-PWM控制舵机.html">04-PWM</a></p>
"""),
    "入门实战/04-PWM控制舵机.html": ("入门实战 04：PWM 控制舵机", "入门实战", "入门实战", """
<h2>PWM 是什么？</h2>
<p><strong>PWM = 快速开关，用占空比模拟「模拟电压」</strong>。舵机根据脉宽（1ms～2ms）转到不同角度。</p>
<pre><code>#include &lt;ESP32Servo.h&gt;
Servo myservo;
myservo.attach(13);
myservo.write(90);  // 转到 90 度</code></pre>
<p>应用：云台、机器人关节、窗帘控制。</p>
<p><strong>下一步：</strong> <a href="05-温湿度传感器.html">05-温湿度</a></p>
"""),
    "入门实战/05-温湿度传感器.html": ("入门实战 05：温湿度传感器", "入门实战", "入门实战", """
<h2>DHT11 读数</h2>
<pre><code>#include &lt;DHT.h&gt;
DHT dht(4, DHT11);

void loop() {
  float t = dht.readTemperature();
  float h = dht.readHumidity();
  Serial.printf("T=%.1f H=%.1f\\n", t, h);
  delay(2000);
}</code></pre>
<p>这就是智能加湿器、农业监测的核心传感器。下一步通过 BLE 发给 iPhone 显示。</p>
<p><strong>下一步：</strong> <a href="../iOS联动/01-BLE蓝牙与iOS通信.html">iOS 联动 01-BLE</a></p>
"""),
    "进阶/01-STM32入门.html": ("进阶 01：STM32 入门", "进阶", "进阶", """
<h2>为什么学 STM32？</h2>
<p>求职嵌入式岗位，JD 里 80% 写 STM32。ESP32 偏 IoT，STM32 偏工业/汽车/医疗。</p>
<h2>开发流程</h2>
<ol>
<li>STM32CubeMX 选芯片 → 配置时钟、GPIO</li>
<li>生成工程 → CubeIDE 打开</li>
<li>在 <code>main.c</code> 的 <code>while(1)</code> 里写逻辑</li>
<li>ST-Link 下载调试</li>
</ol>
<p><strong>下一步：</strong> <a href="02-FreeRTOS基础.html">02-FreeRTOS</a></p>
"""),
    "进阶/02-FreeRTOS基础.html": ("进阶 02：FreeRTOS 基础", "进阶", "进阶", """
<h2>为什么需要 RTOS？</h2>
<p>一个 <code>while(1)</code> 搞不定时：既要读传感器，又要发 Wi-Fi，还要闪 LED——用<strong>多任务</strong>。</p>
<pre><code>// 类似 DispatchQueue：两个任务并行
xTaskCreate(task_sensor, "sensor", 2048, NULL, 1, NULL);
xTaskCreate(task_wifi,   "wifi",   4096, NULL, 1, NULL);
vTaskStartScheduler();</code></pre>
<p>对应 iOS：<code>DispatchQueue.global().async</code> + 信号量/队列。</p>
<p><strong>下一步：</strong> <a href="03-低功耗设计.html">03-低功耗</a></p>
"""),
    "进阶/03-低功耗设计.html": ("进阶 03：低功耗设计", "进阶", "进阶", """
<h2>场景</h2>
<p>门锁电池要撑 1 年、手环要撑 1 周——MCU 大部分时间在睡觉。</p>
<ul>
<li>睡眠模式：μA 级电流</li>
<li>定时唤醒读传感器</li>
<li>BLE 广播间隔拉长</li>
</ul>
<p>面试常问：如何测量功耗？答：万用表串在 VCC 上，看 sleep/active 电流。</p>
"""),
    "进阶/04-OTA固件升级.html": ("进阶 04：OTA 固件升级", "进阶", "进阶", """
<h2>OTA = Over-The-Air</h2>
<p>设备联网后远程更新固件，不用拆机插线——和 iOS App 热更新概念类似（但固件更新要更谨慎）。</p>
<ul>
<li>ESP32：<code>ArduinoOTA</code> 或 ESP-IDF OTA 分区</li>
<li>双分区：一个跑，一个下载，切换启动</li>
<li>必须做：版本号、校验、失败回滚</li>
</ul>
"""),
    "iOS联动/01-BLE蓝牙与iOS通信.html": ("iOS 联动 01：BLE 与 iOS 通信", "iOS 联动", "iOS联动", """
<h2>架构</h2>
<pre><code>ESP32 (Peripheral)  ←BLE→  iPhone (Central / CoreBluetooth)</code></pre>
<h2>BLE 核心概念</h2>
<table>
<thead><tr><th>BLE 术语</th><th>类比</th></tr></thead>
<tbody>
<tr><td>Service</td><td>一组功能的集合（如「温湿度服务」）</td></tr>
<tr><td>Characteristic</td><td>具体数据（温度值、开关状态）</td></tr>
<tr><td>UUID</td><td>唯一标识符</td></tr>
<tr><td>Notify</td><td>设备主动推数据给手机（像 WebSocket）</td></tr>
</tbody>
</table>
<h2>ESP32 端（Arduino）</h2>
<pre><code>#include &lt;BLEDevice.h&gt;
BLECharacteristic *pChar;

void setup() {
  BLEDevice::init("MyLamp");
  BLEServer *server = BLEDevice::createServer();
  BLEService *svc = server-&gt;createService("1234");
  pChar = svc-&gt;createCharacteristic("5678",
    BLECharacteristic::PROPERTY_READ | BLECharacteristic::PROPERTY_NOTIFY);
  svc-&gt;start();
  BLEDevice::getAdvertising()-&gt;start();
}</code></pre>
<p><strong>下一步：</strong> <a href="04-CoreBluetooth实战代码.html">04-CoreBluetooth 实战</a></p>
"""),
    "iOS联动/02-WiFi-MQTT与App联动.html": ("iOS 联动 02：WiFi + MQTT", "iOS 联动", "iOS联动", """
<h2>三方架构</h2>
<pre><code>ESP32 ──MQTT──→ 云端 Broker ←──MQTT── App
         (发布/订阅主题)</code></pre>
<p>主题示例：<code>home/lamp/power</code> 发 <code>ON</code> / <code>OFF</code>。</p>
<ul>
<li>MCU：PubSubClient 库</li>
<li>iOS：CocoaMQTT 或自建 WebSocket</li>
<li>云端：EMQX、阿里云 IoT（免费额度）</li>
</ul>
<p>优点：不限距离；缺点：要联网、要服务器。</p>
"""),
    "iOS联动/03-智能硬件全栈方案.html": ("iOS 联动 03：智能硬件全栈方案", "iOS 联动", "iOS联动", """
<h2>完整产品架构</h2>
<pre><code>┌─────────────┐   BLE/Wi-Fi   ┌─────────────┐
│  ESP32/STM32 │◄────────────►│   iOS App   │
│  传感器/执行器│               │  SwiftUI UI │
└──────┬──────┘               └──────┬──────┘
       │ MQTT/HTTP                     │ HTTPS
       └──────────► 云端 API ◄────────┘
                    (用户/数据/AI)</code></pre>
<h2>你的角色（iOS 背景）</h2>
<ul>
<li>固件：采集 + 通信协议</li>
<li>App：配网、控制、OTA 入口</li>
<li>云端：账号、数据存储、可选 AI</li>
</ul>
<p>这就是小米、涂鸦智能的产品模式——一个人做小版完全可行。</p>
"""),
    "iOS联动/04-CoreBluetooth实战代码.html": ("iOS 联动 04：CoreBluetooth 实战", "iOS 联动", "iOS联动", """
<h2>Swift 扫描 + 连接</h2>
<pre><code>import CoreBluetooth

class BLEManager: NSObject, CBCentralManagerDelegate, CBPeripheralDelegate {
    var central: CBCentralManager!
    var peripheral: CBPeripheral?

    override init() {
        super.init()
        central = CBCentralManager(delegate: self, queue: nil)
    }

    func centralManagerDidUpdateState(_ central: CBCentralManager) {
        if central.state == .poweredOn {
            central.scanForPeripherals(withServices: nil)
        }
    }

    func centralManager(_ central: CBCentralManager,
        didDiscover peripheral: CBPeripheral, ...) {
        if peripheral.name == "MyLamp" {
            self.peripheral = peripheral
            central.connect(peripheral)
        }
    }
}</code></pre>
<p>你在 iOS 项目里已经熟悉 delegate 模式——BLE 全是 delegate 回调。</p>
"""),
    "项目实战/01-智能台灯.html": ("项目实战 01：智能台灯", "项目实战", "项目实战", """
<h2>功能</h2>
<ul>
<li>按键调亮度</li>
<li>App BLE 调亮度 + 定时关闭</li>
<li>记忆上次亮度（Flash 存储）</li>
</ul>
<h2>技术栈</h2>
<p>ESP32 + PWM + BLE + SwiftUI 滑块</p>
<h2>里程碑</h2>
<ol>
<li>第 1 天：PWM 调光</li>
<li>第 2 天：BLE 服务</li>
<li>第 3 天：iOS App 联调</li>
<li>第 4 天：封装小盒子（可选 3D 打印外壳）</li>
</ol>
"""),
    "项目实战/02-远程开关.html": ("项目实战 02：远程开关", "项目实战", "项目实战", """
<h2>功能</h2>
<p>手机在任何地方控制家里插座通断。</p>
<h2>技术栈</h2>
<p>ESP32 + 继电器模块 + MQTT + iOS App</p>
<div class="tip-box">⚠️ <strong>安全警告</strong>：涉及 220V 强电务必用现成合规模块，不要自己焊高压部分！</div>
"""),
    "项目实战/03-环境检测仪.html": ("项目实战 03：环境检测仪", "项目实战", "项目实战", """
<h2>功能</h2>
<p>温湿度 + 空气质量（MQ-135）→ App 图表展示 → 超阈值推送通知。</p>
<h2>技术栈</h2>
<p>ESP32 + DHT22 + MQ-135 + BLE Notify + Swift Charts</p>
<p>这个项目可以写进简历：「独立完成 MCU 固件 + iOS App 联调」。</p>
"""),
    "硬件/01-开发板与工具.html": ("硬件 01：开发板与工具", "硬件入门", "硬件", """
<h2>1. 必备工具清单</h2>
<table>
<tr><th>工具</th><th>用途</th><th>必须？</th></tr>
<tr><td>ESP32 开发板</td><td>主控</td><td>✅</td></tr>
<tr><td>USB 数据线</td><td>供电+烧录</td><td>✅</td></tr>
<tr><td>面包板 + 杜邦线</td><td>免焊接实验</td><td>✅</td></tr>
<tr><td>LED + 电阻 + 按键</td><td>基础实验</td><td>✅</td></tr>
<tr><td>万用表</td><td>测电压/通断</td><td>✅</td></tr>
</table>
<h2>2. 软件工具</h2>
<table>
<tr><th>软件</th><th>用途</th></tr>
<tr><td>Arduino IDE / PlatformIO</td><td>ESP32 快速开发</td></tr>
<tr><td>STM32CubeIDE</td><td>STM32 官方 IDE</td></tr>
<tr><td>Serial Studio</td><td>串口数据可视化</td></tr>
</table>
<h2>3. Mac 环境</h2>
<pre><code>brew install --cask arduino-ide
# 或 VS Code + PlatformIO 插件</code></pre>
<p><strong>下一步：</strong> <a href="02-万用表与焊接入门.html">02-万用表与焊接</a></p>
"""),
    "硬件/02-万用表与焊接入门.html": ("硬件 02：万用表与焊接入门", "硬件入门", "硬件", """
<h2>1. 万用表三件套</h2>
<ol>
<li><strong>测电压</strong>：确认 3.3V / 5V 供电正常</li>
<li><strong>测通断</strong>：检查焊接是否连通（蜂鸣档）</li>
<li><strong>测电阻</strong>：确认阻值正确</li>
</ol>
<h2>2. 安全红线</h2>
<ul>
<li>⚠️ 不要带电焊接</li>
<li>⚠️ 不要短路 VCC 和 GND</li>
<li>⚠️ ESP32 GPIO 只能 3.3V，5V 会烧</li>
</ul>
<h2>3. 焊接五步</h2>
<p>加热焊盘 → 送锡 → 移锡 → 停 1 秒 → 移烙铁。焊点应光滑饱满。</p>
<p><strong>下一步：</strong> <a href="03-原理图阅读入门.html">03-原理图阅读</a></p>
"""),
    "硬件/03-原理图阅读入门.html": ("硬件 03：原理图阅读入门", "硬件入门", "硬件", """
<h2>1. 为什么要看原理图？</h2>
<p>做 iOS 要看 API 文档，做硬件要看原理图——每个引脚连了什么、电源怎么走。</p>
<h2>2. 阅读顺序</h2>
<ol>
<li>找 <strong>MCU 芯片</strong>（引脚最多）</li>
<li>看 <strong>电源</strong>（VCC → 稳压 → 3.3V）</li>
<li>看 <strong>引脚连接</strong>（LED→GPIO2, 按键→GPIO0…）</li>
<li>看 <strong>通信接口</strong>（I2C 传感器、SPI 屏）</li>
</ol>
<div class="tip-box">💡 推荐：立创 EDA（免费在线）、LCSC 商城买元件</div>
<p><strong>下一步：</strong> <a href="../入门实战/01-第一个程序点灯.html">入门实战 01-点灯</a></p>
"""),
    "应用场景/01-行业应用全景.html": ("应用 01：行业应用全景", "应用场景", "应用", """
<h2>七大方向</h2>
<ul>
<li><strong>消费电子</strong>：智能家居、可穿戴——入门首选</li>
<li><strong>工业控制</strong>：PLC、电机驱动——稳定高薪</li>
<li><strong>汽车电子</strong>：ECU、BMS——薪资最高</li>
<li><strong>医疗器械</strong>：血压计、监护仪——合规要求高</li>
<li><strong>农业 IoT</strong>：土壤监测、自动灌溉</li>
<li><strong>新能源</strong>：充电桩、储能 BMS——热门</li>
<li><strong>机器人/无人机</strong>：飞控、舵机</li>
</ul>
<div class="tip-box">💡 对你最现实：<strong>消费电子 IoT + iOS App</strong>，投入小、能出作品集。</div>
<p><strong>下一步：</strong> <a href="02-如何接单赚钱.html">02-如何接单赚钱</a></p>
"""),
    "应用场景/02-如何接单赚钱.html": ("应用 02：如何接单赚钱", "应用场景", "应用", """
<h2>1. 接单渠道</h2>
<table>
<tr><th>渠道</th><th>单价</th></tr>
<tr><td>淘宝/闲鱼小项目</td><td>¥500–5000</td></tr>
<tr><td>猪八戒/程序员客栈</td><td>¥5000–30000</td></tr>
<tr><td>行业人脉/老客户</td><td>¥2万–20万</td></tr>
</table>
<h2>2. 适合 iOS 开发者的项目</h2>
<ol>
<li>App + 硬件套装（ESP32 + iOS 控制）</li>
<li>智能农业监测（温湿度 + App + 报警）</li>
<li>BLE 门禁/考勤</li>
<li>宠物/老人监护传感器 + 推送</li>
</ol>
<h2>3. 从 0 到第一单</h2>
<ol>
<li>做完 3 个项目实战 → 拍照录视频</li>
<li>GitHub 开源 + 技术博客</li>
<li>闲鱼挂「ESP32 定制开发」</li>
<li>首单低价换案例和好评</li>
</ol>
"""),
    "练习/01-入门采购清单.html": ("练习 01：入门采购清单", "练习", "练习", """
<h2>淘宝/拼多多采购表</h2>
<table>
<tr><th>物品</th><th>参考价</th></tr>
<tr><td>ESP32-DevKitC</td><td>¥25</td></tr>
<tr><td>37合1传感器套件</td><td>¥45</td></tr>
<tr><td>面包板+杜邦线</td><td>¥15</td></tr>
<tr><td>万用表</td><td>¥30</td></tr>
<tr><td>DHT22 + 舵机 + 继电器</td><td>¥30</td></tr>
</table>
<p><strong>总计约 ¥170</strong>，一个周末到货。</p>
<h2>12 周学习节奏</h2>
<pre><code>第 1–4 周：ESP32 + BLE + iOS
第 5–8 周：STM32 + FreeRTOS
第 9–12 周：2 个完整项目进作品集</code></pre>
<p><strong>下一步：</strong> <a href="02-自测题.html">02-自测题</a></p>
"""),
    "练习/02-自测题.html": ("练习 02：自测题", "练习", "练习", """
<h2>基础自测（10 题，8 分及格）</h2>
<h3>1. 单片机和 iPhone 芯片的最大区别？</h3>
<details><summary>点击查看答案</summary><p>单片机专注控制、低功耗、无复杂 OS；A 芯片是高性能 AP 跑 iOS。</p></details>
<h3>2. GPIO 输出和输入分别干什么？</h3>
<details><summary>点击查看答案</summary><p>输出控 LED/继电器；输入读按键和数字传感器。</p></details>
<h3>3. 中断和轮询哪个更省电？</h3>
<details><summary>点击查看答案</summary><p>中断。CPU 可 Sleep，事件来了才唤醒。</p></details>
<h3>4. BLE 的 Central 和 Peripheral？</h3>
<details><summary>点击查看答案</summary><p>Central=主机（iPhone），Peripheral=从机（ESP32）。</p></details>
<h3>5. 智能灯项目需要哪三部分？</h3>
<details><summary>点击查看答案</summary><p>ESP32 固件 + iOS App（CoreBluetooth）+ 可选云端。</p></details>
"""),
    "面试题/嵌入式面试题精选.html": ("嵌入式面试题精选", "面试题", "面试题", """
<h2>基础题</h2>
<h3>1. 单片机和 CPU 的区别？</h3>
<p>单片机把 CPU、RAM、Flash、外设集成在一颗芯片里，面向控制；CPU 只是处理器，需要外接内存等。</p>
<h3>2. 什么是中断？</h3>
<p>硬件事件触发 CPU 暂停当前任务，跳转执行中断服务函数，完成后返回。优先级高于轮询。</p>
<h3>3. I2C 和 SPI 区别？</h3>
<p>I2C 两线、多设备、速度较慢；SPI 四线+、速度快、适合 Flash/屏。</p>
<h2>进阶题</h2>
<h3>4. FreeRTOS 任务间通信方式？</h3>
<p>队列、信号量、互斥量、事件组。互斥量保护共享资源防竞态。</p>
<h3>5. 如何降低 MCU 功耗？</h3>
<p>睡眠模式、降频、关外设时钟、减少唤醒次数、BLE 拉长广播间隔。</p>
<h2>iOS 联动题</h2>
<h3>6. BLE 配对和绑定区别？</h3>
<p>配对建立加密连接；绑定把密钥存起来下次自动连。</p>
<h3>7. 固件 OTA 失败怎么兜底？</h3>
<p>双分区 + 启动前校验 CRC + 失败回滚旧分区。</p>
"""),
}

for path, (title, tag, module, body) in MORE.items():
    CHAPTERS[path] = {"title": title, "tag": tag, "module": module, "body": body}


def depth_of(href: str) -> int:
    return href.count("/")


def page_html(href: str, meta: dict) -> str:
    d = depth_of(href)
    prefix = "../" * d if d else ""
    mod = meta.get("module", "")
    crumb_mod = f' &nbsp;/&nbsp; {mod}模块' if mod else ""
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="{prefix}_assets/site.css">
<title>{meta['title']} - 单片机学习教程</title>
</head>
<body>
<div class="page-header">
  <div class="page-header-inner">
    <div class="crumb"><a href="{prefix}README.html">教程首页</a>{crumb_mod}</div>
    <h1>{meta['title']}</h1>
    <span class="header-tag">{meta['tag']}</span>
  </div>
</div>
<div class="container">
  <div class="content-card">
{meta['body']}
<em>（内容由 AI 生成，仅供参考）</em>
  </div>
</div>
<div class="page-footer">
  <p><a href="{prefix}README.html">← 返回教程首页</a> · 单片机 / 嵌入式学习教程</p>
</div>
<script src="{prefix}_assets/site.js" defer></script>
</body>
</html>
"""


README_BODY = """
<blockquote>
<p>一套面向 <strong>零基础 + 有 iOS 背景</strong> 的单片机 / 嵌入式学习体系。<br>
大白话讲解，每章配代码示例和对照表，帮你从「会写 App」到「能做出智能硬件」。</p>
</blockquote>
<hr>
<h2>一、学习路径</h2>
<pre><code>第 1 步 基础（8 篇）→ 概念 / C语言 / GPIO / 协议 / 选型 / 环境
第 2 步 入门实战（5 篇）→ 点灯 / 按键 / 串口 / PWM / 传感器
第 3 步 进阶（4 篇）→ STM32 / FreeRTOS / 低功耗 / OTA
第 4 步 iOS 联动（4 篇）→ BLE / MQTT / 全栈方案 / CoreBluetooth
第 5 步 项目实战（3 篇）→ 台灯 / 远程开关 / 环境检测仪
第 6 步 应用场景（2 篇）→ 行业全景 / 接单赚钱
第 7 步 练习（2 篇）→ 采购清单 / 自测题
第 8 步 面试题 → 嵌入式高频题精选</code></pre>
<h2>二、模块速览</h2>
<table>
<thead><tr><th>模块</th><th>篇数</th><th>学完你能做什么</th></tr></thead>
<tbody>
<tr><td>基础</td><td>8</td><td>搞懂单片机是什么，会选板子、装环境</td></tr>
<tr><td>入门实战</td><td>5</td><td>独立点灯、读传感器、调舵机</td></tr>
<tr><td>进阶</td><td>4</td><td>STM32 开发、多任务、OTA</td></tr>
<tr><td>iOS 联动</td><td>4</td><td>用 iPhone 控制硬件（你的核心竞争力）</td></tr>
<tr><td>硬件入门</td><td>3</td><td>工具、焊接、看原理图</td></tr>
<tr><td>项目实战</td><td>3</td><td>3 个可写进简历的完整项目</td></tr>
<tr><td>应用场景</td><td>2</td><td>行业方向、接单赚钱</td></tr>
<tr><td>练习</td><td>2</td><td>采购清单、自测巩固</td></tr>
<tr><td>面试题</td><td>1</td><td>嵌入式岗位高频题</td></tr>
</tbody>
</table>
<h2>三、推荐硬件（200 元入门）</h2>
<ul>
<li>ESP32-DevKitC × 1（约 30 元）</li>
<li>面包板 + 杜邦线 + LED + 电阻 + 按键</li>
<li>DHT11 温湿度模块</li>
<li>可选：SG90 舵机、继电器模块</li>
</ul>
<h2>四、快速入口</h2>
<ul>
<li><a href="基础/01-单片机是什么.html">基础/01-单片机是什么</a></li>
<li><a href="入门实战/01-第一个程序点灯.html">入门实战/01-第一个程序点灯</a></li>
<li><a href="iOS联动/01-BLE蓝牙与iOS通信.html">iOS联动/01-BLE蓝牙与iOS通信</a></li>
<li><a href="iOS联动/04-CoreBluetooth实战代码.html">iOS联动/04-CoreBluetooth实战</a></li>
</ul>
<h2>五、开始学习</h2>
<p>👉 从 <a href="基础/01-单片机是什么.html">基础/01-单片机是什么</a> 开始。</p>
"""


def main():
    for href, meta in CHAPTERS.items():
        out = ROOT / href
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page_html(href, meta), encoding="utf-8")
        print("wrote", href)

    readme = page_html("README.html", {
        "title": "单片机 / 嵌入式学习教程",
        "tag": "32 篇 · 小白友好 · iOS 开发者专属路径",
        "module": "",
        "body": README_BODY,
    })
    (ROOT / "README.html").write_text(readme, encoding="utf-8")

    index = """<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="refresh" content="0; url=README.html">
  <title>单片机学习教程</title>
  <script>location.replace('README.html');</script>
</head>
<body>
  <p>正在跳转到 <a href="README.html">单片机学习教程</a>…</p>
</body>
</html>
"""
    (ROOT / "index.html").write_text(index, encoding="utf-8")
    print("done:", len(CHAPTERS), "chapters")


if __name__ == "__main__":
    main()
