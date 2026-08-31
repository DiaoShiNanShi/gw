"""Chapter content definitions."""

from .helpers import chapter

CHAPTERS = {
    "项目实战/01-智能台灯.html": chapter(
        '项目实战 01：智能台灯',
        '项目实战',
        '项目实战',
        """<blockquote><p>PWM 调光+BLE+App+可选 MQTT，完整 MVP。</p></blockquote><hr>
<h2>1. 功能</h2>
<table><thead><tr><th>功能</th><th>实现</th></tr></thead><tbody><tr><td>调光</td><td>LEDC PWM</td></tr><tr><td>开关</td><td>BLE Write</td></tr><tr><td>场景</td><td>App 预设</td></tr><tr><td>远程</td><td>MQTT optional</td></tr></tbody></table>
<h2>2. 硬件</h2>
<pre><code class="language-text">ESP32 + MOSFET/PWM 驱动 LED 灯带 + 5V 电源</code></pre>
<h2>3. 里程碑</h2>
<ol><li>PWM 调光验证</li><li>BLE GATT</li><li>SwiftUI App</li><li>演示视频</li></ol>
<h2>4. 简历</h2>
<p>「独立实现 ESP32 固件 + iOS CoreBluetooth 智能灯控，支持 0-100% 无级调光」</p>
<div class="tip-box">💡 GitHub + 1 分钟 demo 视频。</div>
<h2>常见问题</h2>
<h3>周期?</h3><p>3-5天 MVP。</p>
<h3>成本?</h3><p><80元。</p>
<h3>安全?</h3><p>低压 LED 无 220V。</p>
<h2>本章小结</h2><ul>
<li>PWM+BLE+App</li>
<li>MVP 里程碑</li>
<li>作品集素材</li>
<li>低压安全</li>
</ul>
<p><strong>下一步：</strong> <a href="02-远程开关.html">02-开关</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "项目实战/02-远程开关.html": chapter(
        '项目实战 02：远程开关',
        '项目实战',
        '项目实战',
        """<blockquote><p>继电器+MQTT+App，云端控制家电（合规模块）。</p></blockquote><hr>
<table><thead><tr><th>要点</th><th>说明</th></tr></thead><tbody><tr><td>实验</td><td>DevKit 验证</td></tr><tr><td>调试</td><td>串口 printf</td></tr></tbody></table>
<h2>1. 功能</h2>
<p>App/MQTT 发 ON/OFF → ESP32 GPIO → 继电器 → 负载。</p>
<h2>2. 状态回传</h2>
<pre><code class="language-text">publish home/switch/1/status ON
subscribe home/switch/1/cmd</code></pre>
<h2>3. 安全</h2>
<p>220V 用现成合规模块；原型用 5V 风扇/demo 灯。</p>
<h2>4. OTA</h2>
<p>加入 HTTP OTA 字段升级能力。</p>
<div class="tip-box">💡 强电务必合规，副业不接无 CE/3C 风险的量产强电。</div>
<div class="tip-box" style="border-color:#ff6b6b;background:rgba(255,107,107,.08)">⚠️ 220V 必须合规范模块。</div>
<h2>常见问题</h2>
<h3>反馈?</h3><p>读继电器辅助触点/电流传感器。</p>
<h3>掉电记忆?</h3><p>NVS 存最后状态。</p>
<h3>本地按钮?</h3><p>GPIO 中断双控。</p>
<h2>本章小结</h2><ul>
<li>MQTT 远程控</li>
<li>状态回传</li>
<li>强电合规</li>
<li>NVS 记忆</li>
</ul>
<p><strong>下一步：</strong> <a href="03-环境监测.html">03-环境</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "项目实战/03-环境监测.html": chapter(
        '项目实战 03：环境监测',
        '项目实战',
        '项目实战',
        """<blockquote><p>温湿度+光照+MQTT+App 图表。</p></blockquote><hr>
<table><thead><tr><th>要点</th><th>说明</th></tr></thead><tbody><tr><td>实验</td><td>DevKit 验证</td></tr><tr><td>调试</td><td>串口 printf</td></tr></tbody></table>
<h2>1. 传感器</h2>
<p>BME280(I2C) + BH1750 光照，每 30s 上报。</p>
<h2>2. 数据</h2>
<pre><code class="language-json">{"device":"env1","temp":25.3,"humi":60,"lux":320,"ts":1699999999}</code></pre>
<h2>3. App</h2>
<p>SwiftUI Charts 展示历史；阈值推送 Local Notification。</p>
<h2>4. 深度</h2>
<p>加 Deep Sleep 电池版；云端 InfluxDB 存时序。</p>
<div class="tip-box">💡 JSON schema 固件 App 统一。</div>
<h2>常见问题</h2>
<h3>校准?</h3><p>与标准计对比。</p>
<h3>离线?</h3><p>本地 SD/SPIFFS 缓存。</p>
<h3>多房间?</h3><p>device_id 区分。</p>
<h2>本章小结</h2><ul>
<li>多传感器采集</li>
<li>MQTT JSON</li>
<li>App Charts</li>
<li>可扩展睡眠版</li>
</ul>
<p><strong>下一步：</strong> <a href="04-蓝牙小车.html">04-小车</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "项目实战/04-蓝牙小车.html": chapter(
        '项目实战 04：蓝牙小车',
        '项目实战',
        '项目实战',
        """<blockquote><p>L298N 电机+BLE 方向控制，JoyStick UI。</p></blockquote><hr>
<table><thead><tr><th>要点</th><th>说明</th></tr></thead><tbody><tr><td>实验</td><td>DevKit 验证</td></tr><tr><td>调试</td><td>串口 printf</td></tr></tbody></table>
<h2>1. 硬件</h2>
<pre><code class="language-text">ESP32/STM32 + L298N + 2DC电机 + 电池</code></pre>
<h2>2. 协议</h2>
<pre><code class="language-text">Char 0x01: [left_pwm, right_pwm] int8 -100~100</code></pre>
<h2>3. App</h2>
<p>SwiftUI Joystick → BLE write 20Hz；dead zone 防 drift。</p>
<h2>4. 安全</h2>
<p>超时 500ms 无指令自动停车。</p>
<div class="tip-box">💡 电机干扰大，电源电容+去耦；BLE 天线远离电机。</div>
<h2>常见问题</h2>
<h3>PID?</h3><p>循迹进阶。</p>
<h3>Wi-Fi 版?</h3><p>MQTT 远控但延迟大。</p>
<h3>电池?</h3><p>2S LiPo+保护。</p>
<h2>本章小结</h2><ul>
<li>BLE 低延迟控车</li>
<li>Joystick UI</li>
<li>超时停车</li>
<li>电源去耦</li>
</ul>
<p><strong>下一步：</strong> <a href="05-农业IoT.html">05-农业</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "项目实战/05-农业IoT.html": chapter(
        '项目实战 05：农业 IoT',
        '项目实战',
        '项目实战',
        """<blockquote><p>土壤湿度+自动灌溉+太阳能+LoRa可选。</p></blockquote><hr>
<table><thead><tr><th>要点</th><th>说明</th></tr></thead><tbody><tr><td>实验</td><td>DevKit 验证</td></tr><tr><td>调试</td><td>串口 printf</td></tr></tbody></table>
<pre><code class="language-c">// 本章配套：在 DevKit 上验证所学概念
void setup() { Serial.begin(115200); }
void loop() { /* 实验代码 */ }</code></pre>
<h2>1. 传感</h2>
<p>电容式土壤湿度 + DS18B20 水温；避免 corrosion 用电容式。</p>
<h2>2. 控制</h2>
<p>继电器控水泵；阈值 hysteresis 防频繁启停。</p>
<h2>3. 供电</h2>
<p>太阳能板 + LiFePO4 + MPPT 模块；Deep Sleep 间隔采样。</p>
<h2>4. 云</h2>
<p>MQTT 上报 + App 远程手动浇；本地 OLED 显示状态。</p>
<div class="tip-box">💡 农业项目政府补贴多，作品集可接政企单。</div>
<h2>常见问题</h2>
<h3>电阻式腐蚀?</h3><p>换电容式。</p>
<h3>LoRa?</h3><p>远距无 Wi-Fi 场景。</p>
<h3>防水?</h3><p>IP65 外壳。</p>
<h2>本章小结</h2><ul>
<li>土壤+灌溉逻辑</li>
<li>太阳能供电</li>
<li>MQTT 远程</li>
<li>政企项目方向</li>
</ul>
<p><strong>下一步：</strong> <a href="06-工业采集.html">06-工业</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "项目实战/06-工业采集.html": chapter(
        '项目实战 06：工业采集',
        '项目实战',
        '项目实战',
        """<blockquote><p>Modbus RS485 读 PLC/传感器，MQTT 上云。</p></blockquote><hr>
<table><thead><tr><th>要点</th><th>说明</th></tr></thead><tbody><tr><td>实验</td><td>DevKit 验证</td></tr><tr><td>调试</td><td>串口 printf</td></tr></tbody></table>
<h2>1. 硬件</h2>
<pre><code class="language-text">STM32/ESP32 + MAX485 + RS485 总线</code></pre>
<h2>2. Modbus</h2>
<pre><code class="language-c">// 读保持寄存器 0x0000 长度1
uint8_t req[]={0x01,0x03,0x00,0x00,0x00,0x01,CRC_L,CRC_H};</code></pre>
<h2>3. 网关</h2>
<p>轮询多个从站 → 聚合 JSON → MQTT publish。</p>
<h2>4. 可靠</h2>
<p>看门狗+重连+本地 SD 断网缓存。</p>
<div class="tip-box">💡 工业项目单价高，需稳定 7×24。</div>
<h2>常见问题</h2>
<h3>CRC?</h3><p>Modbus RTU 必须。</p>
<h3>终端电阻?</h3><p>485 两端120Ω。</p>
<h3>隔离?</h3><p>工业用隔离 485。</p>
<h2>本章小结</h2><ul>
<li>Modbus 采集网关</li>
<li>485 硬件</li>
<li>MQTT 上云</li>
<li>工业级可靠性</li>
</ul>
<p><strong>下一步：</strong> <a href="../应用场景/01-行业应用全景.html">应用 01</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
}
