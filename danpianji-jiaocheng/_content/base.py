"""基础模块章节内容。"""

CHAPTERS = [
    (
        "基础/01-单片机是什么.html",
        "基础 01：单片机是什么",
        "基础模块",
        "基础",
        """
<blockquote><p>学习目标：理解 MCU 的定义与边界；区分 CPU、AP、SoC 与单片机；认识 2026 年主流芯片与真实产品形态；建立「控制专用小电脑」的心智模型。</p></blockquote>

<h2>1. 单片机（MCU）到底是什么？</h2>
<p><strong>单片机（Microcontroller Unit, MCU）</strong> 是把 <strong>CPU、程序存储（Flash）、数据存储（RAM）、定时器、GPIO、通信外设</strong> 集成在一颗芯片上的「迷你计算机」。它不像 iPhone 那样跑完整操作系统，而是执行你烧录进去的固件，<strong>7×24 小时控制硬件</strong>：读传感器、驱动电机、发蓝牙广播、管理电源。</p>
<p>Industry 里常说「嵌入式」——MCU 是嵌入式最核心的执行单元。一颗 ESP32 卖十几块人民币，却能完成 Wi-Fi 配网、BLE 通信、PWM 调光，这就是 MCU 的价值：<strong>足够便宜、足够省电、足够专精</strong>。</p>

<h2>2. MCU vs CPU vs AP：别被名词绕晕</h2>
<table>
<thead><tr><th>术语</th><th>是什么</th><th>典型例子</th><th>和 MCU 关系</th></tr></thead>
<tbody>
<tr><td><strong>CPU</strong></td><td>中央处理器「核」，只管算</td><td>Cortex-M4、RISC-V 核</td><td>MCU 内部包含一颗 CPU 核</td></tr>
<tr><td><strong>AP</strong></td><td>Application Processor，跑 Linux/iOS 的应用处理器</td><td>Apple A18、高通骁龙</td><td>算力远超 MCU，通常不直接控 GPIO</td></tr>
<tr><td><strong>SoC</strong></td><td>System on Chip，多模块集成</td><td>A 系列、ESP32-S3</td><td>MCU 也是一种 SoC，规模更小</td></tr>
<tr><td><strong>MCU</strong></td><td>面向控制的单片系统</td><td>STM32F103、nRF52840</td><td>本教程主角</td></tr>
</tbody>
</table>
<p>iPhone 里：<strong>A 芯片是 AP</strong> 跑 iOS；Apple Watch 里还有 <strong>协处理器 MCU</strong> 在低功耗下持续采样加速度计——这就是「大脑 + 小脑」分工。</p>

<h2>3. 2026 年主流 MCU 与市场格局</h2>
<table>
<thead><tr><th>厂商/系列</th><th>代表型号</th><th>主频</th><th>特色</th><th>典型场景</th></tr></thead>
<tbody>
<tr><td>乐鑫 Espressif</td><td>ESP32-C3 / S3</td><td>160–240 MHz</td><td>Wi-Fi + BLE，Arduino/IDF 生态</td><td>智能家居、IoT 原型</td></tr>
<tr><td>ST Micro</td><td>STM32F4 / H7 / U5</td><td>84–480 MHz</td><td>外设极全，工业车规线完整</td><td>电机控制、仪表、BMS</td></tr>
<tr><td>Nordic</td><td>nRF52840 / 5340</td><td>64 MHz</td><td>BLE 低功耗标杆</td><td>手环、Beacon、无线键鼠</td></tr>
<tr><td>Microchip</td><td>ATmega328P</td><td>16 MHz</td><td>Arduino Uno 同款，极简</td><td>教学、快速验证</td></tr>
<tr><td>TI</td><td>MSP430 / CC2652</td><td>低～48 MHz</td><td>超低功耗 / Zigbee</td><td>表计、传感器节点</td></tr>
</tbody>
</table>
<div class="tip-box">💡 <strong>选型口诀</strong>：要联网选 ESP32；要找工作选 STM32；要省电 BLE 选 nRF；要零门槛选 Arduino，后面再迁移到 ESP32。</div>

<h2>4. 真实产品里的 MCU 长什么样？</h2>
<ul>
<li><strong>小米智能插座</strong>：ESP8266/ESP32 控继电器 + 电量计量芯片</li>
<li><strong>戴森吹风机</strong>：STM32 类 MCU 做电机 PID 与温度闭环</li>
<li><strong>汽车 ECU</strong>：多颗车规 MCU 管 CAN 总线、气囊、门窗</li>
<li><strong>机械键盘</strong>：STM32/GD32 扫描矩阵 + USB HID</li>
<li><strong>你的 Side Project</strong>：ESP32 固件 + iOS CoreBluetooth = 完整智能硬件</li>
</ul>
<p>程序结构几乎 universal：</p>
<pre><code>int main(void) {
    SystemInit();       // 时钟、电源
    GPIO_Init();        // 引脚模式
    while (1) {
        read_sensors();
        update_outputs();
        // 或 sleep 等中断唤醒
    }
}</code></pre>

<h2>5. 为什么 iOS 开发者该学 MCU？</h2>
<p>App 只能活在 phone 里；MCU 让物理世界「可编程」。你会 Swift、懂 MVVM、做过 BLE——<strong>缺的是 200 元开发板和 30 小时 C 语言硬件直觉</strong>。学完后你能独立交付：固件 + App + 云端，这是普通纯 App 开发者没有的壁垒。</p>

<h2>小结</h2>
<ol>
<li>MCU = CPU + 存储 + 外设的单芯片控制系统</li>
<li>别和 AP 比算力，和 AP 比<strong>实时性、成本、功耗、引脚控制</strong></li>
<li>入门芯片推荐 <strong>ESP32</strong>，求职深度选 <strong>STM32</strong></li>
</ol>
<p><strong>下一步：</strong> <a href="02-从iOS开发者视角看嵌入式.html">02-从 iOS 开发者视角看嵌入式</a></p>
""",
    ),
    (
        "基础/02-从iOS开发者视角看嵌入式.html",
        "基础 02：从 iOS 开发者视角看嵌入式",
        "基础模块",
        "基础",
        """
<blockquote><p>学习目标：用 iOS/Swift 已有知识快速映射嵌入式概念；对比两种开发工作流；明确你的优势与需补的短板；制定 4 周入门路线。</p></blockquote>

<h2>1. 概念对照表（建议打印贴显示器旁）</h2>
<table>
<thead><tr><th>iOS / Swift</th><th>嵌入式 / C</th><th>说明</th></tr></thead>
<tbody>
<tr><td><code>UIView</code> / 布局约束</td><td>GPIO 引脚模式</td><td>对外物理接口，输入/输出/上拉</td></tr>
<tr><td><code>Button target-action</code></td><td>外部中断 EXTI</td><td>硬件事件触发回调函数</td></tr>
<tr><td><code>Timer.scheduledTimer</code></td><td>硬件 Timer + 中断</td><td>精确定时，不占用 CPU 空转</td></tr>
<tr><td><code>URLSession</code></td><td>UART / I2C / SPI</td><td>与其他芯片或模块通信</td></tr>
<tr><td><code>CoreBluetooth</code></td><td>BLE Stack (NimBLE/SoftDevice)</td><td>Peripheral 广播，Central 连接</td></tr>
<tr><td><code>UserDefaults</code></td><td>Flash / EEPROM / NVS</td><td>掉电保存配置与小数据</td></tr>
<tr><td><code>DispatchQueue</code></td><td>FreeRTOS Task / 中断优先级</td><td>并发与抢占式调度</td></tr>
<tr><td><code>Instruments</code></td><td>逻辑分析仪 / 示波器</td><td>时序、功耗、协议解码</td></tr>
<tr><td><code>App Store 审核</code></td><td>CE / FCC / 3C / 车规</td><td>产品合规与认证成本</td></tr>
<tr><td><code>Xcode Build</code></td><td>交叉编译 + 烧录</td><td>目标架构是 ARM Cortex-M，不是 arm64 iOS</td></tr>
</tbody>
</table>

<h2>2. 同一件事，两种写法：LED 闪烁</h2>
<p><strong>Swift（伪代码，运行在 iOS）</strong>——你控制的是 UI，GPIO 由 MFi 或 BLE 间接控制：</p>
<pre><code>class LampViewModel: ObservableObject {
    @Published var isOn = false
    func toggle() {
        isOn.toggle()
        bleManager.writeCharacteristic(data: isOn ? Data([1]) : Data([0]))
    }
}</code></pre>
<p><strong>C（运行在 MCU）</strong>——你直接写寄存器或 HAL，引脚物理变高/低：</p>
<pre><code>while (1) {
    HAL_GPIO_TogglePin(GPIOC, GPIO_PIN_13);
    HAL_Delay(500);
}</code></pre>
<div class="tip-box">💡 <strong>关键差异</strong>：iOS 开发是「调 API 层」；嵌入式是「API 底下还有寄存器位」。HAL 是 ST/乐鑫提供的 Swift 式封装，调试到底层时你要能看 Reference Manual。</div>

<h2>3. 开发工作流对照</h2>
<table>
<thead><tr><th>阶段</th><th>iOS</th><th>嵌入式</th></tr></thead>
<tbody>
<tr><td>IDE</td><td>Xcode</td><td>VS Code + PlatformIO / STM32CubeIDE / ESP-IDF</td></tr>
<tr><td>依赖管理</td><td>SPM / CocoaPods</td><td>组件库 / IDF Component / 手动拷贝 .c/.h</td></tr>
<tr><td>运行</td><td>模拟器 / 真机 Debug</td><td>编译 → 烧录 → 串口看 log（无「模拟 GPIO」）</td></tr>
<tr><td>调试</td><td>断点 + LLDB</td><td>断点 + J-Link/SWD + <code>printf</code> 串口</td></tr>
<tr><td>发布</td><td>TestFlight / App Store</td><td>OTA 或产线烧录 + 版本号管理</td></tr>
<tr><td>联调</td><td>后端 API Mock</td><td>示波器看波形 + 手机 App 实机联调</td></tr>
</tbody>
</table>

<h2>4. iOS 开发者的四大优势</h2>
<ul>
<li><strong>产品思维</strong>：很多嵌入式工程师只会驱动，不懂 onboarding、配网 UX——你能补全体验。</li>
<li><strong>无线协议经验</strong>：CoreBluetooth、Network.framework 让你读 BLE 文档不怵。</li>
<li><strong>架构能力</strong>：MVVM、模块化、单测思维可直接用在固件分层（BSP/HAL/App）。</li>
<li><strong>全栈交付</strong>：MCU + iOS + 可选 MQTT 后端 = 可演示、可商用的智能硬件。</li>
</ul>

<h2>5. 需要刻意练习的短板</h2>
<ul>
<li><strong>C 语言与指针</strong>：没有 ARC，内存与寄存器地址要自己管。</li>
<li><strong>电路直觉</strong>：上拉电阻、灌电流、3.3V vs 5V _TOLERANCE。</li>
<li><strong>实时性</strong>：中断里不能 <code>HAL_Delay</code>，类似主线程不能做耗时网络。</li>
<li><strong>文档阅读</strong>：Datasheet / Reference Manual 几百页，要学会用目录和索引。</li>
</ul>

<h2>6. 建议的 4 周入门节奏</h2>
<pre><code>第 1 周：Arduino/ESP32 点灯 + 串口打印（建立「烧录-运行」闭环）
第 2 周：GPIO/中断/定时器 + 读 DHT11（理解轮询 vs 中断）
第 3 周：BLE 广播 + iOS CoreBluetooth 读写特征值
第 4 周：做一个「App 控灯」完整 demo 放 GitHub</code></pre>

<h2>小结</h2>
<p>你不是从零开始，而是<strong>把 Swift 层的抽象往下挖一层</strong>。对照表和工作流图会帮你少踩 50% 的坑。</p>
<p><strong>下一步：</strong> <a href="03-计算机组成与MCU架构.html">03-计算机组成与 MCU 架构</a></p>
""",
    ),
    (
        "基础/03-计算机组成与MCU架构.html",
        "基础 03：计算机组成与 MCU 架构",
        "基础模块",
        "基础",
        """
<blockquote><p>学习目标：掌握 MCU 内部 CPU/Flash/RAM/外设组成；理解哈佛架构与冯·诺依曼架构区别；能读懂典型 memory map；知道时钟树为何决定一切。</p></blockquote>

<h2>1. MCU 内部 block  diagram（ mental model）</h2>
<p>把 MCU 想象成<strong>一座小工厂</strong>：</p>
<ul>
<li><strong>CPU（工人）</strong>：执行指令，跑你的 <code>while(1)</code></li>
<li><strong>Flash（图纸库）</strong>：存程序，掉电不丢</li>
<li><strong>RAM（工作台）</strong>：存变量、栈、堆，掉电清空</li>
<li><strong>外设（专用机器）</strong>：GPIO、UART、Timer、ADC、DMA……各自有寄存器</li>
<li><strong>总线（传送带）</strong>：AHB/APB 连接 CPU 与外设</li>
<li><strong>时钟树（节拍器）</strong>：给每个模块分频率，关时钟 = 省电</li>
</ul>

<h2>2. 哈佛架构 vs 冯·诺依曼</h2>
<table>
<thead><tr><th>架构</th><th>特点</th><th>典型应用</th><th>对开发的影响</th></tr></thead>
<tbody>
<tr><td><strong>哈佛</strong></td><td>指令总线与数据总线分离</td><td>大多数 Cortex-M、ESP32</td><td>Flash 与 RAM 地址空间独立映射</td></tr>
<tr><td><strong>冯·诺依曼</strong></td><td>指令与数据共用总线</td><td>早期 8051、部分 DSP</td><td>程序可从 RAM 执行（XIP 场景少）</td></tr>
</tbody>
</table>
<p>Cortex-M 采用<strong>哈佛内核 + 统一地址映射</strong>：你用 C 指针看到的 0x08000000 是 Flash，0x20000000 是 SRAM，对外设则是 0x40000000 段——<strong>同一份指针语法，不同物理模块</strong>。</p>

<h2>3. 典型 STM32F103 Memory Map（节选）</h2>
<table>
<thead><tr><th>地址范围</th><th>区域</th><th>内容</th></tr></thead>
<tbody>
<tr><td>0x0800_0000</td><td>Flash</td><td>程序、常量（128KB 等）</td></tr>
<tr><td>0x2000_0000</td><td>SRAM</td><td>全局变量、栈、堆（20KB）</td></tr>
<tr><td>0x4001_0000</td><td>APB2</td><td>GPIOA/B/C、USART1、TIM1…</td></tr>
<tr><td>0x4000_0000</td><td>APB1</td><td>USART2/3、I2C、PWR…</td></tr>
<tr><td>0xE000_0000</td><td>私有外设</td><td>NVIC、SysTick、Debug</td></tr>
</tbody>
</table>
<pre><code>// 直接访问 GPIOA 输出数据寄存器（教学用，生产推荐 HAL）
#define GPIOA_ODR  (*(volatile uint32_t *)0x4001080C)
GPIOA_ODR |= (1 &lt;&lt; 13);   // PC13 对应需查具体板子丝印</code></pre>
<div class="tip-box">💡 <strong>volatile 预告</strong>：寄存器必须用 <code>volatile</code>，否则编译器优化会把你「重复读传感器」优化掉——类似 Swift 里 @MainActor 的语义约束，这里是硬件语义。</div>

<h2>4. 启动流程：从复位到 main</h2>
<ol>
<li>上电 / 复位 → PC 指向 <code>Reset_Handler</code>（在 startup.s）</li>
<li>拷贝 .data 到 RAM，清零 .bss</li>
<li>调用 <code>SystemInit()</code> 配置时钟到 72MHz 等</li>
<li>跳转到 <code>main()</code></li>
</ol>
<p>ESP32 类似，只是 Bootloader 还管 Wi-Fi OTA 分区表。iOS 的 <code>main()` → UIApplicationMain</code> 是 OS 级启动；MCU 的 <code>main</code> 就是你世界的入口。</p>

<h2>5. 时钟树：为什么 LED 延时不对先查时钟</h2>
<p>外设挂在不同 APB 分频上。若 <code>SystemCoreClock</code> 假设 72MHz 实际只开了 8MHz，<code>HAL_Delay(1000)</code> 会变成 9 秒。CubeMX / menuconfig 里时钟配置页是<strong>必查项</strong>。</p>
<table>
<thead><tr><th>时钟源</th><th>用途</th></tr></thead>
<tbody>
<tr><td>HSI / HSE</td><td>内部 8MHz / 外部晶振，PLL 倍频到系统主频</td></tr>
<tr><td>LSI / LSE</td><td>低功耗时钟、RTC 走时</td></tr>
<tr><td>外设时钟使能</td><td>RCC 寄存器某位 = 1 才给 GPIO 模块供电逻辑</td></tr>
</tbody>
</table>

<h2>6. 与 iOS 设备内存的直观对比</h2>
<table>
<thead><tr><th></th><th>iPhone</th><th>STM32F103</th><th>ESP32</th></tr></thead>
<tbody>
<tr><td>程序存储</td><td>128GB+ NAND</td><td>64–512 KB Flash</td><td>4–16 MB Flash</td></tr>
<tr><td>运行内存</td><td>8 GB RAM</td><td>20–128 KB SRAM</td><td>520 KB SRAM</td></tr>
<tr><td>启示</td><td>随便 new 对象</td><td>大数组放 Flash、慎用 malloc</td><td>PSRAM 可选但需注意 DMA</td></tr>
</tbody>
</table>

<h2>小结</h2>
<p>懂架构 = 知道代码烧在哪、变量放哪、寄存器在哪。<strong>Memory map 是嵌入式工程师的「项目目录树」</strong>。</p>
<p><strong>下一步：</strong> <a href="04-开发板怎么选.html">04-开发板怎么选</a></p>
""",
    ),
]
