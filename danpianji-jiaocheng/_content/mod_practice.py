"""Chapter content definitions."""

from .helpers import chapter

CHAPTERS = {
    "入门实战/01-第一个程序点灯.html": chapter(
        '入门实战 01：第一个程序点灯',
        '入门实战',
        '入门实战',
        """<blockquote><p>GPIO 输出 Blink，建立烧录-运行闭环。</p></blockquote><hr>
<h2>1. 目标</h2>
<p>点亮 LED 并闪烁，串口打印确认程序运行。</p>
<h2>2. 接线</h2>
<pre><code class="language-text">ESP32 板载 LED 通常 GPIO2 或 GPIO8，查 DevKit 原理图
外接: 3.3V─220Ω─LED─GPIO</code></pre>
<h2>3. 代码</h2>
<pre><code class="language-c">#define LED 2
void setup(){ pinMode(LED,OUTPUT); Serial.begin(115200); Serial.println("start");}
void loop(){ digitalWrite(LED,HIGH); delay(500); digitalWrite(LED,LOW); delay(500);}</code></pre>
<h2>4. 排错</h2>
<table><thead><tr><th>现象</th><th>检查</th></tr></thead><tbody><tr><td>不亮</td><td>LED极性/引脚号</td></tr><tr><td>不闪</td><td>程序是否跑/看串口</td></tr><tr><td>烧录失败</td><td>端口/BOOT键</td></tr></tbody></table>
<div class="tip-box">💡 第一个里程碑：看到 LED 闪 = 闭环成立。</div>
<h2>常见问题</h2>
<h3>GPIO 选哪个?</h3><p>查 strapping 脚避免。</p>
<h3>3.3V?</h3><p>ESP32 GPIO 仅 3.3V。</p>
<h3>delay 阻塞?</h3><p>入门可用，后面用定时器。</p>
<h2>本章小结</h2><ul>
<li>点灯=Hello World</li>
<li>查原理图引脚</li>
<li>串口确认运行</li>
<li>建立烧录闭环</li>
</ul>
<p><strong>下一步：</strong> <a href="02-按键与中断.html">02-按键</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "入门实战/02-按键与中断.html": chapter(
        '入门实战 02：按键与中断',
        '入门实战',
        '入门实战',
        """<blockquote><p>INPUT_PULLUP、外部中断、防抖。</p></blockquote><hr>
<table><thead><tr><th>要点</th><th>说明</th></tr></thead><tbody><tr><td>实验</td><td>DevKit 验证</td></tr><tr><td>调试</td><td>串口 printf</td></tr></tbody></table>
<h2>1. 原理</h2>
<p>按键一端 GPIO 一端 GND，内部上拉，按下读 LOW。</p>
<h2>2. 中断代码</h2>
<pre><code class="language-c">volatile bool pressed=false;
void IRAM_ATTR isr(){ pressed=true; }
void setup(){ pinMode(15,INPUT_PULLUP); attachInterrupt(digitalPinToInterrupt(15),isr,FALLING);}
void loop(){ if(pressed){ pressed=false; delay(10); if(digitalRead(15)==LOW) Serial.println("key");}}</code></pre>
<h2>3. vs 轮询</h2>
<p>轮询浪费 CPU；中断事件驱动，类似 UIControlEvents。</p>
<h2>4. 消抖</h2>
<p>硬件 RC 或软件 delay 10ms 再确认。</p>
<div class="tip-box">💡 避开 strapping 脚 GPIO0/2/15 等。</div>
<h2>常见问题</h2>
<h3>抖动?</h3><p>delay消抖。</p>
<h3>ISR 规则?</h3><p>短、无delay。</p>
<h3>长按?</h3><p>定时器计时长。</p>
<h2>本章小结</h2><ul>
<li>上拉输入读低</li>
<li>中断事件驱动</li>
<li>ISR置标志主循环处理</li>
<li>消抖必须</li>
</ul>
<p><strong>下一步：</strong> <a href="03-串口调试.html">03-串口</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "入门实战/03-串口调试.html": chapter(
        '入门实战 03：串口调试',
        '入门实战',
        '入门实战',
        """<blockquote><p>115200 printf 调试，格式化输出传感器值。</p></blockquote><hr>
<table><thead><tr><th>要点</th><th>说明</th></tr></thead><tbody><tr><td>实验</td><td>DevKit 验证</td></tr><tr><td>调试</td><td>串口 printf</td></tr></tbody></table>
<h2>1. 初始化</h2>
<pre><code class="language-c">Serial.begin(115200);
while(!Serial) delay(10); // USB CDC 等待</code></pre>
<h2>2. 格式化</h2>
<pre><code class="language-c">Serial.printf("[%.1fs] temp=%.1f humi=%.1f\\n", millis()/1000.0, t, h);</code></pre>
<h2>3. 命令行</h2>
<pre><code class="language-c">if(Serial.available()){
  String cmd=Serial.readStringUntil('\\n');
  if(cmd=="on") digitalWrite(LED,HIGH);
}</code></pre>
<h2>4. iOS 类比</h2>
<p>Serial.printf = NSLog；串口监视器 = Xcode Console。</p>
<div class="tip-box">💡 串口是嵌入式最重要的调试手段。</div>
<h2>常见问题</h2>
<h3>乱码?</h3><p>波特率115200一致。</p>
<h3>printf 浮点?</h3><p>Arduino 需启用。</p>
<h3>太多 log?</h3><p>分级宏 DEBUG_LOG。</p>
<h2>本章小结</h2><ul>
<li>115200标准</li>
<li>printf格式化</li>
<li>可做成CLI</li>
<li>=嵌入式NSLog</li>
</ul>
<p><strong>下一步：</strong> <a href="04-PWM控制舵机.html">04-PWM</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "入门实战/04-PWM控制舵机.html": chapter(
        '入门实战 04：PWM 控制舵机',
        '入门实战',
        '入门实战',
        """<blockquote><p>50Hz PWM，脉宽 1-2ms 控制角度。</p></blockquote><hr>
<table><thead><tr><th>要点</th><th>说明</th></tr></thead><tbody><tr><td>实验</td><td>DevKit 验证</td></tr><tr><td>调试</td><td>串口 printf</td></tr></tbody></table>
<h2>1. 原理</h2>
<p>舵机靠 50Hz 方波脉宽定角度：1ms≈0°，1.5ms≈90°，2ms≈180°。</p>
<h2>2. 接线</h2>
<pre><code class="language-text">舵机: 红VCC(5V) 棕GND 橙信号→GPIO
注意: 大舵机需外接5V供电</code></pre>
<h2>3. 代码</h2>
<pre><code class="language-c">#include <ESP32Servo.h>
Servo sv; sv.attach(18); sv.write(90); // 90度
// LEDC 底层: 50Hz, duty 1.5ms</code></pre>
<h2>4. 应用</h2>
<p>云台、机械臂、智能台灯角度、阀门。</p>
<div class="tip-box">💡 舵机供电不要从 3.3V GPIO 取 5V。</div>
<div class="tip-box" style="border-color:#ff6b6b;background:rgba(255,107,107,.08)">⚠️ 大电流舵机必须外接 5V 电源共地。</div>
<h2>常见问题</h2>
<h3>抖动?</h3><p>供电不足加电容。</p>
<h3>角度不准?</h3><p>calibrate min/max pulse。</p>
<h3>多个舵机?</h3><p>LEDC 多通道。</p>
<h2>本章小结</h2><ul>
<li>50Hz脉宽控角</li>
<li>1-2ms映射0-180</li>
<li>注意5V供电</li>
<li>LEDC/PWM外设</li>
</ul>
<p><strong>下一步：</strong> <a href="05-温湿度传感器.html">05-温湿度</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "入门实战/05-温湿度传感器.html": chapter(
        '入门实战 05：温湿度传感器',
        '入门实战',
        '入门实战',
        """<blockquote><p>DHT22 单总线时序，BME280 I2C 对比。</p></blockquote><hr>
<table><thead><tr><th>要点</th><th>说明</th></tr></thead><tbody><tr><td>实验</td><td>DevKit 验证</td></tr><tr><td>调试</td><td>串口 printf</td></tr></tbody></table>
<h2>1. DHT22</h2>
<pre><code class="language-c">#include <DHT.h>
DHT dht(4, DHT22);
void setup(){ dht.begin();}
void loop(){ float t=dht.readTemperature(); float h=dht.readHumidity();
  if(isnan(t)) Serial.println("read fail"); else Serial.printf("T=%.1f H=%.1f\\n",t,h); delay(2000);}</code></pre>
<h2>2. 接线</h2>
<pre><code class="language-text">DHT: VCC GND DATA→GPIO4 + 4.7k上拉(模块自带)</code></pre>
<h2>3. BME280</h2>
<p>I2C 接口，可同时气压，精度更高，驱动更简单。</p>
<h2>4. 上云</h2>
<p>读数 → MQTT publish → iOS 图表展示，完整数据链路。</p>
<div class="tip-box">💡 DHT 时序严格，读间隔≥2s。</div>
<h2>常见问题</h2>
<h3>NaN?</h3><p>接线/上拉/时序。</p>
<h3>DHT11 vs 22?</h3><p>22精度高。</p>
<h3>校准?</h3><p>与标准温湿度计对比。</p>
<h2>本章小结</h2><ul>
<li>DHT单总线时序</li>
<li>BME280 I2C更稳</li>
<li>读间隔≥2s</li>
<li>可MQTT上云</li>
</ul>
<p><strong>下一步：</strong> <a href="06-ADC采样.html">06-ADC</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "入门实战/06-ADC采样.html": chapter(
        '入门实战 06：ADC 采样',
        '入门实战',
        '入门实战',
        """<blockquote><p>12bit ADC 读电位器，映射 PWM/亮度。</p></blockquote><hr>
<h2>1. 原理</h2>
<p>ESP32 ADC 12bit (0-4095)，STM32 通常 12bit。模拟→数字。</p>
<h2>2. 代码</h2>
<pre><code class="language-c">int raw = analogRead(34); // ADC1 通道
float volt = raw / 4095.0 * 3.3;
int brightness = map(raw, 0, 4095, 0, 255);
analogWrite(LED_PIN, brightness);</code></pre>
<h2>3. 注意</h2>
<table><thead><tr><th>项</th><th>说明</th></tr></thead><tbody><tr><td>衰减</td><td>11dB 量程0-3.3V</td></tr><tr><td>ADC2</td><td>Wi-Fi时部分不可用</td></tr><tr><td>校准</td><td>esp_adc_cal</td></tr></tbody></table>
<h2>4. 应用</h2>
旋钮调光、电池电压监测、光照强度。
<div class="tip-box">💡 ADC 引脚只能输入，不能当 GPIO 输出。</div>
<h2>常见问题</h2>
<h3>不准?</h3><p>校准/参考电压。</p>
<h3>噪声?</h3><p>软件平均多次采样。</p>
<h3>STM32?</h3><p>HAL_ADC_Start+PollForConversion。</p>
<h2>本章小结</h2><ul>
<li>12bit 0-4095</li>
<li>map映射业务值</li>
<li>注意衰减量程</li>
<li>可驱动PWM调光</li>
</ul>
<p><strong>下一步：</strong> <a href="07-OLED显示.html">07-OLED</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "入门实战/07-OLED显示.html": chapter(
        '入门实战 07：OLED 显示',
        '入门实战',
        '入门实战',
        """<blockquote><p>SSD1306 I2C 128x64，Adafruit 库显示温湿度。</p></blockquote><hr>
<table><thead><tr><th>要点</th><th>说明</th></tr></thead><tbody><tr><td>实验</td><td>DevKit 验证</td></tr><tr><td>调试</td><td>串口 printf</td></tr></tbody></table>
<h2>1. 接线</h2>
<pre><code class="language-text">OLED: VCC GND SCL SDA → GPIO22/21
I2C 地址通常 0x3C</code></pre>
<h2>2. 代码</h2>
<pre><code class="language-c">#include <Adafruit_SSD1306.h>
Adafruit_SSD1306 display(128,64,&Wire,-1);
display.begin(SSD1306_SWITCHCAPVCC,0x3C);
display.setCursor(0,0); display.printf("T:%.1fC",t); display.display();</code></pre>
<h2>3. 刷新</h2>
<p>display.display() 刷新整屏；局部刷新可优化速度。</p>
<h2>4. vs App</h2>
<p>OLED 本地 UI；复杂 UI 仍用 iOS App，OLED 做状态屏。</p>
<div class="tip-box">💡 I2C 扫描确认 0x3C/0x3D 地址。</div>
<h2>常见问题</h2>
<h3>不显示?</h3><p>地址/接线/初始化。</p>
<h3>花屏?</h3><p>复位时序/供电。</p>
<h3>中文?</h3><p>取模字库或 u8g2。</p>
<h2>本章小结</h2><ul>
<li>SSD1306 I2C</li>
<li>128x64足够状态</li>
<li>Adafruit/u8g2库</li>
<li>本地小屏UI</li>
</ul>
<p><strong>下一步：</strong> <a href="08-EEPROM存储.html">08-EEPROM</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "入门实战/08-EEPROM存储.html": chapter(
        '入门实战 08：EEPROM 存储',
        '入门实战',
        '入门实战',
        """<blockquote><p>Preferences/NVS 掉电保存计数与配置。</p></blockquote><hr>
<table><thead><tr><th>要点</th><th>说明</th></tr></thead><tbody><tr><td>实验</td><td>DevKit 验证</td></tr><tr><td>调试</td><td>串口 printf</td></tr></tbody></table>
<h2>1. 需求</h2>
<p>保存 Wi-Fi 凭据、亮度档位、累计运行时间——类似 UserDefaults。</p>
<h2>2. ESP32 Preferences</h2>
<pre><code class="language-c">Preferences p; p.begin("myapp", false);
p.putString("ssid", ssid);
p.putInt("boot", p.getInt("boot",0)+1);
String s = p.getString("ssid", "");</code></pre>
<h2>3. STM32</h2>
<p>Flash 末尾划 EEPROM 区，或外接 I2C EEPROM(24C02)。</p>
<h2>4. 寿命</h2>
<p>Flash 擦写有限(~10万次)，频繁写入需 wear leveling。</p>
<div class="tip-box">💡 键名命名规范，begin/end 成对。</div>
<h2>常见问题</h2>
<h3>和 Flash 程序?</h3><p>不同分区。</p>
<h3>清空?</h3><p>p.clear() 或 erase。</p>
<h3>加密?</h3><p>NVS 可加密分区。</p>
<h2>本章小结</h2><ul>
<li>NVS=UserDefaults</li>
<li>掉电保持</li>
<li>注意擦写寿命</li>
<li>存Wi-Fi/配置</li>
</ul>
<p><strong>下一步：</strong> <a href="09-继电器控制.html">09-继电器</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "入门实战/09-继电器控制.html": chapter(
        '入门实战 09：继电器控制',
        '入门实战',
        '入门实战',
        """<blockquote><p>低电平触发模块，MOSFET 驱动，MQTT 远程开关。</p></blockquote><hr>
<table><thead><tr><th>要点</th><th>说明</th></tr></thead><tbody><tr><td>实验</td><td>DevKit 验证</td></tr><tr><td>调试</td><td>串口 printf</td></tr></tbody></table>
<h2>1. 模块</h2>
<p>光耦隔离继电器模块：IN 接 GPIO，COM/NO/NC 接负载。多数低电平触发。</p>
<h2>2. 代码</h2>
<pre><code class="language-c">#define RELAY 26
pinMode(RELAY, OUTPUT);
digitalWrite(RELAY, LOW);  // 吸合(视模块而定)
// MQTT: if(topic.endsWith("/power")) digitalWrite(RELAY, payload=="ON"?LOW:HIGH);</code></pre>
<h2>3. 安全</h2>
<p>220V 必须用合格模块+绝缘；勿裸手碰强电。原型用 5V 灯泡/风扇。</p>
<h2>4. 续流</h2>
<p>直驱继电器线圈需并联二极管；模块已集成。</p>
<div class="tip-box">💡 强电项目找电工，勿自行冒险。</div>
<div class="tip-box" style="border-color:#ff6b6b;background:rgba(255,107,107,.08)">⚠️ 220V 必须用合规范模块，里程碑付款前做安全评审。</div>
<h2>常见问题</h2>
<h3>低电平触发?</h3><p>看模块说明。</p>
<h3>GPIO 电流不够?</h3><p>用模块或三极管。</p>
<h3>反馈状态?</h3><p>读辅助触点或电流传感器。</p>
<h2>本章小结</h2><ul>
<li>光耦隔离安全</li>
<li>低/高电平看模块</li>
<li>220V合规</li>
<li>MQTT远程控</li>
</ul>
<p><strong>下一步：</strong> <a href="10-超声波测距.html">10-超声波</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "入门实战/10-超声波测距.html": chapter(
        '入门实战 10：超声波测距',
        '入门实战',
        '入门实战',
        """<blockquote><p>HC-SR04 Trig/Echo，pulseIn 算距离。</p></blockquote><hr>
<table><thead><tr><th>要点</th><th>说明</th></tr></thead><tbody><tr><td>实验</td><td>DevKit 验证</td></tr><tr><td>调试</td><td>串口 printf</td></tr></tbody></table>
<h2>1. 原理</h2>
<p>Trig 发 10µs 脉冲，Echo 高电平时间 ∝ 距离。声速340m/s，距离=时间µs/58 cm。</p>
<h2>2. 代码</h2>
<pre><code class="language-c">#define TRIG 5
#define ECHO 18
void measure(){
  digitalWrite(TRIG,LOW); delayMicroseconds(2);
  digitalWrite(TRIG,HIGH); delayMicroseconds(10); digitalWrite(TRIG,LOW);
  long us = pulseIn(ECHO, HIGH, 30000);
  if(us==0) Serial.println("timeout");
  else Serial.printf("dist=%.1f cm\\n", us/58.0);
}</code></pre>
<h2>3. 局限</h2>
<p>Soft 材料/角度吸收；近距盲区 ~2cm；实时性受 sound speed 限制。</p>
<h2>4. 项目</h2>
停车辅助、垃圾桶满度、智能门锁接近检测。
<div class="tip-box">💡 Echo 5V 时 ESP32 需分压到 3.3V。</div>
<div class="tip-box" style="border-color:#ff6b6b;background:rgba(255,107,107,.08)">⚠️ HC-SR04 Echo 5V 输出需 1k/2k 分压保护 ESP32。</div>
<h2>常见问题</h2>
<h3>不准?</h3><p>温度补偿/多次平均。</p>
<h3>timeout?</h3><p>超量程或无人。</p>
<h3>vs ToF?</h3><p>ToF 更准更贵。</p>
<h2>本章小结</h2><ul>
<li>Trig/Echo时序</li>
<li>pulseIn测脉宽</li>
<li>距离=us/58</li>
<li>注意5V Echo</li>
</ul>
<p><strong>下一步：</strong> <a href="../STM32/01-入门.html">STM32 01</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
}
