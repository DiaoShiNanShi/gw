"""Chapter content definitions."""

from .helpers import chapter

CHAPTERS = {
    "进阶/01-FreeRTOS任务.html": chapter(
        '进阶 01：FreeRTOS 任务',
        '进阶',
        '进阶',
        """<blockquote><p>Task 创建、优先级、vTaskDelay、对照 GCD。</p></blockquote><hr>
<h2>1. 创建</h2>
<pre><code class="language-c">xTaskCreate(sensor_task, "sensor", 4096, NULL, 5, NULL);
xTaskCreate(wifi_task, "wifi", 8192, NULL, 4, NULL);
vTaskStartScheduler();</code></pre>
<h2>2. 对照</h2>
<table><thead><tr><th>FreeRTOS</th><th>iOS</th></tr></thead><tbody><tr><td>Task</td><td>DispatchQueue</td></tr><tr><td>vTaskDelay</td><td>Task.sleep</td></tr><tr><td>Priority</td><td>QoS</td></tr></tbody></table>
<h2>3. 栈大小</h2>
<p>uxTaskGetStackHighWaterMark 监测剩余栈，防溢出。</p>
<h2>4. 结构</h2>
<p>sensor 读数据 → Queue → wifi 发 MQTT，解耦阻塞。</p>
<div class="tip-box">💡 栈给够，监测 HighWaterMark。</div>
<h2>常见问题</h2>
<h3>栈溢出?</h3><p>增大或优化局部数组。</p>
<h3>vTaskDelay(0)?</h3><p>yield 同优先级。</p>
<h3>idle hook?</h3><p>喂狗/低功耗。</p>
<h2>本章小结</h2><ul>
<li>xTaskCreate 参数</li>
<li>优先级数字大优先</li>
<li>vTaskDelay 非阻塞等待</li>
<li>监测栈水位</li>
</ul>
<p><strong>下一步：</strong> <a href="02-同步机制.html">02-同步</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "进阶/02-同步机制.html": chapter(
        '进阶 02：同步机制',
        '进阶',
        '进阶',
        """<blockquote><p>Queue/Semaphore/Mutex/EventGroup。</p></blockquote><hr>
<h2>1. Queue</h2>
<pre><code class="language-c">QueueHandle_t q = xQueueCreate(10, sizeof(SensorData));
xQueueSend(q, &data, portMAX_DELAY);
xQueueReceive(q, &data, portMAX_DELAY);</code></pre>
<h2>2. Mutex</h2>
<pre><code class="language-c">SemaphoreHandle_t m = xSemaphoreCreateMutex();
xSemaphoreTake(m, portMAX_DELAY); /* 访问 SPI */ xSemaphoreGive(m);</code></pre>
<h2>3. EventGroup</h2>
<p>多位事件同步，如 Wi-Fi 连上 AND 传感器就绪。</p>
<h2>4. 对照</h2>
<table><thead><tr><th>RTOS</th><th>Swift</th></tr></thead><tbody><tr><td>Queue</td><td>AsyncStream/Channel</td></tr><tr><td>Mutex</td><td>NSLock</td></tr><tr><td>Semaphore</td><td>DispatchSemaphore</td></tr></tbody></table>
<div class="tip-box">💡 共享 SPI/I2C 总线必须 Mutex。</div>
<h2>常见问题</h2>
<h3>ISR 用 Queue?</h3><p>xQueueSendFromISR。</p>
<h3>优先级反转?</h3><p>Mutex 继承。</p>
<h3>死锁?</h3><p>固定加锁顺序。</p>
<h2>本章小结</h2><ul>
<li>Queue 传数据</li>
<li>Mutex 保临界区</li>
<li>EventGroup 多条件</li>
<li>FromISR 专用 API</li>
</ul>
<p><strong>下一步：</strong> <a href="03-低功耗设计.html">03-低功耗</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "进阶/03-低功耗设计.html": chapter(
        '进阶 03：低功耗设计',
        '进阶',
        '进阶',
        """<blockquote><p>Sleep/Stop/Standby，外设关钟，Tickless。</p></blockquote><hr>
<pre><code class="language-c">// 本章配套：在 DevKit 上验证所学概念
void setup() { Serial.begin(115200); }
void loop() { /* 实验代码 */ }</code></pre>
<h2>1. 层次</h2>
<table><thead><tr><th>层级</th><th>MCU</th><th>ESP32</th></tr></thead><tbody><tr><td>跑满</td><td>mA</td><td>~100mA</td></tr><tr><td>Sleep</td><td>µA~mA</td><td>Deep Sleep µA</td></tr><tr><td>关电</td><td>0</td><td>0</td></tr></tbody></table>
<h2>2. STM32 Stop</h2>
<p>停 PLL，GPIO 保持，中断唤醒，µA 级。</p>
<h2>3. Tickless</h2>
<p>FreeRTOS configUSE_TICKLESS_IDLE，空闲进低功耗。</p>
<h2>4. 测量</h2>
<p>万用表串 ammeter 测 uA；Power Profiler Kit 更准。</p>
<div class="tip-box">💡 Wi-Fi 是功耗大户，上报完睡 Deep Sleep。</div>
<h2>常见问题</h2>
<h3>GPIO 唤醒?</h3><p>EXTI/RTC。</p>
<h3>RAM 丢?</h3><p>Stop 保留 Standby 丢。</p>
<h3>BLE 连接?</h3><p>Connection interval 调大。</p>
<h2>本章小结</h2><ul>
<li>分层降功耗</li>
<li>关无用外设时钟</li>
<li>Tickless Idle</li>
<li>测 uA 验证</li>
</ul>
<p><strong>下一步：</strong> <a href="04-OTA固件升级.html">04-OTA</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "进阶/04-OTA固件升级.html": chapter(
        '进阶 04：OTA 固件升级',
        '进阶',
        '进阶',
        """<blockquote><p>双分区、HTTPS OTA、版本号、回滚。</p></blockquote><hr>
<table><thead><tr><th>要点</th><th>说明</th></tr></thead><tbody><tr><td>实验</td><td>DevKit 验证</td></tr><tr><td>调试</td><td>串口 printf</td></tr></tbody></table>
<h2>1. 分区</h2>
<pre><code class="language-text">factory | ota_0 | ota_1 | nvs
运行 ota_0 下载到 ota_1 切换</code></pre>
<h2>2. ESP32</h2>
<pre><code class="language-c">httpUpdate.update(client, "https://server/fw.bin");</code></pre>
<h2>3. 安全</h2>
<p>HTTPS + 签名校验；防中间人刷恶意固件。</p>
<h2>4. App 触发</h2>
<p>MQTT cmd=update → 设备拉固件 → 重启 → 上报新版本。</p>
<div class="tip-box">💡 OTA 失败保留旧分区可回滚。</div>
<h2>常见问题</h2>
<h3>Brick?</h3><p>双分区+回滚。</p>
<h3>进度?</h3><p>HTTPClient 回调。</p>
<h3>差分?</h3><p>esp_delta_ota 省流量。</p>
<h2>本章小结</h2><ul>
<li>双分区 A/B</li>
<li>HTTPS+签名</li>
<li>版本号管理</li>
<li>MQTT 触发更新</li>
</ul>
<p><strong>下一步：</strong> <a href="05-Bootloader.html">05-Bootloader</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "进阶/05-Bootloader.html": chapter(
        '进阶 05：Bootloader',
        '进阶',
        '进阶',
        """<blockquote><p>启动加载、IAP、UART/USB DFU。</p></blockquote><hr>
<table><thead><tr><th>要点</th><th>说明</th></tr></thead><tbody><tr><td>实验</td><td>DevKit 验证</td></tr><tr><td>调试</td><td>串口 printf</td></tr></tbody></table>
<h2>1. 流程</h2>
<p>上电 → Bootloader 检查标志 → 进 App 或升级模式。</p>
<h2>2. IAP</h2>
<p>In-Application Programming，App 内写 Flash 升级自身。</p>
<h2>3. STM32</h2>
<p>BOOT0 引脚 + 串口 USART1 ISP；或 USB DFU。</p>
<h2>4. 版本</h2>
<pre><code class="language-c">#define FW_VERSION "1.2.3"
const char *ver __attribute__((section(".version")));</code></pre>
<div class="tip-box">💡 Bootloader 区保护，App 不可擦。</div>
<h2>常见问题</h2>
<h3>变砖?</h3><p>UART 恢复 ISP。</p>
<h3>签名?</h3><p>ECDSA 验签。</p>
<h3>AB 切换?</h3><p>otadata 分区指针。</p>
<h2>本章小结</h2><ul>
<li>Bootloader 独立区</li>
<li>IAP/OTA 入口</li>
<li>BOOT0 串口恢复</li>
<li>版本段独立</li>
</ul>
<p><strong>下一步：</strong> <a href="06-内存优化.html">06-内存</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "进阶/06-内存优化.html": chapter(
        '进阶 06：内存优化',
        '进阶',
        '进阶',
        """<blockquote><p>栈/堆/静态分配，内存池，避免碎片。</p></blockquote><hr>
<table><thead><tr><th>要点</th><th>说明</th></tr></thead><tbody><tr><td>实验</td><td>DevKit 验证</td></tr><tr><td>调试</td><td>串口 printf</td></tr></tbody></table>
<h2>1. 原则</h2>
<ul><li>大缓冲放静态/全局</li><li>避免频繁 malloc/free</li><li>字符串用固定 char[]</li></ul>
<h2>2. 池化</h2>
<pre><code class="language-c">static uint8_t pool[4096];
// 简易 allocator 或 FreeRTOS heap_4</code></pre>
<h2>3. 工具</h2>
<p>map 文件看 .bss/.data；heap_caps_get_free_size(ESP32)。</p>
<h2>4. 对照</h2>
<p>无 ARC；泄漏 = 堆只减不增直到复位。</p>
<div class="tip-box">💡 KB 级 RAM 要精打细算。</div>
<h2>常见问题</h2>
<h3>栈 vs 堆?</h3><p>任务栈预分配；堆动态。</p>
<h3>heap_1-5?</h3><p>heap_4 常用带合并。</p>
<h3>PSRAM?</h3><p>ESP32 扩展注意 DMA。</p>
<h2>本章小结</h2><ul>
<li>静态优于动态</li>
<li>内存池减碎片</li>
<li>map 文件分析</li>
<li>监测 heap 剩余</li>
</ul>
<p><strong>下一步：</strong> <a href="07-JTAG与SWD调试.html">07-调试</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "进阶/07-JTAG与SWD调试.html": chapter(
        '进阶 07：JTAG 与 SWD 调试',
        '进阶',
        '进阶',
        """<blockquote><p>ST-Link/J-Link 断点、单步、Watch 变量。</p></blockquote><hr>
<h2>1. SWD 线</h2>
<pre><code class="language-text">SWDIO / SWCLK / GND / 3.3V — 4线调试</code></pre>
<h2>2. CubeIDE</h2>
<p>Debug As → STM32 C/C++ Application → 断点 F5 继续 F6 单步。</p>
<h2>3. OpenOCD</h2>
<pre><code class="language-bash">openocd -f interface/stlink.cfg -f target/stm32f1x.cfg</code></pre>
<h2>4. vs 串口</h2>
<table><thead><tr><th></th><th>printf</th><th>SWD</th></tr></thead><tbody><tr><td>侵入性</td><td>低</td><td>需 halt</td></tr><tr><td>看变量</td><td>字符串</td><td>任意</td></tr><tr><td>硬故障</td><td>难查</td><td>精准</td></tr></tbody></table>
<div class="tip-box">💡 HardFault 用 LR/PC 查 CFSR 寄存器。</div>
<h2>常见问题</h2>
<h3>J-Link vs ST-Link?</h3><p>J-Link 快支持广。</p>
<h3>ESP32 JTAG?</h3><p>内置，需 USB 桥。</p>
<h3>RTT?</h3><p>SEGGER 无串口 log。</p>
<h2>本章小结</h2><ul>
<li>SWD 四线调试</li>
<li>断点单步看变量</li>
<li>OpenOCD/GDB</li>
<li>HardFault 必备</li>
</ul>
<p><strong>下一步：</strong> <a href="08-代码规范.html">08-规范</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "进阶/08-代码规范.html": chapter(
        '进阶 08：代码规范',
        '进阶',
        '进阶',
        """<blockquote><p>MISRA 要点、模块分层 BSP/HAL/App、Git 协作。</p></blockquote><hr>
<table><thead><tr><th>要点</th><th>说明</th></tr></thead><tbody><tr><td>实验</td><td>DevKit 验证</td></tr><tr><td>调试</td><td>串口 printf</td></tr></tbody></table>
<h2>1. 分层</h2>
<pre><code class="language-text">App/ — 业务逻辑
Board/ — 板级驱动
Middleware/ — RTOS/MQTT
Drivers/ — HAL/CMSIS</code></pre>
<h2>2. 命名</h2>
<p>模块前缀 led_init；宏 LED_PIN；避免 magic number。</p>
<h2>3. 头文件</h2>
<p>#pragma once；最小 include；extern "C" 供 C++ 调。</p>
<h2>4. Git</h2>
<p>.ioc 进版本库；generated 可忽略或 CI 再生；语义化版本 tag。</p>
<div class="tip-box">💡 规范代码 six month 后的自己感谢。</div>
<h2>常见问题</h2>
<h3>MISRA 全遵守?</h3><p>车规才严格，IoT 抓重点。</p>
<h3>匈牙利?</h3><p>type 前缀可选。</p>
<h3>单元测?</h3><p>Unity/CMock 测纯逻辑。</p>
<h2>本章小结</h2><ul>
<li>App/BSP/HAL 分层</li>
<li>一致命名</li>
<li>头文件最小依赖</li>
<li>Git+CI 自动化</li>
</ul>
<p><strong>下一步：</strong> <a href="../iOS联动/01-BLE基础.html">iOS 01</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
}
