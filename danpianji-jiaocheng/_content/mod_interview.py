"""Chapter content definitions."""

from .helpers import chapter

CHAPTERS = {
    "面试题/01-嵌入式基础50题.html": chapter(
        '面试题 01：嵌入式基础 50 题',
        '面试题',
        '面试题',
        """<blockquote><p>学习目标：50 道嵌入式基础面试题含参考答案，覆盖 MCU/GPIO/协议/C/RTOS。</p></blockquote><hr>
<pre><code class="language-c">// 本章配套：在 DevKit 上验证所学概念
void setup() { Serial.begin(115200); }
void loop() { /* 实验代码 */ }</code></pre>
<h2>1. 使用说明</h2>
<p>先自答再展开。校招/社招基础岗常从中抽 5-10 题。</p>
<h2>2. 题目与答案</h2>
<h3>1. 什么是 MCU？</h3><details><summary>参考答案</summary><p>集成 CPU、存储、外设的单芯片控制器，面向嵌入式控制。</p></details><h3>2. Flash 和 RAM 区别？</h3><details><summary>参考答案</summary><p>Flash 掉电保持存程序；RAM 掉电丢失存变量。</p></details><h3>3. 解释 GPIO 推挽输出。</h3><details><summary>参考答案</summary><p>内部 PMOS+NMOS 可主动输出高或低。</p></details><h3>4. 什么是中断？</h3><details><summary>参考答案</summary><p>硬件事件打断 CPU 执行 ISR，再返回。</p></details><h3>5. UART 需要几根线？</h3><details><summary>参考答案</summary><p>至少 TX/RX/GND 三根。</p></details><h3>6. I2C 总线两根线叫什么？</h3><details><summary>参考答案</summary><p>SDA 数据线、SCL 时钟线。</p></details><h3>7. SPI 片选 CS 作用？</h3><details><summary>参考答案</summary><p>多从设备时选择当前通信对象。</p></details><h3>8. 什么是波特率？</h3><details><summary>参考答案</summary><p>串口每秒传输的符号数，常用 115200。</p></details><h3>9. 指针是什么？</h3><details><summary>参考答案</summary><p>存放内存地址的变量。</p></details><h3>10. volatile 关键字？</h3><details><summary>参考答案</summary><p>告诉编译器不要优化对该变量的访问。</p></details><h3>11. 堆和栈区别？</h3><details><summary>参考答案</summary><p>栈自动管理局部变量；堆 malloc 手动 free。</p></details><h3>12. 什么是 PWM？</h3><details><summary>参考答案</summary><p>脉宽调制，用占空比模拟模拟量或控舵机。</p></details><h3>13. ADC 作用？</h3><details><summary>参考答案</summary><p>模拟电压转数字量。</p></details><h3>14. 看门狗 IWDG 作用？</h3><details><summary>参考答案</summary><p>超时复位防程序跑飞。</p></details><h3>15. CAN 总线特点？</h3><details><summary>参考答案</summary><p>差分、多主、抗干扰，汽车常用。</p></details><h3>16. Modbus RTU 物理层？</h3><details><summary>参考答案</summary><p>通常 RS485。</p></details><h3>17. BLE GATT 三层？</h3><details><summary>参考答案</summary><p>Service → Characteristic → Descriptor。</p></details><h3>18. Notify 和 Read 区别？</h3><details><summary>参考答案</summary><p>Notify 设备主动推；Read 主机主动读。</p></details><h3>19. FreeRTOS Task 创建函数？</h3><details><summary>参考答案</summary><p>xTaskCreate。</p></details><h3>20. Mutex 解决什么问题？</h3><details><summary>参考答案</summary><p>多任务访问共享资源互斥，防竞态。</p></details><h3>21. Queue 用途？</h3><details><summary>参考答案</summary><p>任务间安全传递数据。</p></details><h3>22. ESP32 Deep Sleep 唤醒方式？</h3><details><summary>参考答案</summary><p>定时器、GPIO、RTC 等。</p></details><h3>23. NVS 是什么？</h3><details><summary>参考答案</summary><p>ESP32 非易失键值存储。</p></details><h3>24. OTA 双分区目的？</h3><details><summary>参考答案</summary><p>升级失败可回滚旧固件。</p></details><h3>25. STM32 HAL 和 LL？</h3><details><summary>参考答案</summary><p>HAL 抽象易用；LL 接近寄存器高效。</p></details><h3>26. CubeMX 作用？</h3><details><summary>参考答案</summary><p>图形化配引脚时钟并生成初始化代码。</p></details><h3>27. SWD 几根线？</h3><details><summary>参考答案</summary><p>SWDIO/SWCLK/GND/3.3V。</p></details><h3>28. Brownout 复位？</h3><details><summary>参考答案</summary><p>供电电压过低时 MCU 复位保护。</p></details><h3>29. 上拉电阻作用？</h3><details><summary>参考答案</summary><p>为开漏/输入提供默认高电平。</p></details><h3>30. 逻辑分析仪用途？</h3><details><summary>参考答案</summary><p>抓取数字时序，解码 I2C/SPI/UART。</p></details><h3>31. MQTT pub/sub？</h3><details><summary>参考答案</summary><p>发布订阅模式，解耦设备与 App。</p></details><h3>32. QoS 0/1/2 区别？</h3><details><summary>参考答案</summary><p>0 最多一次；1 至少一次；2 恰好一次。</p></details><h3>33. WiFi STA 模式？</h3><details><summary>参考答案</summary><p>Station 连接现有路由器。</p></details><h3>34. 3.3V 和 5V GPIO 能混接吗？</h3><details><summary>参考答案</summary><p>不能，5V 进 3.3V GPIO 会损坏。</p></details><h3>35. struct 和 class？</h3><details><summary>参考答案</summary><p>C 的 struct 无方法默认；C++ struct 可含方法。</p></details><h3>36. 位操作置位公式？</h3><details><summary>参考答案</summary><p>reg |= (1 << n)。</p></details><h3>37. Mem_Read I2C？</h3><details><summary>参考答案</summary><p>HAL_I2C_Mem_Read 带寄存器地址读。</p></details><h3>38. DMA 好处？</h3><details><summary>参考答案</summary><p>外设与内存直传，减 CPU 占用。</p></details><h3>39. Tickless Idle？</h3><details><summary>参考答案</summary><p>空闲时停 SysTick 进低功耗。</p></details><h3>40. Bootloader 作用？</h3><details><summary>参考答案</summary><p>上电加载/升级 App 固件。</p></details><h3>41. MISRA C？</h3><details><summary>参考答案</summary><p>汽车等安全关键领域的 C 编码规范子集。</p></details><h3>42. CoreBluetooth Central？</h3><details><summary>参考答案</summary><p>iPhone 扫描连接外设的角色。</p></details><h3>43. NSBluetoothAlwaysUsageDescription？</h3><details><summary>参考答案</summary><p>iOS 蓝牙权限说明，必填。</p></details><h3>44. SmartConfig 是什么？</h3><details><summary>参考答案</summary><p>手机通过 Wi-Fi 编码广播 SSID 给 ESP。</p></details><h3>45. CocoaMQTT 用途？</h3><details><summary>参考答案</summary><p>iOS MQTT 客户端库。</p></details><h3>46. HomeKit 门槛？</h3><details><summary>参考答案</summary><p>MFi 认证，门槛高于自建 BLE。</p></details><h3>47. Edge AI on MCU？</h3><details><summary>参考答案</summary><p>TinyML 在 MCU 跑推理，如唤醒词。</p></details><h3>48. Matter 协议？</h3><details><summary>参考答案</summary><p>智能家居互操作标准，基于 IP。</p></details><h3>49. Resume 嵌入式项目怎么写？</h3><details><summary>参考答案</summary><p>量化：独立完成固件+App，写了什么协议，解决什么 bug。</p></details><h3>50. 如何排查 HardFault？</h3><details><summary>参考答案</summary><p>看 LR/PC，查 CFSR/HFSR，用 GDB 反汇编。</p></details>
<h2>3. 高频考点</h2>
<table><thead><tr><th>考点</th><th>频率</th></tr></thead><tbody><tr><td>中断与优先级</td><td>极高</td></tr><tr><td>I2C/SPI/UART</td><td>高</td></tr><tr><td>指针/volatile</td><td>高</td></tr><tr><td>FreeRTOS IPC</td><td>中高</td></tr></tbody></table>
<div class="tip-box">💡 理解+项目例子>死记硬背。</div>
<h2>常见问题</h2>
<h3>50题全背?</h3><p>不必，理解为主。</p>
<h3>不会怎么办?</h3><p>诚实+学习意愿+相关经验。</p>
<h3>手写代码?</h3><p>可能让写 GPIO/队列伪代码。</p>
<h2>本章小结</h2><ul>
<li>50题含details答案</li>
<li>覆盖基础高频</li>
<li>结合项目举例</li>
<li>诚实应对</li>
</ul>
<p><strong>下一步：</strong> <a href="02-进阶与iOS联动30题.html">02-进阶30题</a></p>""",
    ),
    "面试题/02-进阶与iOS联动30题.html": chapter(
        '面试题 02：进阶与 iOS 联动 30 题',
        '面试题',
        '面试题',
        """<blockquote><p>学习目标：30 道进阶+ iOS 联动面试题含答案，RTOS/OTA/BLE/MQTT/全栈。</p></blockquote><hr>
<table><thead><tr><th>要点</th><th>说明</th></tr></thead><tbody><tr><td>实验</td><td>DevKit 验证</td></tr><tr><td>调试</td><td>串口 printf</td></tr></tbody></table>
<h2>1. 说明</h2>
<p>中高级与智能硬件全栈岗。每题准备：原理+项目例子+踩坑。</p>
<h2>2. 题目与答案</h2>
<h3>1. FreeRTOS 优先级反转及解决？</h3><details><summary>参考答案</summary><p>低优先级持 Mutex 时高优先级等待；用优先级继承 Mutex。</p></details><h3>2. xQueueSendFromISR 注意？</h3><details><summary>参考答案</summary><p>仅 ISR 内用，可能触发 yield。</p></details><h3>3. ESP32 双核如何分工？</h3><details><summary>参考答案</summary><p>PRO 常跑 Wi-Fi/BT 协议栈，APP 跑用户代码。</p></details><h3>4. NimBLE vs Bluedroid？</h3><details><summary>参考答案</summary><p>NimBLE 省 RAM，IDF 5 默认推荐。</p></details><h3>5. TLS 证书校验 OTA？</h3><details><summary>参考答案</summary><p>HTTPS OTA 验证 server 证书或 embed 公钥。</p></details><h3>6. Tickless 配置项？</h3><details><summary>参考答案</summary><p>configUSE_TICKLESS_IDLE 及 portSUPPRESS_TICKS。</p></details><h3>7. JTAG 和 SWD？</h3><details><summary>参考答案</summary><p>SWD 是 ARM 2线调试接口，JTAG 4/5 线更通用。</p></details><h3>8. Mem manage heap_4？</h3><details><summary>参考答案</summary><p>FreeRTOS 带合并的 heap 算法。</p></details><h3>9. ADC DMA 双缓冲？</h3><details><summary>参考答案</summary><p>半完成/全完成回调交替处理，无丢失。</p></details><h3>10. Modbus CRC 计算？</h3><details><summary>参考答案</summary><p>RTU 帧尾 16 位 CRC，低字节在前。</p></details><h3>11. CAN 扩展帧？</h3><details><summary>参考答案</summary><p>29 位 ID vs 标准 11 位。</p></details><h3>12. BLE 配对 vs 绑定？</h3><details><summary>参考答案</summary><p>配对建立加密；绑定保存密钥下次直连。</p></details><h3>13. MTU 交换流程？</h3><details><summary>参考答案</summary><p>连接后 requestMtu，双方协商更大 payload。</p></details><h3>14. iOS 后台 BLE 限制？</h3><details><summary>参考答案</summary><p>需 bluetooth-central；扫描受限；Notify 可唤醒。</p></details><h3>15. State Restoration 场景？</h3><details><summary>参考答案</summary><p>App 被杀后系统恢复 CB 状态与连接。</p></details><h3>16. NEHotspotConfiguration？</h3><details><summary>参考答案</summary><p>iOS 帮设备连指定 Wi-Fi（能力有限）。</p></details><h3>17. MQTT retained message？</h3><details><summary>参考答案</summary><p>Broker 保留最后一条，新订阅者立即收到。</p></details><h3>18. WebSocket MQTT？</h3><details><summary>参考答案</summary><p>8884/ws 穿透某些防火墙。</p></details><h3>19. Matter 与 BLE？</h3><details><summary>参考答案</summary><p>Matter Commissioning 常用 BLE 传凭据。</p></details><h3>20. TinyML 框架？</h3><details><summary>参考答案</summary><p>TensorFlow Lite Micro、Edge Impulse。</p></details><h3>21. Rust embedded 优势？</h3><details><summary>参考答案</summary><p>内存安全、无 NULL、现代工具链。</p></details><h3>22. Functional Safety ISO 26262？</h3><details><summary>参考答案</summary><p>汽车功能安全标准。</p></details><h3>23. CE/FCC 认证？</h3><details><summary>参考答案</summary><p>欧盟/美国无线电与 EMC 合规。</p></details><h3>24. LCSC vs Digikey？</h3><details><summary>参考答案</summary><p>LCSC 国内快便宜；Digikey 全但贵。</p></details><h3>25. PCBA 代工？</h3><details><summary>参考答案</summary><p>嘉立创 PCBA 小批量贴片。</p></details><h3>26. Scope vs Logic Analyzer？</h3><details><summary>参考答案</summary><p>示波器看 analog 波形；逻辑分析仪 decode 数字协议。</p></details><h3>27. RTT 调试？</h3><details><summary>参考答案</summary><p>SEGGER Real-Time Transfer 无串口 log。</p></details><h3>28. Unit test Unity？</h3><details><summary>参考答案</summary><p>C 单元测试框架，测纯算法。</p></details><h3>29. Git submodule 固件？</h3><details><summary>参考答案</summary><p>第三方库版本锁定。</p></details><h3>30. CI for firmware？</h3><details><summary>参考答案</summary><p>PlatformIO CI 编译+静态分析+硬件在环(可选)。</p></details>
<h2>3. 回答模板</h2>
<pre><code class="language-text">是什么 → 为什么 → 项目中怎么用 → 踩过什么坑</code></pre>
<div class="tip-box">💡 项目经验比背题更能打动面试官。</div>
<h2>常见问题</h2>
<h3>iOS 岗考 MCU?</h3><p>智能硬件/IoT 岗会考。</p>
<h3>RTOS 深度?</h3><p>IPC/优先级常考。</p>
<h3>系统设计?</h3><p>可能画架构图。</p>
<h2>本章小结</h2><ul>
<li>30题进阶+iOS</li>
<li>含details答案</li>
<li>原理+项目+踩坑</li>
<li>全栈差异化</li>
</ul>""",
    ),
}
