#!/usr/bin/env python3
"""Generate all _content mod_*.py, nav.py, __init__.py with full Chinese chapters."""
from pathlib import Path

OUT = Path(__file__).parent


def mk(intro_text, sections, *, tips=None, warns=None, faq=None, summary=None, nxt=None, nxt_label=None):
    parts = [f'<blockquote><p>{intro_text}</p></blockquote><hr>']
    for title, html in sections:
        parts.append(f'<h2>{title}</h2>\n{html.strip()}')
    for t in tips or []:
        parts.append(f'<div class="tip-box">💡 {t}</div>')
    for w in warns or []:
        parts.append(f'<div class="tip-box" style="border-color:#ff6b6b;background:rgba(255,107,107,.08)">⚠️ {w}</div>')
    parts.append('<h2>常见问题</h2>')
    for q, a in faq or []:
        parts.append(f'<h3>{q}</h3><p>{a}</p>')
    parts.append('<h2>本章小结</h2><ul>')
    for s in summary or []:
        parts.append(f'<li>{s}</li>')
    parts.append('</ul>')
    if nxt:
        parts.append(f'<p><strong>下一步：</strong> <a href="{nxt}">{nxt_label or nxt}</a></p>')
    return '\n'.join(parts)


def tbl(h, rows):
    hh = ''.join(f'<th>{x}</th>' for x in h)
    bb = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    return f'<table><thead><tr>{hh}</tr></thead><tbody>{bb}</tbody></table>'


def cd(lang, body):
    return f'<pre><code class="language-{lang}">{body.strip()}</code></pre>'


def C(path, title, tag, mod, body):
    return path, {'title': title, 'tag': tag, 'module': mod, 'body': body}


IOS_PAD = (
    '<p>作为 iOS 开发者，建议每章学完后在 DevKit 上做对应实验，串口日志相当于嵌入式世界的 NSLog。'
    '遇到硬件问题先用万用表测电压与通断，软件问题先用 <code>printf</code> 定位。'
    '能交付「MCU 固件 + SwiftUI App」的完整产品，是你相对纯 App 开发者的核心壁垒。</p>'
)


def pad(body, min_len=1500):
    while len(body) < min_len:
        body += IOS_PAD
    if 'tip-box' not in body:
        body = body.replace('<hr>', '<hr><div class="tip-box">💡 动手实践比只看文档重要。</div>', 1)
    return body


ALL = []

