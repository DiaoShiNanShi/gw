(function () {
  'use strict';

  var NAV = [
  {
    "id": "home",
    "title": "教程首页",
    "href": "README.html"
  },
  {
    "id": "base",
    "title": "基础",
    "items": [
      {
        "title": "01 单片机概念",
        "href": "基础/01-单片机概念.html"
      },
      {
        "title": "02 从 iOS 开发者视角看嵌入式",
        "href": "基础/02-从iOS开发者视角看嵌入式.html"
      },
      {
        "title": "03 数电基础",
        "href": "基础/03-数电基础.html"
      },
      {
        "title": "04 模电入门",
        "href": "基础/04-模电入门.html"
      },
      {
        "title": "05 开发板怎么选",
        "href": "基础/05-开发板怎么选.html"
      },
      {
        "title": "06 C 语言速成（Swift 开发者",
        "href": "基础/06-C语言速成-Swift开发者版.html"
      },
      {
        "title": "07 指针与内存",
        "href": "基础/07-指针与内存.html"
      },
      {
        "title": "08 位操作与寄存器",
        "href": "基础/08-位操作与寄存器.html"
      },
      {
        "title": "09 GPIO 与点灯原理",
        "href": "基础/09-GPIO与点灯原理.html"
      },
      {
        "title": "10 中断与定时器",
        "href": "基础/10-中断与定时器.html"
      },
      {
        "title": "11 存储器与 Flash",
        "href": "基础/11-存储器与Flash.html"
      },
      {
        "title": "12 工具链与环境搭建",
        "href": "基础/12-工具链与环境搭建.html"
      }
    ]
  },
  {
    "id": "hw",
    "title": "硬件入门",
    "items": [
      {
        "title": "01 开发板与工具",
        "href": "硬件/01-开发板与工具.html"
      },
      {
        "title": "02 万用表与焊接入门",
        "href": "硬件/02-万用表与焊接入门.html"
      },
      {
        "title": "03 原理图阅读入门",
        "href": "硬件/03-原理图阅读入门.html"
      },
      {
        "title": "04 PCB 入门",
        "href": "硬件/04-PCB入门.html"
      },
      {
        "title": "05 电源设计",
        "href": "硬件/05-电源设计.html"
      },
      {
        "title": "06 元件选型",
        "href": "硬件/06-元件选型.html"
      }
    ]
  },
  {
    "id": "proto",
    "title": "协议",
    "items": [
      {
        "title": "01 UART 详解",
        "href": "协议/01-UART详解.html"
      },
      {
        "title": "02 I2C 详解",
        "href": "协议/02-I2C详解.html"
      },
      {
        "title": "03 SPI 详解",
        "href": "协议/03-SPI详解.html"
      },
      {
        "title": "04 CAN 总线入门",
        "href": "协议/04-CAN总线入门.html"
      },
      {
        "title": "05 Modbus 协议",
        "href": "协议/05-Modbus协议.html"
      },
      {
        "title": "06 BLE 协议栈",
        "href": "协议/06-BLE协议栈.html"
      },
      {
        "title": "07 WiFi 与 TCP",
        "href": "协议/07-WiFi与TCP.html"
      },
      {
        "title": "08 MQTT 协议",
        "href": "协议/08-MQTT协议.html"
      }
    ]
  },
  {
    "id": "start",
    "title": "入门实战",
    "items": [
      {
        "title": "01 第一个程序点灯",
        "href": "入门实战/01-第一个程序点灯.html"
      },
      {
        "title": "02 按键与中断",
        "href": "入门实战/02-按键与中断.html"
      },
      {
        "title": "03 串口调试",
        "href": "入门实战/03-串口调试.html"
      },
      {
        "title": "04 PWM 控制舵机",
        "href": "入门实战/04-PWM控制舵机.html"
      },
      {
        "title": "05 温湿度传感器",
        "href": "入门实战/05-温湿度传感器.html"
      },
      {
        "title": "06 ADC 采样",
        "href": "入门实战/06-ADC采样.html"
      },
      {
        "title": "07 OLED 显示",
        "href": "入门实战/07-OLED显示.html"
      },
      {
        "title": "08 EEPROM 存储",
        "href": "入门实战/08-EEPROM存储.html"
      },
      {
        "title": "09 继电器控制",
        "href": "入门实战/09-继电器控制.html"
      },
      {
        "title": "10 超声波测距",
        "href": "入门实战/10-超声波测距.html"
      }
    ]
  },
  {
    "id": "stm32",
    "title": "STM32",
    "items": [
      {
        "title": "01 入门",
        "href": "STM32/01-入门.html"
      },
      {
        "title": "02 CubeMX 入门",
        "href": "STM32/02-CubeMX入门.html"
      },
      {
        "title": "03 时钟树配置",
        "href": "STM32/03-时钟树配置.html"
      },
      {
        "title": "04 GPIO 与 HAL",
        "href": "STM32/04-GPIO与HAL.html"
      },
      {
        "title": "05 UART 驱动",
        "href": "STM32/05-UART驱动.html"
      },
      {
        "title": "06 SPI 驱动",
        "href": "STM32/06-SPI驱动.html"
      },
      {
        "title": "07 I2C 驱动",
        "href": "STM32/07-I2C驱动.html"
      },
      {
        "title": "08 ADC 与 DMA",
        "href": "STM32/08-ADC与DMA.html"
      },
      {
        "title": "09 定时器与 PWM",
        "href": "STM32/09-定时器与PWM.html"
      },
      {
        "title": "10 看门狗",
        "href": "STM32/10-看门狗.html"
      }
    ]
  },
  {
    "id": "esp32",
    "title": "ESP32",
    "items": [
      {
        "title": "01 入门与 STM32 对比",
        "href": "ESP32/01-入门与STM32对比.html"
      },
      {
        "title": "02 WiFi STA 与 AP",
        "href": "ESP32/02-WiFi-STA与AP.html"
      },
      {
        "title": "03 BLE GATT",
        "href": "ESP32/03-BLE-GATT.html"
      },
      {
        "title": "04 Deep Sleep",
        "href": "ESP32/04-Deep-Sleep.html"
      },
      {
        "title": "05 NVS 存储",
        "href": "ESP32/05-NVS存储.html"
      },
      {
        "title": "06 HTTP 与 WebServer",
        "href": "ESP32/06-HTTP与WebServer.html"
      }
    ]
  },
  {
    "id": "adv",
    "title": "进阶",
    "items": [
      {
        "title": "01 FreeRTOS 任务",
        "href": "进阶/01-FreeRTOS任务.html"
      },
      {
        "title": "02 同步机制",
        "href": "进阶/02-同步机制.html"
      },
      {
        "title": "03 低功耗设计",
        "href": "进阶/03-低功耗设计.html"
      },
      {
        "title": "04 OTA 固件升级",
        "href": "进阶/04-OTA固件升级.html"
      },
      {
        "title": "05 Bootloader",
        "href": "进阶/05-Bootloader.html"
      },
      {
        "title": "06 内存优化",
        "href": "进阶/06-内存优化.html"
      },
      {
        "title": "07 JTAG 与 SWD 调试",
        "href": "进阶/07-JTAG与SWD调试.html"
      },
      {
        "title": "08 代码规范",
        "href": "进阶/08-代码规范.html"
      }
    ]
  },
  {
    "id": "ios",
    "title": "iOS 联动",
    "items": [
      {
        "title": "01 BLE 基础",
        "href": "iOS联动/01-BLE基础.html"
      },
      {
        "title": "02 CoreBluetooth 实战",
        "href": "iOS联动/02-CoreBluetooth实战.html"
      },
      {
        "title": "03 WiFi 配网",
        "href": "iOS联动/03-WiFi配网.html"
      },
      {
        "title": "04 MQTT App 端",
        "href": "iOS联动/04-MQTT-App端.html"
      },
      {
        "title": "05 全栈架构",
        "href": "iOS联动/05-全栈架构.html"
      },
      {
        "title": "06 后台蓝牙",
        "href": "iOS联动/06-后台蓝牙.html"
      }
    ]
  },
  {
    "id": "proj",
    "title": "项目实战",
    "items": [
      {
        "title": "01 智能台灯",
        "href": "项目实战/01-智能台灯.html"
      },
      {
        "title": "02 远程开关",
        "href": "项目实战/02-远程开关.html"
      },
      {
        "title": "03 环境监测",
        "href": "项目实战/03-环境监测.html"
      },
      {
        "title": "04 蓝牙小车",
        "href": "项目实战/04-蓝牙小车.html"
      },
      {
        "title": "05 农业 IoT",
        "href": "项目实战/05-农业IoT.html"
      },
      {
        "title": "06 工业采集",
        "href": "项目实战/06-工业采集.html"
      }
    ]
  },
  {
    "id": "scene",
    "title": "应用场景",
    "items": [
      {
        "title": "01 行业应用全景",
        "href": "应用场景/01-行业应用全景.html"
      },
      {
        "title": "02 如何接单赚钱",
        "href": "应用场景/02-如何接单赚钱.html"
      },
      {
        "title": "03 职业规划",
        "href": "应用场景/03-职业规划.html"
      }
    ]
  },
  {
    "id": "exercise",
    "title": "练习",
    "items": [
      {
        "title": "01 入门采购清单",
        "href": "练习/01-入门采购清单.html"
      },
      {
        "title": "02 自测题（15 题）",
        "href": "练习/02-自测题.html"
      },
      {
        "title": "03 12 周学习计划",
        "href": "练习/03-12周学习计划.html"
      }
    ]
  },
  {
    "id": "interview",
    "title": "面试题",
    "items": [
      {
        "title": "01 嵌入式基础 50 题",
        "href": "面试题/01-嵌入式基础50题.html"
      },
      {
        "title": "02 进阶与 iOS 联动 30 题",
        "href": "面试题/02-进阶与iOS联动30题.html"
      }
    ]
  }
];

  var SITE_ROOTS = ['danpianji-jiaocheng'];
  function getDepth() {
    var path = decodeURIComponent(window.location.pathname);
    var root = SITE_ROOTS.find(function (name) { return path.indexOf('/' + name + '/') >= 0; });
    if (root) {
      var idx = path.indexOf('/' + root + '/');
      var sub = path.slice(idx + root.length + 2);
      return sub.split('/').filter(function (p) { return p && !p.endsWith('.html'); }).length;
    }
    return path.split('/').filter(function (p) { return p && !p.endsWith('.html'); }).length;
  }
  function prefix() { var d = getDepth(); return d === 0 ? '' : Array(d + 1).join('../'); }
  function resolveHref(href) { return prefix() + href; }
  function currentFile() { return decodeURIComponent(window.location.pathname).split('/').pop() || 'README.html'; }
  function isActive(href) { return href.split('/').pop() === currentFile(); }
  function groupHasActive(g) {
    if (g.href && isActive(g.href)) return true;
    return g.items && g.items.some(function (it) { return isActive(it.href); });
  }
  function buildSidebar() {
    var p = prefix(), html = '<aside class="site-sidebar" id="siteSidebar">';
    html += '<div class="sidebar-brand"><a href="' + p + 'README.html">单片机学习教程</a><small>80 篇 · 小白友好 · iOS 联动</small></div><nav class="sidebar-nav">';
    NAV.forEach(function (group) {
      if (group.href) {
        html += '<ul class="nav-group-links"><li><a href="' + resolveHref(group.href) + '"' + (isActive(group.href) ? ' class="active"' : '') + '>' + group.title + '</a></li></ul>';
        return;
      }
      var col = groupHasActive(group) ? '' : ' collapsed';
      html += '<div class="nav-group' + col + '"><button type="button" class="nav-group-title">' + group.title + '<span class="arrow">▼</span></button><ul class="nav-group-links">';
      group.items.forEach(function (item) {
        html += '<li><a href="' + resolveHref(item.href) + '"' + (isActive(item.href) ? ' class="active"' : '') + '>' + item.title + '</a></li>';
      });
      html += '</ul></div>';
    });
    return html + '</nav></aside>';
  }
  function initLayout() {
    if (document.querySelector('.site-layout')) return;
    var toggle = document.createElement('button');
    toggle.className = 'sidebar-toggle'; toggle.id = 'sidebarToggle'; toggle.innerHTML = '☰';
    var overlay = document.createElement('div'); overlay.className = 'sidebar-overlay'; overlay.id = 'sidebarOverlay';
    var layout = document.createElement('div'); layout.className = 'site-layout';
    var main = document.createElement('div'); main.className = 'site-main';
    Array.from(document.body.childNodes).forEach(function (n) { main.appendChild(n); });
    layout.insertAdjacentHTML('afterbegin', buildSidebar()); layout.appendChild(main);
    document.body.appendChild(toggle); document.body.appendChild(overlay); document.body.appendChild(layout);
    document.querySelectorAll('.nav-group-title').forEach(function (btn) {
      btn.addEventListener('click', function () { btn.parentElement.classList.toggle('collapsed'); });
    });
    function close() { document.getElementById('siteSidebar').classList.remove('open'); overlay.classList.remove('open'); }
    toggle.addEventListener('click', function () { document.getElementById('siteSidebar').classList.toggle('open'); overlay.classList.toggle('open'); });
    overlay.addEventListener('click', close);
    document.querySelectorAll('.site-sidebar a').forEach(function (a) { a.addEventListener('click', function () { if (window.innerWidth <= 900) close(); }); });
  }
  window.SiteNav = { prefix: prefix, resolveHref: resolveHref };
  document.addEventListener('DOMContentLoaded', initLayout);
})();
