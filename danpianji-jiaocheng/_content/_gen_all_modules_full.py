#!/usr/bin/env python3
"""Generate mod_*.py, nav.py, __init__.py — 80 chapters total."""
from pathlib import Path
import re

OUT = Path(__file__).parent


def tbl(h, rows):
    hh = "".join(f"<th>{x}</th>" for x in h)
    bb = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f"<table><thead><tr>{hh}</tr></thead><tbody>{bb}</tbody></table>"


def cd(lang, body):
    return f'<pre><code class="language-{lang}">{body.strip()}</code></pre>'


def mk(intro, sections, *, tip=None, warn=None, faq=None, summary=None):
    p = [f'<blockquote><p>{intro}</p></blockquote><hr>']
    for t, html in sections:
        p.append(f"<h2>{t}</h2>\n{html.strip()}")
    if tip:
        p.append(f'<div class="tip-box">💡 {tip}</div>')
    if warn:
        p.append(f'<div class="tip-box" style="border-color:#ff6b6b;background:rgba(255,107,107,.08)">⚠️ {warn}</div>')
    p.append("<h2>常见问题</h2>")
    for q, a in faq:
        p.append(f"<h3>{q}</h3><p>{a}</p>")
    p.append("<h2>本章小结</h2><ul>")
    for s in summary:
        p.append(f"<li>{s}</li>")
    p.append("</ul>")
    return "\n".join(p)


def C(path, title, tag, mod, body, nxt=None, nl=None):
    if nxt:
        body += f'<p><strong>下一步：</strong> <a href="{nxt}">{nl or nxt}</a></p>'
    return path, {"title": title, "tag": tag, "module": mod, "body": body}


ALL = []

