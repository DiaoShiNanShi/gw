#!/usr/bin/env python3
"""Build full MCU tutorial site from _content package (80 chapters)."""
from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

from _content import CHAPTERS, NAV, TOTAL

ROOT = Path(__file__).parent


def depth_of(href: str) -> int:
    return href.count("/")


def page_html(href: str, meta: dict) -> str:
    d = depth_of(href)
    prefix = "../" * d if d else ""
    mod = meta.get("module", "")
    crumb_mod = f" &nbsp;/&nbsp; {mod}" if mod else ""
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="{prefix}_assets/site.css">
<title>{meta['title']} - 单片机学习教程</title>
</head>
<body>
<div class="page-header">
  <div class="page-header-inner">
    <div class="crumb"><a href="{prefix}README.html">教程首页</a>{crumb_mod}</div>
    <h1>{meta['title']}</h1>
    <span class="header-tag">{meta['tag']}</span>
  </div>
</div>
<div class="container">
  <div class="content-card">
{meta['body']}
<em>（内容由 AI 生成，仅供参考）</em>
  </div>
</div>
<div class="page-footer">
  <p><a href="{prefix}README.html">← 返回教程首页</a> · 单片机 / 嵌入式学习教程</p>
</div>
<script src="{prefix}_assets/site.js" defer></script>
</body>
</html>
"""


def nav_to_js(nav) -> str:
    """Convert NAV tuples to site.js NAV array."""
    items = []
    for group in nav:
        if group.get("href"):
            items.append({
                "id": group["id"],
                "title": group["title"],
                "href": group["href"],
            })
            continue
        sub = []
        for title, href in group["items"]:
            sub.append({"title": title, "href": href})
        items.append({"id": group["id"], "title": group["title"], "items": sub})
    return json.dumps(items, ensure_ascii=False, indent=2)


def build_site_js() -> str:
    nav_json = nav_to_js(NAV)
    return f"""(function () {{
  'use strict';

  var NAV = {nav_json};

  var SITE_ROOTS = ['danpianji-jiaocheng'];
  function getDepth() {{
    var path = decodeURIComponent(window.location.pathname);
    var root = SITE_ROOTS.find(function (name) {{ return path.indexOf('/' + name + '/') >= 0; }});
    if (root) {{
      var idx = path.indexOf('/' + root + '/');
      var sub = path.slice(idx + root.length + 2);
      return sub.split('/').filter(function (p) {{ return p && !p.endsWith('.html'); }}).length;
    }}
    return path.split('/').filter(function (p) {{ return p && !p.endsWith('.html'); }}).length;
  }}
  function prefix() {{ var d = getDepth(); return d === 0 ? '' : Array(d + 1).join('../'); }}
  function resolveHref(href) {{ return prefix() + href; }}
  function currentFile() {{ return decodeURIComponent(window.location.pathname).split('/').pop() || 'README.html'; }}
  function isActive(href) {{ return href.split('/').pop() === currentFile(); }}
  function groupHasActive(g) {{
    if (g.href && isActive(g.href)) return true;
    return g.items && g.items.some(function (it) {{ return isActive(it.href); }});
  }}
  function buildSidebar() {{
    var p = prefix(), html = '<aside class="site-sidebar" id="siteSidebar">';
    html += '<div class="sidebar-brand"><a href="' + p + 'README.html">单片机学习教程</a><small>{TOTAL} 篇 · 小白友好 · iOS 联动</small></div><nav class="sidebar-nav">';
    NAV.forEach(function (group) {{
      if (group.href) {{
        html += '<ul class="nav-group-links"><li><a href="' + resolveHref(group.href) + '"' + (isActive(group.href) ? ' class="active"' : '') + '>' + group.title + '</a></li></ul>';
        return;
      }}
      var col = groupHasActive(group) ? '' : ' collapsed';
      html += '<div class="nav-group' + col + '"><button type="button" class="nav-group-title">' + group.title + '<span class="arrow">▼</span></button><ul class="nav-group-links">';
      group.items.forEach(function (item) {{
        html += '<li><a href="' + resolveHref(item.href) + '"' + (isActive(item.href) ? ' class="active"' : '') + '>' + item.title + '</a></li>';
      }});
      html += '</ul></div>';
    }});
    return html + '</nav></aside>';
  }}
  function initLayout() {{
    if (document.querySelector('.site-layout')) return;
    var toggle = document.createElement('button');
    toggle.className = 'sidebar-toggle'; toggle.id = 'sidebarToggle'; toggle.innerHTML = '☰';
    var overlay = document.createElement('div'); overlay.className = 'sidebar-overlay'; overlay.id = 'sidebarOverlay';
    var layout = document.createElement('div'); layout.className = 'site-layout';
    var main = document.createElement('div'); main.className = 'site-main';
    Array.from(document.body.childNodes).forEach(function (n) {{ main.appendChild(n); }});
    layout.insertAdjacentHTML('afterbegin', buildSidebar()); layout.appendChild(main);
    document.body.appendChild(toggle); document.body.appendChild(overlay); document.body.appendChild(layout);
    document.querySelectorAll('.nav-group-title').forEach(function (btn) {{
      btn.addEventListener('click', function () {{ btn.parentElement.classList.toggle('collapsed'); }});
    }});
    function close() {{ document.getElementById('siteSidebar').classList.remove('open'); overlay.classList.remove('open'); }}
    toggle.addEventListener('click', function () {{ document.getElementById('siteSidebar').classList.toggle('open'); overlay.classList.toggle('open'); }});
    overlay.addEventListener('click', close);
    document.querySelectorAll('.site-sidebar a').forEach(function (a) {{ a.addEventListener('click', function () {{ if (window.innerWidth <= 900) close(); }}); }});
  }}
  window.SiteNav = {{ prefix: prefix, resolveHref: resolveHref }};
  document.addEventListener('DOMContentLoaded', initLayout);
}})();
"""


README_BODY = f"""
<blockquote>
<p>一套面向 <strong>零基础 + 有 iOS 背景</strong> 的单片机 / 嵌入式学习体系。<br>
大白话讲解，每章配代码示例、对照表与 FAQ，帮你从「会写 App」到「能做出智能硬件」。</p>
</blockquote>
<hr>
<h2>一、学习路径（{TOTAL} 篇完整版）</h2>
<pre><code>第 1 步 基础（12 篇）→ MCU 概念 / 数电模电 / C 语言 / GPIO / 中断 / 工具链
第 2 步 硬件入门（6 篇）→ 开发板 / 焊接 / 原理图 / PCB / 电源 / 选型
第 3 步 协议（8 篇）→ UART / I2C / SPI / CAN / Modbus / BLE / WiFi / MQTT
第 4 步 入门实战（10 篇）→ 点灯 / 按键 / 串口 / PWM / 传感器 / OLED / 继电器
第 5 步 STM32（10 篇）→ CubeMX / HAL / UART·SPI·I2C / ADC·DMA / 定时器
第 6 步 ESP32（6 篇）→ WiFi / BLE GATT / Deep Sleep / NVS / WebServer
第 7 步 进阶（8 篇）→ FreeRTOS / 同步 / 低功耗 / OTA / Bootloader / 调试
第 8 步 iOS 联动（6 篇）→ CoreBluetooth / 配网 / MQTT / 全栈 / 后台蓝牙
第 9 步 项目实战（6 篇）→ 台灯 / 远程开关 / 环境监测 / 小车 / 农业 / 工业
第 10 步 应用场景（3 篇）→ 行业全景 / 接单赚钱 / 职业规划
第 11 步 练习（3 篇）→ 采购清单 / 自测题 / 12 周计划
第 12 步 面试题（2 篇）→ 基础 50 题 + 进阶 iOS 联动 30 题</code></pre>
<h2>二、模块速览</h2>
<table>
<thead><tr><th>模块</th><th>篇数</th><th>学完你能做什么</th></tr></thead>
<tbody>
<tr><td>基础</td><td>12</td><td>搞懂 MCU、数电模电、C 语言、GPIO、中断</td></tr>
<tr><td>硬件入门</td><td>6</td><td>工具、焊接、原理图、PCB、电源设计</td></tr>
<tr><td>协议</td><td>8</td><td>UART/I2C/SPI/CAN/Modbus/BLE/MQTT 全掌握</td></tr>
<tr><td>入门实战</td><td>10</td><td>独立点灯、读传感器、OLED、继电器</td></tr>
<tr><td>STM32</td><td>10</td><td>CubeMX + HAL 工业级开发</td></tr>
<tr><td>ESP32</td><td>6</td><td>WiFi/BLE IoT 开发</td></tr>
<tr><td>进阶</td><td>8</td><td>FreeRTOS、OTA、低功耗、调试</td></tr>
<tr><td>iOS 联动</td><td>6</td><td>CoreBluetooth 控制硬件（核心竞争力）</td></tr>
<tr><td>项目实战</td><td>6</td><td>6 个可写进简历的完整项目</td></tr>
<tr><td>应用场景</td><td>3</td><td>行业方向、接单、职业规划</td></tr>
<tr><td>练习</td><td>3</td><td>采购、自测、12 周计划</td></tr>
<tr><td>面试题</td><td>2</td><td>80 道高频面试题</td></tr>
</tbody>
</table>
<h2>三、推荐硬件（约 200 元入门）</h2>
<ul>
<li>ESP32-DevKitC × 1（约 30 元）</li>
<li>STM32F103 最小系统板 × 1（约 12 元）</li>
<li>面包板 + 杜邦线 + LED + 电阻 + 按键</li>
<li>DHT22 温湿度 + OLED 屏 + 继电器模块</li>
<li>万用表（约 30 元）</li>
</ul>
<h2>四、快速入口</h2>
<ul>
<li><a href="基础/01-单片机概念.html">基础/01-单片机概念</a></li>
<li><a href="入门实战/01-第一个程序点灯.html">入门实战/01-第一个程序点灯</a></li>
<li><a href="iOS联动/02-CoreBluetooth实战.html">iOS联动/02-CoreBluetooth 实战</a></li>
<li><a href="项目实战/01-智能台灯.html">项目实战/01-智能台灯</a></li>
<li><a href="面试题/01-嵌入式基础50题.html">面试题/嵌入式基础 50 题</a></li>
</ul>
<h2>五、开始学习</h2>
<p>👉 从 <a href="基础/01-单片机概念.html">基础/01-单片机概念</a> 开始。</p>
"""


def clean_stale_outputs(valid_paths: set[str]) -> None:
    """Remove HTML files/dirs not in the canonical chapter list."""
    skip = {"_assets", "_content", "__pycache__"}
    for path in sorted(ROOT.rglob("*.html")):
        rel = path.relative_to(ROOT).as_posix()
        if rel in valid_paths or rel in {"README.html", "index.html"}:
            continue
        if any(part.startswith("_") or part in skip for part in path.parts):
            continue
        path.unlink()
        print("removed stale", rel)
    for d in sorted(ROOT.iterdir()):
        if not d.is_dir() or d.name.startswith("_") or d.name in skip:
            continue
        if d.name == "实战":
            shutil.rmtree(d)
            print("removed stale dir", d.name)


def main() -> None:
    valid = set(CHAPTERS.keys())
    for href, meta in CHAPTERS.items():
        out = ROOT / href
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page_html(href, meta), encoding="utf-8")

    readme = page_html("README.html", {
        "title": "单片机 / 嵌入式学习教程",
        "tag": f"{TOTAL} 篇 · 小白友好 · iOS 开发者专属路径",
        "module": "",
        "body": README_BODY,
    })
    (ROOT / "README.html").write_text(readme, encoding="utf-8")

    index = """<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="refresh" content="0; url=README.html">
  <title>单片机学习教程</title>
  <script>location.replace('README.html');</script>
</head>
<body>
  <p>正在跳转到 <a href="README.html">单片机学习教程</a>…</p>
</body>
</html>
"""
    (ROOT / "index.html").write_text(index, encoding="utf-8")
    (ROOT / "_assets" / "site.js").write_text(build_site_js(), encoding="utf-8")

    clean_stale_outputs(valid)
    print(f"done: {TOTAL} chapters + README + site.js")


if __name__ == "__main__":
    main()
