"""Daily report from GoatCounter. Prints Markdown. Env: GOATCOUNTER_CODE, GOATCOUNTER_TOKEN.
GoatCounter counts unique visitors per path per day, so event numbers are 'visitors who did X', not raw clicks."""
import datetime as dt, json, os, sys, urllib.request

def api(path, code, token, **q):
    qs = "&".join(f"{k}={v}" for k, v in q.items())
    req = urllib.request.Request(f"https://{code}.goatcounter.com/api/v0/{path}?{qs}",
                                 headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

def pct(a, b): return f"{round(100*a/b)}%" if b else "n/a"

def build(code, token, fetch=api):
    end = dt.datetime.now(dt.timezone.utc).replace(minute=0, second=0, microsecond=0)
    start = end - dt.timedelta(days=1)
    f = lambda d: d.strftime("%Y-%m-%dT%H:%M:%SZ")
    total = fetch("stats/total", code, token, start=f(start), end=f(end))
    hits = fetch("stats/hits", code, token, start=f(start), end=f(end), limit=100)["hits"]
    ev = {h["path"].lstrip("/"): h["count"] for h in hits if h.get("event")}
    g = lambda k: ev.get("ev/" + k, 0)
    visitors = total.get("total", 0) - total.get("total_events", 0)
    lessons = sorted(((k.split("/", 2)[2], v) for k, v in ev.items() if k.startswith("ev/lesson_open/")), key=lambda x: -x[1])
    passed = {k.split("/", 2)[2]: v for k, v in ev.items() if k.startswith("ev/ex_pass/")}
    gaps = sorted(((o - passed.get(l, 0), l, o) for l, o in lessons), reverse=True)
    lines = [f"## Full Claude Course report for {start:%Y-%m-%d}", "",
        f"- Visitors: **{visitors}**",
        f"- Interaction rate (tried an exercise): **{pct(g('ex_attempt'), visitors)}**",
        f"- Passed an exercise: {g('ex_pass')} · prompts copied: {g('prompt_copy')} · opened in Claude: {g('open_claude')}",
        f"- Modules completed: {g('module_complete')} · capstones passed: {g('cap_pass')} · certificates: {g('cert_issued')} · shares: {g('share_click')}", ""]
    if gaps and gaps[0][0] > 0:
        lines.append("Biggest drop-offs (opened minus passed): " + ", ".join(f"`{l}` ({o} opened, {o-d} passed)" for d, l, o in gaps[:3]))
    else:
        lines.append("Biggest drop-offs: no data yet.")
    lines += ["", "_Source: GoatCounter, last 24 hours. Visitors are unique per path._"]
    return "\n".join(lines)

if __name__ == "__main__":
    code, token = os.environ.get("GOATCOUNTER_CODE"), os.environ.get("GOATCOUNTER_TOKEN")
    if not (code and token): sys.exit("Set GOATCOUNTER_CODE and GOATCOUNTER_TOKEN")
    print(build(code, token))
