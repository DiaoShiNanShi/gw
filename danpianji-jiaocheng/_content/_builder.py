"""Shared chapter body builder for _content modules."""

def mk_body(intro_text, sections, tips=None, faq_items=None, summary_items=None, next_link=None, next_label=None):
    """Build HTML body with intro, h2 sections, tips, FAQ, summary."""
    parts = [f'<blockquote><p>{intro_text}</p></blockquote><hr>']
    for title, html in sections:
        parts.append(f'<h2>{title}</h2>\n{html.strip()}')
    if tips:
        for t in tips:
            parts.append(f'<div class="tip-box">{t}</div>')
    if faq_items:
        parts.append('<h2>常见问题</h2>')
        for q, a in faq_items:
            parts.append(f'<h3>{q}</h3><p>{a}</p>')
    if summary_items:
        parts.append('<h2>本章小结</h2><ul>')
        for item in summary_items:
            parts.append(f'<li>{item}</li>')
        parts.append('</ul>')
    if next_link:
        parts.append(f'<p><strong>下一步：</strong> <a href="{next_link}">{next_label or next_link}</a></p>')
    return '\n'.join(parts)


def sec_table(headers, rows):
    h = ''.join(f'<th>{x}</th>' for x in headers)
    body = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    return f'<table><thead><tr>{h}</tr></thead><tbody>{body}</tbody></table>'


def sec_code(lang, body):
    return f'<pre><code class="language-{lang}">{body}</code></pre>'
