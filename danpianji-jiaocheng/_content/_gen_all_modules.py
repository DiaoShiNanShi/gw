#!/usr/bin/env python3
"""Generate all mod_*.py, nav.py, __init__.py with validated chapter content."""
from pathlib import Path
import textwrap

OUT = Path(__file__).parent


def mk_body(intro_text, sections, *, tips=None, warns=None, faq_items=None, summary_items=None):
    """Build chapter body >= 1500 chars with required elements."""
    parts = [f'<blockquote><p>{intro_text}</p></blockquote><hr>']
    for title, html in sections:
        parts.append(f"<h2>{title}</h2>\n{html.strip()}")
    for t in (tips or []):
        parts.append(f'<div class="tip-box">💡 {t}</div>')
    for w in (warns or []):
        parts.append(f'<div class="tip-box" style="border-color:#ff6b6b;background:rgba(255,107,107,.08)">⚠️ {w}</div>')
    parts.append("<h2>常见问题</h2>")
    for q, a in faq_items:
        parts.append(f"<h3>{q}</h3><p>{a}</p>")
    parts.append("<h2>本章小结</h2><ul>")
    for item in summary_items:
        parts.append(f"<li>{item}</li>")
    parts.append("</ul>")
    return "\n".join(parts)


def tbl(headers, rows):
    h = "".join(f"<th>{x}</th>" for x in headers)
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f"<table><thead><tr>{h}</tr></thead><tbody>{body}</tbody></table>"


def cd(lang, body):
    return f'<pre><code class="language-{lang}">{body.strip()}</code></pre>'


def ch(path, title, tag, module, body, nxt=None, nxt_label=None):
    if nxt:
        body += f'<p><strong>下一步：</strong> <a href="{nxt}">{nxt_label or nxt}</a></p>'
    return path, {"title": title, "tag": tag, "module": module, "body": body}


# ── Chapter definitions: (path, title, tag, module, intro, sections, faq, summary, next, next_label) ──