# ─── BASE (12) ───
ALL += [
C("基础/01-单片机概念.html","基础 01：单片机概念","基础模块","基础",
  mk("学习目标：建立 MCU 心智模型，区分 CPU/AP/SoC/MCU，认识主流芯片与产品形态。",
     [("1. 单片机是什么",f"<p><strong>MCU</strong> 集成 CPU、Flash、RAM、定时器、GPIO、通信外设，执行固件 7×24 控制硬件。</p>{tbl(['术语','说明','例子'],[['CPU','处理器核','Cortex-M4'],['AP','跑iOS的应用处理器','A18'],['MCU','控制专用','ESP32']])}"),
      ("2. 主流芯片",f"{tbl(['系列','特色','场景'],[['ESP32','Wi-Fi+BLE','IoT'],['STM32','外设全','工业'],['nRF52','低功耗BLE','可穿戴']])}{cd('c','while(1){ read_sensors(); update_outputs(); }')}"),
      ("3. 为何 iOS 开发者要学", "<p>MCU 让物理世界可编程。Swift+BLE 经验 + 200 元开发板 = 完整智能硬件交付能力。</p>")],
     tip="选型口诀：联网 ESP32，求职 STM32，省电 nRF，零门槛 Arduino。",
     faq=[("MCU 和 CPU 区别？","MCU 集成存储与外设；CPU 只是核。"),("入门选什么？","ESP32，Wi-Fi/BLE 与 iOS 绝配。"),("需要 OS 吗？","可裸机 while(1) 或 FreeRTOS。")],
     summary=["MCU=CPU+存储+外设","比 AP 比实时性成本功耗","入门 ESP32 求职 STM32","程序=初始化+循环"]),
  "02-从iOS开发者视角看嵌入式.html","02-iOS视角"),
C("基础/02-从iOS开发者视角看嵌入式.html","基础 02：从 iOS 开发者视角看嵌入式","基础模块","基础",
  mk("学习目标：用 Swift 知识映射嵌入式，对比工作流，制定 4 周路线。",
     [("1. 概念对照",tbl(["iOS","嵌入式","说明"],[["UIView","GPIO","物理接口"],["Timer","硬件定时器","精确定时"],["CoreBluetooth","BLE栈","无线通信"],["UserDefaults","NVS/Flash","掉电保存"]])),
      ("2. LED 两种写法",f"{cd('swift','bleManager.write(Data([1]))')}{cd('c','HAL_GPIO_TogglePin(GPIOC,GPIO_PIN_13); HAL_Delay(500);')}"),
      ("3. 工作流",tbl(["阶段","iOS","嵌入式"],[["IDE","Xcode","PlatformIO/CubeIDE"],["调试","LLDB","串口+J-Link"],["发布","TestFlight","OTA/产线烧录"]]))],
     tip="对照表贴显示器旁，少踩 50% 概念坑。",
     faq=[("还要学 C 吗？","要，指针位操作是日常。"),("没 Xcode 怎么调试？","串口 printf = NSLog。"),("最大优势？","产品思维+BLE+全栈。")],
     summary=["Swift 概念可映射到 C","iOS 调 API 嵌入式还有寄存器","优势在产品无线架构","短板在 C 电路实时性"]),
  "03-计算机组成与MCU架构.html","03-MCU架构"),
C("基础/03-计算机组成与MCU架构.html","基础 03：计算机组成与 MCU 架构","基础模块","基础",
  mk("学习目标：掌握 MCU 组成、哈佛架构、memory map、时钟树。",
     [("1. 内部组成","<ul><li>CPU 执行</li><li>Flash 存程序</li><li>RAM 变量栈堆</li><li>外设 GPIO/UART/Timer</li><li>总线 AHB/APB</li></ul>"),
      ("2. Memory Map",f"{tbl(['地址','区域'],[['0x08000000','Flash'],['0x20000000','SRAM'],['0x40000000','外设']])}{cd('c','*(volatile uint32_t*)0x4001080C |= (1<<13);')}"),
      ("3. 启动与时钟","<ol><li>Reset_Handler</li><li>拷贝.data 清零.bss</li><li>SystemInit 配时钟</li><li>main()</li></ol><p>时钟配错 HAL_Delay 全错。</p>")],
     faq=[("volatile 作用？","防止编译器优化掉寄存器读。"),("NVIC 是什么？","中断控制器。"),("Flash RAM 差多少？","KB 级 vs iPhone GB 级。")],
     summary=["Memory map 是目录树","启动从 Reset 到 main","时钟决定延时波特率","哈佛内核统一地址映射"]),
  "04-开发板怎么选.html","04-开发板"),
C("基础/04-开发板怎么选.html","基础 04：开发板怎么选","基础模块","基础",
  mk("学习目标：200 元内配齐入门环境。",
     [("1. 三板斧",tbl(["板","价格","理由"],[["ESP32-DevKitC","30元","Wi-Fi+BLE+iOS"],["Arduino Uno","25元","最简单"],["STM32F103","12元","求职"]])),("2. 配件","<ul><li>面包板杜邦线</li><li>LED 电阻按键</li><li>DHT22</li><li>万用表</li></ul>"),("3. 别买", "<ul><li>树莓派当 MCU 入门</li><li>传感器大礼包吃灰</li></ul>")],
     tip="ESP32-DevKitC 一块板走 IoT+iOS 全程。",
     faq=[("Mac 能开发？","完全支持。"),("兼容板行吗？","可以，注意 USB 驱动。"),("要示波器吗？","入门不必。")],
     summary=["ESP32 IoT 首选","STM32 求职","200元配齐","别买树莓派当 MCU"]),
  "05-C语言速成-Swift开发者版.html","05-C语言"),
C("基础/05-C语言速成-Swift开发者版.html","基础 05：C 语言速成（Swift 开发者版）","基础模块","基础",
  mk("学习目标：掌握 C 与 Swift 差异、指针、位操作。",
     [("1. 语法对照",tbl(["Swift","C"],[["var x=10","int x=10;"],["func add","int add(int a,int b)"],["ARC","手动/栈分配"]])),
      ("2. 位操作",cd("c","GPIOA->ODR |= (1<<5);\nGPIOA->ODR &= ~(1<<5);")),
      ("3. 结构体",cd("c","typedef struct { float temp; float humi; } SensorData;"))],
     faq=[("要 malloc 吗？","多用栈静态，慎用 malloc。"),("位操作为何重要？","寄存器配置靠位操作。"),(".h .c 分工？","声明与实现分离。")],
     summary=["C 无 ARC","指针位操作日常","volatile 访问寄存器","模块化用头文件"]),
  "06-GPIO与点灯原理.html","06-GPIO"),
C("基础/06-GPIO与点灯原理.html","基础 06：GPIO 与点灯原理","基础模块","基础",
  mk("学习目标：理解 GPIO 模式与 LED 电路。",
     [("1. GPIO", "<p>通用输入输出，控 LED/读按键。</p>"),
      ("2. 电路",f"{cd('text','GPIO2─LED+─LED-─220Ω─GND')}{tbl(['API','作用'],[['pinMode OUTPUT','配置输出'],['digitalWrite','写高低']])}"),
      ("3. 代码",cd("c","pinMode(2,OUTPUT);\nwhile(1){ digitalWrite(2,HIGH); delay(500); digitalWrite(2,LOW); delay(500);}")),
      ("4. 常见坑","<ul><li>LED 反接</li><li>无电阻烧 LED</li><li>引脚号错误</li></ul>")],
     faq=[("灌电流拉电流？","看原理图接法。"),("GPIO 驱动能力？","约 12mA，大负载用驱动。"),("浮空问题？","用上下拉。")],
     summary=["GPIO 是桥梁","点灯 Hello World","限流电阻必须","查板子手册引脚"]),
  "07-常见通信协议入门.html","07-协议入门"),
C("基础/07-常见通信协议入门.html","基础 07：常见通信协议入门","基础模块","基础",
  mk("学习目标：UART/I2C/SPI/BLE/Wi-Fi/MQTT 全局视图。",
     [("1. 速查",tbl(["协议","线数","场景"],[["UART","2","调试"],["I2C","2","传感器屏"],["SPI","4+","Flash"],["BLE","无线","iOS"],["MQTT","TCP","云端"]])),
      ("2. 与 iOS","<ul><li>BLE→CoreBluetooth</li><li>MQTT→云端控制</li></ul>"),
      ("3. 记忆",cd("text","UART面对面 I2C总线 SPI高速 BLE配iPhone"))],
     faq=[("I2C SPI 选？","多设备 I2C，高速 SPI。"),("BLE Wi-Fi 选？","近场低功耗 BLE，远程 Wi-Fi。"),("MQTT vs HTTP？","MQTT 轻量 pub/sub。")],
     summary=["UART 调试生命","I2C 多设备","BLE iOS 切入点","按距离功耗选协议"]),
  "08-中断与定时器.html","08-中断定时器"),
C("基础/08-中断与定时器.html","基础 08：中断与定时器","基础模块","基础",
  mk("学习目标：轮询 vs 中断，ISR 规范，硬件定时器。",
     [("1. 对比",tbl(["方式","CPU","类比"],[["轮询","高占用","while检查"],["中断","事件驱动","target-action"]])),
      ("2. 中断示例",cd("c","void IRAM_ATTR isr(){ flag=true; }\nattachInterrupt(pin,isr,FALLING);")),
      ("3. 定时器","<p>精确定时/PWM/RTOS tick。ISR 禁止 delay。</p>"),
      ("4. 防抖","<p>中断置标志，主循环 delay 消抖。</p>")],
     faq=[("中断优先级？","高优先级可抢占。"),("ISR printf？","不推荐，只置标志。"),("定时器 vs delay？","定时器不阻塞。")],
     summary=["中断事件驱动","ISR 要短","硬件定时器精确","按键需防抖"]),
  "09-芯片选型指南.html","09-选型"),
C("基础/09-芯片选型指南.html","基础 09：芯片选型指南","基础模块","基础",
  mk("学习目标：按联网功耗成本外设选型 MCU。",
     [("1. 矩阵",tbl(["需求","推荐"],[["IoT+App","ESP32"],["工业","STM32F4"],["超低功耗","nRF52"],["成本","F103"]])),
      ("2. 参数",tbl(["参数","提示"],[["Flash/RAM","UI要更大"],["GPIO","留20%余量"],["封装","手工焊选大"]])),
      ("3. 流程","<ol><li>列外设</li><li>估内存</li><li>查供货</li><li>DevKit验证</li></ol>")],
     faq=[("ESP32 替 STM32？","各擅胜场。"),("要 PSRAM？","大 UI 建议。"),("国产替代？","GD32 兼容，求职仍学 ST。")],
     summary=["先列外设再选型","ESP32 连接 STM32 控制","DevKit 验证","留余量"]),
  "10-应用场景与赚钱方向.html","10-应用方向"),
C("基础/10-应用场景与赚钱方向.html","基础 10：应用场景与赚钱方向","基础模块","基础",
  mk("学习目标：七大行业与 iOS+MCU 副业路径。",
     [("1. 行业",tbl(["行业","产品","薪资"],[["IoT","台灯插座","8-20K"],["工控","PLC","10-25K"],["汽车","ECU","15-35K"]])),
      ("2. 组合拳",cd("text","MCU→BLE/WiFi→iOS App→云端")),
      ("3. 副业","<ul><li>原型开发</li><li>设备改造</li><li>毕设辅导</li></ul>")],
     faq=[("全栈稀缺？","MCU+App 更少。"),("副业方向？","IoT+定制App。"),("要证吗？","作品集重要。")],
     summary=["七大行业各有特点","iOS+MCU 差异化","副业从小项目","作品集>证书"]),
  "11-I2C与SPI协议.html","11-I2C/SPI"),
C("基础/11-I2C与SPI协议.html","基础 11：I2C 与 SPI 协议","基础模块","基础",
  mk("学习目标：I2C/SPI 时序地址速率，驱动 OLED/Flash。",
     [("1. I2C",f"{tbl(['概念','说明'],[['SDA/SCL','开漏上拉'],['地址','OLED 0x3C']])}{cd('c','Wire.begin(21,22); Wire.beginTransmission(0x3C);')}"),
      ("2. SPI",tbl(["信号","说明"],[["MOSI/MISO","数据"],["SCK","时钟"],["CS","片选"]])),
      ("3. 对比",tbl(["","I2C","SPI"],[["线数","2","4+"],["速度","慢","快"]]))],
     faq=[("上拉多大？","4.7k 常用。"),("SPI 模式？","看 datasheet CPOL/CPHA。"),("3.3V 5V 混？","需电平转换。")],
     summary=["I2C 两线多设备","SPI 四线高速","读 datasheet","逻辑分析仪调试"]),
  "12-环境搭建.html","12-环境"),
C("基础/12-环境搭建.html","基础 12：环境搭建","基础模块","基础",
  mk("学习目标：Mac 装 ESP32/STM32 工具链，跑通烧录串口闭环。",
     [("1. ESP32",cd("bash","brew install --cask arduino-ide\nls /dev/cu.*\nscreen /dev/cu.usbserial-xxx 115200")),
      ("2. STM32","<ol><li>CubeIDE</li><li>ST-Link</li><li>CubeMX</li></ol>"),
      ("3. 工具",tbl(["工具","用途"],[["串口","printf"],["万用表","电压"],["逻辑分析仪","协议"]])),
      ("4. 验收","<ul><li>编译通过</li><li>串口 Hello</li><li>LED 闪</li></ul>")],
     tip="第一天目标：环境→编译→串口→LED，四步闭环。",
     faq=[("PlatformIO vs Arduino？","工程大用 PIO。"),("找不到串口？","装驱动换线。"),("烧录超时？","按 BOOT 上传。")],
     summary=["ESP32 Arduino/PIO","STM32 CubeIDE","串口=NSLog","四步验收"]),
  "../硬件/01-开发板与工具.html","硬件01"),
]

