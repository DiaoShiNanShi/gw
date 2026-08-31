#!/usr/bin/env python3
"""Generate 单片机/嵌入式 learning tutorial HTML pages."""
from pathlib import Path

ROOT = Path(__file__).parent
SITE = "单片机嵌入式教程"

NAV = [
    ("基础", [
        ("01-单片机是什么", "基础/01-单片机是什么.html"),
        ("02-从iOS到嵌入式", "基础/02-从iOS到嵌入式.html"),
        ("03-C语言速成", "基础/03-C语言速成.html"),
        ("04-GPIO与点亮LED", "基础/04-GPIO与点亮LED.html"),
        ("05-中断与定时器", "基础/05-中断与定时器.html"),
        ("06-串口UART通信", "基础/06-串口UART通信.html"),
        ("07-I2C与SPI协议", "基础/07-I2C与SPI协议.html"),
        ("08-芯片选型指南", "基础/08-芯片选型指南.html"),
    ]),
    ("硬件入门", [
        ("01-开发板与工具", "硬件/01-开发板与工具.html"),
        ("02-万用表与焊接入门", "硬件/02-万用表与焊接入门.html"),
        ("03-原理图阅读入门", "硬件/03-原理图阅读入门.html"),
    ]),
    ("进阶", [
        ("01-FreeRTOS入门", "进阶/01-FreeRTOS入门.html"),
        ("02-低功耗设计", "进阶/02-低功耗设计.html"),
        ("03-WiFi与MQTT", "进阶/03-WiFi与MQTT.html"),
        ("04-蓝牙BLE通信", "进阶/04-蓝牙BLE通信.html"),
    ]),
    ("实战项目", [
        ("01-智能灯控", "实战/01-智能灯控.html"),
        ("02-温湿度监测", "实战/02-温湿度监测.html"),
        ("03-蓝牙控制小车", "实战/03-蓝牙控制小车.html"),
    ]),
    ("iOS 联动", [
        ("01-BLE与CoreBluetooth", "iOS联动/01-BLE与CoreBluetooth.html"),
        ("02-iOS控制硬件全链路", "iOS联动/02-iOS控制硬件全链路.html"),
    ]),
    ("应用场景", [
        ("01-行业应用全景", "应用场景/01-行业应用全景.html"),
        ("02-如何接单赚钱", "应用场景/02-如何接单赚钱.html"),
    ]),
    ("练习", [
        ("01-入门采购清单", "练习/01-入门采购清单.html"),
        ("02-自测题", "练习/02-自测题.html"),
    ]),
]

