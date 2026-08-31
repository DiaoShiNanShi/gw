"""Chapter content definitions."""

from .helpers import chapter

CHAPTERS = {
    "练习/01-入门采购清单.html": chapter(
        '练习 01：入门采购清单',
        '练习',
        '练习',
        """<blockquote><p>学习目标：200 元内采购清单，知道每项用途与购买关键词。</p></blockquote><hr>
<h2>1. 核心清单</h2>
<table><thead><tr><th>物品</th><th>参考价</th><th>用途</th></tr></thead><tbody><tr><td>ESP32-DevKitC</td><td>¥28</td><td>主控</td></tr><tr><td>USB-C线</td><td>¥8</td><td>供电烧录</td></tr><tr><td>面包板+杜邦线</td><td>¥15</td><td>实验</td></tr><tr><td>LED+电阻+按键</td><td>¥5</td><td>GPIO</td></tr><tr><td>DHT22</td><td>¥8</td><td>传感器</td></tr><tr><td>万用表</td><td>¥30</td><td>排查</td></tr><tr><td>舵机+继电器模块</td><td>¥25</td><td>PWM/强控</td></tr></tbody></table>
<h2>2. 总计</h2>
<p><strong>约 ¥170</strong>，周末到货即可开干。</p>
<h2>3. 可选升级</h2>
<table><thead><tr><th>可选</th><th>价</th></tr></thead><tbody><tr><td>逻辑分析仪</td><td>¥25</td></tr><tr><td>ST-Link+STM32</td><td>¥27</td></tr><tr><td>烙铁套装</td><td>¥40</td></tr></tbody></table>
<h2>4. 关键词</h2>
<pre><code class="language-text">淘宝搜: ESP32-DevKitC-32E 官方版
避免: 传感器大礼包50合1</code></pre>
<div class="tip-box">💡 先买核心七件，别一次买满。</div>
<h2>常见问题</h2>
<h3>哪家买?</h3><p>淘宝/拼多多/立创商城。</p>
<h3>兼容板?</h3><p>可以，注意 CH340 驱动。</p>
<h3>还需要?</h3><p>防静电垫可选。</p>
<h2>本章小结</h2><ul>
<li>170元核心清单</li>
<li>ESP32+DHT22+万用表</li>
<li>按需加 ST-Link</li>
<li>别买大礼包</li>
</ul>
<p><strong>下一步：</strong> <a href="02-自测题.html">02-自测</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "练习/02-自测题.html": chapter(
        '练习 02：自测题（15 题）',
        '练习',
        '练习',
        """<blockquote><p>学习目标：15 道自测题覆盖基础到 iOS 联动，先自答再展开，8 分及格。</p></blockquote><hr>
<pre><code class="language-c">// 本章配套：在 DevKit 上验证所学概念
void setup() { Serial.begin(115200); }
void loop() { /* 实验代码 */ }</code></pre>
<h2>1. 说明</h2>
<p>涵盖 MCU 概念、GPIO、协议、BLE、FreeRTOS、iOS。建议闭卷。</p>
<h2>2. 题目</h2>
<h3>1. MCU 和 CPU 的区别？</h3><details><summary>点击查看答案</summary><p>MCU 集成 CPU+Flash+RAM+外设；CPU 只是运算核心。</p></details><h3>2. GPIO 推挽和开漏区别？</h3><details><summary>点击查看答案</summary><p>推挽可输出高低；开漏只能拉低或高阻，需上拉。</p></details><h3>3. I2C 为什么用上拉？</h3><details><summary>点击查看答案</summary><p>开漏输出只能拉低，释放时靠上拉拉高。</p></details><h3>4. BLE Central 和 Peripheral？</h3><details><summary>点击查看答案</summary><p>Central 发起连接(通常是手机)；Peripheral 广播被连(设备)。</p></details><h3>5. volatile 作用？</h3><details><summary>点击查看答案</summary><p>防止编译器优化掉对寄存器的重复读取。</p></details><h3>6. FreeRTOS 任务和线程？</h3><details><summary>点击查看答案</summary><p>类似，有独立栈和优先级，由调度器抢占。</p></details><h3>7. UART 115200 含义？</h3><details><summary>点击查看答案</summary><p>每秒 115200 比特，常见 8N1 配置。</p></details><h3>8. ESP32 Deep Sleep 功耗？</h3><details><summary>点击查看答案</summary><p>约 10µA 级，RAM 丢失，RTC 内存可保留。</p></details><h3>9. 看门狗作用？</h3><details><summary>点击查看答案</summary><p>程序跑飞超时未喂狗则复位，提高可靠性。</p></details><h3>10. Modbus 功能码 03？</h3><details><summary>点击查看答案</summary><p>读保持寄存器。</p></details><h3>11. ADC 12bit 分辨率？</h3><details><summary>点击查看答案</summary><p>0-4095 对应 0-Vref。</p></details><h3>12. MQTT QoS 1 含义？</h3><details><summary>点击查看答案</summary><p>至少送达一次，可能重复。</p></details><h3>13. STM32 HAL_Delay 不准？</h3><details><summary>点击查看答案</summary><p>先查 SystemCoreClock 和时钟树配置。</p></details><h3>14. iOS CoreBluetooth 扫不到设备？</h3><details><summary>点击查看答案</summary><p>查 UUID、权限、广播、真机。</p></details><h3>15. 指针和数组关系？</h3><details><summary>点击查看答案</summary><p>数组名是指向首元素的常量指针。</p></details>
<h2>3. 评分</h2>
<table><thead><tr><th>得分</th><th>等级</th></tr></thead><tbody><tr><td>12-15</td><td>优秀，进实战</td></tr><tr><td>8-11</td><td>及格，补薄弱章</td></tr><tr><td><8</td><td>重读基础模块</td></tr></tbody></table>
<div class="tip-box">💡 错题回到对应章节动手实验。</div>
<h2>常见问题</h2>
<h3>只做题?</h3><p>必须配合 DevKit。</p>
<h3>15题够?</h3><p>入门检测足够。</p>
<h3>iOS 题?</h3><p>12-15 涉及联动。</p>
<h2>本章小结</h2><ul>
<li>15题含details答案</li>
<li>8分及格</li>
<li>覆盖全模块</li>
<li>错题回章节</li>
</ul>
<p><strong>下一步：</strong> <a href="03-12周学习计划.html">03-计划</a></p>""",
    ),
    "练习/03-12周学习计划.html": chapter(
        '练习 03：12 周学习计划',
        '练习',
        '练习',
        """<blockquote><p>学习目标：12 周从点灯到 2 个完整项目+面试准备，每周可检验产出。</p></blockquote><hr>
<h2>1. 总览</h2>
<pre><code class="language-text">W1-2: 基础+C+GPIO+点灯串口
W3-4: 入门实战10章+协议
W5-6: STM32+ESP32
W7-8: FreeRTOS+低功耗+OTA
W9-10: iOS BLE/MQTT 联动
W11-12: 2项目+面试题</code></pre>
<h2>2. 每周细节</h2>
<table><thead><tr><th>周</th><th>目标</th><th>产出</th></tr></thead><tbody><tr><td>1</td><td>环境+点灯</td><td>Blink 视频</td></tr><tr><td>4</td><td>完成入门实战</td><td>串口日志合集</td></tr><tr><td>8</td><td>STM32+ESP32</td><td>双平台 demo</td></tr><tr><td>10</td><td>App 控灯</td><td>TestFlight 内测</td></tr><tr><td>12</td><td>台灯+环境项目</td><td>GitHub+简历</td></tr></tbody></table>
<h2>3. 时间</h2>
<p>每周至少 5 小时；在职可拉长到 16 周。</p>
<h2>4. 检验</h2>
<p>每章：代码 commit + 串口截图；每项目：1 分钟 demo 视频。</p>
<div class="tip-box">💡 动手>看书，产出>笔记。</div>
<h2>常见问题</h2>
<h3>兼职?</h3><p>5h/周可行。</p>
<h3>跳过STM32?</h3><p>求职建议别跳。</p>
<h3>项目选?</h3><p>台灯+环境监测。</p>
<h2>本章小结</h2><ul>
<li>12周结构化</li>
<li>每周可检验产出</li>
<li>5h/周最低</li>
<li>作品集导向</li>
</ul>
<p><strong>下一步：</strong> <a href="../面试题/01-嵌入式基础50题.html">面试题</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
}
