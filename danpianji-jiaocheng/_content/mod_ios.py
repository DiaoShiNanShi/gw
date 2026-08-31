"""Chapter content definitions."""

from .helpers import chapter

CHAPTERS = {
    "iOS联动/01-BLE基础.html": chapter(
        'iOS 联动 01：BLE 基础',
        'iOS 联动',
        'iOS联动',
        """<blockquote><p>GAP/GATT 回顾，Central/Peripheral，与 MCU 分工。</p></blockquote><hr>
<table><thead><tr><th>要点</th><th>说明</th></tr></thead><tbody><tr><td>实验</td><td>DevKit 验证</td></tr><tr><td>调试</td><td>串口 printf</td></tr></tbody></table>
<h2>1. 架构</h2>
<pre><code class="language-text">ESP32 Peripheral 广播 → iPhone Central 扫描连接 → GATT 读写</code></pre>
<h2>2. 权限</h2>
<pre><code class="language-xml"><key>NSBluetoothAlwaysUsageDescription</key>
<string>用于连接智能灯</string></code></pre>
<h2>3. 状态机</h2>
<p>poweredOn → scan → connect → discoverServices → discoverCharacteristics → subscribe notify。</p>
<h2>4. 分工</h2>
<p>MCU 实现 GATT Server；iOS 做 Client UI —— 你熟悉的一侧。</p>
<div class="tip-box">💡 真机调试，模拟器无 BLE。</div>
<h2>常见问题</h2>
<h3>扫不到?</h3><p>UUID/名称/权限/广播间隔。</p>
<h3>后台?</h3><p>bluetooth-central background mode。</p>
<h3>Android?</h3><p>权限模型不同。</p>
<h2>本章小结</h2><ul>
<li>Central/Peripheral 角色</li>
<li>Info.plist 权限</li>
<li>GATT 发现流程</li>
<li>MCU 做 Peripheral</li>
</ul>
<p><strong>下一步：</strong> <a href="02-CoreBluetooth实战.html">02-CB实战</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "iOS联动/02-CoreBluetooth实战.html": chapter(
        'iOS 联动 02：CoreBluetooth 实战',
        'iOS 联动',
        'iOS联动',
        """<blockquote><p>CBManager/CBPeripheral，读写 Notify 完整 Swift 代码。</p></blockquote><hr>
<table><thead><tr><th>要点</th><th>说明</th></tr></thead><tbody><tr><td>实验</td><td>DevKit 验证</td></tr><tr><td>调试</td><td>串口 printf</td></tr></tbody></table>
<h2>1. Central</h2>
<pre><code class="language-swift">class BLEManager: NSObject, CBCentralManagerDelegate {
  var central: CBCentralManager!
  override init() { central = CBCentralManager(delegate: self, queue: .main) }
  func centralManagerDidUpdateState(_ c: CBCentralManager) {
    if c.state == .poweredOn { c.scanForPeripherals(withServices: [svcUUID]) }
  }
}</code></pre>
<h2>2. 连接读写</h2>
<pre><code class="language-swift">func peripheral(_ p: CBPeripheral, didDiscoverCharacteristicsFor s: CBService, error: Error?) {
  for ch in s.characteristics ?? [] {
    if ch.properties.contains(.notify) { p.setNotifyValue(true, for: ch) }
  }
}
func peripheral(_ p: CBPeripheral, didUpdateValueFor ch: CBCharacteristic, error: Error?) {
  print(ch.value as Any)
}</code></pre>
<h2>3. 写控制</h2>
<pre><code class="language-swift">peripheral.writeValue(Data([0x01]), for: powerChar, type: .withResponse)</code></pre>
<h2>4. MVVM</h2>
<p>LampViewModel 持有 BLEManager，@Published 驱动 SwiftUI。</p>
<div class="tip-box">💡 Retain peripheral 引用，别被 ARC 释放。</div>
<h2>常见问题</h2>
<h3>didDisconnect?</h3><p>自动 reconnect 策略。</p>
<h3>withResponse?</h3><p>可靠写，慢；without 快。</p>
<h3>MTU?</h3><p>maximumWriteValueLength。</p>
<h2>本章小结</h2><ul>
<li>CBCentralManager 状态机</li>
<li>discover+notify</li>
<li>writeValue 控制</li>
<li>MVVM 绑定 UI</li>
</ul>
<p><strong>下一步：</strong> <a href="03-WiFi配网.html">03-配网</a></p>""",
    ),
    "iOS联动/03-WiFi配网.html": chapter(
        'iOS 联动 03：WiFi 配网',
        'iOS 联动',
        'iOS联动',
        """<blockquote><p>Captive Portal、SmartConfig、BLE 传凭据。</p></blockquote><hr>
<table><thead><tr><th>要点</th><th>说明</th></tr></thead><tbody><tr><td>实验</td><td>DevKit 验证</td></tr><tr><td>调试</td><td>串口 printf</td></tr></tbody></table>
<h2>1. Captive Portal</h2>
<p>连 ESP AP → 自动弹 WebView 填 SSID/密码 → POST 保存。</p>
<h2>2. BLE 配网</h2>
<pre><code class="language-swift">// 写 Wi-Fi 凭据 Characteristic
let payload = ssid.data(using:.utf8)! + pass.data(using:.utf8)!
peripheral.writeValue(payload, for: wifiProvChar, type: .withResponse)</code></pre>
<h2>3. iOS 14+ 本地网</h2>
<pre><code class="language-xml"><key>NSLocalNetworkUsageDescription</key>
<string>发现局域网设备</string></code></pre>
<h2>4. UX</h2>
<ol><li>引导开蓝牙</li><li>扫描设备</li><li>选 Wi-Fi（NEHotspotConfiguration 可选）</li><li>成功反馈</li></ol>
<div class="tip-box">💡 配网失败率产品最大吐槽点之一。</div>
<h2>常见问题</h2>
<h3>Hotspot Config?</h3><p>NEHotspotConfiguration 帮连 Wi-Fi。</p>
<h3>ESP-Touch?</h3><p>乐鑫 SmartConfig App。</p>
<h3>企业 Wi-Fi?</h3><p>802.1X 复杂。</p>
<h2>本章小结</h2><ul>
<li>Captive Portal 常见</li>
<li>BLE 传凭据</li>
<li>本地网络权限</li>
<li>UX 引导关键</li>
</ul>
<p><strong>下一步：</strong> <a href="04-MQTT-App端.html">04-MQTT App</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "iOS联动/04-MQTT-App端.html": chapter(
        'iOS 联动 04：MQTT App 端',
        'iOS 联动',
        'iOS联动',
        """<blockquote><p>CocoaMQTT 订阅主题，远程控灯，JSON  payload。</p></blockquote><hr>
<table><thead><tr><th>要点</th><th>说明</th></tr></thead><tbody><tr><td>实验</td><td>DevKit 验证</td></tr><tr><td>调试</td><td>串口 printf</td></tr></tbody></table>
<h2>1. 连接</h2>
<pre><code class="language-swift">import CocoaMQTT
let mqtt = CocoaMQTT(clientID: "ios-\\(UUID().uuidString)", host: "broker.emqx.io", port: 1883)
mqtt.connect()</code></pre>
<h2>2. 订阅发布</h2>
<pre><code class="language-swift">mqtt.subscribe("home/lamp/+/status")
mqtt.publish(CocoaMQTTMessage(topic: "home/lamp/1/cmd", string: "ON"))</code></pre>
<h2>3. 架构</h2>
<pre><code class="language-text">ESP32 pub sensor → Broker → iOS sub 显示
iOS pub cmd → Broker → ESP32 sub 执行</code></pre>
<h2>4. TLS</h2>
<p>8883 端口 + 证书 pinning 生产必备。</p>
<div class="tip-box">💡 clientID 唯一，clean session 看场景。</div>
<h2>常见问题</h2>
<h3>QoS?</h3><p>1 常用。</p>
<h3> retained?</h3><p>上线收最后状态。</p>
<h3>WebSocket MQTT?</h3><p>8884/ws 穿防火墙。</p>
<h2>本章小结</h2><ul>
<li>CocoaMQTT 连接</li>
<li>pub/sub 主题</li>
<li>JSON 协议约定</li>
<li>TLS 生产必须</li>
</ul>
<p><strong>下一步：</strong> <a href="05-全栈架构.html">05-全栈</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "iOS联动/05-全栈架构.html": chapter(
        'iOS 联动 05：全栈架构',
        'iOS 联动',
        'iOS联动',
        """<blockquote><p>MCU+App+云+OTA 架构图，模块边界，协议设计。</p></blockquote><hr>
<h2>1. 四层</h2>
<pre><code class="language-text">Device(Firmware) → Connectivity(BLE/MQTT) → Cloud(Broker/API) → App(SwiftUI)</code></pre>
<h2>2. 协议</h2>
<table><thead><tr><th>通道</th><th>协议</th><th>数据</th></tr></thead><tbody><tr><td>近场</td><td>BLE GATT</td><td>实时控灯</td></tr><tr><td>远程</td><td>MQTT</td><td>状态/sync</td></tr><tr><td>配网</td><td>HTTP/BLE</td><td>凭据</td></tr><tr><td>升级</td><td>HTTPS OTA</td><td>固件.bin</td></tr></tbody></table>
<h2>3. 模块</h2>
<p>固件：BSP/HAL/App/Middleware；App：BLE/MQTT/Repository/UI。</p>
<h2>4. 版本</h2>
<p>语义化 semver；App 检查设备 fw 版本提示升级。</p>
<div class="tip-box">💡 协议文档化，固件 App 各一份 JSON schema。</div>
<h2>常见问题</h2>
<h3>自建云?</h3><p>MQTT+REST 够 MVP。</p>
<h3>HomeKit?</h3><p>MFi 门槛。</p>
<h3>多设备?</h3><p>device_id 主题隔离。</p>
<h2>本章小结</h2><ul>
<li>四层架构清晰</li>
<li>协议文档化</li>
<li>模块边界</li>
<li>版本协同 OTA</li>
</ul>
<p><strong>下一步：</strong> <a href="06-后台蓝牙.html">06-后台</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "iOS联动/06-后台蓝牙.html": chapter(
        'iOS 联动 06：后台蓝牙',
        'iOS 联动',
        'iOS联动',
        """<blockquote><p>bluetooth-central 模式，State Restoration，连接保持。</p></blockquote><hr>
<table><thead><tr><th>要点</th><th>说明</th></tr></thead><tbody><tr><td>实验</td><td>DevKit 验证</td></tr><tr><td>调试</td><td>串口 printf</td></tr></tbody></table>
<h2>1. Background Modes</h2>
<pre><code class="language-xml"><key>UIBackgroundModes</key>
<array><string>bluetooth-central</string></array></code></pre>
<h2>2. Restoration</h2>
<pre><code class="language-swift">central = CBCentralManager(delegate: self, queue: .main,
  options: [CBCentralManagerOptionRestoreIdentifierKey: "com.app.ble"])</code></pre>
<h2>3. 限制</h2>
<p>iOS 后台 BLE 可维持连接收 Notify，但扫描受限；勿期望无限后台算力。</p>
<h2>4. 策略</h2>
<p>关键事件 Notify 唤醒 App；非实时用 MQTT push。</p>
<div class="tip-box">💡 后台 BLE 耗电，产品需权衡。</div>
<h2>常见问题</h2>
<h3>willRestoreState?</h3><p>恢复 peripheral 列表。</p>
<h3>被杀?</h3><p>State restoration 重建。</p>
<h3>Android 后台?</h3><p>策略更松。</p>
<h2>本章小结</h2><ul>
<li>bluetooth-central 模式</li>
<li>State Restoration</li>
<li>Notify 唤醒</li>
<li>远程用 MQTT+Push</li>
</ul>
<p><strong>下一步：</strong> <a href="../项目实战/01-智能台灯.html">项目 01</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
}