PAGES = {
"基础/01-单片机是什么.html": {
    "title": "基础 01：单片机是什么",
    "tag": "基础模块",
    "module": "基础",
    "body": """
<blockquote><p>学习目标：10 分钟搞清单片机是什么，以及它和 iPhone 里的芯片有什么关系。</p></blockquote>
<h2>1. 一句话说清单片机</h2>
<p><strong>单片机（MCU）= 一块指甲盖大小的芯片，里面集成了 CPU + 内存 + 定时器 + 通信接口，专门用来控制硬件。</strong></p>
<p>它不跑 iOS、不跑微信，它的工作就是：<strong>读传感器 → 做判断 → 控制电机/灯/屏幕</strong>，24 小时不停。</p>
<h2>2. 核心比喻：单片机 = 永不关机的后台 Service</h2>
<table>
<tr><th>对比</th><th>iOS App</th><th>单片机</th></tr>
<tr><td>运行环境</td><td>iPhone（A 系列芯片 + iOS）</td><td>独立小芯片，无操作系统或轻量 RTOS</td></tr>
<tr><td>主要任务</td><td>界面交互、网络请求</td><td>读 GPIO、控制继电器、采集数据</td></tr>
<tr><td>功耗</td><td>毫安～安级，需要充电</td><td>微安级，纽扣电池能跑一年</td></tr>
<tr><td>开发语言</td><td>Swift / Objective-C</td><td>C / C++（偶尔 MicroPython）</td></tr>
<tr><td>调试方式</td><td>Xcode + 模拟器</td><td>串口打印 + 示波器 + 逻辑分析仪</td></tr>
</table>
<div class="tip-box">💡 <strong>iOS 开发者优势</strong>：你已经懂内存管理、多线程、协议通信——这些概念在嵌入式里一模一样，只是换了个"更靠近硬件"的写法。</div>
<h2>3. 单片机在哪里？（你每天都在用）</h2>
<ul>
<li>⌚ Apple Watch 里的传感器协处理器</li>
<li>🔌 智能插座、扫地机、空调遥控器</li>
<li>🚗 车窗升降、雨刷、仪表盘</li>
<li>🏥 血压计、血糖仪</li>
<li>🏭 工厂流水线的 PLC 控制器</li>
<li>📡 Wi-Fi 路由器、蓝牙音箱</li>
</ul>
<h2>4. 嵌入式 vs 单片机 vs IoT</h2>
<table>
<tr><th>名词</th><th>大白话</th></tr>
<tr><td><strong>单片机</strong></td><td>特指 MCU 芯片本身（如 STM32、ESP32）</td></tr>
<tr><td><strong>嵌入式</strong></td><td>把软件烧进硬件里的开发方式（广义，含 Linux 板）</td></tr>
<tr><td><strong>IoT 物联网</strong></td><td>嵌入式设备 + 联网 + 云端/App（你的 iOS 技能在这里发光）</td></tr>
</table>
<h2>5. 学单片机能帮你什么？</h2>
<ol>
<li><strong>做智能硬件</strong>：App 控制真实世界的灯、锁、传感器</li>
<li><strong>拓宽职业路径</strong>：IoT 工程师、嵌入式工程师薪资 10K–25K</li>
<li><strong>接外包项目</strong>：智能农业、门禁、工业采集，项目 5K–50K</li>
<li><strong>和大模型结合</strong>：ESP32 采集数据 → 云端 AI 分析 → iOS 展示</li>
</ol>
<h2>小结</h2>
<ul>
<li>单片机 = 控制硬件的小电脑，不是跑 App 的手机</li>
<li>你已有的 iOS 经验是巨大优势（通信、架构、产品思维）</li>
<li>IoT = 单片机 + 联网 + 你的 App，这是最赚钱的组合</li>
</ul>
<p>下一步：→ <a href="02-从iOS到嵌入式.html">从 iOS 到嵌入式：概念对照表</a></p>
""",
},
"基础/02-从iOS到嵌入式.html": {
    "title": "基础 02：从 iOS 到嵌入式",
    "tag": "基础模块",
    "module": "基础",
    "body": """
<blockquote><p>学习目标：用你已经懂的 iOS 概念，快速映射到嵌入式，降低学习曲线。</p></blockquote>
<h2>1. 概念对照表（iOS 开发者速查）</h2>
<table>
<tr><th>iOS 概念</th><th>嵌入式对应</th><th>说明</th></tr>
<tr><td><code>UIViewController</code></td><td>主循环 <code>while(1)</code> / 状态机</td><td>程序的核心调度逻辑</td></tr>
<tr><td><code>UIButton</code> 点击</td><td>GPIO 中断 / 按键扫描</td><td>外部事件触发</td></tr>
<tr><td><code>URLSession</code></td><td>UART / Wi-Fi / MQTT</td><td>设备间通信</td></tr>
<tr><td><code>CoreBluetooth</code></td><td>BLE 协议栈（NimBLE）</td><td>低功耗蓝牙，直接对应！</td></tr>
<tr><td><code>UserDefaults</code></td><td>Flash EEPROM</td><td>掉电不丢的配置存储</td></tr>
<tr><td><code>DispatchQueue</code></td><td>FreeRTOS 任务 / 中断</td><td>并发与优先级</td></tr>
<tr><td><code>Timer</code></td><td>硬件定时器 TIM</td><td>精确到微秒级</td></tr>
<tr><td><code>Instruments</code></td><td>示波器 + 逻辑分析仪</td><td>看"波形"而不是"调用栈"</td></tr>
<tr><td><code>App Delegate</code></td><td><code>main()</code> 函数</td><td>程序入口</td></tr>
<tr><td><code>Storyboard</code></td><td>没有！全写代码</td><td>嵌入式几乎没有可视化 UI 编辑器</td></tr>
</table>
<h2>2. 代码风格对比</h2>
<h3>iOS：读一个按钮状态</h3>
<pre><code>// Swift — 按钮回调
button.addAction(UIAction { _ in
    ledImageView.isHighlighted.toggle()
}, for: .touchUpInside)</code></pre>
<h3>嵌入式：读一个按钮状态</h3>
<pre><code>// C — 轮询 GPIO
while (1) {
    if (HAL_GPIO_ReadPin(BTN_PORT, BTN_PIN) == GPIO_PIN_RESET) {
        HAL_GPIO_TogglePin(LED_PORT, LED_PIN);
        HAL_Delay(200);  // 防抖
    }
}</code></pre>
<p>看出来了吗？<strong>逻辑一样，只是没有 UIKit 帮你封装，你要直接操作硬件寄存器（或通过 HAL 库）。</strong></p>
<h2>3. 开发流程对比</h2>
<table>
<tr><th>步骤</th><th>iOS</th><th>嵌入式</th></tr>
<tr><td>1. 写代码</td><td>Xcode</td><td>VS Code / STM32CubeIDE / Arduino IDE</td></tr>
<tr><td>2. 编译</td><td>⌘B</td><td>make / idf.py build</td></tr>
<tr><td>3. 部署</td><td>⌘R 装到手机</td><td>USB 烧录（ST-Link / CP2102）</td></tr>
<tr><td>4. 调试</td><td>断点 + LLDB</td><td>串口 printf + 示波器</td></tr>
<tr><td>5. 发布</td><td>App Store 审核</td><td>批量烧录到产品里</td></tr>
</table>
<h2>4. 你的 iOS 经验能直接用在哪？</h2>
<ol>
<li><strong>BLE 通信</strong>：CoreBluetooth 的 Central/Peripheral 概念和嵌入式 BLE 一模一样</li>
<li><strong>网络协议</strong>：HTTP/WebSocket/MQTT 在 ESP32 上也有对应库</li>
<li><strong>架构设计</strong>：MVVM、状态机、模块化在嵌入式项目同样适用</li>
<li><strong>产品思维</strong>：硬件只是后端，App 才是用户看到的——你比纯硬件工程师更懂用户</li>
</ol>
<div class="tip-box">💡 推荐路线：<strong>ESP32 + BLE → iOS App 控制</strong>，第一周内就能做出"用手机开关灯"的完整 Demo，成就感拉满。</div>
""",
},
"基础/03-C语言速成.html": {
    "title": "基础 03：C 语言速成（iOS 开发者版）",
    "tag": "基础模块",
    "module": "基础",
    "body": """
<blockquote><p>学习目标：有 Swift/ObjC 基础的你，2 小时掌握嵌入式 C 的核心语法。</p></blockquote>
<h2>1. 为什么嵌入式用 C 不用 Swift？</h2>
<ul>
<li>Swift 运行时太大（几 MB），MCU 只有 64KB–512KB RAM</li>
<li>C 编译后直接操作寄存器，零开销</li>
<li>所有芯片厂商 SDK 都是 C/C++</li>
</ul>
<h2>2. Swift → C 语法对照</h2>
<table>
<tr><th>Swift</th><th>C</th></tr>
<tr><td><code>var count = 0</code></td><td><code>int count = 0;</code></td></tr>
<tr><td><code>let pi = 3.14</code></td><td><code>const float pi = 3.14f;</code></td></tr>
<tr><td><code>func add(a: Int, b: Int) -> Int</code></td><td><code>int add(int a, int b)</code></td></tr>
<tr><td><code>if count > 0 { }</code></td><td><code>if (count > 0) { }</code></td></tr>
<tr><td><code>for i in 0..&lt;10</code></td><td><code>for (int i = 0; i &lt; 10; i++)</code></td></tr>
<tr><td><code>struct Point { var x, y: Int }</code></td><td><code>typedef struct { int x, y; } Point;</code></td></tr>
<tr><td><code>enum State { case on, off }</code></td><td><code>typedef enum { STATE_ON, STATE_OFF } State;</code></td></tr>
<tr><td><code>[Int]</code> 数组</td><td><code>int arr[10];</code> 固定长度</td></tr>
<tr><td><code>String</code></td><td><code>char str[] = "hello";</code></td></tr>
<tr><td><code>nil</code></td><td><code>NULL</code></td></tr>
<tr><td><code>guard let</code></td><td><code>if (ptr == NULL) return;</code></td></tr>
</table>
<h2>3. 嵌入式必知：指针（Swift 里隐藏了，C 里躲不掉）</h2>
<pre><code>// 指针 = 内存地址，类似 Swift 的 UnsafePointer
int temperature = 25;
int *ptr = &temperature;  // ptr 存的是 temperature 的地址
*ptr = 30;                // 通过指针修改值 → temperature 变成 30

// 数组名就是指针
int data[5] = {1, 2, 3, 4, 5};
int *p = data;            // p 指向第一个元素
printf("%d", *(p + 2));   // 输出 3（类似 data[2]）</code></pre>
<div class="tip-box">💡 记忆口诀：看到 <code>*</code> 是"取值"，看到 <code>&amp;</code> 是"取地址"。</div>
<h2>4. 位操作（嵌入式天天用）</h2>
<pre><code>// 设置 GPIO 第 5 位为高电平
GPIOA->ODR |= (1 &lt;&lt; 5);    // 置 1
GPIOA->ODR &amp;= ~(1 &lt;&lt; 5);   // 置 0
GPIOA->ODR ^= (1 &lt;&lt; 5);    // 翻转

// 读取第 3 位
if (GPIOA->IDR &amp; (1 &lt;&lt; 3)) { /* 高电平 */ }</code></pre>
<h2>5. 头文件与模块化（类似 Swift import）</h2>
<pre><code>// led.h — 声明
#ifndef LED_H
#define LED_H
void led_init(void);
void led_on(void);
void led_off(void);
#endif

// led.c — 实现
#include "led.h"
void led_init(void) { /* 配置 GPIO */ }
void led_on(void)    { HAL_GPIO_WritePin(LED_PORT, LED_PIN, GPIO_PIN_SET); }</code></pre>
<h2>6. 常见坑（iOS 开发者特别容易踩）</h2>
<ol>
<li><strong>忘记分号</strong>：C 每行末尾必须 <code>;</code></li>
<li><strong>数组越界</strong>：没有 Swift 的 bounds check，越界 = 程序崩溃或硬件乱动</li>
<li><strong>栈溢出</strong>：MCU 栈只有 1–4KB，大数组放全局或堆</li>
<li><strong>未初始化变量</strong>：不像 Swift 强制初始化，C 里可能是随机值</li>
</ol>
""",
},
"基础/04-GPIO与点亮LED.html": {
    "title": "基础 04：GPIO 与点亮 LED（第一个程序）",
    "tag": "基础模块",
    "module": "基础",
    "body": """
<blockquote><p>学习目标：理解 GPIO，写出嵌入式界的 "Hello World"——点亮 LED。</p></blockquote>
<h2>1. GPIO 是什么？</h2>
<p><strong>GPIO = General Purpose Input/Output（通用输入输出引脚）</strong></p>
<p>芯片引出来的"手"，可以：<strong>输出</strong>（控制灯/继电器）或 <strong>输入</strong>（读按钮/传感器）。</p>
<p>类比 iOS：<code>GPIO 输出</code> = 你设置 <code>view.backgroundColor</code>；<code>GPIO 输入</code> = 你读 <code>button.isSelected</code>。</p>
<h2>2. 电路基础（超简版）</h2>
<pre><code>         VCC (3.3V)
          │
         [R]  限流电阻 220Ω–1kΩ
          │
         LED →  发光二极管（长脚正极）
          │
         GPIO 引脚（输出高电平 = 亮）
          │
         GND（地）</code></pre>
<p><strong>记住</strong>：LED 有方向，反接不亮；必须加限流电阻，否则烧 LED 或烧 GPIO。</p>
<h2>3. ESP32 点亮 LED（Arduino 框架，最简单）</h2>
<pre><code>const int LED_PIN = 2;  // ESP32 开发板自带 LED 在 GPIO2

void setup() {
    pinMode(LED_PIN, OUTPUT);  // 设为输出模式
}

void loop() {
    digitalWrite(LED_PIN, HIGH);  // 亮
    delay(1000);
    digitalWrite(LED_PIN, LOW);   // 灭
    delay(1000);
}</code></pre>
<h2>4. STM32 点亮 LED（HAL 库，工业标准）</h2>
<pre><code>// main.c
int main(void) {
    HAL_Init();
    SystemClock_Config();
    MX_GPIO_Init();  // CubeMX 自动生成

    while (1) {
        HAL_GPIO_TogglePin(GPIOC, GPIO_PIN_13);
        HAL_Delay(500);
    }
}</code></pre>
<h2>5. GPIO 的 4 种模式</h2>
<table>
<tr><th>模式</th><th>用途</th><th>类比 iOS</th></tr>
<tr><td>输出 Push-Pull</td><td>驱动 LED、继电器</td><td>设置 UI 属性</td></tr>
<tr><td>输入 Floating</td><td>读按键（需外部上下拉）</td><td>读控件状态</td></tr>
<tr><td>输入 Pull-Up</td><td>按键默认高，按下低</td><td>默认 true，触发 false</td></tr>
<tr><td>输入 Pull-Down</td><td>按键默认低，按下高</td><td>默认 false，触发 true</td></tr>
</table>
<h2>6. 动手清单</h2>
<ol>
<li>买 ESP32 开发板（约 25 元）</li>
<li>安装 Arduino IDE，选 ESP32 板型</li>
<li>上传 Blink 例程，看到 LED 闪烁 ✅</li>
<li>外接一个 LED + 电阻到 GPIO，验证控制</li>
</ol>
""",
},
"基础/05-中断与定时器.html": {
    "title": "基础 05：中断与定时器",
    "tag": "基础模块",
    "module": "基础",
    "body": """
<blockquote><p>学习目标：理解中断机制——嵌入式最重要的概念之一。</p></blockquote>
<h2>1. 中断是什么？</h2>
<p><strong>中断 = 硬件强行打断当前程序，优先处理紧急事件。</strong></p>
<p>类比 iOS：</p>
<ul>
<li>你在刷抖音（主循环）→ 来电了（中断）→ 暂停抖音接电话 → 挂掉继续刷</li>
<li><code>NotificationCenter</code> 就是软件版"中断"</li>
</ul>
<h2>2. 为什么需要中断？</h2>
<table>
<tr><th>方式</th><th>做法</th><th>问题</th></tr>
<tr><td>轮询 Polling</td><td><code>while(1) { if(按键) ... }</code></td><td>CPU 空转浪费电，可能漏检</td></tr>
<tr><td>中断 Interrupt</td><td>按键按下 → 硬件自动跳转</td><td>CPU 休眠，事件来了才醒</td></tr>
</table>
<h2>3. 按键中断示例（STM32 HAL）</h2>
<pre><code>// 初始化时使能 EXTI 中断
void HAL_GPIO_EXTI_Callback(uint16_t GPIO_Pin) {
    if (GPIO_Pin == BTN_Pin) {
        HAL_GPIO_TogglePin(LED_GPIO_Port, LED_Pin);
    }
}</code></pre>
<h2>4. 定时器（Timer）</h2>
<p>硬件定时器 = 精确闹钟，不占用 CPU：</p>
<pre><code>// 每 1ms 触发一次中断（用于系统 tick）
void HAL_TIM_PeriodElapsedCallback(TIM_HandleTypeDef *htim) {
    if (htim->Instance == TIM2) {
        system_tick_ms++;  // 全局毫秒计数
    }
}</code></pre>
<p>常见用途：</p>
<ul>
<li><strong>系统时钟</strong>：FreeRTOS 调度依赖 1ms tick</li>
<li><strong>PWM 调光</strong>：LED 亮度、电机调速</li>
<li><strong>超时检测</strong>：通信协议的超时重传</li>
<li><strong>采样定时</strong>：每 100ms 读一次传感器</li>
</ul>
<h2>5. PWM：让 LED"呼吸"（类比 iOS 动画）</h2>
<pre><code>// Arduino — LED 呼吸效果
int brightness = 0;
int delta = 5;
void loop() {
    analogWrite(LED_PIN, brightness);
    brightness += delta;
    if (brightness &lt;= 0 || brightness &gt;= 255) delta = -delta;
    delay(30);
}</code></pre>
<p><code>analogWrite</code> 本质是 PWM：快速开关 GPIO，利用人眼视觉暂留模拟"亮度变化"。</p>
""",
},
"基础/06-串口UART通信.html": {
    "title": "基础 06：串口 UART 通信",
    "tag": "基础模块",
    "module": "基础",
    "body": """
<blockquote><p>学习目标：掌握嵌入式调试的"生命线"——串口通信。</p></blockquote>
<h2>1. UART 是什么？</h2>
<p><strong>UART = 两根线（TX/RX）传数据，最简单最古老的通信方式。</strong></p>
<p>类比 iOS：UART 就像两个设备之间的"对讲机"，没有 Wi-Fi 那么复杂，但可靠直接。</p>
<h2>2. 接线（记住 TX 接 RX，RX 接 TX）</h2>
<pre><code>ESP32          USB-TTL 模块         Mac/PC
 GPIO17 (TX) ──→ RX
 GPIO16 (RX) ←── TX
 GND         ──→ GND</code></pre>
<h2>3. 第一个串口程序</h2>
<pre><code>void setup() {
    Serial.begin(115200);  // 波特率 115200
    Serial.println("Hello from ESP32!");
}

void loop() {
    float temp = readTemperature();
    Serial.printf("温度: %.1f°C\\n", temp);
    delay(1000);
}</code></pre>
<h2>4. Mac 上看串口输出</h2>
<ol>
<li>安装 CP2102/CH340 驱动</li>
<li>Arduino IDE → 工具 → 串口监视器</li>
<li>或用命令行：<code>screen /dev/cu.usbserial-xxx 115200</code></li>
</ol>
<h2>5. 串口在开发中的角色</h2>
<table>
<tr><th>用途</th><th>说明</th></tr>
<tr><td><strong>调试打印</strong></td><td><code>printf</code> 是嵌入式唯一的" NSLog"</td></tr>
<tr><td><strong>接收命令</strong></td><td>PC 发指令控制设备</td></tr>
<tr><td><strong>模块通信</strong></td><td>和 GPS、蓝牙、4G 模块对话</td></tr>
<tr><td><strong>固件升级</strong></td><td>UART Bootloader 烧录</td></tr>
</table>
<div class="tip-box">💡 波特率常用值：9600（老设备）、115200（最常用）、921600（高速调试）</div>
""",
},
"基础/07-I2C与SPI协议.html": {
    "title": "基础 07：I2C 与 SPI 协议",
    "tag": "基础模块",
    "module": "基础",
    "body": """
<blockquote><p>学习目标：搞懂两种最常用的"芯片间对话"协议。</p></blockquote>
<h2>1. 为什么需要协议？</h2>
<p>一个 MCU 要同时连屏幕、传感器、存储器——各用各的线太乱。I2C 和 SPI 就是<strong>标准化的接线+说话规则</strong>。</p>
<h2>2. I2C：两线走天下</h2>
<pre><code>     MCU                    传感器A    传感器B
  SDA ─┬──────────────────────┬──────────
  SCL ─┴──────────────────────┴──────────
       (只需要 2 根线，可挂 127 个设备)</code></pre>
<table>
<tr><th>特点</th><th>说明</th></tr>
<tr><td>线数</td><td>2 根（SDA 数据 + SCL 时钟）</td></tr>
<tr><td>速度</td><td>100K / 400K / 1M</td></tr>
<tr><td>优点</td><td>省引脚，多设备</td></tr>
<tr><td>缺点</td><td>速度较慢</td></tr>
<tr><td>常见设备</td><td>OLED 屏、温湿度 SHT30、加速度计 MPU6050、EEPROM</td></tr>
</table>
<h3>代码示例：读 I2C 温湿度</h3>
<pre><code>#include &lt;Wire.h&gt;
#include &lt;Adafruit_SHT31.h&gt;
Adafruit_SHT31 sht31 = Adafruit_SHT31();

void setup() {
    sht31.begin(0x44);  // I2C 地址 0x44
}
void loop() {
    float t = sht31.readTemperature();
    float h = sht31.readHumidity();
    Serial.printf("T=%.1f H=%.1f\\n", t, h);
    delay(2000);
}</code></pre>
<h2>3. SPI：速度之王</h2>
<table>
<tr><th>特点</th><th>说明</th></tr>
<tr><td>线数</td><td>4 根（MOSI + MISO + SCK + CS）</td></tr>
<tr><td>速度</td><td>可达 80MHz</td></tr>
<tr><td>优点</td><td>快！适合屏幕、Flash</td></tr>
<tr><td>缺点</td><td>线多，每个设备要一根 CS</td></tr>
<tr><td>常见设备</td><td>TFT 彩屏、SD 卡、W25Q Flash、LoRa 模块</td></tr>
</table>
<h2>4. 怎么选？</h2>
<table>
<tr><th>场景</th><th>推荐</th></tr>
<tr><td>多个传感器</td><td>I2C</td></tr>
<tr><td>屏幕/Flash/高速</td><td>SPI</td></tr>
<tr><td>和 PC/模块通信</td><td>UART</td></tr>
<tr><td>和手机通信</td><td>BLE</td></tr>
<tr><td>远程/云端</td><td>Wi-Fi + MQTT</td></tr>
</table>
""",
},
"基础/08-芯片选型指南.html": {
    "title": "基础 08：芯片选型指南",
    "tag": "基础模块",
    "module": "基础",
    "body": """
<blockquote><p>学习目标：知道什么项目用什么芯片，不花冤枉钱。</p></blockquote>
<h2>1. 主流平台对比</h2>
<table>
<tr><th>平台</th><th>特点</th><th>适合</th><th>价格</th><th>难度</th></tr>
<tr><td><strong>Arduino UNO</strong></td><td>8 位 AVR，资料最多</td><td>纯入门体验</td><td>¥30</td><td>⭐</td></tr>
<tr><td><strong>ESP32</strong></td><td>双核 + Wi-Fi + BLE</td><td>IoT、智能家居</td><td>¥25</td><td>⭐⭐</td></tr>
<tr><td><strong>ESP8266</strong></td><td>Wi-Fi only，超便宜</td><td>简单联网项目</td><td>¥10</td><td>⭐⭐</td></tr>
<tr><td><strong>STM32F103</strong></td><td>ARM Cortex-M3，工业级</td><td>工控、电机控制</td><td>¥15</td><td>⭐⭐⭐</td></tr>
<tr><td><strong>STM32H7</strong></td><td>480MHz，带 FPU</td><td>高性能、音频</td><td>¥80</td><td>⭐⭐⭐⭐</td></tr>
<tr><td><strong>Raspberry Pi Pico</strong></td><td>RP2040 双核</td><td>教育、MicroPython</td><td>¥30</td><td>⭐⭐</td></tr>
<tr><td><strong>nRF52840</strong></td><td>BLE 5.0 低功耗之王</td><td>可穿戴、Beacon</td><td>¥60</td><td>⭐⭐⭐</td></tr>
</table>
<h2>2. iOS 开发者推荐路线</h2>
<div class="tip-box">
<strong>第一步：ESP32（Arduino 框架）</strong> → 快速出成果，Wi-Fi + BLE 都有<br>
<strong>第二步：ESP32（ESP-IDF）</strong> → 专业 FreeRTOS 开发<br>
<strong>第三步：STM32</strong> → 工业级，求职必备<br>
<strong>全程：iOS App 做控制端</strong> → 你的核心竞争力
</div>
<h2>3. 选型决策树</h2>
<pre><code>需要联网吗？
├─ 是 → 需要 BLE 吗？
│       ├─ 是 → ESP32 ✅（最推荐）
│       └─ 否 → ESP8266（省钱）
└─ 否 → 需要高性能吗？
        ├─ 是 → STM32H7 / RP2040
        └─ 否 → STM32F103 / Arduino</code></pre>
<h2>4. 开发板购买建议（2026）</h2>
<table>
<tr><th>板子</th><th>推荐型号</th><th>参考价</th></tr>
<tr><td>ESP32</td><td>ESP32-DevKitC-32E</td><td>¥25</td></tr>
<tr><td>STM32</td><td>STM32F103C8T6 最小系统板</td><td>¥12</td></tr>
<tr><td>传感器套件</td><td>37-in-1 传感器套件</td><td>¥45</td></tr>
<tr><td>USB-TTL</td><td>CP2102 模块</td><td>¥8</td></tr>
<tr><td>杜邦线+面包板</td><td>套装</td><td>¥15</td></tr>
</table>
<p><strong>入门总预算：约 ¥100–150</strong></p>
""",
},
}

