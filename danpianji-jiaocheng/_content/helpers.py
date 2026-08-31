"""HTML helpers for chapter generation."""

def tip(text):
    return f'<div class="tip-box">💡 {text}</div>'

def warn(text):
    return f'<div class="tip-box" style="border-color:#ff6b6b;background:rgba(255,107,107,.08)">⚠️ {text}</div>'

def intro(text):
    return f'<blockquote><p>{text}</p></blockquote><hr>'

def code(lang, body):
    return f'<pre><code class="language-{lang}">{body}</code></pre>'

def table(headers, rows):
    h = ''.join(f'<th>{x}</th>' for x in headers)
    body = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    return f'<table><thead><tr>{h}</tr></thead><tbody>{body}</tbody></table>'

def chapter(title, tag, module, body, next_link=None, next_label=None):
    if next_link:
        body += f'<p><strong>下一步：</strong> <a href="{next_link}">{next_label or next_link}</a></p>'
    return {"title": title, "tag": tag, "module": module, "body": body}

def faq(items):
    html = '<h2>常见问题</h2>'
    for q, a in items:
        html += f'<h3>{q}</h3><p>{a}</p>'
    return html

def summary(items):
    html = '<h2>本章小结</h2><ul>'
    for i in items:
        html += f'<li>{i}</li>'
    return html + '</ul>'
