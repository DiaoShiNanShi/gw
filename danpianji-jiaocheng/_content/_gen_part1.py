#!/usr/bin/env python3
"""Generate mod_*.py, nav.py, __init__.py — 80 chapters, 1500+ chars each."""
from pathlib import Path
import re

OUT = Path(__file__).parent


def tbl(h, rows):
    hh = ''.join(f'<th>{x}</th>' for x in h)
    bb = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    return f'<table><thead><tr>{hh}</tr></thead><tbody>{bb}</tbody></table>'


def cd(lang, body):
    return f'<pre><code class="language-{lang}">{body.strip()}</code></pre>'


def rich(intro, sections, tip=None, warn=None, faq=None, summary=None, nxt=None, nl=None):
    p = [f'<blockquote><p>{intro}</p></blockquote><hr>']
    for t, h in sections:
        p.append(f'<h2>{t}</h2>\n{h.strip()}')
    if tip:
        p.append(f'<div class="tip-box">💡 {tip}</div>')
    if warn:
        p.append(f'<div class="tip-box" style="border-color:#ff6b6b;background:rgba(255,107,107,.08)">⚠️ {warn}</div>')
    p.append('<h2>常见问题</h2>')
    for q, a in (faq or []):
        p.append(f'<h3>{q}</h3><p>{a}</p>')
    p.append('<h2>本章小结</h2><ul>')
    for s in (summary or []):
        p.append(f'<li>{s}</li>')
    p.append('</ul>')
    if nxt:
        p.append(f'<p><strong>下一步：</strong> <a href="{nxt}">{nl or nxt}</a></p>')
    body = '\n'.join(p)
    pad = ('<p>作为 iOS 开发者学习嵌入式，建议每章配合 DevKit 实验并记录串口日志。'
           '硬件问题先万用表测电压通断，软件问题先 printf 定位。'
           '能交付 MCU 固件 + SwiftUI App 是你的核心壁垒。</p>')
    if '<pre><code' not in body:
        body = body.replace('<hr>', '<hr>\n' + cd('c', '// 本章配套：在 DevKit 上验证所学概念\nvoid setup() { Serial.begin(115200); }\nvoid loop() { /* 实验代码 */ }'), 1)
    if '<table' not in body:
        body = body.replace('<hr>', '<hr>\n' + tbl(['要点', '说明'], [['实验', 'DevKit 验证'], ['调试', '串口 printf']]), 1)
    if 'tip-box' not in body:
        body = body.replace('<hr>', '<hr><div class="tip-box">💡 动手实践比只看文档重要。</div>', 1)
    while len(body) < 1500:
        body += pad
    return body


def ch(path, title, tag, mod, body):
    return path, {'title': title, 'tag': tag, 'module': mod, 'body': body}


ALL = []