# Add remaining pages with shorter but quality content
EXTRA = {
"硬件/01-开发板与工具.html": ("硬件 01：开发板与工具", "硬件入门", """
<h2>1. 必备工具清单</h2>
<table>
<tr><th>工具</th><th>用途</th><th>必须？</th></tr>
<tr><td>ESP32 开发板</td><td>主控</td><td>✅</td></tr>
<tr><td>USB 数据线（Micro-USB / Type-C）</td><td>供电+烧录</td><td>✅</td></tr>
<tr><td>面包板 + 杜邦线</td><td>免焊接实验</td><td>✅</td></tr>
<tr><td>LED + 电阻(220Ω) + 按键</td><td>基础实验</td><td>✅</td></tr>
<tr><td>万用表</td><td>测电压/通断</td><td>✅</td></tr>
<tr><td>电烙铁</td><td>焊接</td><td>进阶</td></tr>
<tr><td>示波器</td><td>看波形</td><td>进阶</td></tr>
<tr><td>逻辑分析仪</td><td>分析 I2C/SPI 时序</td><td>可选</td></tr>
</table>
<h2>2. 软件工具</h2>
<table>
<tr><th>软件</th><th>平台</th><th>用途</th></tr>
<tr><td>Arduino IDE 2.x</td><td>Mac/Win</td><td>ESP32/Arduino 快速开发</td></tr>
<tr><td>VS Code + PlatformIO</td><td>Mac/Win</td><td>专业嵌入式 IDE（推荐）</td></tr>
<tr><td>STM32CubeIDE</td><td>Mac/Win</td><td>ST 官方 STM32 开发</td></tr>
<tr><td>ESP-IDF</td><td>Mac/Win/Linux</td><td>ESP32 原生 SDK</td></tr>
<tr><td>Serial Studio</td><td>Mac/Win</td><td>串口数据可视化</td></tr>
</table>
<h2>3. Mac 开发环境搭建</h2>
<pre><code># 安装 Arduino IDE
brew install --cask arduino-ide

# 或 PlatformIO（VS Code 插件）
brew install --cask visual-studio-code
# VS Code 里搜索安装 PlatformIO IDE 插件</code></pre>
"""),
"硬件/02-万用表与焊接入门.html": ("硬件 02：万用表与焊接入门", "硬件入门", """
<h2>1. 万用表三件套</h2>
<ol>
<li><strong>测电压</strong>：确认 3.3V / 5V 供电是否正常（别把 5V 接到 3.3V 芯片上！）</li>
<li><strong>测通断</strong>：检查焊接/连线是否连通（蜂鸣档）</li>
<li><strong>测电阻</strong>：确认电阻值是否正确</li>
</ol>
<h2>2. 安全红线</h2>
<ul>
<li>⚠️ 不要带电焊接</li>
<li>⚠️ 不要短路 VCC 和 GND（会冒烟）</li>
<li>⚠️ ESP32 GPIO 只能承受 3.3V，5V 会烧</li>
<li>⚠️ 人体静电可能击穿芯片，摸板前先放电</li>
</ul>
<h2>3. 焊接入门（5 步）</h2>
<ol>
<li>电烙铁加热到 320°C</li>
<li>焊盘和引脚同时加热 2 秒</li>
<li>送锡丝（量：刚好覆盖焊盘）</li>
<li>移锡 → 停 1 秒 → 移烙铁</li>
<li>检查：焊点应光滑饱满，像"圆锥形"</li>
</ol>
"""),
"硬件/03-原理图阅读入门.html": ("硬件 03：原理图阅读入门", "硬件入门", """
<h2>1. 为什么要看原理图？</h2>
<p>做 iOS 要看 API 文档，做硬件要看原理图。它告诉你每个引脚连了什么、电源怎么走的。</p>
<h2>2. 常见符号</h2>
<table>
<tr><th>符号</th><th>含义</th></tr>
<tr><td>—▷|—</td><td>二极管/LED（箭头方向是电流方向）</td></tr>
<tr><td>—/\/\/\—</td><td>电阻</td></tr>
<tr><td>—||—</td><td>电容</td></tr>
<tr><td>VCC / 3V3</td><td>电源正极</td></tr>
<tr><td>GND ⏚</td><td>地（零电位参考）</td></tr>
</table>
<h2>3. 阅读顺序</h2>
<ol>
<li>找 <strong>MCU 芯片</strong>（中心位置，引脚最多）</li>
<li>看 <strong>电源部分</strong>（VCC → 稳压 → 3.3V）</li>
<li>看 <strong>MCU 引脚连了什么</strong>（LED→PC13, 按键→PA0…）</li>
<li>看 <strong>通信接口</strong>（I2C 传感器、SPI 屏幕）</li>
</ol>
<div class="tip-box">💡 推荐工具：立创 EDA（免费在线画/看原理图）、LCSC 商城（买元件）</div>
"""),
"进阶/01-FreeRTOS入门.html": ("进阶 01：FreeRTOS 入门", "进阶", """
<h2>1. 为什么需要 RTOS？</h2>
<p>当项目变复杂（同时读传感器 + 控电机 + 发 Wi-Fi），一个 <code>while(1)</code> 不够用。FreeRTOS 让你创建多个"任务"并行运行。</p>
<p>类比 iOS：<strong>FreeRTOS 任务 ≈ DispatchQueue / Thread</strong></p>
<h2>2. 核心概念</h2>
<table>
<tr><th>FreeRTOS</th><th>iOS 对应</th></tr>
<tr><td>Task 任务</td><td>DispatchQueue / Thread</td></tr>
<tr><td>Queue 队列</td><td>DispatchQueue (serial)</td></tr>
<tr><td>Semaphore 信号量</td><td>DispatchSemaphore</td></tr>
<tr><td>Mutex 互斥锁</td><td>NSLock / os_unfair_lock</td></tr>
<tr><td>Timer 软件定时器</td><td>Timer / DispatchSourceTimer</td></tr>
</table>
<h2>3. 创建两个任务</h2>
<pre><code>void sensor_task(void *pv) {
    while (1) {
        float t = read_temp();
        xQueueSend(data_queue, &t, 0);
        vTaskDelay(pdMS_TO_TICKS(1000));
    }
}
void wifi_task(void *pv) {
    float t;
    while (1) {
        if (xQueueReceive(data_queue, &t, portMAX_DELAY))
            mqtt_publish("temp", t);
    }
}
// 启动
xTaskCreate(sensor_task, "sensor", 2048, NULL, 1, NULL);
xTaskCreate(wifi_task, "wifi", 4096, NULL, 1, NULL);
vTaskStartScheduler();</code></pre>
"""),
"进阶/02-低功耗设计.html": ("进阶 02：低功耗设计", "进阶", """
<h2>1. 为什么低功耗重要？</h2>
<p>智能门锁、传感器节点靠电池跑 1–3 年。iPhone 一天一充是因为 A 芯片算力太强；MCU 的优势就是<strong>极致省电</strong>。</p>
<h2>2. 功耗模式</h2>
<table>
<tr><th>模式</th><th>电流</th><th>唤醒</th></tr>
<tr><td>运行 Run</td><td>~80mA</td><td>—</td></tr>
<tr><td>睡眠 Sleep</td><td>~10mA</td><td>任意中断</td></tr>
<tr><td>Stop 停止</td><td>~20μA</td><td>外部中断</td></tr>
<tr><td>Standby 待机</td><td>~2μA</td><td>复位/WKUP</td></tr>
</table>
<h2>3. 省电技巧</h2>
<ol>
<li>不用的外设关掉时钟</li>
<li>用中断代替轮询</li>
<li>Wi-Fi 用完后断开</li>
<li>降低 CPU 频率（80MHz 够用就不跑 240MHz）</li>
<li>Deep Sleep + 定时唤醒（每 5 分钟读一次传感器）</li>
</ol>
"""),
"进阶/03-WiFi与MQTT.html": ("进阶 03：WiFi 与 MQTT", "进阶", """
<h2>1. ESP32 连 Wi-Fi</h2>
<pre><code>#include &lt;WiFi.h&gt;
const char* ssid = "你的WiFi";
const char* pass = "密码";
void setup() {
    WiFi.begin(ssid, pass);
    while (WiFi.status() != WL_CONNECTED) delay(500);
    Serial.println("WiFi 已连接");
}</code></pre>
<h2>2. MQTT：IoT 的"微信"</h2>
<p>设备通过 MQTT 协议和云端"订阅/发布"消息，轻量、省电、适合 IoT。</p>
<pre><code>// 发布温度到云端
client.publish("home/bedroom/temp", "25.6");

// iOS App 也订阅同一个 topic → 实时显示</code></pre>
<h2>3. 完整链路</h2>
<pre><code>ESP32 传感器 → MQTT Broker(云端) → iOS App 显示
                    ↑
              也可以 ← iOS App 发指令 → ESP32 执行</code></pre>
<div class="tip-box">💡 免费 MQTT Broker：EMQX Cloud、HiveMQ、或自建 Mosquitto</div>
"""),
"进阶/04-蓝牙BLE通信.html": ("进阶 04：蓝牙 BLE 通信", "进阶", """
<h2>1. BLE 是什么？</h2>
<p><strong>BLE = Bluetooth Low Energy</strong>，低功耗蓝牙。Apple 从 iPhone 4S 起全面支持，你的 CoreBluetooth 经验直接能用！</p>
<h2>2. BLE 核心概念（和 CoreBluetooth 一一对应）</h2>
<table>
<tr><th>BLE 概念</th><th>CoreBluetooth</th></tr>
<tr><td>Peripheral 外设</td><td><code>CBPeripheral</code></td></tr>
<tr><td>Central 中心</td><td><code>CBCentralManager</code></td></tr>
<tr><td>Service 服务</td><td><code>CBService</code></td></tr>
<tr><td>Characteristic 特征</td><td><code>CBCharacteristic</code></td></tr>
<tr><td>Notify 通知</td><td><code>didUpdateValueFor</code></td></tr>
<tr><td>Write 写入</td><td><code>writeValue</code></td></tr>
</table>
<h2>3. ESP32 BLE 从机示例</h2>
<pre><code>#include &lt;BLEDevice.h&gt;
BLECharacteristic *pChar;

void setup() {
    BLEDevice::init("MyLight");
    BLEServer *server = BLEDevice::createServer();
    BLEService *svc = server->createService("FFE0");
    pChar = svc->createCharacteristic("FFE1",
        BLECharacteristic::PROPERTY_READ |
        BLECharacteristic::PROPERTY_WRITE);
    svc->start();
    BLEDevice::startAdvertising();
}</code></pre>
<p>iOS 端用 CoreBluetooth 扫描 "MyLight" → 连接 → 写 FFE1 特征值 → 灯亮。完整代码见 <a href="../iOS联动/01-BLE与CoreBluetooth.html">iOS 联动章节</a>。</p>
"""),
"实战/01-智能灯控.html": ("实战 01：智能灯控（ESP32 + iOS）", "实战项目", """
<h2>项目目标</h2>
<p>用 iPhone 通过 BLE 或 Wi-Fi 控制 ESP32 上的 LED 灯，实现开关和亮度调节。</p>
<h2>硬件清单</h2>
<ul><li>ESP32 开发板 ×1</li><li>LED ×1 + 220Ω 电阻</li><li>可选：MOSFET + 12V 灯带（做真灯）</li></ul>
<h2>架构</h2>
<pre><code>iOS App (CoreBluetooth)
    ↕ BLE
ESP32 (BLE Server)
    → GPIO PWM → LED 亮度</code></pre>
<h2>ESP32 端关键代码</h2>
<pre><code>class LedCallbacks : public BLECharacteristicCallbacks {
    void onWrite(BLECharacteristic *p) {
        std::string val = p->getValue();
        int brightness = val[0];  // 0-255
        analogWrite(LED_PIN, brightness);
    }
};</code></pre>
<h2>验收标准</h2>
<ol><li>✅ iPhone 扫描到 "SmartLight" 设备</li><li>✅ App 滑动条控制 LED 亮度 0–100%</li><li>✅ 断连后 ESP32 保持最后状态</li></ol>
"""),
"实战/02-温湿度监测.html": ("实战 02：温湿度监测站", "实战项目", """
<h2>项目目标</h2>
<p>ESP32 读取 DHT22 温湿度 → MQTT 上报云端 → iOS App 实时显示 + 历史曲线。</p>
<h2>硬件</h2>
<ul><li>ESP32 ×1</li><li>DHT22 或 SHT30 传感器 ×1</li></ul>
<h2>数据流</h2>
<pre><code>DHT22 → ESP32 → MQTT("home/temp") → 云端
                                      ↓
                              iOS App 订阅显示</code></pre>
<h2>扩展功能</h2>
<ul>
<li>温度超过 30°C → 推送通知（APNs）</li>
<li>数据存 InfluxDB → 历史曲线</li>
<li>多房间多传感器</li>
</ul>
"""),
"实战/03-蓝牙控制小车.html": ("实战 03：蓝牙控制小车", "实战项目", """
<h2>项目目标</h2>
<p>iPhone 虚拟摇杆 → BLE → ESP32 → 电机驱动 → 小车前进/后退/转向。</p>
<h2>硬件</h2>
<ul><li>ESP32 ×1</li><li>L298N 电机驱动模块 ×1</li><li>TT 马达 + 轮子 ×2</li><li>18650 电池</li></ul>
<h2>核心逻辑</h2>
<pre><code>// iOS 发送: "F"=前进 "B"=后退 "L"=左转 "R"=右转 "S"=停止
void onBLEWrite(char cmd) {
    switch(cmd) {
        case 'F': motor_L(200); motor_R(200); break;
        case 'B': motor_L(-200); motor_R(-200); break;
        case 'L': motor_L(-150); motor_R(150); break;
        case 'R': motor_L(150); motor_R(-150); break;
        case 'S': motor_L(0); motor_R(0); break;
    }
}</code></pre>
<p>这个项目做完，你就有了完整的 <strong>App + 嵌入式 + 硬件</strong> 作品集。</p>
"""),
"iOS联动/01-BLE与CoreBluetooth.html": ("iOS 01：BLE 与 CoreBluetooth", "iOS 联动", """
<h2>1. 你的主场：CoreBluetooth</h2>
<p>作为 iOS 开发者，BLE 是你连接硬件的最自然方式。不需要 Wi-Fi，不需要配对，低功耗。</p>
<h2>2. iOS 端完整示例</h2>
<pre><code>import CoreBluetooth

class BLEManager: NSObject, CBCentralManagerDelegate, CBPeripheralDelegate {
    var central: CBCentralManager!
    var peripheral: CBPeripheral?
    let serviceUUID = CBUUID(string: "FFE0")
    let charUUID    = CBUUID(string: "FFE1")

    func start() {
        central = CBCentralManager(delegate: self, queue: nil)
    }

    func centralManagerDidUpdateState(_ central: CBCentralManager) {
        if central.state == .poweredOn {
            central.scanForPeripherals(withServices: [serviceUUID])
        }
    }

    func centralManager(_ central: CBCentralManager,
                        didDiscover p: CBPeripheral, ...) {
        self.peripheral = p
        central.connect(p)
    }

    func peripheral(_ peripheral: CBPeripheral,
                    didDiscoverCharacteristicsFor service: CBService, ...) {
        if let char = service.characteristics?.first(where: {
            $0.uuid == charUUID
        }) {
            peripheral.setNotifyValue(true, for: char)
        }
    }

    func sendCommand(_ byte: UInt8) {
        guard let char = /* find char */ else { return }
        peripheral?.writeValue(Data([byte]), for: char, type: .withResponse)
    }
}</code></pre>
<h2>3. 注意事项</h2>
<ul>
<li><code>Info.plist</code> 加 <code>NSBluetoothAlwaysUsageDescription</code></li>
<li>后台 BLE 需要 <code>bluetooth-central</code> Background Mode</li>
<li>真机调试，模拟器不支持 BLE</li>
</ul>
"""),
"iOS联动/02-iOS控制硬件全链路.html": ("iOS 02：控制硬件全链路", "iOS 联动", """
<h2>1. 完整产品架构</h2>
<pre><code>┌─────────────┐    BLE/MQTT    ┌──────────────┐
│  iOS App    │ ←──────────→  │  ESP32/STM32  │
│  (SwiftUI)  │               │  (C/FreeRTOS) │
└──────┬──────┘               └──────┬───────┘
       │                             │
       ↕ HTTPS                  传感器/执行器
┌─────────────┐               (DHT22/LED/电机)
│  云端 API   │
│  (可选)     │
└─────────────┘</code></pre>
<h2>2. 通信方案选择</h2>
<table>
<tr><th>场景</th><th>方案</th><th>理由</th></tr>
<tr><td>近距离控制（灯/锁）</td><td>BLE</td><td>低延迟、省电、iOS 原生支持</td></tr>
<tr><td>远程控制（不在家）</td><td>Wi-Fi + MQTT</td><td>穿透局域网</td></tr>
<tr><td>大数据传输（固件升级）</td><td>Wi-Fi + HTTP</td><td>带宽大</td></tr>
<tr><td>户外远距</td><td>4G/NB-IoT 模块</td><td>无 Wi-Fi 场景</td></tr>
</table>
<h2>3. 你的差异化优势</h2>
<p>纯嵌入式工程师不懂 UI/UX，纯 iOS 工程师不懂硬件。你能做<strong>完整的 IoT 产品</strong>：</p>
<ul>
<li>硬件端：ESP32 采集 + 控制</li>
<li>App 端：SwiftUI 精美界面</li>
<li>云端：可选 AI 分析（你的大模型经验）</li>
</ul>
"""),
"应用场景/01-行业应用全景.html": ("应用 01：行业应用全景", "应用场景", """
<h2>1. 消费电子</h2>
<p>智能家居（灯/锁/插座）、可穿戴、小家电。量大，入门首选。</p>
<h2>2. 工业控制</h2>
<p>PLC、电机驱动、流水线自动化。稳定高薪，STM32/PLC 为主。</p>
<h2>3. 汽车电子</h2>
<p>ECU、BMS 电池管理、仪表盘。车规级，薪资最高（20K–40K）。</p>
<h2>4. 医疗仪器</h2>
<p>血压计、血糖仪、便携诊断。合规要求高，项目利润好。</p>
<h2>5. 农业 IoT</h2>
<p>土壤监测、自动灌溉、温室控制。政府补贴多，外包需求大。</p>
<h2>6. 新能源</h2>
<p>光伏逆变器、储能 BMS、充电桩。2024–2026 最热门方向。</p>
<h2>7. 机器人/无人机</h2>
<p>飞控、舵机控制、SLAM 导航。技术门槛高，但有趣。</p>
<div class="tip-box">💡 对你最现实的切入点：<strong>消费电子 IoT + iOS App</strong>，投入小、周期短、能出作品集。</div>
"""),
"应用场景/02-如何接单赚钱.html": ("应用 02：如何接单赚钱", "应用场景", """
<h2>1. 接单渠道</h2>
<table>
<tr><th>渠道</th><th>项目类型</th><th>单价</th></tr>
<tr><td>淘宝/闲鱼</td><td>小项目（灯控/采集）</td><td>¥500–5000</td></tr>
<tr><td>猪八戒/程序员客栈</td><td>中等项目</td><td>¥5000–30000</td></tr>
<tr><td>行业人脉/老客户</td><td>工业/农业 IoT</td><td>¥2万–20万</td></tr>
<tr><td>自己的产品</td><td>智能硬件创业</td><td>无限可能</td></tr>
</table>
<h2>2. 适合 iOS 开发者的项目类型</h2>
<ol>
<li><strong>App + 硬件套装</strong>：卖"ESP32 开发板 + iOS 控制 App"教程/套件</li>
<li><strong>智能农业监测</strong>：温湿度 + App + 报警，政府项目多</li>
<li><strong>门禁/考勤</strong>：BLE Beacon + iOS 打卡</li>
<li><strong>宠物/老人监护</strong>：传感器 + App 推送</li>
</ol>
<h2>3. 报价参考（2026）</h2>
<table>
<tr><th>项目</th><th>工作量</th><th>报价</th></tr>
<tr><td>BLE 灯控 App + ESP32 固件</td><td>1–2 周</td><td>¥8000–15000</td></tr>
<tr><td>温湿度监测 + 云端 + App</td><td>2–3 周</td><td>¥15000–25000</td></tr>
<tr><td>工业采集 + 485 协议 + 后台</td><td>1–2 月</td><td>¥30000–80000</td></tr>
</table>
<h2>4. 从 0 到第一单</h2>
<ol>
<li>做完本教程 3 个实战项目 → 拍照/录视频</li>
<li>GitHub 开源 + 写技术博客</li>
<li>闲鱼挂"ESP32 定制开发"服务</li>
<li>第一个项目低价接，换好评和案例</li>
</ol>
"""),
"练习/01-入门采购清单.html": ("练习 01：入门采购清单", "练习", """
<h2>淘宝/拼多多搜索关键词</h2>
<table>
<tr><th>物品</th><th>搜索词</th><th>参考价</th></tr>
<tr><td>ESP32 开发板</td><td>ESP32-DevKitC</td><td>¥25</td></tr>
<tr><td>传感器套件</td><td>37合1传感器套件</td><td>¥45</td></tr>
<tr><td>面包板套装</td><td>面包板+杜邦线套装</td><td>¥15</td></tr>
<tr><td>USB-TTL</td><td>CP2102 USB转TTL</td><td>¥8</td></tr>
<tr><td>万用表</td><td>胜利VC890D</td><td>¥30</td></tr>
<tr><td>电烙铁</td><td>936 恒温电烙铁</td><td>¥35</td></tr>
<tr><td>DHT22 传感器</td><td>DHT22 AM2302</td><td>¥8</td></tr>
<tr><td>L298N 电机驱动</td><td>L298N 驱动模块</td><td>¥8</td></tr>
</table>
<p><strong>总计约 ¥170</strong>，一个周末就能全部到货。</p>
<h2>学习进度建议</h2>
<pre><code>第 1 周：Arduino IDE + ESP32 点灯 + 串口
第 2 周：I2C 传感器 + PWM + 中断
第 3 周：BLE 通信 + iOS App 控制
第 4 周：MQTT + 云端 + 完整项目
第 5–8 周：STM32 入门 + FreeRTOS
第 9–12 周：做 2 个完整项目放作品集</code></pre>
"""),
"练习/02-自测题.html": ("练习 02：自测题", "练习", """
<h2>基础自测（每题 1 分，8 分及格）</h2>
<h3>1. 单片机和 iPhone 芯片的最大区别是什么？</h3>
<details><summary>点击查看答案</summary><p>单片机专注控制硬件、低功耗、无复杂 OS；iPhone 的 A 芯片是高性能 AP，跑完整 iOS。</p></details>
<h3>2. GPIO 输出和输入分别用来干什么？</h3>
<details><summary>点击查看答案</summary><p>输出：控制 LED、继电器、电机。输入：读按键、传感器数字信号。</p></details>
<h3>3. 中断和轮询哪个更省电？为什么？</h3>
<details><summary>点击查看答案</summary><p>中断。CPU 可以 Sleep，事件来了才唤醒；轮询 CPU 一直空转。</p></details>
<h3>4. I2C 需要几根线？SPI 呢？</h3>
<details><summary>点击查看答案</summary><p>I2C：2 根（SDA+SCL）。SPI：4 根（MOSI+MISO+SCK+CS）。</p></details>
<h3>5. ESP32 相比 STM32 最大的优势？</h3>
<details><summary>点击查看答案</summary><p>内置 Wi-Fi + BLE，适合 IoT；STM32 工业级稳定性更好。</p></details>
<h3>6. BLE 的 Central 和 Peripheral 分别是什么？</h3>
<details><summary>点击查看答案</summary><p>Central=主机（iPhone），Peripheral=从机（ESP32 传感器）。</p></details>
<h3>7. FreeRTOS 的任务类似 iOS 的什么？</h3>
<details><summary>点击查看答案</summary><p>DispatchQueue / Thread。</p></details>
<h3>8. 为什么嵌入式用 C 不用 Swift？</h3>
<details><summary>点击查看答案</summary><p>MCU 资源有限（RAM 64KB–512KB），Swift 运行时太大；C 编译后直接操作硬件，零开销。</p></details>
<h3>9. UART 调试中，TX 应该接对方的什么引脚？</h3>
<details><summary>点击查看答案</summary><p>TX 接 RX，RX 接 TX，GND 接 GND。</p></details>
<h3>10. 做一个"iOS 控制智能灯"项目需要哪三部分？</h3>
<details><summary>点击查看答案</summary><p>① ESP32 固件（BLE Server + GPIO 控灯）② iOS App（CoreBluetooth 发指令）③ 可选云端（远程控制/数据统计）。</p></details>
"""),
}