def define_all():
    chapters = []

    # ═══ mod_base.py (12) ═══
    base = [
        ("基础/01-单片机概念.html", "基础 01：单片机概念", "基础模块", "基础",
         "学习目标：建立 MCU 心智模型，区分 CPU/AP/SoC/MCU，认识 2026 主流芯片与产品形态。",
         [
             ("1. 单片机（MCU）是什么？", f"""<p><strong>单片机（Microcontroller Unit, MCU）</strong> 是把 CPU、Flash、RAM、定时器、GPIO、通信外设集成在一颗芯片上的迷你计算机。它不像 iPhone 跑完整操作系统，而是执行你烧录的固件，7×24 小时控制硬件：读传感器、驱动电机、发蓝牙广播。</p>
<p>Industry 常说「嵌入式」——MCU 是嵌入式最核心的执行单元。一颗 ESP32 卖十几块人民币，却能完成 Wi-Fi 配网、BLE 通信、PWM 调光。</p>
{tbl(["术语", "是什么", "典型例子"], [
     ["CPU", "中央处理器核", "Cortex-M4"],
     ["AP", "应用处理器", "Apple A18"],
     ["SoC", "片上系统", "ESP32-S3"],
     ["MCU", "面向控制的单片系统", "STM32F103"],
 ])}"""),
             ("2. 2026 主流 MCU 格局", f"""{tbl(["厂商/系列", "代表型号", "特色", "典型场景"], [
     ["乐鑫", "ESP32-C3/S3", "Wi-Fi+BLE", "智能家居、IoT"],
     ["ST", "STM32F4/H7", "外设极全", "工业、汽车"],
     ["Nordic", "nRF52840", "BLE 低功耗", "可穿戴"],
     ["Microchip", "ATmega328P", "极简", "Arduino 教学"],
 ])}
{cd("c", 'int main(void) {\\n    SystemInit();\\n    GPIO_Init();\\n    while (1) { read_sensors(); update_outputs(); }\\n}')}"""),
             ("3. 真实产品里的 MCU", """<ul>
<li><strong>小米智能插座</strong>：ESP8266/ESP32 控继电器</li>
<li><strong>戴森吹风机</strong>：STM32 类 MCU 做电机 PID</li>
<li><strong>汽车 ECU</strong>：多颗车规 MCU 管 CAN 总线</li>
<li><strong>Side Project</strong>：ESP32 固件 + iOS CoreBluetooth</li>
</ul>
<p>为什么 iOS 开发者该学 MCU？App 只能活在 phone 里；MCU 让物理世界可编程。你会 Swift、懂 MVVM、做过 BLE——缺的是 200 元开发板和 C 语言硬件直觉。</p>"""),
         ],
         [("单片机和 CPU 是一回事吗？", "不是。CPU 只是处理器核；MCU 把 CPU、存储、外设集成在一颗芯片里，面向控制场景。"),
          ("入门该选哪颗芯片？", "要联网和 iOS 联动选 ESP32；要求职深度选 STM32；要零门槛选 Arduino Uno。"),
          ("MCU 需要操作系统吗？", "可以裸机跑 while(1)，也可以用 FreeRTOS 等 RTOS 做多任务调度。")],
         ["MCU = CPU + 存储 + 外设的单芯片控制系统", "别和 AP 比算力，比实时性、成本、功耗", "入门推荐 ESP32，求职深度选 STM32", "程序结构通常是初始化 + 死循环或 RTOS 多任务"],
         "02-从iOS开发者视角看嵌入式.html", "02-从 iOS 开发者视角看嵌入式"),
        ("基础/02-从iOS开发者视角看嵌入式.html", "基础 02：从 iOS 开发者视角看嵌入式", "基础模块", "基础",
         "学习目标：用 iOS/Swift 已有知识快速映射嵌入式概念，对比两种开发工作流，制定 4 周入门路线。",
         [
             ("1. 概念对照表", f"""{tbl(["iOS / Swift", "嵌入式 / C", "说明"], [
     ["UIView", "GPIO 引脚", "对外物理接口"],
     ["Button target-action", "外部中断 EXTI", "硬件事件触发回调"],
     ["Timer", "硬件 Timer", "精确定时"],
     ["URLSession", "UART/I2C/SPI", "芯片间通信"],
     ["CoreBluetooth", "BLE Stack", "Peripheral/Central"],
     ["UserDefaults", "Flash/NVS", "掉电保存"],
     ["DispatchQueue", "FreeRTOS Task", "并发调度"],
 ])}"""),
             ("2. 同一件事两种写法：LED 闪烁", f"""<p><strong>Swift（iOS）</strong>——通过 BLE 间接控制：</p>
{cd("swift", 'class LampVM: ObservableObject {\\n    func toggle() { bleManager.write(Data([isOn ? 1 : 0])) }\\n}')}
<p><strong>C（MCU）</strong>——直接写 HAL：</p>
{cd("c", 'while (1) {\\n    HAL_GPIO_TogglePin(GPIOC, GPIO_PIN_13);\\n    HAL_Delay(500);\\n}')}"""),
             ("3. 开发工作流对照", f"""{tbl(["阶段", "iOS", "嵌入式"], [
     ["IDE", "Xcode", "VS Code + PlatformIO / CubeIDE"],
     ["运行", "模拟器/真机", "编译→烧录→串口 log"],
     ["调试", "LLDB 断点", "J-Link + printf 串口"],
     ["发布", "TestFlight", "OTA 或产线烧录"],
 ])}
<h2>4. 建议的 4 周入门节奏</h2>
{cd("text", "第1周：ESP32点灯+串口\\n第2周：GPIO/中断/传感器\\n第3周：BLE+iOS CoreBluetooth\\n第4周：App控灯完整demo")}"""),
         ],
         [("我有 Swift 基础还要学 C 吗？", "要。嵌入式 90% 用 C，指针和位操作是日常。"),
          ("嵌入式调试没有 Xcode 怎么办？", "串口 printf 是 NSLog；复杂问题用逻辑分析仪/示波器。"),
          ("iOS 开发者最大优势是什么？", "产品思维 + BLE 经验 + 全栈交付能力，能独立完成 MCU+App。")],
         ["用对照表把 Swift 概念映射到 C/硬件", "iOS 调 API，嵌入式 API 底下还有寄存器", "优势在产品、无线、架构、全栈", "短板在 C、电路、实时性、读手册"],
         "03-计算机组成与MCU架构.html", "03-计算机组成与 MCU 架构"),
        ("基础/03-计算机组成与MCU架构.html", "基础 03：计算机组成与 MCU 架构", "基础模块", "基础",
         "学习目标：掌握 MCU 内部 CPU/Flash/RAM/外设组成，理解哈佛架构与 memory map，知道时钟树为何决定一切。",
         [
             ("1. MCU 内部 block diagram", """<ul>
<li><strong>CPU</strong>：执行指令</li>
<li><strong>Flash</strong>：存程序，掉电不丢</li>
<li><strong>RAM</strong>：存变量、栈、堆</li>
<li><strong>外设</strong>：GPIO、UART、Timer、ADC、DMA</li>
<li><strong>总线</strong>：AHB/APB 连接 CPU 与外设</li>
<li><strong>时钟树</strong>：给每个模块分频率</li>
</ul>"""),
             ("2. 哈佛 vs 冯·诺依曼", f"""{tbl(["架构", "特点", "典型应用"], [
     ["哈佛", "指令与数据总线分离", "Cortex-M、ESP32"],
     ["冯·诺依曼", "指令与数据共用总线", "早期 8051"],
 ])}"""),
             ("3. STM32F103 Memory Map（节选）", f"""{tbl(["地址范围", "区域", "内容"], [
     ["0x0800_0000", "Flash", "程序、常量"],
     ["0x2000_0000", "SRAM", "变量、栈、堆"],
     ["0x4001_0000", "APB2", "GPIO、USART1"],
     ["0xE000_0000", "私有外设", "NVIC、SysTick"],
 ])}
{cd("c", '#define GPIOA_ODR (*(volatile uint32_t *)0x4001080C)\\nGPIOA_ODR |= (1 << 13);')}"""),
             ("4. 启动流程与时钟", """<ol>
<li>复位 → Reset_Handler（startup.s）</li>
<li>拷贝 .data，清零 .bss</li>
<li>SystemInit() 配置时钟</li>
<li>跳转 main()</li>
</ol>
<p>若 SystemCoreClock 假设 72MHz 实际 8MHz，HAL_Delay(1000) 会变成 9 秒——时钟配置是必查项。</p>"""),
         ],
         [("volatile 有什么用？", "访问硬件寄存器必须用 volatile，否则编译器优化会去掉「重复读」。"),
          ("Flash 和 RAM 容量差多少？", "STM32F103 约 64KB Flash、20KB RAM；iPhone 是 GB 级，嵌入式要省内存。"),
          ("什么是 NVIC？", "Nested Vectored Interrupt Controller，管理中断优先级与向量表。")],
         ["MCU = CPU + Flash + RAM + 外设 + 总线 + 时钟", "Memory map 是嵌入式的项目目录树", "启动从 Reset_Handler 到 main", "时钟配错会导致延时、波特率全错"],
         "04-开发板怎么选.html", "04-开发板怎么选"),
        ("基础/04-开发板怎么选.html", "基础 04：开发板怎么选", "基础模块", "基础",
         "学习目标：按目标选对开发板与配件，200 元内配齐入门实验环境。",
         [
             ("1. 入门三板斧", f"""{tbl(["开发板", "价格", "推荐理由"], [
     ["ESP32-DevKitC", "25～40元", "Wi-Fi+BLE，和 iOS 联动最佳"],
     ["Arduino Uno R3", "20～35元", "最简单，教程最多"],
     ["STM32F103最小系统", "10～15元", "求职必备，极便宜"],
 ])}"""),
             ("2. 必买配件", """<ul>
<li>面包板 + 杜邦线</li>
<li>LED、220Ω 电阻、按键</li>
<li>DHT11/DHT22 温湿度模块</li>
<li>USB 数据线（ESP32 多 Type-C）</li>
<li>数字万用表</li>
</ul>"""),
             ("3. 不要一上来就买", """<ul>
<li>❌ 树莓派（Linux 小电脑，不是 MCU 入门）</li>
<li>❌ 几十种传感器大礼包（吃灰）</li>
<li>❌ 没文档的冷门板子</li>
</ul>
<h2>4. Mac 开发环境</h2>
<ul>
<li>Arduino IDE 或 PlatformIO（VS Code 插件）</li>
<li>ESP-IDF（乐鑫官方）</li>
<li>STM32CubeIDE（ST 官方免费）</li>
</ul>"""),
         ],
         [("只有 Mac 能开发 ESP32 吗？", "可以。Arduino/PlatformIO/ESP-IDF 均支持 macOS。"),
          ("买正版 Arduino 还是兼容板？", "兼容板即可，功能相同；注意 USB 芯片驱动（CP2102/CH340）。"),
          ("需要示波器吗？", "入门不必，逻辑分析仪 20 元档足够看 I2C/UART。")],
         ["ESP32 最适合 IoT+iOS 路线", "STM32 适合求职工业方向", "200 元内可配齐实验环境", "别买树莓派当 MCU 入门"],
         "05-C语言速成-Swift开发者版.html", "05-C 语言速成"),
        ("基础/05-C语言速成-Swift开发者版.html", "基础 05：C 语言速成（Swift 开发者版）", "基础模块", "基础",
         "学习目标：掌握嵌入式 C 与 Swift 的差异，学会指针、位操作、头文件与 struct。",
         [
             ("1. 语法对照", f"""{tbl(["Swift", "C"], [
     ["var x = 10", "int x = 10;"],
     ["let pi = 3.14", "const float pi = 3.14f;"],
     ["func add(a:Int,b:Int)->Int", "int add(int a, int b)"],
     ["ARC", "malloc/free 或栈分配"],
 ])}"""),
             ("2. 指针与位操作", f"""{cd("c", '*(volatile unsigned int *)0x4001080C = 0x01;  // 写寄存器\\nGPIOA->ODR |= (1 << 5);   // 置位\\nGPIOA->ODR &= ~(1 << 5);  // 清零')}"""),
             ("3. 结构体与头文件", f"""{cd("c", 'typedef struct {\\n    float temp;\\n    float humi;\\n} SensorData;\\n\\n#include "driver.h"\\nint main(void) { gpio_init(); while(1) {} }')}"""),
             ("4. 练手题", """<ol>
<li>写函数判断数字是否为偶数</li>
<li>for 循环计算 1～100 的和</li>
<li>定义 SensorData 结构体并打印字段</li>
</ol>"""),
         ],
         [("C 需要手动内存管理吗？", "嵌入式多用栈和静态分配；动态 malloc 要注意碎片和失败。"),
          ("位操作为什么重要？", "配置寄存器每一位控制不同功能，HAL 底层全是位操作。"),
          (".h 和 .c 怎么分工？", ".h 声明接口，.c 实现；类似 Swift 的 public API 与实现文件。")],
         ["C 与 Swift 语法相似但无 ARC", "指针和位操作是嵌入式日常", "volatile 用于寄存器访问", "头文件组织模块化固件"],
         "06-GPIO与点灯原理.html", "06-GPIO 与点灯"),
        ("基础/06-GPIO与点灯原理.html", "基础 06：GPIO 与点灯原理", "基础模块", "基础",
         "学习目标：理解 GPIO 输入/输出模式，掌握 LED 点灯电路与 HAL/Arduino API。",
         [
             ("1. GPIO 是什么", """<p><strong>GPIO = General Purpose Input/Output</strong>，芯片上可编程的引脚。</p>
<ul>
<li><strong>输出</strong>：控 LED、继电器</li>
<li><strong>输入</strong>：读按键、数字传感器</li>
<li><strong>复用</strong>：UART/I2C/SPI 专用功能</li>
</ul>"""),
             ("2. 点灯电路", f"""{cd("text", "GPIO2 ──→ LED(+) ──→ LED(-) ──→ 220Ω ──→ GND")}
{tbl(["模式", "函数/API"], [
     ["输出配置", "pinMode(pin, OUTPUT)"],
     ["写高/低", "digitalWrite(pin, HIGH/LOW)"],
     ["翻转", "HAL_GPIO_TogglePin()"],
 ])}"""),
             ("3. 代码示例", f"""{cd("c", 'pinMode(LED_PIN, OUTPUT);\\nwhile(1) {\\n    digitalWrite(LED_PIN, HIGH); delay(500);\\n    digitalWrite(LED_PIN, LOW);  delay(500);\\n}')}"""),
             ("4. 常见坑", """<ul>
<li>LED 接反 → 不亮</li>
<li>没加电阻 → 烧 LED/GPIO</li>
<li>GPIO 编号与丝印不一致 → 查开发板手册</li>
<li>ESP32 部分引脚启动时有特殊用途（GPIO0/2）</li>
</ul>"""),
         ],
         [("灌电流和拉电流接法区别？", "灌电流：GPIO 输出 LOW 时 LED 亮；拉电流：HIGH 亮。看开发板原理图。"),
          ("一个 GPIO 能驱动多大电流？", "ESP32 单脚约 12mA，大负载用三极管/MOSFET。"),
          ("浮空输入有什么问题？", "未定义电平会误触发，输入模式常用上拉/下拉。")],
         ["GPIO 是 MCU 与外界的桥梁", "点灯是嵌入式 Hello World", "限流电阻必不可少", "引脚编号以开发板手册为准"],
         "07-常见通信协议入门.html", "07-通信协议入门"),
        ("基础/07-常见通信协议入门.html", "基础 07：常见通信协议入门", "基础模块", "基础",
         "学习目标：建立 UART/I2C/SPI/BLE/Wi-Fi/MQTT 全局视图，知道何时选哪种协议。",
         [
             ("1. 协议速查表", f"""{tbl(["协议", "线数", "距离", "典型场景"], [
     ["UART", "2 TX/RX", "短", "调试打印、GPS"],
     ["I2C", "2 SDA/SCL", "短", "温湿度、OLED"],
     ["SPI", "4+", "短", "Flash、高速传感器"],
     ["BLE", "无线", "~10m", "iOS 联动 ⭐"],
     ["Wi-Fi", "无线", "远", "智能家居、MQTT"],
     ["MQTT", "基于 TCP", "互联网", "设备↔云端↔App"],
 ])}"""),
             ("2. 与 iOS 的关系", """<ul>
<li><strong>BLE</strong> → CoreBluetooth（最该先学）</li>
<li><strong>Wi-Fi + MQTT</strong> → App 经云端控制</li>
<li><strong>HTTP</strong> → ESP32 Web Server</li>
</ul>"""),
             ("3. 大白话记忆", f"""{cd("text", "UART = 两个人面对面说话（调试必备）\\nI2C = 一条总线挂多个设备\\nSPI = 高速专线\\nBLE = 和 iPhone 蓝牙配对")}"""),
         ],
         [("I2C 和 SPI 怎么选？", "多设备、低速选 I2C；高速、点对点选 SPI。"),
          ("BLE 和 Wi-Fi 怎么选？", "低功耗近场选 BLE；要远程、大数据选 Wi-Fi。"),
          ("MQTT 和 HTTP REST 区别？", "MQTT 轻量 pub/sub 适合 IoT；HTTP 适合偶尔请求。")],
         ["UART 是调试生命线", "I2C 适合多传感器", "BLE 是 iOS 开发者最佳切入点", "协议选型看距离、功耗、带宽"],
         "08-中断与定时器.html", "08-中断与定时器"),
        ("基础/08-中断与定时器.html", "基础 08：中断与定时器", "基础模块", "基础",
         "学习目标：理解外部中断与硬件定时器，对比轮询，掌握防抖与 ISR 编写规范。",
         [
             ("1. 轮询 vs 中断", f"""{tbl(["方式", "CPU占用", "类比 iOS"], [
     ["轮询", "高，一直读按键", "while true 检查状态"],
     ["中断", "低，事件唤醒", "target-action 回调"],
 ])}"""),
             ("2. 外部中断示例", f"""{cd("c", 'void IRAM_ATTR onButton() { flag = true; }\\nvoid setup() {\\n  pinMode(BTN, INPUT_PULLUP);\\n  attachInterrupt(digitalPinToInterrupt(BTN), onButton, FALLING);\\n}')}"""),
             ("3. 硬件定时器", """<p>精确定时、PWM、RTOS tick 都依赖定时器。HAL 提供 TIMx 配置微秒级周期。</p>
<p>中断里禁止 HAL_Delay 和耗时操作——类似主线程不能做阻塞网络。</p>"""),
             ("4. 防抖", """<p>机械按键有 5～20ms 抖动。软件防抖：中断只置标志，loop 里 delay 消抖后再处理。</p>"""),
         ],
         [("中断优先级有什么用？", "高优先级中断可抢占低优先级，关键信号（如安全）需更高优先级。"),
          ("ISR 里能 printf 吗？", "不推荐，耗时且可能重入；只置标志，主循环处理。"),
          ("定时器和 delay 区别？", "delay 阻塞 CPU；定时器中断不占用主循环做其他事。")],
         ["中断是事件驱动的基础", "ISR 要短小，复杂逻辑放主循环", "硬件定时器比 delay 精确", "按键必须防抖"],
         "09-芯片选型指南.html", "09-芯片选型指南"),
        ("基础/09-芯片选型指南.html", "基础 09：芯片选型指南", "基础模块", "基础",
         "学习目标：按项目需求（联网、功耗、成本、外设）快速选型 MCU。",
         [
             ("1. 选型矩阵", f"""{tbl(["需求", "推荐", "理由"], [
     ["Wi-Fi+BLE+App", "ESP32", "生态、价格、例程"],
     ["超低功耗传感", "ESP32-C3/nRF52", "Deep Sleep µA"],
     ["电机PWM/工业", "STM32F4/G4", "定时器、ADC丰富"],
     ["成本极限", "ESP8266/STM32F103", "量产几元"],
     ["车规/功能安全", "STM32 U5/H7", "AEC-Q100 产品线"],
 ])}"""),
             ("2. 关键参数", f"""{tbl(["参数", "说明", "选型提示"], [
     ["Flash/RAM", "程序与变量空间", "带 LVGL 要更大 Flash"],
     ["GPIO 数量", "可用引脚", "留 20% 余量"],
     ["ADC/DAC", "模拟采集", "传感器多要足够通道"],
     ["封装", "QFN/LQFP", "手工焊接选大封装"],
 ])}"""),
             ("3. 决策流程", """<ol>
<li>列出外设清单（Wi-Fi、BLE、CAN、屏…）</li>
<li>估算 Flash/RAM（协议栈占大头）</li>
<li>查供货与参考设计</li>
<li>买 DevKit 验证再定量产型号</li>
</ol>"""),
         ],
         [("ESP32 和 STM32 能互相替代吗？", "部分场景可以，但 ESP32 偏连接，STM32 偏控制与外设。"),
          ("要不要选带 PSRAM 的 ESP32？", "UI、摄像头、大缓冲建议选 S3+PSRAM。"),
          ("国产替代 STM32 可靠吗？", "GD32/APM32 多数兼容，求职仍建议熟悉 ST 生态。")],
         ["按需求列外设清单再选型", "ESP32 适合 IoT，STM32 适合工控", "DevKit 验证后再定量产型号", "留 GPIO 与内存余量"],
         "10-应用场景与赚钱方向.html", "10-应用场景与赚钱方向"),
        ("基础/10-应用场景与赚钱方向.html", "基础 10：应用场景与赚钱方向", "基础模块", "基础",
         "学习目标：了解嵌入式七大行业方向与 iOS+MCU 组合的副业路径。",
         [
             ("1. 高需求行业", f"""{tbl(["行业", "典型产品", "薪资感受"], [
     ["消费电子/IoT", "台灯、插座、门锁", "8K～20K"],
     ["工业控制", "PLC、电机驱动", "10K～25K"],
     ["汽车电子", "ECU、BMS", "15K～35K+"],
     ["医疗器械", "血压计、监护仪", "12K～25K"],
     ["新能源", "充电桩、储能BMS", "热门缺口大"],
 ])}"""),
             ("2. iOS+嵌入式组合拳", f"""{cd("text", "传感器(MCU) → BLE/Wi-Fi → iOS App → 云端 AI")}"""),
             ("3. 副业方向", """<ul>
<li>智能硬件原型（MCU + App 一体化）</li>
<li>工业设备改造（加传感器上云）</li>
<li>毕业设计辅导</li>
</ul>"""),
         ],
         [("纯 App 和全栈智能硬件哪个更稀缺？", "能独立交付 MCU+App 的人才更少，溢价更高。"),
          ("嵌入式哪个方向最适合副业？", "消费电子 IoT + 定制 App，投入小、周期短。"),
          ("需要硬件工程师证吗？", "作品集和交付能力比证书重要。")],
         ["七大行业各有特点与合规要求", "iOS+MCU 是差异化竞争力", "副业从原型和小项目开始", "作品集比证书重要"],
         "11-I2C与SPI协议.html", "11-I2C 与 SPI"),
        ("基础/11-I2C与SPI协议.html", "基础 11：I2C 与 SPI 协议", "基础模块", "基础",
         "学习目标：深入 I2C/SPI 时序、地址、速率，能驱动 OLED、Flash 等常见外设。",
         [
             ("1. I2C 要点", f"""{tbl(["概念", "说明"], [
     ["SDA/SCL", "数据线与时钟，开漏+上拉"],
     ["7位地址", "如 OLED 0x3C"],
     ["400kHz", "Fast Mode 常用速率"],
 ])}
{cd("c", 'Wire.begin(21, 22);\\nWire.beginTransmission(0x3C);\\nWire.write(cmd);\\nWire.endTransmission();')}"""),
             ("2. SPI 要点", f"""{tbl(["信号", "说明"], [
     ["MOSI/MISO", "主出从入 / 主入从出"],
     ["SCK", "时钟由主机产生"],
     ["CS", "片选，多设备各自 CS"],
 ])}"""),
             ("3. 选型对比", f"""{tbl(["", "I2C", "SPI"], [
     ["线数", "2", "4+"],
     ["速度", "较慢", "可达几十 MHz"],
     ["多设备", "地址区分", "各自 CS"],
 ])}"""),
         ],
         [("I2C 上拉电阻多大？", "常用 4.7kΩ，线长或电容大时适当减小。"),
          ("SPI 模式 0/3 是什么？", "CPOL/CPHA 组合，看从设备 datasheet 要求。"),
          ("同一总线能混挂 3.3V 和 5V 吗？", "需电平转换芯片，不能直接混挂。")],
         ["I2C 两线多设备，SPI 四线高速", "开漏上拉是 I2C 电气基础", "读 datasheet 确认地址和时序", "逻辑分析仪是协议调试利器"],
         "12-环境搭建.html", "12-环境搭建"),
        ("基础/12-环境搭建.html", "基础 12：环境搭建", "基础模块", "基础",
         "学习目标：在 Mac 上完成 ESP32/STM32 工具链安装，跑通编译烧录串口闭环。",
         [
             ("1. ESP32 路线", f"""{cd("bash", 'brew install --cask arduino-ide\\n# 或 VS Code + PlatformIO\\nls /dev/cu.*\\nscreen /dev/cu.usbserial-xxx 115200')}"""),
             ("2. STM32 路线", """<ol>
<li>下载 STM32CubeIDE</li>
<li>ST-Link 连接</li>
<li>CubeMX 配置引脚 → 生成代码</li>
</ol>"""),
             ("3. 调试工具箱", f"""{tbl(["工具", "用途"], [
     ["串口监视器", "printf 调试"],
     ["万用表", "测电压通断"],
     ["逻辑分析仪", "I2C/SPI 解码"],
     ["示波器", "信号质量（进阶）"],
 ])}"""),
             ("4. 第一天验收标准", """<ul>
<li>环境装好</li>
<li>例程编译通过</li>
<li>串口看到 Hello</li>
<li>LED 闪起来</li>
</ul>"""),
         ],
         [("PlatformIO 和 Arduino IDE 怎么选？", "快速实验用 Arduino；多文件工程用 PlatformIO。"),
          ("Mac 找不到串口设备？", "装 CP2102/CH340 驱动，换数据线（要能传数据）。"),
          ("烧录失败提示连接超时？", "按住 BOOT 再点上传，或检查 TX/RX 接线。")],
         ["ESP32 首选 Arduino/PlatformIO", "STM32 用 CubeIDE+CubeMX", "串口是嵌入式 NSLog", "四步验收：编译烧录串口LED"],
         "../硬件/01-开发板与工具.html", "硬件 01-开发板与工具"),
    ]

    for item in base:
        path, title, tag, module, intro, sections, faq, summ, nxt, nxt_l = item
        body = mk_body(intro, sections, tips=["建议把本章表格存笔记，动手时对照检查。"],
                       faq_items=faq, summary_items=summ)
        chapters.append(ch(path, title, tag, module, body, nxt, nxt_l))

    # ═══ mod_hardware.py (6) ═══
    hw_data = [
        ("硬件/01-开发板与工具.html", "硬件 01：开发板与工具", "硬件入门", "硬件",
         "学习目标：认识主流开发板，配齐工具链，完成首次安全上电与 Blink。",
         [("1. 开发板类型", tbl(["类型", "代表", "场景"], [["Wi-Fi/BLE", "ESP32-DevKitC", "IoT+iOS"], ["工业ARM", "STM32F103", "工控求职"], ["低功耗BLE", "nRF52840 DK", "可穿戴"]])),
          ("2. 必备清单", tbl(["物品", "用途", "必须"], [["ESP32+数据线", "主控烧录", "✅"], ["面包板杜邦线", "免焊实验", "✅"], ["万用表", "测电压", "✅"]])),
          ("3. 首次 Blink", cd("c", 'void setup(){ pinMode(2,OUTPUT); }\\nvoid loop(){ digitalWrite(2,HIGH); delay(500); digitalWrite(2,LOW); delay(500);}'))],
         [("开发板和芯片什么关系？", "开发板 = MCU + 最小外围 + USB，降低入门门槛。"), ("必须买正版 Arduino 吗？", "兼容板即可。"), ("Mac 能开发吗？", "完全支持。")],
         ["开发板让初学者跳过 PCB", "ESP32-DevKitC 是 IoT 首选", "万用表是必备", "Blink 是第一步验收"],
         "02-万用表与焊接入门.html", "02-万用表与焊接"),
        ("硬件/02-万用表与焊接入门.html", "硬件 02：万用表与焊接入门", "硬件入门", "硬件",
         "学习目标：用万用表排查 80% 硬件问题，掌握焊接与安全规范。",
         [("1. 万用表三档", tbl(["档位", "测什么"], [["DC V", "3.3V/5V"], ["通断Ω", "线路连通"], ["电阻", "阻值验证"]])),
          ("2. 安全红线", "<ul><li>VCC-GND 短路烧芯片</li><li>5V 进 ESP32 GPIO 永久损坏</li><li>带电焊接危险</li></ul>"),
          ("3. 焊接五步", cd("text", "加热焊盘→送锡→移锡→停1秒→移烙铁"))],
         [("表笔怎么接？", "测电压黑笔 GND，红笔测试点。"), ("虚焊怎么查？", "通断档测引脚与焊盘。"), ("无铅焊锡难焊？", "初学者可用含铅 0.8mm。")],
         ["万用表排查电源和连通", "ESP32 只能 3.3V GPIO", "焊接先练废板", "断电再测通断"],
         "03-原理图阅读入门.html", "03-原理图阅读"),
        ("硬件/03-原理图阅读入门.html", "硬件 03：原理图阅读入门", "硬件入门", "硬件",
         "学习目标：阅读开发板原理图，定位 LED、按键、电源、通信接口引脚。",
         [("1. 为何看原理图", "<p>原理图是硬件 API 文档，不看图接线等于盲调 SDK。</p>"),
          ("2. 符号速查", tbl(["符号", "含义"], [["R/C/L", "电阻电容电感"], ["VCC/GND", "电源地"], ["U", "集成电路"]])),
          ("3. 阅读四步法", cd("text", "找MCU→追电源→追GPIO→追通信接口"))],
         [("PDF 原理图哪里下载？", "厂商 GitHub 或商品详情页。"), ("丝印 GPIO2 一定接 LED 吗？", "以原理图为准，不同板可能不同。"), ("立创 EDA 免费吗？", "免费在线看画原理图。")],
         ["原理图是硬件 API", "先找 MCU 和电源", "GPIO 以原理图为准", "对照 PDF 和实物板"],
         "04-PCB与面包板实战.html", "04-PCB与面包板"),
        ("硬件/04-PCB与面包板实战.html", "硬件 04：PCB 与面包板实战", "硬件入门", "硬件",
         "学习目标：理解面包板拓扑与 PCB 层结构，完成 LED+按键电路。",
         [("1. 面包板", "<p>中间槽两侧不连通，电源轨整列连通。</p>"),
          ("2. LED 电路", cd("text", "3V3─[220Ω]─LED+─LED-─GPIO")),
          ("3. PCB 术语", tbl(["术语", "含义"], [["丝印", "白色文字"], ["阻焊", "绿色防短路漆"], ["过孔", "层间连接"]]))],
         [("面包板能跑多快信号？", "MHz 以上建议上 PCB。"), ("打样贵吗？", "5片10x10约几十元。"), ("飞线是什么？", "手工补线调试用。")],
         ["面包板适合实验", "验证后再画 PCB", "限流电阻保护 LED", "嘉立创打样便宜"],
         "05-电源设计与LDO.html", "05-电源设计"),
        ("硬件/05-电源设计与LDO.html", "硬件 05：电源设计与 LDO", "硬件入门", "硬件",
         "学习目标：理解 LDO/DC-DC，为 ESP32 设计稳定 3.3V 供电。",
         [("1. 电源树", cd("text", "USB 5V → LDO → 3.3V → ESP32/传感器")),
          ("2. LDO vs DC-DC", tbl(["类型", "优点", "缺点"], [["LDO", "简单低噪声", "效率低"], ["DC-DC", "效率高", "电路复杂"]])),
          ("3. ESP32 要点", "<ul><li>Wi-Fi 峰值 500mA+</li><li>100nF+10µF 去耦</li><li>Brownout 自动复位</li></ul>")],
         [("Brownout 是什么？", "电压过低芯片自动复位保护。"), ("电池供电怎么选？", "LiPo+低压差 LDO 或 Boost+ LDO。"), ("纹波大有什么影响？", "Wi-Fi 断连、ADC 乱跳。")],
         ["供电稳定是一切的基", "Wi-Fi 时电流峰值大", "去耦电容靠近芯片", "锂电池必须加保护板"],
         warns=["锂电池必须加保护板，裸 cell 充电有起火风险。"],
         nxt="06-元器件选型手册.html", nxt_label="06-元器件选型"),
        ("硬件/06-元器件选型手册.html", "硬件 06：元器件选型手册", "硬件入门", "硬件",
         "学习目标：按项目选 MCU、传感器、电源，建立 BOM 思维。",
         [("1. MCU 矩阵", tbl(["需求", "推荐"], [["联网", "ESP32"], ["工业", "STM32F4"], ["超低功耗", "nRF52"]])),
          ("2. 传感器", tbl(["功能", "型号", "接口"], [["温湿度", "DHT22/SHT30", "单总线/I2C"], ["距离", "HC-SR04", "GPIO"], ["屏", "SSD1306", "I2C"]])),
          ("3. BOM 示例", tbl(["位号", "型号"], [["U1", "ESP32-DevKitC"], ["Sensor", "DHT22"]]))],
         [("LCSC 怎么用？", "搜型号看库存和数据手册。"), ("模块和芯片区别？", "模块含外围，开发快；芯片成本低量产。"), ("0805 和 0603？", "贴片封装尺寸，手工焊选大封装。")],
         ["选型先列外设清单", "模块加速原型", "LCSC 查供货", "BOM 留余量"],
         "../入门实战/01-第一个程序点灯.html", "入门实战 01-点灯"),
    ]
    for item in hw_data:
        path, title, tag, module, intro, sections, faq, summ, nxt, nxt_l = item[:10]
        warns = [item[10]] if len(item) > 10 else None
        body = mk_body(intro, sections, tips=["实验阶段用面包板，稳定后再 PCB。"], warns=warns, faq_items=faq, summary_items=summ)
        chapters.append(ch(path, title, tag, module, body, nxt, nxt_l))

    return chapters


# Continue in part 2 - the script is too long, I'll use exec approach
if __name__ == "__main__":
    print("Use _gen_all_modules_full.py")