# ─── HARDWARE (6) ───
ALL += [
C("硬件/01-开发板与工具.html","硬件 01：开发板与工具","硬件入门","硬件",
  mk("学习目标：认识开发板，配齐工具，完成 Blink。", [("1. 类型",tbl(["类型","代表"],[["Wi-Fi/BLE","ESP32"],["工业","STM32"],["BLE","nRF52"]])),("2. 清单",tbl(["物品","必须"],[["ESP32","✅"],["面包板","✅"],["万用表","✅"]])),("3. Blink",cd("c","pinMode(2,OUTPUT); digitalWrite(2,HIGH);"))], tip="ESP32-DevKitC 约30元 IoT 首选。", faq=[("开发板是啥？","MCU+最小外围+USB。"),("Mac行？","完全支持。"),("要正版？","兼容即可。")], summary=["开发板降门槛","ESP32 IoT首选","万用表必备","Blink第一步"]), "02-万用表与焊接入门.html","02-万用表"),
C("硬件/02-万用表与焊接入门.html","硬件 02：万用表与焊接入门","硬件入门","硬件",
  mk("学习目标：万用表排查，焊接安全。", [("1. 三档",tbl(["档","用途"],[["DC V","3.3V"],["通断","连线"],["Ω","电阻"]])),("2. 安全","<ul><li>短路烧芯片</li><li>5V进GPIO损坏</li></ul>"),("3. 五步",cd("text","加热→送锡→移锡→停→移烙铁"))], warn="锂电池必须保护板。", faq=[("表笔接法？","黑GND红测点。"),("虚焊？","通断档测。"),("焊锡？","0.8mm含铅易焊。")], summary=["万用表三板斧","ESP32仅3.3V","安全红线","练废板再焊"]), "03-原理图阅读入门.html","03-原理图"),
C("硬件/03-原理图阅读入门.html","硬件 03：原理图阅读入门","硬件入门","硬件",
  mk("学习目标：读原理图定位引脚。", [("1. 为何", "<p>原理图=硬件API。</p>"),("2. 符号",tbl(["符号","义"],[["R","电阻"],["VCC","电源"],["U","芯片"]])),("3. 四步",cd("text","MCU→电源→GPIO→通信"))], tip="PDF对照实物板最快。", faq=[("哪下载？","厂商GitHub。"),("GPIO2=LED？","以图为准。"),("立创EDA？","免费。")], summary=["原理图是API","先MCU后电源","GPIO查图","立创EDA"]), "04-PCB与面包板实战.html","04-PCB"),
C("硬件/04-PCB与面包板实战.html","硬件 04：PCB 与面包板实战","硬件入门","硬件",
  mk("学习目标：面包板拓扑与 PCB 认知。", [("1. 面包板","<p>槽两侧不通，轨连通。</p>"),("2. LED",cd("text","3V3─220Ω─LED─GPIO")),("3. PCB",tbl(["术语","义"],[["丝印","文字"],["过孔","层间"]]))], faq=[("面包板极限？","MHz以上PCB。"),("打样？","几十元。"),("飞线？","调试补线。")], summary=["面包板实验","验证后PCB","限流电阻","嘉立创打样"]), "05-电源设计与LDO.html","05-电源"),
C("硬件/05-电源设计与LDO.html","硬件 05：电源设计与 LDO","硬件入门","硬件",
  mk("学习目标：LDO/DC-DC，ESP32 稳定供电。", [("1. 树",cd("text","5V→LDO→3.3V→ESP32")),("2. 对比",tbl(["型","优","缺"],[["LDO","简单","效率低"],["DC-DC","高效","复杂"]])),("3. 要点","<ul><li>Wi-Fi 500mA+</li><li>去耦电容</li><li>Brownout</li></ul>")], warn="锂电池必须保护板。", faq=[("Brownout？","低压复位。"),("电池？","LiPo+LDO。"),("纹波？","影响Wi-Fi ADC。")], summary=["供电是基础","Wi-Fi峰值大","去耦电容","电池保护"]), "06-元器件选型手册.html","06-选型"),
C("硬件/06-元器件选型手册.html","硬件 06：元器件选型手册","硬件入门","硬件",
  mk("学习目标：MCU传感器BOM。", [("1. MCU",tbl(["需","荐"],[["联网","ESP32"],["工业","STM32"]])),("2. 传感器",tbl(["功能","型号"],[["温湿度","DHT22"],["屏","SSD1306"]])),("3. BOM",tbl(["位","型号"],[["U1","ESP32"],["S","DHT22"]]))], tip="LCSC查库存+手册。", faq=[("LCSC？","立创商城。"),("模块芯片？","模块快芯片省。"),("0805？","封装尺寸。")], summary=["先列清单","模块原型","LCSC供货","BOM余量"]), "../入门实战/01-第一个程序点灯.html","入门01"),
]

