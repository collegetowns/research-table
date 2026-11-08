"""Builds index.html (teacher builder) and demo.html (ready-made student activity) from src/."""
import base64, json, pathlib

src = pathlib.Path(__file__).parent / "src"
def js(o): return json.dumps(o, ensure_ascii=False).replace("<", "\\u003c")

icons = json.loads((src / "icons.json").read_text())
starters = json.loads((src / "starter-articles.json").read_text())
defaults = json.loads((src / "defaults.json").read_text())
defaults["a2"]["articles"] = starters

t = (src / "student-src.html").read_text().replace("/*__ICONS__*/{}", js(icons))
assert "/*__CONFIG__*/null" in t

demo = dict(defaults, id="demo")
pathlib.Path("demo.html").write_text(t.replace("/*__CONFIG__*/null", "/*CFG-START*/" + js(demo) + "/*CFG-END*/"))

b = (src / "builder-src.html").read_text()
for k, v in {"/*__TEMPLATE__*/": 'const TEMPLATE_B64="' + base64.b64encode(t.encode()).decode() + '";',
             "/*__DEFAULTS__*/null": js(defaults), "/*__STARTERS__*/[]": js(starters), "/*__ICONS__*/{}": js(icons)}.items():
    assert b.count(k) == 1, k
    b = b.replace(k, v)
pathlib.Path("index.html").write_text(b)
print(len(t) // 1024, "KB student template;", len(b) // 1024, "KB builder")
