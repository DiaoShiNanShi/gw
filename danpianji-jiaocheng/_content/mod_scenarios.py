"""Chapter content definitions."""

from .helpers import chapter

CHAPTERS = {
    "应用场景/01-行业应用全景.html": chapter(
        '应用 01：行业应用全景',
        '应用场景',
        '应用场景',
        """<blockquote><p>七大嵌入式方向与 iOS+MCU 切入建议。</p></blockquote><hr>
<pre><code class="language-c">// 本章配套：在 DevKit 上验证所学概念
void setup() { Serial.begin(115200); }
void loop() { /* 实验代码 */ }</code></pre>
<h2>1. 七大方向</h2>
<ul><li>消费电子 IoT</li><li>工业控制</li><li>汽车电子</li><li>医疗设备</li><li>智慧农业</li><li>新能源 BMS</li><li>机器人</li></ul>
<h2>2. 对比</h2>
<table><thead><tr><th>方向</th><th>门槛</th><th>薪资</th><th>iOS协同</th></tr></thead><tbody><tr><td>IoT</td><td>低</td><td>8-20K</td><td>极高</td></tr><tr><td>工业</td><td>中</td><td>10-25K</td><td>中</td></tr><tr><td>汽车</td><td>高</td><td>15-35K</td><td>低</td></tr></tbody></table>
<h2>3. 建议</h2>
<p>你背景最适合 <strong>消费电子 IoT</strong>：ESP32+App，投入小、作品集直观、接单快。</p>
<h2>4. 趋势 2026</h2>
<p>Edge AI、Matter 协议、车规 MCU、储能 BMS 增长。</p>
<div class="tip-box">💡 选对方向比盲目深钻更重要。</div>
<h2>常见问题</h2>
<h3>转行?</h3><p>IoT 全栈 3-6 个月可出作品。</p>
<h3>汽车?</h3><p>需 C++ AUTOSAR 深。</p>
<h3>医疗?</h3><p>法规严周期长。</p>
<h2>本章小结</h2><ul>
<li>七大方向各有特点</li>
<li>IoT 最适合 iOS 背景</li>
<li>作品集导向</li>
<li>关注 Matter/Edge AI</li>
</ul>
<p><strong>下一步：</strong> <a href="02-如何接单赚钱.html">02-接单</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "应用场景/02-如何接单赚钱.html": chapter(
        '应用 02：如何接单赚钱',
        '应用场景',
        '应用场景',
        """<blockquote><p>渠道、定价、首单路径。</p></blockquote><hr>
<h2>1. 渠道</h2>
<table><thead><tr><th>渠道</th><th>单价</th><th>特点</th></tr></thead><tbody><tr><td>闲鱼/淘宝</td><td>500-5K</td><td>入门快</td></tr><tr><td>程序员客栈</td><td>5K-30K</td><td>项目制</td></tr><tr><td>人脉转介绍</td><td>2万+</td><td>信任溢价</td></tr></tbody></table>
<h2>2. 高溢价项目</h2>
<ol><li>App+硬件套装</li><li>农业监测</li><li>BLE 门禁/打印</li><li>毕设辅导</li></ol>
<h2>3. 定价</h2>
<pre><code class="language-text">报价 = 工时×(300-800元/h) + 硬件成本×1.2 + 风险系数</code></pre>
<h2>4. 首单</h2>
<p>3 个 GitHub demo → 闲鱼挂「iOS+ESP32 开发」→ 首单 5 折换好评案例。</p>
<div class="tip-box">💡 案例>证书，demo 视频是成交关键。</div>
<h2>常见问题</h2>
<h3>没案例?</h3><p>先做台灯+环境监测开源。</p>
<h3>合同?</h3><p>里程碑 30-40-30 付款。</p>
<h3>维护?</h3><p>年费 15-20%。</p>
<h2>本章小结</h2><ul>
<li>多渠道</li>
<li>iOS+硬件溢价</li>
<li>里程碑付款</li>
<li>案例先行</li>
</ul>
<p><strong>下一步：</strong> <a href="03-职业规划.html">03-职业</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
    "应用场景/03-职业规划.html": chapter(
        '应用 03：职业规划',
        '应用场景',
        '应用场景',
        """<blockquote><p>嵌入式+iOS 双栈职业路径，学习路线与薪资。</p></blockquote><hr>
<pre><code class="language-c">// 本章配套：在 DevKit 上验证所学概念
void setup() { Serial.begin(115200); }
void loop() { /* 实验代码 */ }</code></pre>
<h2>1. 路径</h2>
<table><thead><tr><th>阶段</th><th>技能</th><th>目标</th></tr></thead><tbody><tr><td>0-3月</td><td>ESP32+BLE+App</td><td>2个demo</td></tr><tr><td>3-6月</td><td>STM32+RTOS</td><td>求职/接单</td></tr><tr><td>6-12月</td><td>OTA+项目</td><td>全栈工程师</td></tr></tbody></table>
<h2>2. 岗位</h2>
<p>智能硬件工程师、IoT 全栈、嵌入式软件(iOS 协同)、创业产品负责人。</p>
<h2>3. 简历</h2>
<p>突出：独立完成固件+App 联调；GitHub；demo 链接；解决过的 hard bug。</p>
<h2>4. 持续</h2>
<p>Matter/HomeKit、Edge ML(TinyML)、Rust embedded 是加分项。</p>
<div class="tip-box">💡 T 型人才：iOS 深 + MCU 够用宽。</div>
<h2>常见问题</h2>
<h3>纯嵌入式?</h3><p>可，但 iOS 是差异化。</p>
<h3>管理岗?</h3><p>5年+项目经验。</p>
<h3>创业?</h3><p>小批量验证再投。</p>
<h2>本章小结</h2><ul>
<li>分阶段目标</li>
<li>智能硬件岗位</li>
<li>作品集简历</li>
<li>T 型双栈</li>
</ul>
<p><strong>下一步：</strong> <a href="../练习/01-入门采购清单.html">练习 01</a></p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p><p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。硬件问题先万用表测电压通断，软件问题先 printf 定位。能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>""",
    ),
}
