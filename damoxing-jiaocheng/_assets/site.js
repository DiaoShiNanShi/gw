(function () {
  'use strict';

  var NAV = [
    { id: 'home', title: '教程首页', href: 'README.html' },
    { id: 'base', title: '基础', items: [
      { title: '01 大模型是什么', href: '基础/01-大模型是什么.html' },
      { title: '02 参数与参数量', href: '基础/02-参数与参数量.html' },
      { title: '03 AI发展脉络与模型选型', href: '基础/03-AI发展脉络与模型选型.html' },
      { title: '04 Transformer架构入门', href: '基础/04-Transformer架构入门.html' },
      { title: '05 Token与分词详解', href: '基础/05-Token与分词详解.html' },
      { title: '06 主流开源模型全景', href: '基础/06-主流开源模型全景.html' },
      { title: '07 大模型能力与局限', href: '基础/07-大模型能力与局限.html' },
      { title: '08 算力硬件与成本入门', href: '基础/08-算力硬件与成本入门.html' },
    ]},
    { id: 'mid', title: '中级', items: [
      { title: '01 推理原理', href: '中级/01-推理原理.html' },
      { title: '02 训练原理', href: '中级/02-训练原理.html' },
      { title: '03 注意力机制深入', href: '中级/03-注意力机制深入.html' },
      { title: '04 位置编码与Decoder结构', href: '中级/04-位置编码与Decoder结构.html' },
      { title: '05 对齐技术SFT-RLHF-DPO', href: '中级/05-对齐技术SFT-RLHF-DPO.html' },
      { title: '06 损失函数与优化器', href: '中级/06-损失函数与优化器.html' },
    ]},
    { id: 'adv', title: '高级', items: [
      { title: '01 核心技术名词（上）', href: '高级/01-核心技术名词（上）.html' },
      { title: '02 核心技术名词（下）', href: '高级/02-核心技术名词（下）.html' },
      { title: '03 架构与性能优化', href: '高级/03-架构与性能优化.html' },
      { title: '04 长上下文与语义缓存', href: '高级/04-长上下文与语义缓存.html' },
      { title: '05 量化与GGUF实战', href: '高级/05-量化与GGUF实战.html' },
      { title: '06 KV Cache与推理加速', href: '高级/06-KV Cache与推理加速.html' },
      { title: '07 MoE混合专家模型', href: '高级/07-MoE混合专家模型.html' },
      { title: '08 向量数据库全解析', href: '高级/08-向量数据库全解析.html' },
      { title: '09 端侧推理全栈', href: '高级/09-端侧推理全栈.html' },
    ]},
    { id: 'work', title: '工作实战', items: [
      { title: '01 Prompt工程实战', href: '工作实战/01-Prompt工程实战.html' },
      { title: '02 大模型API对接', href: '工作实战/02-大模型API对接.html' },
      { title: '03 RAG企业级实战', href: '工作实战/03-RAG企业级实战.html' },
      { title: '04 Agent智能体与Function-Ca', href: '工作实战/04-Agent智能体与Function-Calling.html' },
      { title: '05 微调实战', href: '工作实战/05-微调实战.html' },
      { title: '06 部署与工程化', href: '工作实战/06-部署与工程化.html' },
      { title: '07 iOS端AI开发', href: '工作实战/07-iOS端AI开发.html' },
      { title: '08 多模态与语音实战', href: '工作实战/08-多模态与语音实战.html' },
      { title: '09 LLM评测与可观测性', href: '工作实战/09-LLM评测与可观测性.html' },
      { title: '10 AI安全与合规实战', href: '工作实战/10-AI安全与合规实战.html' },
      { title: '11 LangChain与LlamaIndex', href: '工作实战/11-LangChain与LlamaIndex实战.html' },
      { title: '12 向量库Milvus与Pgvector实战', href: '工作实战/12-向量库Milvus与Pgvector实战.html' },
      { title: '13 结构化输出与JSON模式', href: '工作实战/13-结构化输出与JSON模式.html' },
      { title: '14 Graph-RAG与知识图谱', href: '工作实战/14-Graph-RAG与知识图谱.html' },
      { title: '15 语义缓存与成本优化', href: '工作实战/15-语义缓存与成本优化.html' },
      { title: '16 Docker与K8s部署入门', href: '工作实战/16-Docker与K8s部署入门.html' },
      { title: '17 前端AI流式集成', href: '工作实战/17-前端AI流式集成.html' },
      { title: '18 微调数据工程', href: '工作实战/18-微调数据工程.html' },
      { title: '19 iOS-CoreML模型部署', href: '工作实战/19-iOS-CoreML模型部署.html' },
      { title: '20 iOS端侧RAG与语音助手', href: '工作实战/20-iOS端侧RAG与语音助手.html' },
    ]},
    { id: 'ios', title: 'iOS 原生', items: [
      { title: '01 Swift语言与UIKit基础', href: 'iOS原生/01-Swift语言与UIKit基础.html' },
      { title: '02 SwiftUI与现代架构', href: 'iOS原生/02-SwiftUI与现代架构.html' },
      { title: '03 网络存储与系统框架', href: 'iOS原生/03-网络存储与系统框架.html' },
      { title: '04 Instruments性能与调试', href: 'iOS原生/04-Instruments性能与调试.html' },
      { title: '05 Objective-C与Swift混编', href: 'iOS原生/05-Objective-C与Swift混编.html' },
      { title: '06 多线程GCD与Operation', href: 'iOS原生/06-多线程GCD与Operation.html' },
      { title: '07 UITableView与UICollec', href: 'iOS原生/07-UITableView与UICollectionView.html' },
      { title: '08 AutoLayout与SnapKit', href: 'iOS原生/08-AutoLayout与SnapKit.html' },
      { title: '09 网络层架构设计', href: 'iOS原生/09-网络层架构设计.html' },
      { title: '10 CoreData与SwiftData', href: 'iOS原生/10-CoreData与SwiftData.html' },
      { title: '11 音视频与AVFoundation', href: 'iOS原生/11-音视频与AVFoundation.html' },
      { title: '12 推送通知与后台任务', href: 'iOS原生/12-推送通知与后台任务.html' },
      { title: '13 架构模式深入', href: 'iOS原生/13-架构模式深入.html' },
      { title: '14 单元测试与UI测试', href: 'iOS原生/14-单元测试与UI测试.html' },
      { title: '15 AppStore上架与审核', href: 'iOS原生/15-AppStore上架与审核.html' },
      { title: '16 Swift并发深入', href: 'iOS原生/16-Swift并发深入.html' },
      { title: '17 Combine响应式编程', href: 'iOS原生/17-Combine响应式编程.html' },
      { title: '18 Keychain与安全存储', href: 'iOS原生/18-Keychain与安全存储.html' },
    ]},
    { id: 'rev', title: 'iOS 逆向', items: [
      { title: '01 逆向基础与环境', href: 'iOS逆向/01-逆向基础与环境.html' },
      { title: '02 Hook与动态调试', href: 'iOS逆向/02-Hook与动态调试.html' },
      { title: '03 静态分析与砸壳', href: 'iOS逆向/03-静态分析与砸壳.html' },
      { title: '04 逆向实战与合规', href: 'iOS逆向/04-逆向实战与合规.html' },
      { title: '05 ARM汇编与IDA入门', href: 'iOS逆向/05-ARM汇编与IDA入门.html' },
      { title: '06 Objective-C-Runtime深', href: 'iOS逆向/06-Objective-C-Runtime深入.html' },
      { title: '07 Swift逆向与符号还原', href: 'iOS逆向/07-Swift逆向与符号还原.html' },
      { title: '08 加密签名与证书链', href: 'iOS逆向/08-加密签名与证书链.html' },
      { title: '09 抓包分析与SSL-Pinning', href: 'iOS逆向/09-抓包分析与SSL-Pinning.html' },
      { title: '10 越狱原理与Cydia插件', href: 'iOS逆向/10-越狱原理与Cydia插件.html' },
      { title: '11 加固脱壳与反调试', href: 'iOS逆向/11-加固脱壳与反调试.html' },
      { title: '12 移动安全审计实战', href: 'iOS逆向/12-移动安全审计实战.html' },
      { title: '13 Frida脚本实战集锦', href: 'iOS逆向/13-Frida脚本实战集锦.html' },
      { title: '14 网络安全与隐私合规', href: 'iOS逆向/14-网络安全与隐私合规.html' },
    ]},
    { id: 'practice', title: '练习', items: [
      { title: '01 环境搭建指南', href: '练习/01-环境搭建指南.html' },
      { title: '02 基础项目实战', href: '练习/02-基础项目实战.html' },
      { title: '03 自测题', href: '练习/03-自测题.html' },
      { title: '04 工作实战项目', href: '练习/04-工作实战项目.html' },
      { title: '05 AI项目进阶实战', href: '练习/05-AI项目进阶实战.html' },
      { title: '06 iOS综合项目实战', href: '练习/06-iOS综合项目实战.html' },
    ]},
    { id: 'interview', title: '面试题', items: [
      { title: 'iOS原生面试题大全', href: '面试题/iOS原生面试题大全.html' },
      { title: 'iOS逆向面试题大全', href: '面试题/iOS逆向面试题大全.html' },
      { title: '大模型AI应用工程师面试题集合', href: '面试题/大模型AI应用工程师面试题集合.html' },
    ]},
    { id: 'flutter', title: 'Flutter', items: [
      { title: 'Flutter是什么', href: 'Flutter/01-基础入门/01-Flutter是什么.html' },
      { title: 'Dart语言基础', href: 'Flutter/01-基础入门/02-Dart语言基础.html' },
      { title: '环境搭建与第一个App', href: 'Flutter/01-基础入门/03-环境搭建与第一个App.html' },
      { title: 'Widget基础', href: 'Flutter/01-基础入门/04-Widget基础.html' },
      { title: '布局与页面', href: 'Flutter/02-中级进阶/01-布局与页面.html' },
      { title: '状态管理', href: 'Flutter/02-中级进阶/02-状态管理.html' },
      { title: '路由导航', href: 'Flutter/02-中级进阶/03-路由导航.html' },
      { title: '网络与异步', href: 'Flutter/02-中级进阶/04-网络与异步.html' },
      { title: '动画与自定义绘制', href: 'Flutter/03-高级深入/01-动画与自定义绘制.html' },
      { title: '性能优化', href: 'Flutter/03-高级深入/02-性能优化.html' },
      { title: '底层原理', href: 'Flutter/03-高级深入/03-底层原理.html' },
      { title: '混合开发与原生交互', href: 'Flutter/03-高级深入/04-混合开发与原生交互.html' },
      { title: '项目架构与工程化', href: 'Flutter/04-工作实战/01-项目架构与工程化.html' },
      { title: '测试', href: 'Flutter/04-工作实战/02-测试.html' },
      { title: '打包与上架', href: 'Flutter/04-工作实战/03-打包与上架.html' },
      { title: '常用插件与实战案例', href: 'Flutter/04-工作实战/04-常用插件与实战案例.html' },
      { title: '面试题合集', href: 'Flutter/05-面试题与练习/01-面试题合集.html' },
      { title: '练习题与答案', href: 'Flutter/05-面试题与练习/02-练习题与答案.html' },
      { title: '项目实战题与答案', href: 'Flutter/05-面试题与练习/03-项目实战题与答案.html' },
    ]},
  ];

  var SITE_ROOTS = ['damoxing-jiaocheng', '大模型学习教程'];
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
    html += '<div class="sidebar-brand"><a href="' + p + 'README.html">大模型学习教程</a><small>104 篇 · AI + iOS + 逆向</small></div><nav class="sidebar-nav">';
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