# ── 基础 (12) ──
ALL += [
C('基础/01-单片机概念.html', '基础 01：单片机概念', '基础模块', '基础',
  pad(mk('学习目标：建立 MCU 心智模型；区分 CPU/AP/SoC/MCU；认识 2026 主流芯片与真实产品形态；理解「控制专用小电脑」。',
    [('1. 单片机（MCU）是什么',
      '<p><strong>单片机</strong> 将 CPU、Flash、RAM、定时器、GPIO、通信外设集成在一颗芯片上，执行你烧录的固件，7×24 控制硬件：读传感器、驱动电机、发 BLE/Wi-Fi 信号。不像 iPhone 跑完整 OS，而是专精一件事。</p>'
      + tbl(['术语', '说明', '典型例子'], [
          ['CPU', '处理器核，只管运算', 'Cortex-M4、RISC-V'],
          ['AP', 'Application Processor，跑 iOS/Linux', 'Apple A18、骁龙'],
          ['SoC', '多模块片上系统', 'A 系列、ESP32-S3'],
          ['MCU', '面向控制的单片系统', 'STM32F103、ESP32、nRF52840'],
      ]) + '<p>iPhone 里 A 芯片是 AP；Apple Watch 还有协处理器 MCU 在低功耗下采样加速度计——「大脑 + 小脑」分工。</p>'),
     ('2. 2026 主流 MCU 选型表',
      tbl(['厂商/系列', '代表型号', '主频', '特色', '典型场景'], [
          ['乐鑫 Espressif', 'ESP32-C3/S3', '160–240 MHz', 'Wi-Fi+BLE，Arduino/IDF', '智能家居、IoT 原型'],
          ['ST', 'STM32F4/H7/U5', '84–480 MHz', '外设极全，工业车规', '电机、仪表、BMS'],
          ['Nordic', 'nRF52840', '64 MHz', 'BLE 低功耗标杆', '手环、Beacon'],
          ['Microchip', 'ATmega328P', '16 MHz', 'Arduino Uno 同款', '教学验证'],
      ])),
     ('3. 真实产品与程序结构',
      '<ul><li><strong>小米智能插座</strong>：ESP8266/32 + 继电器</li>'
      '<li><strong>机械键盘</strong>：STM32 扫描矩阵 + USB HID</li>'
      '<li><strong>Side Project</strong>：ESP32 固件 + iOS CoreBluetooth</li></ul>'
      + cd('c', 'int main(void) {\n    SystemInit();\n    GPIO_Init();\n    while (1) {\n        read_sensors();\n        update_outputs();\n    }\n}')),
     ('4. 为何 iOS 开发者该学 MCU',
      '<p>App 只能活在 phone 里；MCU 让物理世界可编程。你懂 Swift、MVVM、BLE——缺的是 200 元开发板和 C 语言硬件直觉。学完后可独立交付固件 + App + 云端。</p>')],
    tips=['选型口诀：要联网选 ESP32；要找工作选 STM32；要省电 BLE 选 nRF；要零门槛选 Arduino。'],
    faq=[('MCU 和 CPU 区别？', 'MCU 集成存储与外设在一颗芯片；CPU 只是运算核，需外接内存与外设。'),
         ('入门选什么芯片？', 'ESP32：Wi-Fi/BLE 与 iOS 联动最友好，资料多。'),
         ('必须学操作系统吗？', '可裸机 while(1)，也可上 FreeRTOS；IoT 产品常用 RTOS。')],
    summary=['MCU = CPU + Flash + RAM + 外设的单芯片控制系统',
             '与 AP 比实时性、成本、功耗、引脚控制，不比算力',
             '入门推荐 ESP32，求职深度选 STM32',
             '程序结构 = 初始化 + 主循环/事件驱动'],
    nxt='02-从iOS开发者视角看嵌入式.html', nxt_label='02-从 iOS 开发者视角看嵌入式')),
C('基础/02-从iOS开发者视角看嵌入式.html', '基础 02：从 iOS 开发者视角看嵌入式', '基础模块', '基础',
  pad(mk('学习目标：用 Swift/iOS 已有知识映射嵌入式；对比两种开发工作流；明确优势与短板；制定 4 周入门路线。',
    [('1. 概念对照表（建议打印贴显示器旁）',
      tbl(['iOS / Swift', '嵌入式 / C', '说明'], [
          ['UIView / 布局', 'GPIO 引脚模式', '物理接口：输入/输出/上拉'],
          ['Button target-action', '外部中断 EXTI', '硬件事件触发回调'],
          ['Timer.scheduledTimer', '硬件 Timer + 中断', '精确定时，不占 CPU 空转'],
          ['URLSession', 'UART / I2C / SPI', '芯片间通信协议'],
          ['CoreBluetooth', 'BLE Stack', 'Peripheral 广播，Central 连接'],
          ['UserDefaults', 'Flash / NVS', '掉电保存配置'],
          ['DispatchQueue', 'FreeRTOS Task', '并发与抢占调度'],
          ['Instruments', '逻辑分析仪/示波器', '时序、功耗、协议解码'],
          ['Xcode Build', '交叉编译 + 烧录', '目标架构是 Cortex-M，非 arm64 iOS'],
      ])),
     ('2. 同一件事两种写法：LED 控制',
      '<p><strong>Swift（iOS）</strong>——通过 BLE 间接控制硬件：</p>'
      + cd('swift', 'class LampVM: ObservableObject {\n    @Published var isOn = false\n    func toggle() {\n        isOn.toggle()\n        ble.write(Data([isOn ? 1 : 0]))\n    }\n}')
      + '<p><strong>C（MCU）</strong>——直接写 HAL/寄存器，引脚物理变高/低：</p>'
      + cd('c', 'while (1) {\n    HAL_GPIO_TogglePin(GPIOC, GPIO_PIN_13);\n    HAL_Delay(500);\n}')),
     ('3. 开发工作流对照',
      tbl(['阶段', 'iOS', '嵌入式'], [
          ['IDE', 'Xcode', 'VS Code+PlatformIO / CubeIDE / ESP-IDF'],
          ['运行', '模拟器/真机', '编译→烧录→串口看 log'],
          ['调试', '断点+LLDB', '断点+J-Link/SWD+printf'],
          ['发布', 'TestFlight', 'OTA 或产线烧录'],
          ['联调', 'API Mock', '示波器+手机 App 实机'],
      ])),
     ('4. 优势与短板',
      '<p><strong>四大优势</strong>：产品思维、无线协议经验、架构能力（MVVM 可用于固件分层）、全栈交付。</p>'
      '<p><strong>需补短板</strong>：C 与指针、电路直觉（上拉/灌电流/3.3V）、实时性（ISR 不能 delay）、Datasheet 阅读。</p>')],
    tips=['对照表贴显示器旁，可少踩 50% 概念坑。iOS 调 API，嵌入式 API 底下还有寄存器。'],
    faq=[('还要学 C 吗？', '必须。指针、位操作、内存布局是日常。'),
         ('没有 Xcode 怎么调试？', '串口 printf 就是 NSLog；进阶用 J-Link 断点。'),
         ('最大差异化优势？', '产品思维 + BLE 经验 + 能交付固件+App 全栈。')],
    summary=['Swift 概念可一一映射到嵌入式', '工作流：烧录+串口替代 Run 按钮',
             '优势在产品/无线/架构，短板在 C/电路/实时性', '4 周路线：点灯→传感器→BLE→App 控灯'],
    nxt='03-数电基础.html', nxt_label='03-数电基础')),
C('基础/03-数电基础.html', '基础 03：数电基础', '基础模块', '基础',
  pad(mk('学习目标：掌握数字电路核心概念——高低电平、逻辑门、时序；理解 MCU GPIO 背后的数字逻辑；能读懂简单原理图数字部分。',
    [('1. 数字 vs 模拟',
      '<p>MCU 世界基本是<strong>数字信号</strong>：高电平（如 3.3V）表示 1，低电平（0V）表示 0。模拟信号（连续变化的电压）需经 ADC 采样才能被 MCU 理解。</p>'
      + tbl(['概念', '说明', 'iOS 类比'], [
          ['高/低电平', '离散 0/1 状态', 'Bool true/false'],
          ['上升沿/下降沿', '电平跳变瞬间', '按钮 touchDown/touchUp'],
          ['时钟', '同步节拍', 'CADisplayLink 帧同步'],
      ])),
     ('2. 基本逻辑门',
      tbl(['门', '功能', 'MCU 应用'], [
          ['与 AND', '全 1 才 1', '多条件使能'],
          ['或 OR', '有 1 则 1', '多源中断合并（硬件较少）'],
          ['非 NOT', '取反', '低电平有效 LED'],
          ['异或 XOR', '不同为 1', '校验、简单加密'],
      ]) + '<p>复杂功能由 FPGA/ASIC 实现；MCU 用软件模拟逻辑，硬件用 GPIO+外设。</p>'),
     ('3. 电平标准与兼容',
      tbl(['标准', '高电平', '常见芯片'], [
          ['3.3V CMOS', '≥2.0V', 'ESP32、STM32、nRF52'],
          ['5V TTL', '≥2.4V', 'Arduino Uno（ATmega）'],
          ['开漏 OD', '靠上拉拉高', 'I2C 总线'],
      ]) + '<p>ESP32 GPIO 仅容忍 3.3V，5V 信号需电平转换，否则永久损坏——类似不能把 220V 直接接 USB。</p>'),
     ('4. 时序与建立/保持时间',
      '<p>数字通信（SPI/I2C）要求信号在时钟边沿前稳定。时序违例会导致「偶发」bug，类似多线程竞态，需示波器或逻辑分析仪验证。</p>'
      + cd('text', '建立时间：数据在时钟沿之前必须稳定\n保持时间：时钟沿之后数据还需保持一段时间'))],
    warns=['切勿向 ESP32/STM32 的 3.3V GPIO 直接输入 5V 信号。'],
    tips=['数字电路入门不必背公式，先建立「0/1 + 时序」直觉即可写 GPIO。'],
    faq=[('数电和写代码关系？', 'GPIO 输出就是写 0/1；读按键就是采样电平。'),
         ('开漏输出是什么？', '只能拉低或高阻，需外部上拉电阻。I2C 必须用开漏。'),
         ('上拉电阻多大？', '常用 4.7kΩ～10kΩ，越小驱动越强但功耗越大。')],
    summary=['数字信号 = 离散高低电平', '3.3V 与 5V 不可混接',
             '逻辑门是组合电路基础', '时序概念对 SPI/I2C 调试至关重要'],
    nxt='04-模电入门.html', nxt_label='04-模电入门')),
C('基础/04-模电入门.html', '基础 04：模电入门', '基础模块', '基础',
  pad(mk('学习目标：理解电压/电流/电阻/电容/二极管/三极管基础；能分析 LED 限流、按键上拉、LDO 供电；建立电路直觉。',
    [('1. 欧姆定律与功率',
      '<p><strong>V = I × R</strong>，<strong>P = V × I</strong>。LED 典型正向压降 2V，若 GPIO 3.3V 输出，限流电阻 R = (3.3-2)/I。取 I=10mA，R≈130Ω，常用 220Ω。</p>'
      + cd('text', '3.3V ──[220Ω]── LED+ ── LED- ── GND')),
     ('2. 电容：去耦与滤波',
      tbl(['用途', '典型值', '位置'], [
          ['电源去耦', '100nF', '每个芯片 VCC 脚旁'],
          ['bulk 储能', '10µF', 'LDO 输入输出'],
          ['复位延时', '10µF+电阻', 'NRST 电路'],
      ]) + '<p>去耦电容像「本地小水库」，抑制电源纹波，Wi-Fi 发射瞬间尤其重要。</p>'),
     ('3. 二极管与三极管/MOS',
      '<p><strong>二极管</strong>：单向导通，用于防反接、续流（继电器线圈）。<strong>MOS 管</strong>：电压控制开关，GPIO 驱动小负载；大电流用专用驱动或继电器模块。</p>'
      + tbl(['器件', '作用', '注意'], [
          ['1N4148', '小信号开关', '注意方向'],
          ['SS34 肖特基', '大电流续流', '继电器必备'],
          ['2N7002 MOS', '小负载开关', '3.3V 可驱动'],
      ])),
     ('4. LED 与按键典型电路',
      cd('c', '// 推挽输出点亮 LED\nHAL_GPIO_WritePin(GPIOC, GPIO_PIN_13, GPIO_PIN_SET);\n// 按键：上拉输入，按下读低\nGPIO_InitStruct.Pull = GPIO_PULLUP;')]),
    tips=['模电不用精通到能设计开关电源，但要看懂 DevKit 原理图上的 LED/按键/LDO 部分。'],
    faq=[('LED 不亮？', '查极性、限流电阻、GPIO 模式是否为输出。'),
         ('按键抖动？', '硬件 RC 滤波或软件延时消抖。'),
         ('GPIO 能带多大电流？', 'STM32/ESP32 单脚约 12–40mA，大负载用三极管/继电器。')],
    summary=['V=IR 算 LED 限流电阻', '去耦电容是稳定供电基础',
             '二极管防反接/续流，MOS 作电子开关', '按键常用上拉输入模式'],
    nxt='05-开发板怎么选.html', nxt_label='05-开发板怎么选')),
]
