(function () {
  'use strict';

  var NAV = [
    { id: 'home', title: '教程首页', href: 'README.html' },
    { id: 'base', title: '基础', items: [
      { title: '01 单片机是什么', href: '基础/01-单片机是什么.html' },
      { title: '02 iOS开发者视角', href: '基础/02-从iOS开发者视角看嵌入式.html' },
      { title: '03 开发板怎么选', href: '基础/03-开发板怎么选.html' },
      { title: '04 C语言速成', href: '基础/04-C语言速成-Swift开发者版.html' },
      { title: '05 GPIO与点灯', href: '基础/05-GPIO与点灯原理.html' },
      { title: '06 通信协议入门', href: '基础/06-常见通信协议入门.html' },
      { title: '07 应用场景与方向', href: '基础/07-应用场景与赚钱方向.html' },
      { title: '08 环境搭建', href: '基础/08-工具链与环境搭建.html' },
    ]},
    { id: 'start', title: '入门实战', items: [
      { title: '01 第一个程序点灯', href: '入门实战/01-第一个程序点灯.html' },
      { title: '02 按键与中断', href: '入门实战/02-按键与中断.html' },
      { title: '03 串口调试', href: '入门实战/03-串口调试.html' },
      { title: '04 PWM与舵机', href: '入门实战/04-PWM控制舵机.html' },
      { title: '05 温湿度传感器', href: '入门实战/05-温湿度传感器.html' },
    ]},
    { id: 'adv', title: '进阶', items: [
      { title: '01 STM32入门', href: '进阶/01-STM32入门.html' },
      { title: '02 FreeRTOS基础', href: '进阶/02-FreeRTOS基础.html' },
      { title: '03 低功耗设计', href: '进阶/03-低功耗设计.html' },
      { title: '04 OTA固件升级', href: '进阶/04-OTA固件升级.html' },
    ]},
    { id: 'ios', title: 'iOS 联动', items: [
      { title: '01 BLE与iOS通信', href: 'iOS联动/01-BLE蓝牙与iOS通信.html' },
      { title: '02 WiFi与MQTT', href: 'iOS联动/02-WiFi-MQTT与App联动.html' },
      { title: '03 智能硬件全栈', href: 'iOS联动/03-智能硬件全栈方案.html' },
      { title: '04 CoreBluetooth实战', href: 'iOS联动/04-CoreBluetooth实战代码.html' },
    ]},
    { id: 'proj', title: '项目实战', items: [
      { title: '01 智能台灯', href: '项目实战/01-智能台灯.html' },
      { title: '02 远程开关', href: '项目实战/02-远程开关.html' },
      { title: '03 环境检测仪', href: '项目实战/03-环境检测仪.html' },
    ]},
    { id: 'interview', title: '面试题', items: [
      { title: '嵌入式面试题精选', href: '面试题/嵌入式面试题精选.html' },
    ]},
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
    html += '<div class="sidebar-brand"><a href="' + p + 'README.html">单片机学习教程</a><small>24 篇 · 小白友好 · iOS 联动</small></div><nav class="sidebar-nav">';
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