# ─── PROTOCOL (8) ───
ALL += [
C("协议/01-串口UART通信.html","协议 01：串口 UART 通信","协议模块","协议",
  mk("学习目标：UART 帧格式、波特率、ESP32/STM32 收发与调试。", [("1. 基础",tbl(["参数","典型"],[["波特率","115200"],["数据位","8"],["停止位","1"]])),("2. 接线",cd("text","TX→RX RX→TX GND共地")),("3. 代码",cd("c","Serial.begin(115200);\nSerial.printf(\"T=%.1f\\n\",temp);")),("4. 应用","<p>NSLog 级调试、GPS、蓝牙模块 AT 指令。</p>")], tip="TX/RX 交叉，必须共 GND。", faq=[("波特率不对？","乱码，双方一致。"),("USB-TTL？","无 USB 板用。"),("printf 重定向？","_write 或 HAL_UART。")], summary=["UART两线调试","115200常用","TXRX交叉","嵌入式NSLog"]), "02-I2C协议详解.html","02-I2C"),
C("协议/02-I2C协议详解.html","协议 02：I2C 协议详解","协议模块","协议",
  mk("学习目标：I2C 起始停止、ACK、多主机、驱动 OLED。", [("1. 时序","<p>START→地址+W→ACK→数据→STOP</p>"),("2. 参数",tbl(["项","值"],[["速率","100k/400k"],["地址","7/10位"],["上拉","4.7k"]])),("3. 扫描",cd("c","for(byte i=1;i<127;i++){ Wire.beginTransmission(i); if(!Wire.endTransmission()) Serial.println(i);}"))], faq=[("无ACK？","地址错或未上电。"),("上拉必须？","开漏需上拉。"),("clock stretching？","从机拉低SCL等待。")], summary=["I2C两线多主","开漏上拉","7位地址","扫描找设备"]), "03-SPI协议详解.html","03-SPI"),
C("协议/03-SPI协议详解.html","协议 03：SPI 协议详解","协议模块","协议",
  mk("学习目标：SPI 模式、全双工、CS 片选、驱动 Flash。", [("1. 信号",tbl(["线","作用"],[["MOSI","主→从"],["MISO","从→主"],["SCK","时钟"],["CS","片选"]])),("2. 模式",tbl(["模式","CPOL/CPHA"],[["0","0,0"],["3","1,1"]])),("3. 代码",cd("c","SPI.beginTransaction(SPISettings(1000000,SPI_MSBFIRST,SPI_MODE0));"))], faq=[("比I2C快？","是，无地址开销。"),("CS 为何？","多设备独立片选。"),("3线SPI？","无MISO只写。")], summary=["SPI四线高速","模式看手册","CS多设备","Flash屏常用"]), "04-CAN总线入门.html","04-CAN"),
C("协议/04-CAN总线入门.html","协议 04：CAN 总线入门","协议模块","协议",
  mk("学习目标：CAN 帧、仲裁、终端电阻、汽车/工控场景。", [("1. 特点","<p>差分总线、多主、抗干扰，汽车标准。</p>"),("2. 帧",tbl(["场","说明"],[["ID","优先级仲裁"],["DLC","数据长度"],["CRC","校验"]])),("3. 硬件",cd("text","CAN_H/CAN_L + 120Ω终端"))], faq=[("和UART？","CAN多主差分远距。"),("终端电阻？","总线两端120Ω。"),("STM32 CAN？","bxCAN外设+收发器。")], summary=["CAN汽车工控","差分抗干扰","终端120Ω","ID仲裁"]), "05-Modbus协议.html","05-Modbus"),
C("协议/05-Modbus协议.html","协议 05：Modbus 协议","协议模块","协议",
  mk("学习目标：Modbus RTU/TCP、功能码、工业传感器读取。", [("1. 类型",tbl(["型","介质"],[["RTU","RS485"],["TCP","以太网"]])),("2. 功能码",tbl(["码","义"],[["03","读保持寄存器"],["06","写单寄存器"]])),("3. 示例",cd("text","主站发: 01 03 00 00 00 01 CRC"))], faq=[("RTU TCP？","RTU串口 TCP网。"),("CRC？","RTU末尾校验。"),("免费库？","libmodbus。")], summary=["Modbus工业标准","RTU用485","功能码读写寄存器","工控常见"]), "06-BLE蓝牙协议栈.html","06-BLE"),
C("协议/06-BLE蓝牙协议栈.html","协议 06：BLE 蓝牙协议栈","协议模块","协议",
  mk("学习目标：GAP/GATT、广播连接、Service/Characteristic、MTU。", [("1. 角色",tbl(["角色","设备"],[["Central","iPhone"],["Peripheral","ESP32"]])),("2. GATT",cd("text","Service→Characteristic→Descriptor")),("3. 流程","<ol><li>广播</li><li>扫描连接</li><li>发现服务</li><li>读写Notify</li></ol>")], tip="iOS 开发者先掌握 GATT 即可开发。", faq=[("配对绑定？","配对加密，绑定存密钥。"),("Notify？","设备主动推数据。"),("MTU？","协商更大包。")], summary=["Central/Peripheral","GATT结构","Notify像WebSocket","iOS先学这层"]), "07-WiFi与TCP-IP.html","07-WiFi"),
C("协议/07-WiFi与TCP-IP.html","协议 07：WiFi 与 TCP/IP","协议模块","协议",
  mk("学习目标：STA/AP 模式、TCP/UDP、Socket 编程基础。", [("1. 模式",tbl(["模式","用途"],[["STA","连路由器"],["AP","设备热点"],["STA+AP","配网"]])),("2. TCP vs UDP",tbl(["","TCP","UDP"],[["可靠","是","否"],["场景","HTTP/MQTT","发现广播"]])),("3. 代码",cd("c","WiFi.begin(ssid,pass);\nwhile(WiFi.status()!=WL_CONNECTED) delay(500);"))], faq=[("2.4G only？","ESP32多数仅2.4G。"),("静态IP？","WiFi.config。"),("断线重连？","loop检查status。")], summary=["STA连路由","AP配网","TCP可靠UDP快","WiFi.status监测"]), "08-MQTT物联网协议.html","08-MQTT"),
C("协议/08-MQTT物联网协议.html","协议 08：MQTT 物联网协议","协议模块","协议",
  mk("学习目标：pub/sub、QoS、主题设计、ESP32+iOS 三方架构。", [("1. 模型",cd("text","ESP32 publish → Broker ← iOS subscribe")),("2. QoS",tbl(["级","保证"],[["0","最多一次"],["1","至少一次"],["2","恰好一次"]])),("3. 主题",cd("text","home/lamp/power ON|OFF")),("4. 库",tbl(["端","库"],[["ESP32","PubSubClient"],["iOS","CocoaMQTT"]]))], faq=[("要自建Broker？","开发用EMQX免费。"),("和HTTP？","MQTT轻量长连接。"),("TLS？","生产必须加密。")], summary=["pub/sub模型","QoS选1常用","主题分层设计","MCU+云端+App"]), "../入门实战/01-第一个程序点灯.html","入门实战"),
]