for path, (title, module, body) in EXTRA.items():
    PAGES[path] = {"title": title, "tag": module, "module": module, "body": body}

README_BODY = """
<blockquote>
<p>一套面向 iOS 开发者、从零开始的单片机 / 嵌入式学习体系。<br>
用你已经懂的 Swift、CoreBluetooth、Xcode 概念做桥梁，<br>
每个模块都配比喻 + 代码 + 实战，保证小白也能看懂。</p>
</blockquote>
<hr>
<h2>一、这套教程怎么用</h2>
<h3>学习路径（建议按顺序）</h3>
<pre><code>第 1 步 基础（8 篇）→ 单片机概念 / C语言 / GPIO / 中断 / 串口 / I2C·SPI / 选型
第 2 步 硬件入门（3 篇）→ 开发板工具 / 万用表焊接 / 原理图阅读
第 3 步 进阶（4 篇）→ FreeRTOS / 低功耗 / WiFi·MQTT / BLE
第 4 步 实战项目（3 篇）→ 智能灯控 / 温湿度监测 / 蓝牙小车
第 5 步 iOS 联动（2 篇）→ CoreBluetooth / 全链路架构
第 6 步 应用场景（2 篇）→ 行业全景 / 接单赚钱
第 7 步 练习（2 篇）→ 采购清单 / 自测题
</code></pre>
<h3>学习方法（给 iOS 开发者）</h3>
<ol>
<li><strong>带着 iOS 思维学</strong>：每个概念都给了 iOS 对照，不要从零开始。</li>
<li><strong>先跑起来</strong>：花 ¥100 买 ESP32 套件，第一章就点灯。</li>
<li><strong>做项目驱动</strong>：不要只看不做，第 3 周就应该有 iOS 控制 LED 的 Demo。</li>
<li><strong>结合你的 App 能力</strong>：硬件只是后端，App 才是产品——这是你的优势。</li>
</ol>
<hr>
<h2>二、模块速览</h2>
<table>
<tr><th>模块</th><th>篇数</th><th>学完你能做什么</th></tr>
<tr><td><strong>基础</strong></td><td>8</td><td>理解 MCU 原理，写出 GPIO/串口/I2C 代码</td></tr>
<tr><td><strong>硬件入门</strong></td><td>3</td><td>会看原理图、用万用表、基础焊接</td></tr>
<tr><td><strong>进阶</strong></td><td>4</td><td>FreeRTOS 多任务、Wi-Fi/MQTT、BLE 通信</td></tr>
<tr><td><strong>实战项目</strong></td><td>3</td><td>独立完成 3 个 IoT 项目</td></tr>
<tr><td><strong>iOS 联动</strong></td><td>2</td><td>用 CoreBluetooth 控制硬件，完整产品链路</td></tr>
<tr><td><strong>应用场景</strong></td><td>2</td><td>了解行业方向，知道怎么接单赚钱</td></tr>
<tr><td><strong>练习</strong></td><td>2</td><td>采购清单 + 自测检验</td></tr>
</table>
<p><strong>总计 24 篇</strong>，入门预算约 ¥100–170。</p>
<hr>
<h2>三、快速入口</h2>
<ul>
<li>👉 <a href="基础/01-单片机是什么.html">从「单片机是什么」开始</a></li>
<li>👉 <a href="基础/02-从iOS到嵌入式.html">iOS 开发者速查对照表</a></li>
<li>👉 <a href="实战/01-智能灯控.html">第一个实战：智能灯控</a></li>
<li>👉 <a href="iOS联动/01-BLE与CoreBluetooth.html">用你的 CoreBluetooth 经验控制硬件</a></li>
</ul>
<hr>
<h2>四、和 iOS 开发者的关系</h2>
<div class="tip-box">
<strong>你不是从零开始。</strong> 你已经会 Swift、网络通信、蓝牙、App 架构、产品思维——<br>
单片机只是让你多掌握"控制真实世界"的能力。<br>
<strong>IoT = 你的 iOS App + 单片机硬件 + 可选云端 AI</strong>，这是最值钱的组合。
</div>
"""


