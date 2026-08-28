(function () {
  'use strict';

  var pyodideReady = null;

  function decodeHtml(s) {
    var el = document.createElement('textarea');
    el.innerHTML = s;
    return el.value;
  }

  function getLang(pre) {
    var code = pre.querySelector('code');
    if (!code) return 'text';
    var cls = code.className || '';
    var m = cls.match(/language-(\w+)/);
    return m ? m[1].toLowerCase() : 'text';
  }

  function getCode(pre) {
    var code = pre.querySelector('code');
    return decodeHtml((code ? code.textContent : pre.textContent).trim());
  }

  function isRunnable(lang, code) {
    if (lang === 'javascript' || lang === 'js') return true;
    if (lang === 'html') return true;
    if (lang === 'python' || lang === 'py') {
      if (/import\s+(openai|chromadb|fastapi|mlx|torch|tensorflow)/.test(code)) return false;
      if (/subprocess|os\.system|requests\.|urllib/.test(code)) return false;
      if (/input\s*\(/.test(code)) return false;
      if (code.length > 3000) return false;
      return true;
    }
    return false;
  }

  function preFromCode() { return null; }

  function isStaticOnly(lang, code) {
    if (lang === 'bash' || lang === 'shell' || lang === 'sh' || lang === 'zsh') return true;
    if (lang === 'dart' || lang === 'swift' || lang === 'kotlin') return true;
    if (lang === 'json' && code.includes('"text"')) return true;
    if (/curl |pip install|npm |flutter |ollama |uvicorn |conda /.test(code)) return true;
    if (/^#/.test(code.trim()) && lang === 'python' && /chat\.py|translator\.py|rag_demo|web_chat/.test(code)) return true;
    return false;
  }

  function copyText(text, btn) {
    navigator.clipboard.writeText(text).then(function () {
      var orig = btn.textContent;
      btn.textContent = '已复制 ✓';
      setTimeout(function () { btn.textContent = orig; }, 1500);
    });
  }

  function wrapCodeBlock(pre) {
    if (pre.closest('.code-block-wrap') || pre.closest('.demo-card')) return;
    if (pre.closest('blockquote')) return;

    var lang = getLang(pre);
    var code = getCode(pre);
    if (!code || code.length < 3) return;
    if (lang === 'text' && (code.includes('┌─') || code.includes('├──'))) return;

    var runnable = !isStaticOnly(lang, code) && isRunnable(lang, code);
    var wrap = document.createElement('div');
    wrap.className = 'code-block-wrap';
    if (runnable) wrap.setAttribute('data-runnable', lang);

    var header = document.createElement('div');
    header.className = 'code-block-header';
    header.innerHTML = '<span class="lang-badge">' + lang + '</span><span class="' + (runnable ? 'badge-run">▶ 可运行' : 'badge-static">📋 终端命令') + '</span>';

    var actions = document.createElement('div');
    actions.className = 'code-block-actions';

    var copyBtn = document.createElement('button');
    copyBtn.type = 'button';
    copyBtn.textContent = '复制';
    copyBtn.addEventListener('click', function () { copyText(code, copyBtn); });
    actions.appendChild(copyBtn);

    if (runnable) {
      var runBtn = document.createElement('button');
      runBtn.type = 'button';
      runBtn.className = 'btn-run';
      runBtn.textContent = '▶ 运行';
      actions.appendChild(runBtn);
    }

    header.appendChild(actions);
    wrap.appendChild(header);

    if (runnable) {
      var editor = document.createElement('textarea');
      editor.className = 'playground-editor';
      editor.spellcheck = false;
      editor.value = code;
      wrap.appendChild(editor);

      var output = document.createElement('div');
      output.className = 'playground-output empty';
      output.textContent = '点击「运行」查看结果…';
      wrap.appendChild(output);

      if (lang === 'html') {
        var preview = document.createElement('div');
        preview.className = 'playground-preview';
        preview.style.display = 'none';
        wrap.appendChild(preview);
      }

      var runBtnEl = actions.querySelector('.btn-run');
      runBtnEl.addEventListener('click', function () {
        runCode(lang, editor.value, output, wrap.querySelector('.playground-preview'));
      });
    } else {
      pre.style.margin = '0';
      wrap.appendChild(pre.cloneNode(true));
      pre.remove();
    }

    pre.parentNode.insertBefore(wrap, pre);
    if (runnable) pre.remove();
  }

  function loadPyodide() {
    if (pyodideReady) return pyodideReady;
    pyodideReady = new Promise(function (resolve, reject) {
      if (window.loadPyodide) {
        window.loadPyodide({ indexURL: 'https://cdn.jsdelivr.net/pyodide/v0.26.4/full/' }).then(resolve).catch(reject);
        return;
      }
      var s = document.createElement('script');
      s.src = 'https://cdn.jsdelivr.net/pyodide/v0.26.4/full/pyodide.js';
      s.onload = function () {
        window.loadPyodide({ indexURL: 'https://cdn.jsdelivr.net/pyodide/v0.26.4/full/' }).then(resolve).catch(reject);
      };
      s.onerror = reject;
      document.head.appendChild(s);
    });
    return pyodideReady;
  }

  function runPython(code, output) {
    output.className = 'playground-output loading';
    output.textContent = '正在加载 Python 运行环境（首次约 5~10 秒）…';
    loadPyodide().then(function (pyodide) {
      var lines = [];
      pyodide.setStdout({
        batched: function (s) { lines.push(s); }
      });
      pyodide.setStderr({
        batched: function (s) { lines.push('[错误] ' + s); }
      });
      return pyodide.runPythonAsync(code).then(function (result) {
        var text = lines.join('\n');
        if (result !== undefined && result !== null && result !== '') {
          text += (text ? '\n' : '') + String(result);
        }
        output.className = 'playground-output';
        output.textContent = text || '(运行完成，无输出)';
      });
    }).catch(function (e) {
      output.className = 'playground-output error';
      output.textContent = String(e.message || e);
    });
  }

  function runJavaScript(code, output, preview) {
    output.className = 'playground-output';
    var logs = [];
    var origLog = console.log;
    console.log = function () {
      logs.push(Array.from(arguments).map(String).join(' '));
    };
    try {
      var fn = new Function(code);
      var result = fn();
      if (result !== undefined) logs.push(String(result));
      output.textContent = logs.length ? logs.join('\n') : '(运行完成，无输出)';
    } catch (e) {
      output.className = 'playground-output error';
      output.textContent = e.message;
    } finally {
      console.log = origLog;
    }
    if (preview && code.includes('<')) {
      preview.style.display = 'block';
      preview.innerHTML = '';
      var iframe = document.createElement('iframe');
      iframe.style.cssText = 'width:100%;min-height:200px;border:1px solid #e2e8f0;border-radius:8px;';
      iframe.sandbox = 'allow-scripts';
      preview.appendChild(iframe);
      iframe.contentDocument.open();
      iframe.contentDocument.write(code);
      iframe.contentDocument.close();
    }
  }

  function runCode(lang, code, output, preview) {
    if (lang === 'python' || lang === 'py') {
      runPython(code, output);
    } else if (lang === 'html') {
      runJavaScript('', output, preview);
      if (preview) {
        preview.style.display = 'block';
        preview.innerHTML = '';
        var iframe = document.createElement('iframe');
        iframe.style.cssText = 'width:100%;min-height:220px;border:1px solid #e2e8f0;border-radius:8px;';
        iframe.sandbox = 'allow-scripts';
        preview.appendChild(iframe);
        iframe.contentDocument.open();
        iframe.contentDocument.write(code);
        iframe.contentDocument.close();
      }
      output.className = 'playground-output';
      output.textContent = '↑ 上方预览区查看 HTML 效果';
    } else {
      runJavaScript(code, output, preview);
    }
  }

  /* ===== 内置交互演示 ===== */
  var DEMOS = {
    'token-demo': function (el) {
      el.innerHTML =
        '<div class="demo-card-header">🧩 交互演示：Token 分词</div><div class="demo-card-body">' +
        '<label>输入一句话，看看怎么被拆成 Token（模拟）</label>' +
        '<input type="text" id="tokenInput" value="电池要不要换" placeholder="输入中文或英文">' +
        '<button type="button" class="btn-run" id="tokenBtn" style="padding:8px 20px;border:none;border-radius:8px;background:#16a34a;color:#fff;cursor:pointer;margin-bottom:12px">拆分</button>' +
        '<div class="demo-result"><strong>Token 列表：</strong><div class="demo-tags" id="tokenOut"></div></div></div>';
      document.getElementById('tokenBtn').onclick = function () {
        var text = document.getElementById('tokenInput').value.trim();
        var tokens = [];
        if (/[\u4e00-\u9fff]/.test(text)) {
          var i = 0;
          while (i < text.length) {
            if (i + 1 < text.length && ['要不要', '是不是', '能不能'].some(function (w) { return text.slice(i).startsWith(w); })) {
              tokens.push(text.slice(i, i + 3)); i += 3;
            } else { tokens.push(text[i]); i++; }
          }
        } else {
          tokens = text.split(/(\s+)/).filter(function (t) { return t.trim(); });
        }
        document.getElementById('tokenOut').innerHTML = tokens.map(function (t, idx) {
          return '<span class="demo-tag">' + (idx + 1) + '. ' + t + '</span>';
        }).join('');
      };
      document.getElementById('tokenBtn').click();
    },

    'temp-demo': function (el) {
      var words = [
        { w: '建议', p: 45 }, { w: '考虑', p: 20 }, { w: '去', p: 8 },
        { w: '先', p: 5 }, { w: '睡觉', p: 2 }, { w: '换', p: 12 }, { w: '等等', p: 8 }
      ];
      el.innerHTML =
        '<div class="demo-card-header">🌡️ 交互演示：Temperature 温度采样</div><div class="demo-card-body">' +
        '<label>温度值：<span id="tempVal">0.7</span>（越低越稳，越高越随机）</label>' +
        '<input type="range" id="tempSlider" min="0.1" max="2" step="0.1" value="0.7">' +
        '<div id="tempBars"></div>' +
        '<button type="button" id="sampleBtn" style="margin-top:12px;padding:8px 20px;border:none;border-radius:8px;background:#2563eb;color:#fff;cursor:pointer">🎲 抽一个字</button>' +
        '<div class="demo-result" id="sampleResult">点击按钮模拟「按概率抽签」选下一个字</div></div>';

      function softmax(arr, temp) {
        var exps = arr.map(function (p) { return Math.exp(p / temp); });
        var sum = exps.reduce(function (a, b) { return a + b; }, 0);
        return exps.map(function (e) { return e / sum * 100; });
      }

      function renderBars() {
        var temp = parseFloat(document.getElementById('tempSlider').value);
        document.getElementById('tempVal').textContent = temp.toFixed(1);
        var probs = softmax(words.map(function (x) { return x.p; }), temp);
        document.getElementById('tempBars').innerHTML = words.map(function (x, i) {
          return '<div class="demo-bar-row"><span class="bar-label">' + x.w + '</span>' +
            '<div class="bar-track"><div class="bar-fill" style="width:' + probs[i].toFixed(1) + '%"></div></div>' +
            '<span class="bar-pct">' + probs[i].toFixed(1) + '%</span></div>';
        }).join('');
        el._probs = probs;
      }

      document.getElementById('tempSlider').oninput = renderBars;
      document.getElementById('sampleBtn').onclick = function () {
        var temp = parseFloat(document.getElementById('tempSlider').value);
        var probs = softmax(words.map(function (x) { return x.p; }), temp);
        var r = Math.random() * 100, acc = 0, picked = words[0].w;
        for (var i = 0; i < words.length; i++) {
          acc += probs[i];
          if (r <= acc) { picked = words[i].w; break; }
        }
        document.getElementById('sampleResult').innerHTML =
          '抽中了：<strong style="font-size:20px;color:#2563eb">「' + picked + '」</strong>（温度=' + temp + '，再点可再抽）';
      };
      renderBars();
    },

    'embed-demo': function (el) {
      var words = {
        '电池': [0.8, 0.9], '电量': [0.75, 0.85], '充电': [0.7, 0.8],
        '香蕉': [-0.8, 0.2], '苹果': [-0.3, 0.5], '手机': [0.5, 0.6]
      };
      el.innerHTML =
        '<div class="demo-card-header">📐 交互演示：Embedding 语义距离</div><div class="demo-card-body">' +
        '<label>词 A</label><select id="wordA">' + Object.keys(words).map(function (w) { return '<option>' + w + '</option>'; }).join('') + '</select>' +
        '<label>词 B</label><select id="wordB">' + Object.keys(words).map(function (w) { return '<option>电池</option><option>电量</option><option>香蕉</option>'; }).join('') + '</select>' +
        '<button type="button" id="simBtn" style="padding:8px 20px;border:none;border-radius:8px;background:#16a34a;color:#fff;cursor:pointer">计算相似度</button>' +
        '<div class="demo-result" id="simResult"></div>' +
        '<canvas id="embedCanvas" width="400" height="200" style="width:100%;max-width:400px;margin-top:12px;border:1px solid #e2e8f0;border-radius:8px"></canvas></div>';

      function cosine(a, b) {
        var dot = a[0] * b[0] + a[1] * b[1];
        var na = Math.sqrt(a[0] * a[0] + a[1] * a[1]);
        var nb = Math.sqrt(b[0] * b[0] + b[1] * b[1]);
        return dot / (na * nb);
      }

      function draw() {
        var canvas = document.getElementById('embedCanvas');
        var ctx = canvas.getContext('2d');
        ctx.clearRect(0, 0, 400, 200);
        Object.keys(words).forEach(function (w) {
          var v = words[w];
          var x = 200 + v[0] * 80, y = 100 - v[1] * 60;
          ctx.beginPath(); ctx.arc(x, y, 6, 0, Math.PI * 2);
          ctx.fillStyle = '#2563eb'; ctx.fill();
          ctx.fillStyle = '#334155'; ctx.font = '12px sans-serif';
          ctx.fillText(w, x + 8, y + 4);
        });
      }

      document.getElementById('simBtn').onclick = function () {
        var a = document.getElementById('wordA').value;
        var b = document.getElementById('wordB').value;
        var sim = cosine(words[a], words[b]);
        var pct = (sim * 100).toFixed(1);
        var desc = sim > 0.8 ? '非常相近（意思差不多）' : sim > 0.5 ? '有点关系' : '关系不大';
        document.getElementById('simResult').innerHTML =
          '「' + a + '」和「' + b + '」的相似度：<strong>' + pct + '%</strong> — ' + desc;
        draw();
      };
      draw();
      document.getElementById('simBtn').click();
    },

    'prompt-demo': function (el) {
      el.innerHTML =
        '<div class="demo-card-header">✍️ 交互演示：好 Prompt vs 烂 Prompt</div><div class="demo-card-body">' +
        '<label>你的问题</label><input type="text" id="promptQ" value="帮我写个产品介绍">' +
        '<label>Prompt 风格</label><select id="promptStyle"><option value="bad">烂 Prompt（太模糊）</option><option value="good">好 Prompt（角色+格式+约束）</option></select>' +
        '<button type="button" id="promptBtn" style="padding:8px 20px;border:none;border-radius:8px;background:#2563eb;color:#fff;cursor:pointer">模拟 AI 回答</button>' +
        '<div class="demo-result" id="promptOut"></div></div>';

      var responses = {
        bad: '好的，这是一个产品介绍：我们的产品非常好，质量优秀，价格实惠，欢迎购买……（太泛，不知道卖啥）',
        good: '【产品】智能手环 X1\n【目标用户】运动爱好者\n【核心卖点】\n1. 14 天续航\n2. 心率/血氧监测\n3. 50 米防水\n【文案】X1，你的 24 小时健康管家……'
      };

      document.getElementById('promptBtn').onclick = function () {
        var style = document.getElementById('promptStyle').value;
        var q = document.getElementById('promptQ').value;
        var prefix = style === 'good'
          ? '<em style="color:#64748b">（系统提示：你是资深文案，输出格式为【产品】【目标用户】【核心卖点】【文案】）</em><br>'
          : '<em style="color:#64748b">（无系统提示，直接问）</em><br>';
        document.getElementById('promptOut').innerHTML = prefix + responses[style];
      };
      document.getElementById('promptBtn').click();
    },

    'param-demo': function (el) {
      el.innerHTML =
        '<div class="demo-card-header">🧠 交互演示：参数量 vs 模型大小</div><div class="demo-card-body">' +
        '<label>参数量（B = 十亿）</label><input type="range" id="paramSlider" min="0.5" max="70" step="0.5" value="7">' +
        '<p>当前：<strong id="paramLabel">7B</strong> 参数</p>' +
        '<div class="demo-result" id="paramOut"></div></div>';

      document.getElementById('paramSlider').oninput = function () {
        var b = parseFloat(this.value);
        document.getElementById('paramLabel').textContent = b + 'B';
        var fp16gb = (b * 2).toFixed(1);
        var q4gb = (b * 0.6).toFixed(1);
        var desc = b <= 3 ? '手机/笔电可跑（量化后）' : b <= 13 ? '16GB 内存 Mac 可跑（量化）' : '需要专业 GPU 或多卡';
        document.getElementById('paramOut').innerHTML =
          'FP16 约 <strong>' + fp16gb + ' GB</strong> · Q4 量化约 <strong>' + q4gb + ' GB</strong><br>' + desc;
      };
      document.getElementById('paramSlider').oninput();
    },

    'voice-loop-demo': function (el) {
      el.innerHTML =
        '<div class="demo-card-header">🎤 交互演示：语音助手闭环（模拟）</div><div class="demo-card-body">' +
        '<label>模拟语音输入（文字代替）</label><input type="text" id="voiceIn" value="今天天气怎么样">' +
        '<button type="button" id="voiceBtn" style="padding:8px 20px;border:none;border-radius:8px;background:#2563eb;color:#fff;cursor:pointer">🎙️ 模拟：听→想→说</button>' +
        '<div class="demo-result" id="voiceOut"></div></div>';
      document.getElementById('voiceBtn').onclick = function () {
        var q = document.getElementById('voiceIn').value;
        document.getElementById('voiceOut').innerHTML = [
          '① Speech 识别：「' + q + '」',
          '② LLM 思考：生成回答…',
          '③ TTS 播报：「今天晴，25 度，适合出门。」'
        ].join('<br>');
      };
    },

    'rag-demo': function (el) {
      el.innerHTML =
        '<div class="demo-card-header">📚 交互演示：RAG 检索问答流程</div><div class="demo-card-body">' +
        '<label>你的问题</label><input type="text" id="ragQ" value="公司年假有多少天？">' +
        '<button type="button" id="ragBtn" style="padding:8px 20px;border:none;border-radius:8px;background:#2563eb;color:#fff;cursor:pointer">模拟 RAG 回答</button>' +
        '<div class="demo-result" id="ragSteps"></div></div>';
      var docs = [
        '员工手册第3章：年假规定，入职满1年享5天，满3年享10天。',
        '考勤制度：迟到3次扣绩效，需提前在系统请假。',
        '报销流程：填写报销单，附发票，部门经理审批。'
      ];
      document.getElementById('ragBtn').onclick = function () {
        var q = document.getElementById('ragQ').value;
        var scored = docs.map(function (d) {
          var score = 0.2;
          if (/年假|假期|休假/.test(q) && /年假/.test(d)) score = 0.92;
          else if (/考勤|迟到/.test(q) && /考勤/.test(d)) score = 0.88;
          else if (/报销/.test(q) && /报销/.test(d)) score = 0.90;
          return { d: d, s: score };
        }).sort(function (a, b) { return b.s - a.s; });
        var top = scored[0];
        var steps = [
          '① 问题向量化完成',
          '② 检索文档库（3 篇），Top1 相似度 ' + (top.s * 100).toFixed(0) + '%',
          '③ 召回片段：「' + top.d + '」',
          '④ 拼进 Prompt 发给大模型',
          '⑤ 回答：<strong style="color:#2563eb">根据员工手册，入职满1年享5天年假，满3年享10天。</strong>'
        ];
        document.getElementById('ragSteps').innerHTML = steps.join('<br>');
      };
      document.getElementById('ragBtn').click();
    },

    'next-token-demo': function (el) {
      el.innerHTML =
        '<div class="demo-card-header">🔮 交互演示：猜下一个字（4 步推理）</div><div class="demo-card-body">' +
        '<label>输入上文</label><input type="text" id="ctxInput" value="电池要不要">' +
        '<button type="button" id="nextBtn" style="padding:8px 20px;border:none;border-radius:8px;background:#16a34a;color:#fff;cursor:pointer">猜下一个字</button>' +
        '<div id="stepOut" class="demo-result" style="margin-top:12px"></div></div>';

      document.getElementById('nextBtn').onclick = function () {
        var ctx = document.getElementById('ctxInput').value;
        var steps = [
          '① 分词：' + JSON.stringify(ctx.match(/[\u4e00-\u9fff]+|./g) || [ctx]),
          '② 变数字：每个词 → 1536 维向量（Embedding）',
          '③ 注意力：「要不要」和「电池」互相关注，权重 0.85',
          '④ 预测概率：「换」42% · 「更换」18% · 「充」12% · …',
          '⑤ 采样选中：<strong style="color:#2563eb;font-size:18px">「换」</strong> → 输出「' + ctx + '换」'
        ];
        document.getElementById('stepOut').innerHTML = steps.join('<br>');
      };
      document.getElementById('nextBtn').click();
    }
  };

  function injectDemos() {
    document.querySelectorAll('[data-demo]').forEach(function (el) {
      var name = el.getAttribute('data-demo');
      if (DEMOS[name]) DEMOS[name](el);
    });
  }

  function initPlaygrounds() {
    document.querySelectorAll('.content-card pre, main pre, .container pre').forEach(wrapCodeBlock);
    injectDemos();
  }

  document.addEventListener('DOMContentLoaded', initPlaygrounds);
})();