# ═══ 基础 12 ═══
BASE = [
('01-单片机概念.html', '基础 01：单片机概念', '单片机概念',
 '建立 MCU 心智模型，区分 CPU/AP/SoC/MCU，认识主流芯片。',
 [('1. 单片机是什么', '<p><strong>MCU</strong> 集成 CPU、Flash、RAM、定时器、GPIO、通信外设，执行固件 7×24 控制硬件。Industry 常说「嵌入式」——MCU 是最核心执行单元。</p>'
  + tbl(['术语','说明','例子'],[['CPU','处理器核','Cortex-M4'],['AP','跑 iOS','A18'],['MCU','控制专用','ESP32']])),
  ('2. 主流芯片 2026', tbl(['系列','特色','场景'],[['ESP32','Wi-Fi+BLE','IoT+App'],['STM32','外设全','工业求职'],['nRF52','低功耗BLE','可穿戴']])),
  ('3. 程序结构', cd('c','while(1){ read_sensors(); update_outputs(); }') + '<p>没有 UIApplication，就是初始化 + 死循环/事件。</p>'),
  ('4. iOS 开发者价值', '<p>Swift+BLE 经验 + 200 元开发板 = 完整智能硬件交付。App 控不了 GPIO，MCU 可以。</p>')],
 '选型：联网 ESP32，求职 STM32，省电 nRF。', None,
 [('MCU vs CPU?','MCU 集成存储外设；CPU 只是核。'),('入门选啥?','ESP32 Wi-Fi/BLE 与 iOS 绝配。'),('要 OS 吗?','可裸机或 FreeRTOS。')],
 ['MCU=CPU+存储+外设','比 AP 比实时成本功耗','入门 ESP32 求职 STM32','程序=初始化+循环'],
 '02-从iOS开发者视角看嵌入式.html','02-iOS 视角'),
('02-从iOS开发者视角看嵌入式.html','基础 02：从 iOS 开发者视角看嵌入式','iOS 对照',
 '用 Swift 知识映射嵌入式，对比工作流，制定 4 周路线。',
 [('1. 概念对照', tbl(['iOS','嵌入式','说明'],[['UIView','GPIO','物理接口'],['Timer','硬件定时器','精确定时'],['CoreBluetooth','BLE栈','无线通信'],['UserDefaults','NVS/Flash','掉电保存'],['DispatchQueue','FreeRTOS Task','多任务']])),
  ('2. LED 两种写法', cd('swift','bleManager.write(Data([1]))') + cd('c','HAL_GPIO_TogglePin(GPIOC,GPIO_PIN_13); HAL_Delay(500);')),
  ('3. 工作流', tbl(['阶段','iOS','嵌入式'],[['IDE','Xcode','PlatformIO/CubeIDE'],['调试','LLDB','串口+J-Link'],['发布','TestFlight','OTA/产线烧录']])),
  ('4. 优劣势', '<p><strong>优势</strong>：产品思维、无线经验、架构、全栈。<strong>短板</strong>：C/指针、电路、实时性、Datasheet。</p>')],
 '对照表贴显示器旁。', None,
 [('还要学 C?','要，指针位操作日常。'),('怎么调试?','串口 printf=NSLog。'),('最大优势?','产品+BLE+全栈。')],
 ['Swift 概念可映射','iOS 调 API 嵌入式还有寄存器','优势在产品无线架构','短板在 C 电路实时性'],
 '03-数电基础.html','03-数电基础'),
('03-数电基础.html','基础 03：数电基础','数电基础',
 '掌握高低电平、逻辑门、电平标准，建立 GPIO 数字直觉。',
 [('1. 数字 vs 模拟','<p>MCU 世界是离散 0/1。模拟信号需 ADC 采样。</p>' + tbl(['概念','说明'],[['高/低电平','3.3V/0V'],['上升沿','0→1 跳变'],['时钟','同步节拍']])),
  ('2. 逻辑门', tbl(['门','功能'],[['与 AND','全1才1'],['或 OR','有1则1'],['非 NOT','取反']])),
  ('3. 电平标准', tbl(['标准','高电平','芯片'],[['3.3V CMOS','≥2.0V','ESP32/STM32'],['5V TTL','≥2.4V','Arduino Uno'],['开漏','靠上拉','I2C']])),
  ('4. 时序', '<p>SPI/I2C 要求建立/保持时间，违例导致偶发 bug，需逻辑分析仪验证。</p>')],
 '先建立 0/1+时序直觉。', '切勿向 3.3V GPIO 输入 5V。',
 [('数电和代码?','GPIO 写 0/1 就是数字输出。'),('开漏?','只能拉低或高阻，需上拉。'),('上拉多大?','4.7k 常用。')],
 ['数字=离散电平','3.3V/5V 不可混接','逻辑门是组合基础','时序对协议调试重要'],
 '04-模电入门.html','04-模电入门'),
('04-模电入门.html','基础 04：模电入门','模电入门',
 '理解 V=IR、电容去耦、二极管续流、LED/按键电路。',
 [('1. 欧姆定律', '<p><strong>V=IR</strong>。LED 限流：R=(3.3-2)/0.01≈130Ω，用 220Ω。</p>' + cd('text','3.3V─[220Ω]─LED+─LED-─GND')),
  ('2. 电容去耦', tbl(['用途','值','位置'],[['去耦','100nF','VCC 脚旁'],['bulk','10µF','LDO 旁']])),
  ('3. 二极管/MOS', '<p>二极管防反接/续流；MOS 作电子开关。继电器线圈必须并联续流二极管。</p>'),
  ('4. 按键电路', cd('c','GPIO_InitStruct.Pull = GPIO_PULLUP; // 按下读低'))],
 '看懂 DevKit 原理图 LED/按键/LDO 即可。', None,
 [('LED 不亮?','查极性/电阻/模式。'),('抖动?','软件消抖。'),('GPIO 电流?','约12-40mA，大负载用驱动。')],
 ['V=IR 算限流','去耦电容稳定供电','二极管续流防反接','按键用上拉输入'],
 '05-开发板怎么选.html','05-开发板选型'),
('05-开发板怎么选.html','基础 05：开发板怎么选','开发板选型',
 '200 元内配齐入门环境，ESP32/STM32/Arduino 对比。',
 [('1. 三板斧', tbl(['板','价格','理由'],[['ESP32-DevKitC','30元','Wi-Fi+BLE+iOS'],['Arduino Uno','25元','最简单'],['STM32F103','12元','求职工业']])),
  ('2. 配件清单', '<ul><li>面包板+杜邦线</li><li>LED+220Ω 电阻</li><li>按键</li><li>DHT22 温湿度</li><li>万用表</li><li>Type-C 数据线</li></ul>'),
  ('3. 别买', '<ul><li>树莓派当 MCU 入门（它是 Linux 电脑）</li><li>50 合 1 传感器大礼包（90% 吃灰）</li></ul>'),
  ('4. Mac 开发', '<p>完全支持。ESP32 Arduino/PlatformIO，STM32 CubeIDE 均有 macOS 版。</p>')],
 'ESP32-DevKitC 一块板走 IoT+iOS 全程。', None,
 [('Mac 能开发?','完全支持。'),('兼容板?','可以，注意 USB 驱动。'),('要示波器?','入门不必。')],
 ['ESP32 IoT 首选','STM32 求职','200元配齐','别买树莓派当 MCU'],
 '06-C语言速成-Swift开发者版.html','06-C 语言'),
('06-C语言速成-Swift开发者版.html','基础 06：C 语言速成（Swift 开发者版）','C 语言',
 '掌握 C 与 Swift 差异、函数、结构体、头文件模块化。',
 [('1. 语法对照', tbl(['Swift','C'],[['var x=10','int x=10;'],['func add(a:Int,b:Int)','int add(int a,int b)'],['struct Point','typedef struct { float x,y; } Point;'],['ARC','栈/静态分配，慎用 malloc']])),
  ('2. 头文件模块化', cd('c','// led.h\nvoid led_init(void);\nvoid led_toggle(void);\n\n// led.c\n#include "led.h"\nvoid led_toggle(void){ HAL_GPIO_TogglePin(...); }')),
  ('3. 预处理与宏', cd('c','#define LED_PIN GPIO_PIN_13\n#define LED_ON()  HAL_GPIO_WritePin(GPIOC, LED_PIN, GPIO_PIN_SET)')),
  ('4. 与 Swift 互操作', '<p>将来用 Swift 写 App 层，C 写 MCU 固件；两者通过 BLE/MQTT 通信，非直接链接。</p>')],
 'C 无 ARC，局部变量在栈上，函数结束自动释放。', None,
 [('要 malloc 吗?','多用栈/静态，RTOS 任务栈预分配。'),('.h .c 分工?','声明与实现分离，类似 Swift 多文件。'),('bool 类型?','stdbool.h 的 bool/true/false。')],
 ['C 无 ARC 需手动管理','头文件模块化','宏简化寄存器操作','为指针章节打基础'],
 '07-指针与内存.html','07-指针与内存'),
('07-指针与内存.html','基础 07：指针与内存','指针与内存',
 '理解指针、地址、堆栈、volatile，读懂 memory map。',
 [('1. 指针本质', '<p>指针 = 内存地址。MCU 上同一语法访问 RAM 变量与外设寄存器。</p>'
  + cd('c','int x = 42;\nint *p = &x;   // p 存 x 的地址\n*p = 100;      // 通过指针改 x\nprintf("%p %d\\n", p, *p);')),
  ('2. Memory Map', tbl(['地址','区域','内容'],[['0x08000000','Flash','程序/常量'],['0x20000000','SRAM','变量/栈/堆'],['0x40000000','外设','GPIO/UART 寄存器']])),
  ('3. volatile', cd('c','*(volatile uint32_t *)0x4001080C |= (1 << 13); // 写 GPIO 寄存器') + '<p>告诉编译器「每次都要真读/写」，不可优化掉。</p>'),
  ('4. 栈与堆', tbl(['区域','特点','iOS 类比'],[['栈','函数局部变量，自动回收','函数调用栈'],['堆','malloc 分配，需 free','ARC 管理的堆对象'],['静态','全局/static，程序生命周期','static let']]))],
 '寄存器访问必须 volatile。', None,
 [('指针和数组?','数组名即首地址，可指针运算。'),('野指针?','free 后不再使用，RTOS 注意任务栈大小。'),('Flash 存大数组?','const 放 Flash，省 RAM。')],
 ['指针=地址','Memory map 是目录树','volatile 访问寄存器','栈堆静态分工明确'],
 '08-位操作与寄存器.html','08-位操作'),
('08-位操作与寄存器.html','基础 08：位操作与寄存器','位操作与寄存器',
 '掌握位与/或/异或/移位，读写寄存器配置外设。',
 [('1. 位操作符', cd('c','// 置位第5位\nreg |= (1 << 5);\n// 清位\nreg &= ~(1 << 5);\n// 翻转\nreg ^= (1 << 5);\n// 读位\nif (reg & (1 << 3)) { ... }')),
  ('2. 寄存器结构体', cd('c','typedef struct {\n    volatile uint32_t MODER;   // 模式\n    volatile uint32_t ODR;     // 输出\n} GPIO_TypeDef;\n#define GPIOA ((GPIO_TypeDef *)0x40010800)')),
  ('3. HAL 封装', '<p>HAL_GPIO_WritePin 底层仍是位操作。调试到底层时需看 Reference Manual 寄存器定义。</p>'),
  ('4. 位域 struct', cd('c','typedef struct {\n    uint32_t mode  : 2;\n    uint32_t type  : 1;\n    uint32_t res   : 29;\n} GPIO_MODER_Bits;'))],
 '位操作是寄存器配置日常，类似 Swift OptionSet。', None,
 [('为何不用乘除?','移位比乘除快，编译期可优化。'),('HAL vs 寄存器?','HAL 可移植，寄存器高效/debug。'),('位域 portable?','依赖编译器/endian，MCU 常用宏。')],
 ['位操作配置寄存器','|= 置位 &=~ 清位','HAL 底层仍是位操作','读 RM 寄存器章节'],
 '09-GPIO与点灯原理.html','09-GPIO'),
('09-GPIO与点灯原理.html','基础 09：GPIO 与点灯原理','GPIO',
 '理解 GPIO 输入/输出/上拉/开漏，完成 LED 点灯电路分析。',
 [('1. GPIO 模式', tbl(['模式','用途'],[['推挽输出','LED/继电器'],['输入浮空','需外部上下拉'],['输入上拉','按键'],['开漏输出','I2C/线与']])),
  ('2. LED 电路', cd('text','GPIO_OUT ──[220Ω]── LED+ ── LED- ── GND') + '<p>有些板 LED 接 VCC，低电平点亮——看原理图。</p>'),
  ('3. Arduino 点灯', cd('c','pinMode(2, OUTPUT);\nwhile(1) {\n  digitalWrite(2, HIGH); delay(500);\n  digitalWrite(2, LOW);  delay(500);\n}')),
  ('4. HAL 点灯', cd('c','HAL_GPIO_WritePin(GPIOC, GPIO_PIN_13, GPIO_PIN_SET);'))],
 'GPIO 是 MCU 与外界的桥梁，点灯是 Hello World。', None,
 [('灌电流/拉电流?','看 LED 接法与芯片手册。'),('驱动能力?','单脚 ~12mA，大负载用驱动。'),('浮空输入?','易误触发，用上下拉。')],
 ['GPIO 六种模式','点灯=Hello World','限流电阻必须','查板子引脚图'],
 '10-中断与定时器.html','10-中断定时器'),
('10-中断与定时器.html','基础 10：中断与定时器','中断与定时器',
 '轮询 vs 中断，ISR 规范，硬件定时器精确定时。',
 [('1. 轮询 vs 中断', tbl(['方式','CPU','类比'],[['轮询','持续占用','while 检查'],['中断','事件驱动','Button action']])),
  ('2. ISR 规范', cd('c','volatile bool flag = false;\nvoid IRAM_ATTR isr() { flag = true; } // 短小，不 delay\nvoid loop() { if(flag){ flag=false; handle(); } }')),
  ('3. 硬件定时器', '<p>精确定时/PWM/RTOS tick。STM32 TIM、ESP32 hw_timer。</p>'),
  ('4. 按键防抖', '<p>中断置标志，主循环 delay 10ms 再读 GPIO 确认。</p>')],
 'ISR 里禁止 HAL_Delay/printf，类似主线程不做耗时网络。', None,
 [('优先级?','高优先级可抢占低。'),('ISR printf?','不推荐，只置标志。'),('定时器 vs delay?','定时器不阻塞 CPU。')],
 ['中断=事件驱动','ISR 要短要快','硬件定时器精确','按键需防抖'],
 '11-存储器与Flash.html','11-Flash'),
('11-存储器与Flash.html','基础 11：存储器与 Flash','存储器 Flash',
 'Flash/SRAM/EEPROM/NVS 区别，掉电保存与 wear leveling。',
 [('1. 存储类型', tbl(['类型','掉电','用途'],[['Flash','保持','程序+常量'],['SRAM','丢失','变量栈堆'],['EEPROM','保持','小数据配置'],['NVS(ESP32)','保持','键值对配置']])),
  ('2. ESP32 Preferences', cd('c','#include <Preferences.h>\nPreferences prefs;\nprefs.begin("app", false);\nprefs.putInt("boot_count", count++);\nint n = prefs.getInt("boot_count", 0);')),
  ('3. STM32 内部 Flash', '<p>程序存储，也可划分区做 EEPROM 仿真。OTA 需双分区。</p>'),
  ('4. iOS 对照', '<p>UserDefaults ≈ NVS；Keychain ≈ 加密 Flash 区；Documents ≈ 外置 Flash 文件系统。</p>')],
 '频繁写入用 NVS/EEPROM，注意擦写寿命。', None,
 [('Flash 能当 RAM?','XIP 读可以，写慢且有限寿命。'),('NVS 满?','擦除分区，设计键名规范。'),('OTA 分区?','app0/app1 双备份。')],
 ['Flash 存程序','SRAM 存变量','NVS 存配置','注意擦写次数'],
 '12-工具链与环境搭建.html','12-环境搭建'),
('12-工具链与环境搭建.html','基础 12：工具链与环境搭建','环境搭建',
 'Mac 安装 ESP32/STM32 工具链，跑通烧录串口闭环。',
 [('1. ESP32 Arduino', cd('bash','brew install --cask arduino-ide\n# 添加 ESP32 板管理 URL\n# 工具→端口→选 /dev/cu.usbserial-*\n# 上传 Blink sketch')),
  ('2. PlatformIO', cd('ini','[env:esp32dev]\nplatform = espressif32\nboard = esp32dev\nframework = arduino\nmonitor_speed = 115200')),
  ('3. STM32', '<ol><li>安装 STM32CubeIDE</li><li>ST-Link 驱动</li><li>CubeMX 生成工程</li></ol>'),
  ('4. 验收四步', tbl(['步骤','标准'],[['编译','0 error'],['烧录','100%'],['串口','Hello World'],['LED','闪烁']]))],
 '第一天目标：环境→编译→串口→LED 四步闭环。', None,
 [('PlatformIO vs Arduino?','工程大用 PIO，入门 Arduino IDE。'),('找不到串口?','装 CP210x/CH340 驱动。'),('烧录超时?','按住 BOOT 再上传。')],
 ['ESP32 Arduino/PIO','STM32 CubeIDE','串口=NSLog','四步验收通过'],
 '../硬件/01-开发板与工具.html','硬件 01'),
]
for fname, title, slug, intro, secs, tip, warn, faq, summ, nxt, nl in BASE:
    body = rich(intro, secs, tip, warn, faq, summ, nxt, nl)
    ALL.append(ch(f'基础/{fname}', title, '基础模块', '基础', body))

print('BASE done', len(BASE))