def page_html(meta, depth):
    prefix = "../" * depth
    module = meta.get("module", "")
    crumb = f'<a href="{prefix}README.html">教程首页</a>'
    if module and depth > 0:
        crumb += f' &nbsp;/&nbsp; {module}'
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="{prefix}_assets/site.css">
<title>{meta['title']} - {SITE}</title>
</head>
<body>
<div class="page-header">
  <div class="page-header-inner">
    <div class="crumb">{crumb}</div>
    <h1>{meta['title']}</h1>
    <span class="header-tag">{meta['tag']}</span>
  </div>
</div>
<div class="container">
  <div class="content-card">
{meta['body']}
  </div>
</div>
<div class="page-footer">
  <p><a href="{prefix}README.html">← 返回教程首页</a> · {SITE}</p>
</div>
<script src="{prefix}_assets/site.js" defer></script>
</body>
</html>"""


def main():
    # README
    readme = page_html({"title": "单片机/嵌入式学习教程", "tag": "教程首页", "module": "", "body": README_BODY}, 0)
    readme = readme.replace("<h1>单片机/嵌入式学习教程</h1>", "<h1>单片机 / 嵌入式学习教程</h1>")
    (ROOT / "README.html").write_text(readme, encoding="utf-8")

    # index redirect
    (ROOT / "index.html").write_text("""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; url=README.html">
  <title>单片机嵌入式教程</title>
</head>
<body><p>正在跳转… <a href="README.html">进入教程</a></p></body>
</html>""", encoding="utf-8")

    for path, meta in PAGES.items():
        depth = path.count("/")
        out = ROOT / path
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page_html(meta, depth), encoding="utf-8")

    print(f"Generated {len(PAGES) + 2} files")


if __name__ == "__main__":
    main()