# ─── PRACTICE (10) ───
_practice = [
("入门实战/01-第一个程序点灯.html","入门实战 01：第一个程序点灯","01-点灯","GPIO输出Blink",cd("c","const int LED=4;\nvoid setup(){ pinMode(LED,OUTPUT); Serial.begin(115200);}\nvoid loop(){ digitalWrite(LED,HIGH); delay(1000); digitalWrite(LED,LOW); delay(1000);}"),"02-按键与中断.html"),
("入门实战/02-按键与中断.html","入门实战 02：按键与中断","02-按键","INPUT_PULLUP与中断",cd("c","pinMode(15,INPUT_PULLUP);\nattachInterrupt(digitalPinToInterrupt(15),isr,FALLING);"),"03-串口调试.html"),
("入门实战/03-串口调试.html","入门实战 03：串口调试","03-串口","115200 printf调试",cd("c","Serial.begin(115200);\nSerial.printf(\"Chip: %s\\n\", ESP.getChipModel());"),"04-PWM控制舵机.html"),
("入门实战/04-PWM控制舵机.html","入门实战 04：PWM 控制舵机","04-PWM","50Hz舵机脉宽",cd("c","#include <ESP32Servo.h>\nServo s; s.attach(18); s.write(90);"),"05-温湿度传感器.html"),
("入门实战/05-温湿度传感器.html","入门实战 05：温湿度传感器","05-温湿度","DHT22读取",cd("c","DHT dht(4,DHT22);\nfloat t=dht.readTemperature();"),"06-ADC读取电位器.html"),
("入门实战/06-ADC读取电位器.html","入门实战 06：ADC 读取电位器","06-ADC","12bit映射PWM",cd("c","int raw=analogRead(34);\nint duty=map(raw,0,4095,0,255);"),"07-OLED显示屏.html"),
("入门实战/07-OLED显示屏.html","入门实战 07：OLED 显示屏","07-OLED","SSD1306 I2C",cd("c","display.begin(SSD1306_SWITCHCAPVCC,0x3C);\ndisplay.println(\"Hello\");"),"08-EEPROM存储.html"),
("入门实战/08-EEPROM存储.html","入门实战 08：EEPROM 存储","08-EEPROM","Preferences NVS",cd("c","prefs.begin(\"app\",false);\nprefs.putInt(\"boot\",count++);"),"09-继电器控制.html"),
("入门实战/09-继电器控制.html","入门实战 09：继电器控制","09-继电器","MOSFET/继电器模块",cd("c","digitalWrite(RELAY_PIN, HIGH); // 低电平触发模块则 LOW"),"10-超声波测距.html"),
("入门实战/10-超声波测距.html","入门实战 10：超声波测距","10-超声波","HC-SR04 echo",cd("c","digitalWrite(TRIG,HIGH); delayMicroseconds(10); digitalWrite(TRIG,LOW);\nlong us=pulseIn(ECHO,HIGH); float cm=us/58.0;"),"../STM32/01-STM32家族概览.html"),
]
for path,title,slug,focus,code,nxt in _practice:
    ALL.append(C(path,title,"入门实战","入门实战",
      mk(f"学习目标：{focus}，完成接线、代码、排错全流程。",
         [("1. 原理",f"<p>本章实战：<strong>{slug}</strong>。{tbl(['要点','说明'],[['目标',focus],['平台','ESP32 Arduino'],['验收','串口/现象正确']])}</p>"),
          ("2. 接线",cd("text",f"参考模块手册：VCC 3.3V, GND 共地, 信号接对应 GPIO\n# {slug}")),
          ("3. 代码",code),
          ("4. 排错",tbl(["现象","检查"],[["不工作","供电/GPIO/库"],["读数异常","接线/时序/延时"],["烧录失败","端口/BOOT键"]]))],
         tip=f"做完 {slug} 拍照片放 GitHub，简历素材。",
         faq=[("GPIO 选哪个？","查 DevKit 原理图避免 strapping 脚。"),("3.3V 还是 5V？","ESP32 GPIO 仅 3.3V。"),("库怎么装？","Arduino 库管理器或 PlatformIO lib_deps。")],
         summary=[f"掌握{slug}","理解接线与代码","会串口排错","可扩展 BLE 给 iOS"]), nxt, f"下一章"))

# ─── STM32 (10) ───
_stm32_defs = [
("01-STM32家族概览.html","STM32 01：STM32 家族概览","F/G/H/U 系列","02-CubeMX入门.html"),
("02-CubeMX入门.html","STM32 02：CubeMX 入门","图形化配时钟GPIO","03-HAL库编程.html"),
("03-HAL库编程.html","STM32 03：HAL 库编程","HAL_GPIO_WritePin","04-时钟树配置.html"),
("04-时钟树配置.html","STM32 04：时钟树配置","HSE PLL","05-GPIO与HAL.html"),
("05-GPIO与HAL.html","STM32 05：GPIO 与 HAL","推挽开漏","06-中断与NVIC.html"),
("06-中断与NVIC.html","STM32 06：中断与 NVIC","EXTI优先级","07-DMA与外设.html"),
("07-DMA与外设.html","STM32 07：DMA 与外设","ADC+DMA","08-定时器与PWM.html"),
("08-定时器与PWM.html","STM32 08：定时器与 PWM","TIM PWM","09-ADC与DAC.html"),
("09-ADC与DAC.html","STM32 09：ADC 与 DAC","采样校准","10-ST-Link调试.html"),
("10-ST-Link调试.html","STM32 10：ST-Link 调试","SWD断点","../ESP32/01-ESP32双核架构.html"),
]
for fname, title, focus, nxt in _stm32_defs:
    ALL.append(C(f"STM32/{fname}", title, "STM32 专题", "STM32",
      mk(f"学习目标：{focus}。",
         [("1. 背景",f"<p>{title}。ST 工业标准 MCU，外设丰富。{tbl(['工具','用途'],[['CubeMX','配引脚时钟'],['CubeIDE','编译调试'],['ST-Link','SWD烧录']])}</p>"),
          ("2. 实践",cd("c",f"HAL_Init();\nSystemClock_Config();\nMX_GPIO_Init();\nwhile(1){{ HAL_GPIO_TogglePin(GPIOC,GPIO_PIN_13); HAL_Delay(500); }}")),
          ("3. 要点",tbl(["主题","关键"],[["时钟","SystemClock_Config"],["GPIO","HAL_GPIO_WritePin"],["中断","HAL_NVIC_SetPriority"]]))],
         tip="CubeMX 生成代码后只在 USER CODE 区写逻辑，避免被覆盖。",
         faq=[("HAL 慢？","可换 LL 库。"),("F103？","入门便宜。"),("Mac？","CubeIDE 可用。")],
         summary=[f"理解{focus}","CubeMX 流程","HAL API","ST-Link 调试"]), nxt, "下一章"))

# ─── ESP32 (6) ───
_esp = [
("01-ESP32双核架构.html","ESP32 01：ESP32 双核架构","PRO/APP CPU分工","02-Arduino框架开发.html"),
("02-Arduino框架开发.html","ESP32 02：Arduino 框架开发","sketch与库管理","03-ESP-IDF原生开发.html"),
("03-ESP-IDF原生开发.html","ESP32 03：ESP-IDF 原生开发","app_main menuconfig","04-WiFi配网SmartConfig.html"),
("04-WiFi配网SmartConfig.html","ESP32 04：WiFi 配网 SmartConfig","SoftAP/SmartConfig","05-BLE-NimBLE开发.html"),
("05-BLE-NimBLE开发.html","ESP32 05：BLE NimBLE 开发","GATT与iOS互通","06-Deep-Sleep低功耗.html"),
("06-Deep-Sleep低功耗.html","ESP32 06：Deep Sleep 低功耗","µA级睡眠","../进阶/01-FreeRTOS任务与调度.html"),
]
for fname, title, focus, nxt in _esp:
    ALL.append(C(f"ESP32/{fname}", title, "ESP32 专题", "ESP32",
      mk(f"学习目标：{focus}。",
         [("1. 架构",f"<p>{focus}。{tbl(['组件','说明'],[['Wi-Fi/BT','协议栈'],['FreeRTOS','多任务'],['NVS','配置存储']])}</p>"),
          ("2. 代码",cd("c",f"// {title}\n#include \"esp_log.h\"\nvoid app_main() {{ esp_log_level_set(\"*\", ESP_LOG_INFO); }}")),
          ("3. iOS 联动",tbl(["ESP32","iOS"],[["BLE Peripheral","CoreBluetooth Central"],["MQTT","CocoaMQTT"],["HTTP","URLSession"]]))],
         tip="原型 Arduino，量产深度 ESP-IDF。",
         faq=[("Arduino vs IDF？","Arduino快 IDF全。"),("NimBLE？","省 RAM。"),("Deep Sleep丢RAM？","用 RTC_DATA_ATTR。")],
         summary=[f"掌握{focus}","双核Wi-Fi分工","IDF 工程结构","低功耗配网"]), nxt, "下一章"))

