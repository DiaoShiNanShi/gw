"""Chapter content definitions."""

from .helpers import chapter

CHAPTERS = {
    "协议/01-UART详解.html": chapter(
        '协议 01：UART 详解',
        '协议模块',
        '协议',
        """<blockquote><p>UART 帧格式、波特率、接线、ESP32/STM32 收发。</p></blockquote><hr>
<h2>1. 基础</h2>
<table><thead><tr><th>参数</th><th>典型值</th></tr></thead><tbody><tr><td>波特率</td><td>115200</td></tr><tr><td>数据位</td><td>8</td></tr><tr><td>停止位</td><td>1</td></tr><tr><td>校验</td><td>None</td></tr></tbody></table>
<h2>2. 接线</h2>
<pre><code class="language-text">MCU TX → 模块 RX
MCU RX → 模块 TX
GND 必须共地</code></pre>
<h2>3. ESP32 代码</h2>
<pre><code class="language-c">Serial.begin(115200);
Serial.printf("Chip: %s\\n", ESP.getChipModel());
while(Serial.available()) {
  char c = Serial.read();
  Serial.write(c); // echo
}</code></pre>
<h2>4. 应用</h2>
<p>调试 NSLog 级、GPS NMEA、蓝牙 AT 指令、Modbus RTU 物理层。</p>
<div class="tip-box">💡 TX/RX 交叉，必须共 GND。</div>
<h2>常见问题</h2>
<h3>乱码?</h3><p>波特率不一致。</p>
<h3>USB-TTL?</h3><p>无 USB 的板子需要。</p>
<h3>printf 重定向?</h3><p>_write 或 HAL_UART_Transmit。</p>
<h2>本章小结</h2><ul>
<li>UART两线全双工</li>
<li>115200最常用</li>
<li>TXRX交叉共地</li>
<li>嵌入式NSLog</li>
</ul>
<p><strong>下一步：</strong> <a href="02-I2C详解.html">02-I2C</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "协议/02-I2C详解.html": chapter(
        '协议 02：I2C 详解',
        '协议模块',
        '协议',
        """<blockquote><p>I2C 时序、地址、开漏上拉、OLED 驱动。</p></blockquote><hr>
<h2>1. 时序</h2>
<p>START → 7位地址+W/R → ACK → 数据字节 → ACK → STOP</p>
<h2>2. 参数</h2>
<table><thead><tr><th>项</th><th>值</th></tr></thead><tbody><tr><td>标准速率</td><td>100kHz</td></tr><tr><td>快速</td><td>400kHz</td></tr><tr><td>地址</td><td>7位(0x03C OLED)</td></tr><tr><td>上拉</td><td>4.7kΩ</td></tr></tbody></table>
<h2>3. 扫描代码</h2>
<pre><code class="language-c">Wire.begin(21,22);
for(byte a=1;a<127;a++){
  Wire.beginTransmission(a);
  if(!Wire.endTransmission()) Serial.printf("0x%02X\\n",a);
}</code></pre>
<h2>4. OLED 初始化</h2>
<pre><code class="language-c">display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
display.clearDisplay();
display.setTextSize(1);
display.println("Hello iOS Dev");
display.display();</code></pre>
<div class="tip-box">💡 开漏+上拉，多设备共 SDA/SCL。</div>
<h2>常见问题</h2>
<h3>无ACK?</h3><p>地址错/未上电/无上下拉。</p>
<h3>clock stretching?</h3><p>从机拉低SCL等待。</p>
<h3>3.3V 5V?</h3><p>需电平转换。</p>
<h2>本章小结</h2><ul>
<li>I2C两线多主</li>
<li>开漏必须上拉</li>
<li>7位地址查手册</li>
<li>扫描找设备</li>
</ul>
<p><strong>下一步：</strong> <a href="03-SPI详解.html">03-SPI</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "协议/03-SPI详解.html": chapter(
        '协议 03：SPI 详解',
        '协议模块',
        '协议',
        """<blockquote><p>SPI 四线、模式 CPOL/CPHA、CS 片选、Flash 驱动。</p></blockquote><hr>
<h2>1. 信号</h2>
<table><thead><tr><th>线</th><th>方向</th><th>作用</th></tr></thead><tbody><tr><td>MOSI</td><td>主→从</td><td>主发数据</td></tr><tr><td>MISO</td><td>从→主</td><td>从发数据</td></tr><tr><td>SCK</td><td>主→从</td><td>时钟</td></tr><tr><td>CS</td><td>主→从</td><td>片选</td></tr></tbody></table>
<h2>2. 四种模式</h2>
<table><thead><tr><th>模式</th><th>CPOL</th><th>CPHA</th></tr></thead><tbody><tr><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>1</td></tr><tr><td>2</td><td>1</td><td>0</td></tr><tr><td>3</td><td>1</td><td>1</td></tr></tbody></table>
<h2>3. 代码</h2>
<pre><code class="language-c">SPI.beginTransaction(SPISettings(1000000, MSBFIRST, SPI_MODE0));
digitalWrite(CS, LOW);
SPI.transfer(0x03); // read cmd
byte b = SPI.transfer(0xFF);
digitalWrite(CS, HIGH);</code></pre>
<h2>4. vs I2C</h2>
<table><thead><tr><th></th><th>I2C</th><th>SPI</th></tr></thead><tbody><tr><td>线数</td><td>2</td><td>4+</td></tr><tr><td>速度</td><td>慢</td><td>快</td></tr><tr><td>寻址</td><td>地址字节</td><td>CS引脚</td></tr></tbody></table>
<div class="tip-box">💡 模式必须对照 slave datasheet。</div>
<h2>常见问题</h2>
<h3>比I2C快?</h3><p>是，无地址开销。</p>
<h3>CS 作用?</h3><p>多设备独立片选。</p>
<h3>3线SPI?</h3><p>无MISO只写。</p>
<h2>本章小结</h2><ul>
<li>SPI四线全双工</li>
<li>CPOL/CPHA看手册</li>
<li>CS选设备</li>
<li>Flash/屏常用</li>
</ul>
<p><strong>下一步：</strong> <a href="04-CAN总线入门.html">04-CAN</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "协议/04-CAN总线入门.html": chapter(
        '协议 04：CAN 总线入门',
        '协议模块',
        '协议',
        """<blockquote><p>CAN 帧、仲裁、终端电阻、汽车工控。</p></blockquote><hr>
<h2>1. 特点</h2>
<p>差分总线 CAN_H/CAN_L，多主，抗干扰，传输距离远。汽车/工控标准。</p>
<h2>2. 标准帧</h2>
<table><thead><tr><th>场</th><th>说明</th></tr></thead><tbody><tr><td>ID</td><td>11位优先级仲裁</td></tr><tr><td>DLC</td><td>0-8字节</td></tr><tr><td>Data</td><td> payload</td></tr><tr><td>CRC</td><td>校验</td></tr></tbody></table>
<h2>3. 硬件</h2>
<pre><code class="language-text">MCU CAN_TX/RX → TJA1050 收发器 → CAN_H/CAN_L
总线两端各120Ω终端电阻</code></pre>
<h2>4. STM32</h2>
<p>bxCAN/FDCAN 外设 + 外部收发器。ID 越小优先级越高。</p>
<div class="tip-box">💡 终端电阻缺一会反射导致通信失败。</div>
<h2>常见问题</h2>
<h3>和UART?</h3><p>CAN多主差分远距。</p>
<h3>120Ω?</h3><p>总线两端各一个。</p>
<h3>CAN FD?</h3><p>更高速率更多数据。</p>
<h2>本章小结</h2><ul>
<li>CAN汽车工控标准</li>
<li>差分抗干扰</li>
<li>终端120Ω</li>
<li>ID仲裁优先级</li>
</ul>
<p><strong>下一步：</strong> <a href="05-Modbus协议.html">05-Modbus</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "协议/05-Modbus协议.html": chapter(
        '协议 05：Modbus 协议',
        '协议模块',
        '协议',
        """<blockquote><p>Modbus RTU/TCP、功能码、工业传感器。</p></blockquote><hr>
<h2>1. 类型</h2>
<table><thead><tr><th>类型</th><th>物理层</th></tr></thead><tbody><tr><td>RTU</td><td>RS485/UART</td></tr><tr><td>TCP</td><td>以太网</td></tr><tr><td>ASCII</td><td>少见</td></tr></tbody></table>
<h2>2. 功能码</h2>
<table><thead><tr><th>码</th><th>含义</th></tr></thead><tbody><tr><td>03</td><td>读保持寄存器</td></tr><tr><td>06</td><td>写单寄存器</td></tr><tr><td>16</td><td>写多寄存器</td></tr></tbody></table>
<h2>3. RTU 帧</h2>
<pre><code class="language-text">[地址1B][功能码1B][起始2B][数量2B][CRC2B]
例: 01 03 00 00 00 01 CRC</code></pre>
<h2>4. 工具</h2>
<p>Modbus Poll/Slave 调试；libmodbus 开源库；工控 PLC 标配。</p>
<div class="tip-box">💡 CRC 小端，寄存器地址查设备手册。</div>
<h2>常见问题</h2>
<h3>RTU vs TCP?</h3><p>RTU串口485，TCP网口。</p>
<h3>免费库?</h3><p>libmodbus。</p>
<h3>和MQTT?</h3><p>Modbus工控现场，MQTT上云。</p>
<h2>本章小结</h2><ul>
<li>Modbus工业标准</li>
<li>RTU用RS485</li>
<li>功能码读写寄存器</li>
<li>工控传感器常见</li>
</ul>
<p><strong>下一步：</strong> <a href="06-BLE协议栈.html">06-BLE</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "协议/06-BLE协议栈.html": chapter(
        '协议 06：BLE 协议栈',
        '协议模块',
        '协议',
        """<blockquote><p>GAP/GATT、广播连接、Service/Characteristic、MTU。</p></blockquote><hr>
<h2>1. 角色</h2>
<table><thead><tr><th>角色</th><th>设备</th><th>iOS API</th></tr></thead><tbody><tr><td>Central</td><td>手机</td><td>CBCentralManager</td></tr><tr><td>Peripheral</td><td>ESP32</td><td>CBPeripheralManager(少见)</td></tr></tbody></table>
<h2>2. GATT 层次</h2>
<pre><code class="language-text">Profile → Service(0x180F Battery) → Characteristic(0x2A19 Level) → Descriptor</code></pre>
<h2>3. 连接流程</h2>
<ol><li>Peripheral 广播</li><li>Central 扫描</li><li>connect</li><li>discoverServices</li><li>read/write/notify</li></ol>
<h2>4. ESP32 NimBLE</h2>
<pre><code class="language-c">NimBLEDevice::init("MyLamp");
NimBLEService *svc = server->createService(SERVICE_UUID);
NimBLECharacteristic *ch = svc->createCharacteristic(CHAR_UUID, NIMBLE_PROPERTY::READ | NIMBLE_PROPERTY::NOTIFY);</code></pre>
<div class="tip-box">💡 iOS 开发者先掌握 GATT 层即可开发 90% 产品。</div>
<h2>常见问题</h2>
<h3>配对绑定?</h3><p>配对加密，绑定存LTK。</p>
<h3>Notify?</h3><p>设备主动推送，类似 WebSocket。</p>
<h3>MTU?</h3><p>协商更大包减开销。</p>
<h2>本章小结</h2><ul>
<li>Central/Peripheral</li>
<li>GATT结构清晰</li>
<li>Notify推数据</li>
<li>iOS先学GATT</li>
</ul>
<p><strong>下一步：</strong> <a href="07-WiFi与TCP.html">07-WiFi</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "协议/07-WiFi与TCP.html": chapter(
        '协议 07：WiFi 与 TCP',
        '协议模块',
        '协议',
        """<blockquote><p>STA/AP 模式、TCP/UDP Socket、ESP32 联网。</p></blockquote><hr>
<h2>1. WiFi 模式</h2>
<table><thead><tr><th>模式</th><th>用途</th></tr></thead><tbody><tr><td>STA</td><td>连路由器上网</td></tr><tr><td>AP</td><td>设备做热点</td></tr><tr><td>STA+AP</td><td>SmartConfig配网</td></tr></tbody></table>
<h2>2. TCP vs UDP</h2>
<table><thead><tr><th></th><th>TCP</th><th>UDP</th></tr></thead><tbody><tr><td>可靠</td><td>是</td><td>否</td></tr><tr><td>有序</td><td>是</td><td>否</td></tr><tr><td>场景</td><td>HTTP/MQTT</td><td>发现/mDNS</td></tr></tbody></table>
<h2>3. ESP32 STA</h2>
<pre><code class="language-c">WiFi.begin(ssid, pass);
while(WiFi.status()!=WL_CONNECTED) delay(500);
Serial.println(WiFi.localIP());</code></pre>
<h2>4. TCP Client</h2>
<pre><code class="language-c">WiFiClient client;
client.connect("192.168.1.100", 8080);
client.println("GET /status HTTP/1.0\\r\\n\\r\\n");</code></pre>
<div class="tip-box">💡 ESP32 多数仅 2.4GHz。</div>
<h2>常见问题</h2>
<h3>2.4G only?</h3><p>ESP32经典款是。</p>
<h3>断线?</h3><p>loop检查WiFi.status重连。</p>
<h3>静态IP?</h3><p>WiFi.config。</p>
<h2>本章小结</h2><ul>
<li>STA连路由AP配网</li>
<li>TCP可靠UDP快</li>
<li>WiFi.status监测</li>
<li>Socket类似URLSession</li>
</ul>
<p><strong>下一步：</strong> <a href="08-MQTT协议.html">08-MQTT</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "协议/08-MQTT协议.html": chapter(
        '协议 08：MQTT 协议',
        '协议模块',
        '协议',
        """<blockquote><p>pub/sub、QoS、主题设计、ESP32+iOS 三方。</p></blockquote><hr>
<h2>1. 模型</h2>
<pre><code class="language-text">ESP32 --publish--> Broker <--subscribe-- iOS App
                <--publish---        ---subscribe--> ESP32</code></pre>
<h2>2. QoS</h2>
<table><thead><tr><th>级别</th><th>语义</th></tr></thead><tbody><tr><td>0</td><td>最多一次</td></tr><tr><td>1</td><td>至少一次</td></tr><tr><td>2</td><td>恰好一次</td></tr></tbody></table>
<h2>3. 主题设计</h2>
<pre><code class="language-text">home/{device_id}/sensor/temp
home/{device_id}/cmd/power
home/{device_id}/status/online</code></pre>
<h2>4. 库</h2>
<table><thead><tr><th>端</th><th>库</th></tr></thead><tbody><tr><td>ESP32</td><td>PubSubClient/async_mqtt</td></tr><tr><td>iOS</td><td>CocoaMQTT/Native MQTT5</td></tr><tr><td>Broker</td><td>EMQX/Mosquitto</td></tr></tbody></table>
<div class="tip-box">💡 生产环境 MQTT 必须 TLS。</div>
<h2>常见问题</h2>
<h3>自建Broker?</h3><p>开发用EMQX Docker。</p>
<h3>vs HTTP?</h3><p>MQTT轻量长连接pub/sub。</p>
<h3> retained?</h3><p>Broker保留最后一条。</p>
<h2>本章小结</h2><ul>
<li>pub/sub解耦</li>
<li>QoS1常用</li>
<li>主题分层设计</li>
<li>MCU+Broker+App</li>
</ul>
<p><strong>下一步：</strong> <a href="../入门实战/01-第一个程序点灯.html">入门实战</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
}
