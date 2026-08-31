"""Chapter content definitions."""

from .helpers import chapter

CHAPTERS = {
    "基础/01-单片机概念.html": chapter(
        '基础 01：单片机概念',
        '基础模块',
        '基础',
        """<blockquote><p>建立 MCU 心智模型，区分 CPU/AP/SoC/MCU，认识主流芯片。</p></blockquote><hr>
<h2>1. 单片机是什么</h2>
<p><strong>MCU</strong> 集成 CPU、Flash、RAM、定时器、GPIO、通信外设，执行固件 7×24 控制硬件。Industry 常说「嵌入式」——MCU 是最核心执行单元。</p><table><thead><tr><th>术语</th><th>说明</th><th>例子</th></tr></thead><tbody><tr><td>CPU</td><td>处理器核</td><td>Cortex-M4</td></tr><tr><td>AP</td><td>跑 iOS</td><td>A18</td></tr><tr><td>MCU</td><td>控制专用</td><td>ESP32</td></tr></tbody></table>
<h2>2. 主流芯片 2026</h2>
<table><thead><tr><th>系列</th><th>特色</th><th>场景</th></tr></thead><tbody><tr><td>ESP32</td><td>Wi-Fi+BLE</td><td>IoT+App</td></tr><tr><td>STM32</td><td>外设全</td><td>工业求职</td></tr><tr><td>nRF52</td><td>低功耗BLE</td><td>可穿戴</td></tr></tbody></table>
<h2>3. 程序结构</h2>
<pre><code class="language-c">while(1){ read_sensors(); update_outputs(); }</code></pre><p>没有 UIApplication，就是初始化 + 死循环/事件。</p>
<h2>4. iOS 开发者价值</h2>
<p>Swift+BLE 经验 + 200 元开发板 = 完整智能硬件交付。App 控不了 GPIO，MCU 可以。</p>
<div class="tip-box">💡 选型：联网 ESP32，求职 STM32，省电 nRF。</div>
<h2>常见问题</h2>
<h3>MCU vs CPU?</h3><p>MCU 集成存储外设；CPU 只是核。</p>
<h3>入门选啥?</h3><p>ESP32 Wi-Fi/BLE 与 iOS 绝配。</p>
<h3>要 OS 吗?</h3><p>可裸机或 FreeRTOS。</p>
<h2>本章小结</h2><ul>
<li>MCU=CPU+存储+外设</li>
<li>比 AP 比实时成本功耗</li>
<li>入门 ESP32 求职 STM32</li>
<li>程序=初始化+循环</li>
</ul>
<p><strong>下一步：</strong> <a href="02-从iOS开发者视角看嵌入式.html">02-iOS 视角</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "基础/02-从iOS开发者视角看嵌入式.html": chapter(
        '基础 02：从 iOS 开发者视角看嵌入式',
        '基础模块',
        '基础',
        """<blockquote><p>用 Swift 知识映射嵌入式，对比工作流，制定 4 周路线。</p></blockquote><hr>
<h2>1. 概念对照</h2>
<table><thead><tr><th>iOS</th><th>嵌入式</th><th>说明</th></tr></thead><tbody><tr><td>UIView</td><td>GPIO</td><td>物理接口</td></tr><tr><td>Timer</td><td>硬件定时器</td><td>精确定时</td></tr><tr><td>CoreBluetooth</td><td>BLE栈</td><td>无线通信</td></tr><tr><td>UserDefaults</td><td>NVS/Flash</td><td>掉电保存</td></tr><tr><td>DispatchQueue</td><td>FreeRTOS Task</td><td>多任务</td></tr></tbody></table>
<h2>2. LED 两种写法</h2>
<pre><code class="language-swift">bleManager.write(Data([1]))</code></pre><pre><code class="language-c">HAL_GPIO_TogglePin(GPIOC,GPIO_PIN_13); HAL_Delay(500);</code></pre>
<h2>3. 工作流</h2>
<table><thead><tr><th>阶段</th><th>iOS</th><th>嵌入式</th></tr></thead><tbody><tr><td>IDE</td><td>Xcode</td><td>PlatformIO/CubeIDE</td></tr><tr><td>调试</td><td>LLDB</td><td>串口+J-Link</td></tr><tr><td>发布</td><td>TestFlight</td><td>OTA/产线烧录</td></tr></tbody></table>
<h2>4. 优劣势</h2>
<p><strong>优势</strong>：产品思维、无线经验、架构、全栈。<strong>短板</strong>：C/指针、电路、实时性、Datasheet。</p>
<div class="tip-box">💡 对照表贴显示器旁。</div>
<h2>常见问题</h2>
<h3>还要学 C?</h3><p>要，指针位操作日常。</p>
<h3>怎么调试?</h3><p>串口 printf=NSLog。</p>
<h3>最大优势?</h3><p>产品+BLE+全栈。</p>
<h2>本章小结</h2><ul>
<li>Swift 概念可映射</li>
<li>iOS 调 API 嵌入式还有寄存器</li>
<li>优势在产品无线架构</li>
<li>短板在 C 电路实时性</li>
</ul>
<p><strong>下一步：</strong> <a href="03-数电基础.html">03-数电基础</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "基础/03-数电基础.html": chapter(
        '基础 03：数电基础',
        '基础模块',
        '基础',
        """<blockquote><p>掌握高低电平、逻辑门、电平标准，建立 GPIO 数字直觉。</p></blockquote><hr>
<pre><code class="language-c">// 本章配套：在 DevKit 上验证所学概念
void setup() { Serial.begin(115200); }
void loop() { /* 实验代码 */ }</code></pre>
<h2>1. 数字 vs 模拟</h2>
<p>MCU 世界是离散 0/1。模拟信号需 ADC 采样。</p><table><thead><tr><th>概念</th><th>说明</th></tr></thead><tbody><tr><td>高/低电平</td><td>3.3V/0V</td></tr><tr><td>上升沿</td><td>0→1 跳变</td></tr><tr><td>时钟</td><td>同步节拍</td></tr></tbody></table>
<h2>2. 逻辑门</h2>
<table><thead><tr><th>门</th><th>功能</th></tr></thead><tbody><tr><td>与 AND</td><td>全1才1</td></tr><tr><td>或 OR</td><td>有1则1</td></tr><tr><td>非 NOT</td><td>取反</td></tr></tbody></table>
<h2>3. 电平标准</h2>
<table><thead><tr><th>标准</th><th>高电平</th><th>芯片</th></tr></thead><tbody><tr><td>3.3V CMOS</td><td>≥2.0V</td><td>ESP32/STM32</td></tr><tr><td>5V TTL</td><td>≥2.4V</td><td>Arduino Uno</td></tr><tr><td>开漏</td><td>靠上拉</td><td>I2C</td></tr></tbody></table>
<h2>4. 时序</h2>
<p>SPI/I2C 要求建立/保持时间，违例导致偶发 bug，需逻辑分析仪验证。</p>
<div class="tip-box">💡 先建立 0/1+时序直觉。</div>
<div class="tip-box" style="border-color:#ff6b6b;background:rgba(255,107,107,.08)">⚠️ 切勿向 3.3V GPIO 输入 5V。</div>
<h2>常见问题</h2>
<h3>数电和代码?</h3><p>GPIO 写 0/1 就是数字输出。</p>
<h3>开漏?</h3><p>只能拉低或高阻，需上拉。</p>
<h3>上拉多大?</h3><p>4.7k 常用。</p>
<h2>本章小结</h2><ul>
<li>数字=离散电平</li>
<li>3.3V/5V 不可混接</li>
<li>逻辑门是组合基础</li>
<li>时序对协议调试重要</li>
</ul>
<p><strong>下一步：</strong> <a href="04-模电入门.html">04-模电入门</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "基础/04-模电入门.html": chapter(
        '基础 04：模电入门',
        '基础模块',
        '基础',
        """<blockquote><p>理解 V=IR、电容去耦、二极管续流、LED/按键电路。</p></blockquote><hr>
<h2>1. 欧姆定律</h2>
<p><strong>V=IR</strong>。LED 限流：R=(3.3-2)/0.01≈130Ω，用 220Ω。</p><pre><code class="language-text">3.3V─[220Ω]─LED+─LED-─GND</code></pre>
<h2>2. 电容去耦</h2>
<table><thead><tr><th>用途</th><th>值</th><th>位置</th></tr></thead><tbody><tr><td>去耦</td><td>100nF</td><td>VCC 脚旁</td></tr><tr><td>bulk</td><td>10µF</td><td>LDO 旁</td></tr></tbody></table>
<h2>3. 二极管/MOS</h2>
<p>二极管防反接/续流；MOS 作电子开关。继电器线圈必须并联续流二极管。</p>
<h2>4. 按键电路</h2>
<pre><code class="language-c">GPIO_InitStruct.Pull = GPIO_PULLUP; // 按下读低</code></pre>
<div class="tip-box">💡 看懂 DevKit 原理图 LED/按键/LDO 即可。</div>
<h2>常见问题</h2>
<h3>LED 不亮?</h3><p>查极性/电阻/模式。</p>
<h3>抖动?</h3><p>软件消抖。</p>
<h3>GPIO 电流?</h3><p>约12-40mA，大负载用驱动。</p>
<h2>本章小结</h2><ul>
<li>V=IR 算限流</li>
<li>去耦电容稳定供电</li>
<li>二极管续流防反接</li>
<li>按键用上拉输入</li>
</ul>
<p><strong>下一步：</strong> <a href="05-开发板怎么选.html">05-开发板选型</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "基础/05-开发板怎么选.html": chapter(
        '基础 05：开发板怎么选',
        '基础模块',
        '基础',
        """<blockquote><p>200 元内配齐入门环境，ESP32/STM32/Arduino 对比。</p></blockquote><hr>
<pre><code class="language-c">// 本章配套：在 DevKit 上验证所学概念
void setup() { Serial.begin(115200); }
void loop() { /* 实验代码 */ }</code></pre>
<h2>1. 三板斧</h2>
<table><thead><tr><th>板</th><th>价格</th><th>理由</th></tr></thead><tbody><tr><td>ESP32-DevKitC</td><td>30元</td><td>Wi-Fi+BLE+iOS</td></tr><tr><td>Arduino Uno</td><td>25元</td><td>最简单</td></tr><tr><td>STM32F103</td><td>12元</td><td>求职工业</td></tr></tbody></table>
<h2>2. 配件清单</h2>
<ul><li>面包板+杜邦线</li><li>LED+220Ω 电阻</li><li>按键</li><li>DHT22 温湿度</li><li>万用表</li><li>Type-C 数据线</li></ul>
<h2>3. 别买</h2>
<ul><li>树莓派当 MCU 入门（它是 Linux 电脑）</li><li>50 合 1 传感器大礼包（90% 吃灰）</li></ul>
<h2>4. Mac 开发</h2>
<p>完全支持。ESP32 Arduino/PlatformIO，STM32 CubeIDE 均有 macOS 版。</p>
<div class="tip-box">💡 ESP32-DevKitC 一块板走 IoT+iOS 全程。</div>
<h2>常见问题</h2>
<h3>Mac 能开发?</h3><p>完全支持。</p>
<h3>兼容板?</h3><p>可以，注意 USB 驱动。</p>
<h3>要示波器?</h3><p>入门不必。</p>
<h2>本章小结</h2><ul>
<li>ESP32 IoT 首选</li>
<li>STM32 求职</li>
<li>200元配齐</li>
<li>别买树莓派当 MCU</li>
</ul>
<p><strong>下一步：</strong> <a href="06-C语言速成-Swift开发者版.html">06-C 语言</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "基础/06-C语言速成-Swift开发者版.html": chapter(
        '基础 06：C 语言速成（Swift 开发者版）',
        '基础模块',
        '基础',
        """<blockquote><p>掌握 C 与 Swift 差异、函数、结构体、头文件模块化。</p></blockquote><hr>
<h2>1. 语法对照</h2>
<table><thead><tr><th>Swift</th><th>C</th></tr></thead><tbody><tr><td>var x=10</td><td>int x=10;</td></tr><tr><td>func add(a:Int,b:Int)</td><td>int add(int a,int b)</td></tr><tr><td>struct Point</td><td>typedef struct { float x,y; } Point;</td></tr><tr><td>ARC</td><td>栈/静态分配，慎用 malloc</td></tr></tbody></table>
<h2>2. 头文件模块化</h2>
<pre><code class="language-c">// led.h
void led_init(void);
void led_toggle(void);

// led.c
#include "led.h"
void led_toggle(void){ HAL_GPIO_TogglePin(...); }</code></pre>
<h2>3. 预处理与宏</h2>
<pre><code class="language-c">#define LED_PIN GPIO_PIN_13
#define LED_ON()  HAL_GPIO_WritePin(GPIOC, LED_PIN, GPIO_PIN_SET)</code></pre>
<h2>4. 与 Swift 互操作</h2>
<p>将来用 Swift 写 App 层，C 写 MCU 固件；两者通过 BLE/MQTT 通信，非直接链接。</p>
<div class="tip-box">💡 C 无 ARC，局部变量在栈上，函数结束自动释放。</div>
<h2>常见问题</h2>
<h3>要 malloc 吗?</h3><p>多用栈/静态，RTOS 任务栈预分配。</p>
<h3>.h .c 分工?</h3><p>声明与实现分离，类似 Swift 多文件。</p>
<h3>bool 类型?</h3><p>stdbool.h 的 bool/true/false。</p>
<h2>本章小结</h2><ul>
<li>C 无 ARC 需手动管理</li>
<li>头文件模块化</li>
<li>宏简化寄存器操作</li>
<li>为指针章节打基础</li>
</ul>
<p><strong>下一步：</strong> <a href="07-指针与内存.html">07-指针与内存</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "基础/07-指针与内存.html": chapter(
        '基础 07：指针与内存',
        '基础模块',
        '基础',
        """<blockquote><p>理解指针、地址、堆栈、volatile，读懂 memory map。</p></blockquote><hr>
<h2>1. 指针本质</h2>
<p>指针 = 内存地址。MCU 上同一语法访问 RAM 变量与外设寄存器。</p><pre><code class="language-c">int x = 42;
int *p = &x;   // p 存 x 的地址
*p = 100;      // 通过指针改 x
printf("%p %d\\n", p, *p);</code></pre>
<h2>2. Memory Map</h2>
<table><thead><tr><th>地址</th><th>区域</th><th>内容</th></tr></thead><tbody><tr><td>0x08000000</td><td>Flash</td><td>程序/常量</td></tr><tr><td>0x20000000</td><td>SRAM</td><td>变量/栈/堆</td></tr><tr><td>0x40000000</td><td>外设</td><td>GPIO/UART 寄存器</td></tr></tbody></table>
<h2>3. volatile</h2>
<pre><code class="language-c">*(volatile uint32_t *)0x4001080C |= (1 << 13); // 写 GPIO 寄存器</code></pre><p>告诉编译器「每次都要真读/写」，不可优化掉。</p>
<h2>4. 栈与堆</h2>
<table><thead><tr><th>区域</th><th>特点</th><th>iOS 类比</th></tr></thead><tbody><tr><td>栈</td><td>函数局部变量，自动回收</td><td>函数调用栈</td></tr><tr><td>堆</td><td>malloc 分配，需 free</td><td>ARC 管理的堆对象</td></tr><tr><td>静态</td><td>全局/static，程序生命周期</td><td>static let</td></tr></tbody></table>
<div class="tip-box">💡 寄存器访问必须 volatile。</div>
<h2>常见问题</h2>
<h3>指针和数组?</h3><p>数组名即首地址，可指针运算。</p>
<h3>野指针?</h3><p>free 后不再使用，RTOS 注意任务栈大小。</p>
<h3>Flash 存大数组?</h3><p>const 放 Flash，省 RAM。</p>
<h2>本章小结</h2><ul>
<li>指针=地址</li>
<li>Memory map 是目录树</li>
<li>volatile 访问寄存器</li>
<li>栈堆静态分工明确</li>
</ul>
<p><strong>下一步：</strong> <a href="08-位操作与寄存器.html">08-位操作</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "基础/08-位操作与寄存器.html": chapter(
        '基础 08：位操作与寄存器',
        '基础模块',
        '基础',
        """<blockquote><p>掌握位与/或/异或/移位，读写寄存器配置外设。</p></blockquote><hr>
<table><thead><tr><th>要点</th><th>说明</th></tr></thead><tbody><tr><td>实验</td><td>DevKit 验证</td></tr><tr><td>调试</td><td>串口 printf</td></tr></tbody></table>
<h2>1. 位操作符</h2>
<pre><code class="language-c">// 置位第5位
reg |= (1 << 5);
// 清位
reg &= ~(1 << 5);
// 翻转
reg ^= (1 << 5);
// 读位
if (reg & (1 << 3)) { ... }</code></pre>
<h2>2. 寄存器结构体</h2>
<pre><code class="language-c">typedef struct {
    volatile uint32_t MODER;   // 模式
    volatile uint32_t ODR;     // 输出
} GPIO_TypeDef;
#define GPIOA ((GPIO_TypeDef *)0x40010800)</code></pre>
<h2>3. HAL 封装</h2>
<p>HAL_GPIO_WritePin 底层仍是位操作。调试到底层时需看 Reference Manual 寄存器定义。</p>
<h2>4. 位域 struct</h2>
<pre><code class="language-c">typedef struct {
    uint32_t mode  : 2;
    uint32_t type  : 1;
    uint32_t res   : 29;
} GPIO_MODER_Bits;</code></pre>
<div class="tip-box">💡 位操作是寄存器配置日常，类似 Swift OptionSet。</div>
<h2>常见问题</h2>
<h3>为何不用乘除?</h3><p>移位比乘除快，编译期可优化。</p>
<h3>HAL vs 寄存器?</h3><p>HAL 可移植，寄存器高效/debug。</p>
<h3>位域 portable?</h3><p>依赖编译器/endian，MCU 常用宏。</p>
<h2>本章小结</h2><ul>
<li>位操作配置寄存器</li>
<li>|= 置位 &=~ 清位</li>
<li>HAL 底层仍是位操作</li>
<li>读 RM 寄存器章节</li>
</ul>
<p><strong>下一步：</strong> <a href="09-GPIO与点灯原理.html">09-GPIO</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "基础/09-GPIO与点灯原理.html": chapter(
        '基础 09：GPIO 与点灯原理',
        '基础模块',
        '基础',
        """<blockquote><p>理解 GPIO 输入/输出/上拉/开漏，完成 LED 点灯电路分析。</p></blockquote><hr>
<h2>1. GPIO 模式</h2>
<table><thead><tr><th>模式</th><th>用途</th></tr></thead><tbody><tr><td>推挽输出</td><td>LED/继电器</td></tr><tr><td>输入浮空</td><td>需外部上下拉</td></tr><tr><td>输入上拉</td><td>按键</td></tr><tr><td>开漏输出</td><td>I2C/线与</td></tr></tbody></table>
<h2>2. LED 电路</h2>
<pre><code class="language-text">GPIO_OUT ──[220Ω]── LED+ ── LED- ── GND</code></pre><p>有些板 LED 接 VCC，低电平点亮——看原理图。</p>
<h2>3. Arduino 点灯</h2>
<pre><code class="language-c">pinMode(2, OUTPUT);
while(1) {
  digitalWrite(2, HIGH); delay(500);
  digitalWrite(2, LOW);  delay(500);
}</code></pre>
<h2>4. HAL 点灯</h2>
<pre><code class="language-c">HAL_GPIO_WritePin(GPIOC, GPIO_PIN_13, GPIO_PIN_SET);</code></pre>
<div class="tip-box">💡 GPIO 是 MCU 与外界的桥梁，点灯是 Hello World。</div>
<h2>常见问题</h2>
<h3>灌电流/拉电流?</h3><p>看 LED 接法与芯片手册。</p>
<h3>驱动能力?</h3><p>单脚 ~12mA，大负载用驱动。</p>
<h3>浮空输入?</h3><p>易误触发，用上下拉。</p>
<h2>本章小结</h2><ul>
<li>GPIO 六种模式</li>
<li>点灯=Hello World</li>
<li>限流电阻必须</li>
<li>查板子引脚图</li>
</ul>
<p><strong>下一步：</strong> <a href="10-中断与定时器.html">10-中断定时器</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "基础/10-中断与定时器.html": chapter(
        '基础 10：中断与定时器',
        '基础模块',
        '基础',
        """<blockquote><p>轮询 vs 中断，ISR 规范，硬件定时器精确定时。</p></blockquote><hr>
<h2>1. 轮询 vs 中断</h2>
<table><thead><tr><th>方式</th><th>CPU</th><th>类比</th></tr></thead><tbody><tr><td>轮询</td><td>持续占用</td><td>while 检查</td></tr><tr><td>中断</td><td>事件驱动</td><td>Button action</td></tr></tbody></table>
<h2>2. ISR 规范</h2>
<pre><code class="language-c">volatile bool flag = false;
void IRAM_ATTR isr() { flag = true; } // 短小，不 delay
void loop() { if(flag){ flag=false; handle(); } }</code></pre>
<h2>3. 硬件定时器</h2>
<p>精确定时/PWM/RTOS tick。STM32 TIM、ESP32 hw_timer。</p>
<h2>4. 按键防抖</h2>
<p>中断置标志，主循环 delay 10ms 再读 GPIO 确认。</p>
<div class="tip-box">💡 ISR 里禁止 HAL_Delay/printf，类似主线程不做耗时网络。</div>
<h2>常见问题</h2>
<h3>优先级?</h3><p>高优先级可抢占低。</p>
<h3>ISR printf?</h3><p>不推荐，只置标志。</p>
<h3>定时器 vs delay?</h3><p>定时器不阻塞 CPU。</p>
<h2>本章小结</h2><ul>
<li>中断=事件驱动</li>
<li>ISR 要短要快</li>
<li>硬件定时器精确</li>
<li>按键需防抖</li>
</ul>
<p><strong>下一步：</strong> <a href="11-存储器与Flash.html">11-Flash</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "基础/11-存储器与Flash.html": chapter(
        '基础 11：存储器与 Flash',
        '基础模块',
        '基础',
        """<blockquote><p>Flash/SRAM/EEPROM/NVS 区别，掉电保存与 wear leveling。</p></blockquote><hr>
<h2>1. 存储类型</h2>
<table><thead><tr><th>类型</th><th>掉电</th><th>用途</th></tr></thead><tbody><tr><td>Flash</td><td>保持</td><td>程序+常量</td></tr><tr><td>SRAM</td><td>丢失</td><td>变量栈堆</td></tr><tr><td>EEPROM</td><td>保持</td><td>小数据配置</td></tr><tr><td>NVS(ESP32)</td><td>保持</td><td>键值对配置</td></tr></tbody></table>
<h2>2. ESP32 Preferences</h2>
<pre><code class="language-c">#include <Preferences.h>
Preferences prefs;
prefs.begin("app", false);
prefs.putInt("boot_count", count++);
int n = prefs.getInt("boot_count", 0);</code></pre>
<h2>3. STM32 内部 Flash</h2>
<p>程序存储，也可划分区做 EEPROM 仿真。OTA 需双分区。</p>
<h2>4. iOS 对照</h2>
<p>UserDefaults ≈ NVS；Keychain ≈ 加密 Flash 区；Documents ≈ 外置 Flash 文件系统。</p>
<div class="tip-box">💡 频繁写入用 NVS/EEPROM，注意擦写寿命。</div>
<h2>常见问题</h2>
<h3>Flash 能当 RAM?</h3><p>XIP 读可以，写慢且有限寿命。</p>
<h3>NVS 满?</h3><p>擦除分区，设计键名规范。</p>
<h3>OTA 分区?</h3><p>app0/app1 双备份。</p>
<h2>本章小结</h2><ul>
<li>Flash 存程序</li>
<li>SRAM 存变量</li>
<li>NVS 存配置</li>
<li>注意擦写次数</li>
</ul>
<p><strong>下一步：</strong> <a href="12-工具链与环境搭建.html">12-环境搭建</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "基础/12-工具链与环境搭建.html": chapter(
        '基础 12：工具链与环境搭建',
        '基础模块',
        '基础',
        """<blockquote><p>Mac 安装 ESP32/STM32 工具链，跑通烧录串口闭环。</p></blockquote><hr>
<h2>1. ESP32 Arduino</h2>
<pre><code class="language-bash">brew install --cask arduino-ide
# 添加 ESP32 板管理 URL
# 工具→端口→选 /dev/cu.usbserial-*
# 上传 Blink sketch</code></pre>
<h2>2. PlatformIO</h2>
<pre><code class="language-ini">[env:esp32dev]
platform = espressif32
board = esp32dev
framework = arduino
monitor_speed = 115200</code></pre>
<h2>3. STM32</h2>
<ol><li>安装 STM32CubeIDE</li><li>ST-Link 驱动</li><li>CubeMX 生成工程</li></ol>
<h2>4. 验收四步</h2>
<table><thead><tr><th>步骤</th><th>标准</th></tr></thead><tbody><tr><td>编译</td><td>0 error</td></tr><tr><td>烧录</td><td>100%</td></tr><tr><td>串口</td><td>Hello World</td></tr><tr><td>LED</td><td>闪烁</td></tr></tbody></table>
<div class="tip-box">💡 第一天目标：环境→编译→串口→LED 四步闭环。</div>
<h2>常见问题</h2>
<h3>PlatformIO vs Arduino?</h3><p>工程大用 PIO，入门 Arduino IDE。</p>
<h3>找不到串口?</h3><p>装 CP210x/CH340 驱动。</p>
<h3>烧录超时?</h3><p>按住 BOOT 再上传。</p>
<h2>本章小结</h2><ul>
<li>ESP32 Arduino/PIO</li>
<li>STM32 CubeIDE</li>
<li>串口=NSLog</li>
<li>四步验收通过</li>
</ul>
<p><strong>下一步：</strong> <a href="../硬件/01-开发板与工具.html">硬件 01</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
}