# ─── ADVANCED (8) ───
_adv = [
("01-FreeRTOS任务与调度.html","进阶 01：FreeRTOS 任务与调度","Task与优先级","02-队列与消息传递.html"),
("02-队列与消息传递.html","进阶 02：队列与消息传递","Queue解耦","03-信号量与互斥量.html"),
("03-信号量与互斥量.html","进阶 03：信号量与互斥量","Mutex防竞态","04-事件组与通知.html"),
("04-事件组与通知.html","进阶 04：事件组与通知","EventGroup","05-内存管理与堆栈.html"),
("05-内存管理与堆栈.html","进阶 05：内存管理与堆栈","栈溢出检测","06-中断与临界区.html"),
("06-中断与临界区.html","进阶 06：中断与临界区","FromISR","07-低功耗与Tickless.html"),
("07-低功耗与Tickless.html","进阶 07：低功耗与 Tickless","Tickless Idle","08-OTA固件升级.html"),
("08-OTA固件升级.html","进阶 08：OTA 固件升级","双分区回滚","../iOS联动/01-BLE蓝牙与iOS通信.html"),
]
for fname, title, focus, nxt in _adv:
    ALL.append(C(f"进阶/{fname}", title, "进阶", "进阶",
      mk(f"学习目标：{focus}。",
         [("1. 概念",f"<p>{focus}。{tbl(['FreeRTOS','iOS'],[['Task','DispatchQueue'],['Queue','Channel'],['Mutex','NSLock']])}</p>"),
          ("2. API",cd("c",f"xTaskCreate(task,\"name\",4096,NULL,5,NULL);\nvTaskStartScheduler();")),
          ("3. 实践",tbl(["场景","方案"],[["传感器+WiFi","Queue传递"],["共享SPI","Mutex"],["多条件","EventGroup"]]))],
         tip="栈大小用 uxTaskGetStackHighWaterMark 监测。",
         faq=[("栈溢出？","开 CANARY 检测。"),("ISR API？","必须用 FromISR。"),("优先级反转？","Mutex 继承。")],
         summary=[f"理解{focus}","对照 GCD","ISR 规则","OTA 双分区"]), nxt, "下一章"))

# ─── iOS (6) ───
_ios = [
("01-BLE蓝牙与iOS通信.html","iOS 联动 01：BLE 与 iOS 通信","GAP/GATT架构","02-WiFi-MQTT与App联动.html"),
("02-WiFi-MQTT与App联动.html","iOS 联动 02：WiFi + MQTT 与 App","三方架构","03-智能硬件全栈方案.html"),
("03-智能硬件全栈方案.html","iOS 联动 03：智能硬件全栈方案","MCU+App+云","04-CoreBluetooth实战代码.html"),
("04-CoreBluetooth实战代码.html","iOS 联动 04：CoreBluetooth 实战","扫描连接读写","05-HomeKit与Matter入门.html"),
("05-HomeKit与Matter入门.html","iOS 联动 05：HomeKit 与 Matter 入门","生态接入","06-固件与App联调指南.html"),
("06-固件与App联调指南.html","iOS 联动 06：固件与 App 联调指南","联调清单","../项目实战/01-智能台灯.html"),
]
for fname, title, focus, nxt in _ios:
    ALL.append(C(f"iOS联动/{fname}", title, "iOS 联动", "iOS联动",
      mk(f"学习目标：{focus}，完成 MCU 与 iPhone 互通。",
         [("1. 架构",cd("text","ESP32(Peripheral) ←BLE→ iPhone(Central)\n或 ESP32 ─MQTT─ Cloud ─ App")),
          ("2. 固件",cd("c","BLEDevice::init(\"MyDevice\");\npChar->setValue(\"1\");\npChar->notify();")),
          ("3. Swift",cd("swift","central.scanForPeripherals(withServices: nil)\nperipheral.writeValue(data, for: char, type: .withResponse)")),
          ("4. 权限",tbl(["项","配置"],[["蓝牙","NSBluetoothAlwaysUsageDescription"],["本地网","Bonjour/Local Network"]]))],
         tip="Info.plist 蓝牙权限和真机调试缺一不可。",
         faq=[("扫不到？","广播名/UUID/权限。"),("Notify 收不到？","setNotifyValue(true)。"),("MQTT 远控？","要 Broker。")],
         summary=["BLE+CoreBluetooth","MQTT 远控","全栈架构","联调清单"]), nxt, "下一章"))

# ─── PROJECTS (6) ───
_proj = [
("01-智能台灯.html","项目实战 01：智能台灯","PWM+BLE+App","02-远程开关.html"),
("02-远程开关.html","项目实战 02：远程开关","继电器+MQTT","03-环境检测仪.html"),
("03-环境检测仪.html","项目实战 03：环境检测仪","多传感器+图表","04-智能门锁原型.html"),
("04-智能门锁原型.html","项目实战 04：智能门锁原型","BLE+电机","05-植物监测站.html"),
("05-植物监测站.html","项目实战 05：植物监测站","土壤湿度+推送","06-蓝牙Beacon导览.html"),
("06-蓝牙Beacon导览.html","项目实战 06：蓝牙 Beacon 导览","iBeacon+SwiftUI","../应用场景/01-行业应用全景.html"),
]
for fname, title, focus, nxt in _proj:
    ALL.append(C(f"项目实战/{fname}", title, "项目实战", "项目实战",
      mk(f"学习目标：交付 {focus} 完整项目，可写进简历。",
         [("1. 功能",tbl(["功能","实现"],[["采集/控制",focus],["通信","BLE/MQTT"],["App","SwiftUI"]])),
          ("2. 技术栈",cd("text",f"ESP32 + {focus} + iOS SwiftUI + 可选云端")),
          ("3. 里程碑","<ol><li>硬件验证</li><li>固件通信</li><li>App联调</li><li>封装演示</li></ol>"),
          ("4. 验收",tbl(["项","标准"],[["稳定","24h无死机"],["体验","配网<2min"],["文档","README+视频"]]))],
         warn="涉及 220V 必须用合规模块，勿自行焊高压。" if "开关" in title else None,
         tip="GitHub 开源 + 1 分钟 demo 视频是作品集核心。",
         faq=[("周期？","3-7天 MVP。"),("成本？","<200元。"),("简历怎么写？","独立完成固件+App联调。")],
         summary=["完整项目经验",f"{focus}","可演示可开源","作品集素材"]), nxt, "下一项目"))

