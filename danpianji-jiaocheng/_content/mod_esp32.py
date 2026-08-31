"""Chapter content definitions."""

from .helpers import chapter

CHAPTERS = {
    "ESP32/01-入门与STM32对比.html": chapter(
        'ESP32 01：入门与 STM32 对比',
        'ESP32 专题',
        'ESP32',
        """<blockquote><p>双核 Wi-Fi/BT，Arduino vs IDF，与 STM32 分工。</p></blockquote><hr>
<pre><code class="language-c">// 本章配套：在 DevKit 上验证所学概念
void setup() { Serial.begin(115200); }
void loop() { /* 实验代码 */ }</code></pre>
<h2>1. 架构</h2>
<table><thead><tr><th>组件</th><th>说明</th></tr></thead><tbody><tr><td>PRO CPU</td><td>协议栈/Wi-Fi</td></tr><tr><td>APP CPU</td><td>用户代码</td></tr><tr><td>NVS</td><td>配置存储</td></tr><tr><td>RTC</td><td>Deep Sleep</td></tr></tbody></table>
<h2>2. vs STM32</h2>
<table><thead><tr><th></th><th>ESP32</th><th>STM32</th></tr></thead><tbody><tr><td>联网</td><td>内置Wi-Fi/BLE</td><td>需外接模块</td></tr><tr><td>实时</td><td>较弱</td><td>强</td></tr><tr><td>生态</td><td>Arduino/IDF</td><td>CubeMX/HAL</td></tr><tr><td>场景</td><td>IoT 原型</td><td>工业控制</td></tr></tbody></table>
<h2>3. 框架</h2>
<p>原型 Arduino 快；量产 ESP-IDF（FreeRTOS 原生、低功耗全）。</p>
<h2>4. 分工</h2>
<p>典型产品：STM32 控电机传感器 + ESP32 负责联网 —— 或单 ESP32 全包。</p>
<div class="tip-box">💡 IoT+iOS 优先 ESP32；工业实时选 STM32。</div>
<h2>常见问题</h2>
<h3>Arduino vs IDF?</h3><p>快 vs 全。</p>
<h3>双核?</h3><p>Wi-Fi 占一核，用户另一核。</p>
<h3>GPIO 少?</h3><p>扩展 I2C GPIO 芯片。</p>
<h2>本章小结</h2><ul>
<li>ESP32 联网强</li>
<li>双核 Wi-Fi/BT</li>
<li>Arduino 原型 IDF 量产</li>
<li>与 STM32 可分工</li>
</ul>
<p><strong>下一步：</strong> <a href="02-WiFi-STA与AP.html">02-WiFi</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "ESP32/02-WiFi-STA与AP.html": chapter(
        'ESP32 02：WiFi STA 与 AP',
        'ESP32 专题',
        'ESP32',
        """<blockquote><p>连路由、开热点、SmartConfig 配网思路。</p></blockquote><hr>
<table><thead><tr><th>要点</th><th>说明</th></tr></thead><tbody><tr><td>实验</td><td>DevKit 验证</td></tr><tr><td>调试</td><td>串口 printf</td></tr></tbody></table>
<h2>1. STA</h2>
<pre><code class="language-c">WiFi.mode(WIFI_STA);
WiFi.begin(ssid, pass);
while(WiFi.status()!=WL_CONNECTED) delay(500);</code></pre>
<h2>2. AP 配网</h2>
<pre><code class="language-c">WiFi.softAP("ESP32-Setup", "12345678");
// WebServer 收 ssid/pass 后切 STA</code></pre>
<h2>3. SmartConfig</h2>
<p>ESP-Touch / AirKiss 手机发 UDP 编码 SSID —— 类似声波配网。</p>
<h2>4. 重连</h2>
<pre><code class="language-c">if(WiFi.status()!=WL_CONNECTED){ WiFi.disconnect(); WiFi.begin(ssid,pass);}</code></pre>
<div class="tip-box">💡 配网 UX 决定产品第一印象，iOS 开发者优势区。</div>
<h2>常见问题</h2>
<h3>Captive Portal?</h3><p>连 AP 弹网页配网。</p>
<h3>WiFiMulti?</h3><p>保存多组凭据。</p>
<h3>mDNS?</h3><p>esp32.local 发现。</p>
<h2>本章小结</h2><ul>
<li>STA 连路由</li>
<li>AP 热点配网</li>
<li>SmartConfig 免输入</li>
<li>断线自动重连</li>
</ul>
<p><strong>下一步：</strong> <a href="03-BLE-GATT.html">03-BLE</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "ESP32/03-BLE-GATT.html": chapter(
        'ESP32 03：BLE GATT',
        'ESP32 专题',
        'ESP32',
        """<blockquote><p>NimBLE/Bluedroid，Service/Characteristic，Notify iOS。</p></blockquote><hr>
<table><thead><tr><th>要点</th><th>说明</th></tr></thead><tbody><tr><td>实验</td><td>DevKit 验证</td></tr><tr><td>调试</td><td>串口 printf</td></tr></tbody></table>
<h2>1. 初始化</h2>
<pre><code class="language-c">BLEDevice::init("SmartLamp");
BLEServer *s = BLEDevice::createServer();
BLEService *svc = s->createService(LAMP_SERVICE_UUID);</code></pre>
<h2>2. Characteristic</h2>
<pre><code class="language-c">BLECharacteristic *c = svc->createCharacteristic(POWER_UUID,
  BLECharacteristic::PROPERTY_READ | BLECharacteristic::PROPERTY_WRITE | BLECharacteristic::PROPERTY_NOTIFY);
c->setCallbacks(new LampCallbacks()); svc->start();</code></pre>
<h2>3. 广播</h2>
<pre><code class="language-c">BLEAdvertising *adv = BLEDevice::getAdvertising();
adv->addServiceUUID(LAMP_SERVICE_UUID); adv->start();</code></pre>
<h2>4. iOS 对接</h2>
<p>固定 UUID 写入 App；Notify 推状态；Write 控开关。</p>
<div class="tip-box">💡 NimBLE 比 Bluedroid 省 RAM，IDF 5 推荐。</div>
<h2>常见问题</h2>
<h3>连不上?</h3><p>广播/UUID/权限。</p>
<h3>MTU?</h3><p>517 减开销。</p>
<h3>多连接?</h3><p>参数 max connections。</p>
<h2>本章小结</h2><ul>
<li>GATT Service/Char</li>
<li>Notify 推状态</li>
<li>Write 收命令</li>
<li>UUID 与 iOS 一致</li>
</ul>
<p><strong>下一步：</strong> <a href="04-Deep-Sleep.html">04-Sleep</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "ESP32/04-Deep-Sleep.html": chapter(
        'ESP32 04：Deep Sleep',
        'ESP32 专题',
        'ESP32',
        """<blockquote><p>Light/Deep Sleep，µA 级，RTC 唤醒。</p></blockquote><hr>
<h2>1. 模式</h2>
<table><thead><tr><th>模式</th><th>功耗</th><th>唤醒</th></tr></thead><tbody><tr><td>Active</td><td>~100mA</td><td>—</td></tr><tr><td>Modem Sleep</td><td>~20mA</td><td>Wi-Fi 保连接</td></tr><tr><td>Deep Sleep</td><td>~10µA</td><td>GPIO/Timer/RTC</td></tr></tbody></table>
<h2>2. Deep Sleep</h2>
<pre><code class="language-c">esp_sleep_enable_timer_wakeup(60 * 1000000ULL); // 60s
esp_deep_sleep_start();</code></pre>
<h2>3. 数据保持</h2>
<pre><code class="language-c">RTC_DATA_ATTR int boot_count = 0; // RTC 内存保留
boot_count++;</code></pre>
<h2>4. 设计</h2>
<p>传感器节点：睡 59 分钟醒 1 分钟上报 MQTT。</p>
<div class="tip-box">💡 Deep Sleep 掉电 RAM，仅 RTC 内存保留。</div>
<h2>常见问题</h2>
<h3>Light vs Deep?</h3><p>Light 保 RAM 耗 mA。</p>
<h3>GPIO 唤醒?</h3><p>ext0/ext1。</p>
<h3>Wi-Fi 睡?</h3><p>Modem sleep 保连接。</p>
<h2>本章小结</h2><ul>
<li>Deep Sleep µA 级</li>
<li>RTC_DATA_ATTR 保留</li>
<li>定时/GPIO 唤醒</li>
<li>IoT 电池必备</li>
</ul>
<p><strong>下一步：</strong> <a href="05-NVS存储.html">05-NVS</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "ESP32/05-NVS存储.html": chapter(
        'ESP32 05：NVS 存储',
        'ESP32 专题',
        'ESP32',
        """<blockquote><p>键值对、Wear leveling、加密分区。</p></blockquote><hr>
<table><thead><tr><th>要点</th><th>说明</th></tr></thead><tbody><tr><td>实验</td><td>DevKit 验证</td></tr><tr><td>调试</td><td>串口 printf</td></tr></tbody></table>
<h2>1. IDF NVS</h2>
<pre><code class="language-c">nvs_handle_t h; nvs_open("storage", NVS_READWRITE, &h);
nvs_set_i32(h, "boot", ++count); nvs_commit(h); nvs_close(h);</code></pre>
<h2>2. Arduino Preferences</h2>
<p>封装 NVS，API 类似 UserDefaults。</p>
<h2>3. 分区</h2>
<pre><code class="language-text">nvs分区在 partition table; 可 nvs_flash_erase 恢复出厂</code></pre>
<h2>4. 加密</h2>
<p>NVS 加密需 flash 加密 + nvs_flash_secure_init。</p>
<div class="tip-box">💡 键名长度有限，namespace 规划好。</div>
<h2>常见问题</h2>
<h3>满?</h3><p>nvs_flash_erase 或换分区。</p>
<h3>字符串?</h3><p>nvs_set_str/get_str。</p>
<h3>Blob?</h3><p>nvs_set_blob 存结构体。</p>
<h2>本章小结</h2><ul>
<li>NVS=键值存储</li>
<li>Wear leveling</li>
<li>Preferences 封装</li>
<li>分区表规划</li>
</ul>
<p><strong>下一步：</strong> <a href="06-HTTP与WebServer.html">06-HTTP</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "ESP32/06-HTTP与WebServer.html": chapter(
        'ESP32 06：HTTP 与 WebServer',
        'ESP32 专题',
        'ESP32',
        """<blockquote><p>AsyncWebServer 配网页、REST API、与 URLSession 对接。</p></blockquote><hr>
<table><thead><tr><th>要点</th><th>说明</th></tr></thead><tbody><tr><td>实验</td><td>DevKit 验证</td></tr><tr><td>调试</td><td>串口 printf</td></tr></tbody></table>
<h2>1. WebServer</h2>
<pre><code class="language-c">AsyncWebServer server(80);
server.on("/api/status", HTTP_GET, [](AsyncWebServerRequest *r){
  r->send(200, "application/json", "{\\"temp\\":25.3}");
});
server.begin();</code></pre>
<h2>2. 配网页</h2>
<p>PROGMEM HTML 表单 POST /save → 写 NVS → 重启 STA。</p>
<h2>3. iOS URLSession</h2>
<pre><code class="language-swift">let url = URL(string: "http://192.168.4.1/api/status")!
URLSession.shared.dataTask(with: url) { data,_,_ in /* parse JSON */ }.resume()</code></pre>
<h2>4. HTTPS</h2>
<p>设备端 TLS 证书管理复杂；内网可用 HTTP，公网必须 TLS。</p>
<div class="tip-box">💡 AP 模式下 192.168.4.1 是常见配网地址。</div>
<h2>常见问题</h2>
<h3>Async vs sync?</h3><p>Async 不阻塞。</p>
<h3>CORS?</h3><p>App WebView 可能需。</p>
<h3>OTA HTTP?</h3><p>/update POST 固件。</p>
<h2>本章小结</h2><ul>
<li>WebServer 配网+API</li>
<li>JSON REST</li>
<li>iOS URLSession 对接</li>
<li>量产考虑 TLS</li>
</ul>
<p><strong>下一步：</strong> <a href="../进阶/01-FreeRTOS任务.html">进阶 01</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
}