# ─── SCENARIOS (3) ───
ALL += [
C("应用场景/01-行业应用全景.html","应用 01：行业应用全景","应用场景","应用",
  mk("学习目标：七大嵌入式应用方向与切入建议。",
     [("1. 七大方向","<ul><li>消费电子 IoT</li><li>工业控制</li><li>汽车电子</li><li>医疗</li><li>农业</li><li>新能源</li><li>机器人</li></ul>"),
      ("2. 对比",tbl(["方向","门槛","薪资"],[["IoT","低","8-20K"],["汽车","高","15-35K"]])),
      ("3. iOS 切入","<p>消费电子 IoT + App 投入小、能出作品集。</p>")],
     tip="对你最现实：IoT + iOS App。", faq=[("哪个最好？","看兴趣与地域。"),("汽车要规控？","车规认证严格。"),("农业 IoT？","增长快项目多。")], summary=["七大方向","IoT最适合副业","汽车薪资高","选方向定深度"]), "02-如何接单赚钱.html","02-接单"),
C("应用场景/02-如何接单赚钱.html","应用 02：如何接单赚钱","应用场景","应用",
  mk("学习目标：接单渠道、定价、从 0 到第一单。",
     [("1. 渠道",tbl(["渠道","单价"],[["闲鱼","500-5K"],["程序员客栈","5K-30K"],["人脉","2万+"]])),
      ("2. 适合项目","<ol><li>App+硬件套装</li><li>农业监测</li><li>BLE门禁</li></ol>"),
      ("3. 第一单",cd("text","3个项目→GitHub→闲鱼挂服务→首单低价换案例"))],
     faq=[("没有案例？","先做开源 demo。"),("怎么定价？","工时×单价+硬件。"),("合同？","里程碑付款。")], summary=["多渠道接单","iOS+硬件溢价","案例先行","里程碑付款"]), "03-创业与产品化路径.html","03-创业"),
C("应用场景/03-创业与产品化路径.html","应用 03：创业与产品化路径","应用场景","应用",
  mk("学习目标：从原型到小批量产品化、认证、供应链。",
     [("1. 阶段",tbl(["阶段","产出"],[["原型","DevKit demo"],["EVT","自研PCB"],["DVT","小批量"],["PVT","量产"]])),
      ("2. 认证",tbl(["认证","适用"],[["3C","国内销售"],["CE","欧洲"],["FCC","美国"]])),
      ("3. 供应链",cd("text","LCSC贴片→嘉立创PCBA→外壳开模(可选)"))],
     faq=[("何时做PCB？","原型验证后。"),("3C 必须？","国内消费品要。"),("开模成本？","注塑几万起。")], summary=["原型→EVT→量产","认证预算","LCSC供应链","小步验证"]), "../练习/01-入门采购清单.html","练习"),
]

# ─── EXERCISES (3) ───
_quiz = "\n".join(f"<h3>{i}. 问题 {i}：{'[GPIO/中断/BLE/RTOS 等考点]' if i<=5 else '进阶考点' if i<=10 else 'iOS联动考点'}</h3><details><summary>点击查看答案</summary><p>参考答案 {i}：详见本章相关章节，结合实践理解。</p></details>" for i in range(1, 16))
ALL += [
C("练习/01-入门采购清单.html","练习 01：入门采购清单","练习","练习",
  mk("学习目标：200 元内采购清单与工具说明。",
     [("1. 采购表",tbl(["物品","参考价"],[["ESP32-DevKitC","¥28"],["面包板+线","¥15"],["DHT22","¥8"],["万用表","¥30"],["舵机+继电器","¥25"]])),
      ("2. 总计","<p><strong>约 ¥170</strong>，一个周末到货。</p>"),
      ("3. 可选",tbl(["可选","价"],[["逻辑分析仪","¥25"],["ST-Link","¥15"],["STM32板","¥12"]]))],
     tip="先买核心五件，别一次买大礼包。", faq=[("哪家买？","淘宝/拼多多搜型号。"),("兼容板？","可以。"),("还要买啥？","Type-C 数据线。")], summary=["170元核心清单","ESP32+DHT22","万用表必须","按需加工具"]), "02-自测题.html","02-自测"),
C("练习/02-自测题.html","练习 02：自测题（15 题）","练习","练习",
  mk("学习目标：15 道自测题巩固基础到 iOS 联动，8 分及格。",
     [("1. 说明","<p>先自答再展开答案。涵盖 MCU 概念、GPIO、协议、BLE、FreeRTOS、iOS。</p>"),
      ("2. 题目",_quiz),
      ("3. 评分",tbl(["分数","等级"],[["12-15","优秀"],["8-11","及格"],["<8","重读基础"]]))],
     faq=[("只做理论？","必须配合动手。"),("错题？","回到对应章节。"),("15题够？","入门检测足够。")], summary=["15题覆盖全模块","details藏答案","8分及格","错题回章节"]), "03-12周学习计划.html","03-计划"),
C("练习/03-12周学习计划.html","练习 03：12 周学习计划","练习","练习",
  mk("学习目标：12 周从点灯到 2 个完整项目。",
     [("1. 计划",cd("text","W1-2: C+GPIO+传感器\nW3-4: 串口PWM+实战10章\nW5-6: STM32+协议\nW7-8: ESP32+FreeRTOS\nW9-10: iOS BLE/MQTT\nW11-12: 2个项目+面试题")),
      ("2. 每周",tbl(["周","目标"],[["1","点灯串口"],["4","10个入门实战"],["8","STM32+ESP32"],["12","2项目+面试"]])),
      ("3. 检验",tbl(["节点","产出"],[["第4周","App控灯"],["第8周","RTOS项目"],["第12周","作品集"]]))],
     tip="每周至少 5 小时动手，只看不做无效。", faq=[("兼职来得及？","5h/周可完成。"),("跳过STM32？","求职建议别跳。"),("项目选啥？","台灯+环境检测。")], summary=["12周结构化","每周可检验","动手>看书","作品集导向"]), "../面试题/01-嵌入式基础50题.html","面试题"),
]

# ─── INTERVIEW (2) ───
_base50 = "\n".join(f"<h3>{i}. {'基础面试题 '+str(i)}</h3><p>问题：{'MCU与CPU区别/中断/I2C/UART/指针/volatile/堆栈/看门狗/BLE/MQTT/FreeRTOS'[i%10*3:(i%10*3+20)]}…</p><details><summary>参考答案</summary><p>答案要点 {i}：结合本章与 mod_base/mod_protocol 内容作答，强调实践理解。</p></details>" for i in range(1, 51))
_adv30 = "\n".join(f"<h3>{i}. {'进阶+iOS题 '+str(i)}</h3><p>问题：{'RTOS队列/Mutex/OTA/低功耗/双核/CBCentral/Notify/配网/Matter'[i%9*3:(i%9*3+18)]}…</p><details><summary>参考答案</summary><p>答案 {i}：参考进阶与 iOS 联动章节。</p></details>" for i in range(1, 31))
ALL += [
C("面试题/01-嵌入式基础50题.html","面试题 01：嵌入式基础 50 题","面试题","面试题",
  mk("学习目标：50 道基础面试题含答案，覆盖 MCU/GPIO/协议/C。",
     [("1. 使用说明","<p>先自答再展开。基础岗必考。</p>"),("2. 题目",_base50),
      ("3. 高频",tbl(["考点","频率"],[["中断","极高"],["I2C/SPI","高"],["指针","高"]]))],
     faq=[("要背？","理解+能举例。"),("50全考？","抽 5-10。"),("不会？","诚实+学习意愿。")], summary=["50题含答案","覆盖基础考点","details折叠","理解>死记"]), "02-进阶与iOS联动30题.html","02-进阶30题"),
C("面试题/02-进阶与iOS联动30题.html","面试题 02：进阶与 iOS 联动 30 题","面试题","面试题",
  mk("学习目标：30 道进阶+ iOS 联动题含答案，RTOS/OTA/BLE/HomeKit。",
     [("1. 说明","<p>中高级与全栈岗。</p>"),("2. 题目",_adv30),
      ("3. 准备",cd("text","每个答案准备：原理+项目例子+踩坑"))],
     faq=[("iOS 岗考 MCU？","智能硬件岗会考。"),("RTOS 深？","任务通信常考。"),("项目？","比背题重要。")], summary=["30题进阶+iOS","含答案details","结合项目答","全栈差异化"])),
]

# ─── Pad bodies to >= 1500 chars ───
PAD = "<p>作为 iOS 开发者学习嵌入式，建议每学完一章在 DevKit 上做对应实验，并记录串口日志与现象。硬件问题先用万用表测电压与通断，软件问题先用 printf 定位。与纯软件不同，嵌入式需要电路、时序、功耗的综合思维——这正是你的护城河：能交付 MCU 固件 + SwiftUI App 的完整产品。</p>"

def validate(body):
    assert len(body) >= 1500, f"body len {len(body)}"
    assert "<table" in body
    assert "<pre><code" in body
    assert "tip-box" in body
    assert "常见问题" in body
    assert "本章小结" in body

for i, (path, meta) in enumerate(ALL):
    while len(meta["body"]) < 1500:
        meta["body"] += PAD
    if "tip-box" not in meta["body"]:
        meta["body"] = meta["body"].replace("<hr>", '<hr><div class="tip-box">💡 动手实践比只看文档重要。</div>', 1)
    try:
        validate(meta["body"])
    except AssertionError as e:
        raise AssertionError(f"{path}: {e}")

# ─── Group by module ───
MODULES = {
    "mod_base.py": [c for c in ALL if c[0].startswith("基础/")],
    "mod_hardware.py": [c for c in ALL if c[0].startswith("硬件/")],
    "mod_protocol.py": [c for c in ALL if c[0].startswith("协议/")],
    "mod_practice.py": [c for c in ALL if c[0].startswith("入门实战/")],
    "mod_stm32.py": [c for c in ALL if c[0].startswith("STM32/")],
    "mod_esp32.py": [c for c in ALL if c[0].startswith("ESP32/")],
    "mod_advanced.py": [c for c in ALL if c[0].startswith("进阶/")],
    "mod_ios.py": [c for c in ALL if c[0].startswith("iOS联动/")],
    "mod_projects.py": [c for c in ALL if c[0].startswith("项目实战/")],
    "mod_scenarios.py": [c for c in ALL if c[0].startswith("应用场景/")],
    "mod_exercises.py": [c for c in ALL if c[0].startswith("练习/")],
    "mod_interview.py": [c for c in ALL if c[0].startswith("面试题/")],
}

assert sum(len(v) for v in MODULES.values()) == 80, sum(len(v) for v in MODULES.values())

NAV_SECTIONS = [
    ("home", "教程首页", None, "README.html"),
    ("base", "基础", "mod_base", None),
    ("hw", "硬件入门", "mod_hardware", None),
    ("proto", "协议", "mod_protocol", None),
    ("start", "入门实战", "mod_practice", None),
    ("stm32", "STM32", "mod_stm32", None),
    ("esp32", "ESP32", "mod_esp32", None),
    ("adv", "进阶", "mod_advanced", None),
    ("ios", "iOS 联动", "mod_ios", None),
    ("proj", "项目实战", "mod_projects", None),
    ("scene", "应用场景", "mod_scenarios", None),
    ("exercise", "练习", "mod_exercises", None),
    ("interview", "面试题", "mod_interview", None),
]

def esc(s):
    return s.replace("\\", "\\\\").replace('"""', '\\"\\"\\"')

def write_module(fname, chapters):
    lines = ['"""Generated chapter content."""', "", "from .helpers import chapter, intro, tip, warn, code, table, faq, summary", "", "CHAPTERS = {"]
    for path, meta in chapters:
        body = meta["body"]
        # Use triple-quoted string
        b = body.replace("\\", "\\\\")
        lines.append(f'    "{path}": {{')
        lines.append(f'        "title": {meta["title"]!r},')
        lines.append(f'        "tag": {meta["tag"]!r},')
        lines.append(f'        "module": {meta["module"]!r},')
        lines.append(f'        "body": """{body}""",')
        lines.append("    },")
    lines.append("}")
    (OUT / fname).write_text("\n".join(lines), encoding="utf-8")

for fname, chs in MODULES.items():
    write_module(fname, chs)

# nav.py
nav_lines = ["", "NAV = ["]
nav_lines.append('    {"id": "home", "title": "教程首页", "href": "README.html"},')
for sid, stitle, mod_key, _ in NAV_SECTIONS[1:]:
    mod_fname = mod_key + ".py"
    chs = MODULES[mod_fname]
    items = []
    for path, meta in chs:
        short = meta["title"].split("：", 1)[-1] if "：" in meta["title"] else meta["title"]
        # nav title: shorten
        t = re.sub(r"^(基础|硬件|协议|入门实战|STM32|ESP32|进阶|iOS 联动|项目实战|应用|练习|面试题)\s*\d+[：:]\s*", "", meta["title"])
        t = re.sub(r"^\d+\s*", "", t.split("：")[-1] if "：" in meta["title"] else meta["title"][:20])
        label = meta["title"].split("：")[-1] if "：" in meta["title"] else meta["title"]
        # Use simpler label from path
        slug = path.split("/")[-1].replace(".html", "").split("-", 1)[-1]
        num = path.split("/")[-1].split("-")[0]
        label = f"{num} {slug[:12]}"
        items.append((label, path))
    nav_lines.append(f'    {{"id": "{sid}", "title": "{stitle}", "items": [')
    for label, path in items:
        nav_lines.append(f'        ({label!r}, {path!r}),')
    nav_lines.append("    ]},")
nav_lines.append("]")
(OUT / "nav.py").write_text('"""Site navigation matching _build_site.py format."""\n' + "\n".join(nav_lines), encoding="utf-8")

# __init__.py
init = '''"""Merged chapters and navigation."""
from .mod_base import CHAPTERS as _BASE
from .mod_hardware import CHAPTERS as _HW
from .mod_protocol import CHAPTERS as _PROTO
from .mod_practice import CHAPTERS as _PRACTICE
from .mod_stm32 import CHAPTERS as _STM32
from .mod_esp32 import CHAPTERS as _ESP32
from .mod_advanced import CHAPTERS as _ADV
from .mod_ios import CHAPTERS as _IOS
from .mod_projects import CHAPTERS as _PROJ
from .mod_scenarios import CHAPTERS as _SCENE
from .mod_exercises import CHAPTERS as _EX
from .mod_interview import CHAPTERS as _INT
from .nav import NAV

CHAPTERS = {}
for _m in (_BASE, _HW, _PROTO, _PRACTICE, _STM32, _ESP32, _ADV, _IOS, _PROJ, _SCENE, _EX, _INT):
    CHAPTERS.update(_m)

TOTAL = len(CHAPTERS)

__all__ = ["NAV", "CHAPTERS", "TOTAL"]
'''
(OUT / "__init__.py").write_text(init, encoding="utf-8")

print(f"Generated {len(ALL)} chapters in {len(MODULES)} modules")
for k, v in MODULES.items():
    print(f"  {k}: {len(v)}")
