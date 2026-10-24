# Full Claude Course

Free, self-paced, hands-on training for Claude: **9 modules, 37 lessons, 4 shareable capstones, 10 certificates**, plus a working Q&A app you deploy at the end. A static site (no build step, no server, no cost) with progress stored in each learner's browser. Independent of the separate Claude Code course.

| Module | Stage | Lessons |
|---|---|---|
| 1 Claude Basics | Foundations | 5 |
| 2 Prompt Engineering | Foundations | 7 |
| 3 Artifacts | Build | 3 |
| 4 Claude Skills | Build | 3 |
| 5 Workflow Design | Build | 3 |
| 6 Connect & Integrate | Connect & automate | 3 |
| 7 Automate | Connect & automate | 4 |
| 8 Code & Build | Connect & automate | 4 |
| 9 Ship it: RAG, GitHub, Railway | Ship | 5 |

Capstones: **Prompt Pack** (after M2), **Build-and-Reuse Kit** (after M5), **Connected Automation** (after M8), **Shipped Q&A App** (final). Each gives a downloadable share card, ready-to-post text and a Markdown portfolio entry.

## Publish on GitHub Pages (about 10 minutes, free)
1. Create a **public** repository, e.g. `claude-course`. Upload everything in this folder (keep `.github` and `.nojekyll`).
2. Settings → Pages → Deploy from a branch → `main` / `(root)`. Your site: `https://YOURNAME.github.io/claude-course/`.
3. In `index.html` set `SITE_URL` to that address (used in share posts) and change `og:image` to the full address of `assets/og.png` so link previews show the image.
4. `CODE_COURSE_URL` already points to your Claude Code course.

## Measure interaction (free)
1. Create a site at goatcounter.com (free for non-commercial use; check their terms).
2. In `index.html` uncomment the GoatCounter `<script>` at the bottom and put your code in it.
3. Events sent (as GoatCounter "events", path `ev/...`): `lesson_open/<id>`, `ex_attempt/<id>`, `ex_pass/<id>`, `prompt_copy`, `open_claude`, `quiz_submit`, `module_complete`, `cap_submit`, `cap_pass`, `cert_issued`, `share_click`, `card_download`. GoatCounter counts unique visitors per path per day.
4. **Daily report**: in GoatCounter create an API key (Username → API). In the GitHub repo add secrets `GOATCOUNTER_CODE` and `GOATCOUNTER_TOKEN`. `.github/workflows/daily-report.yml` opens an Issue every morning with visitors, interaction rate, passes, shares and the biggest drop-offs; GitHub emails you. Test it with Actions → Daily report → Run workflow. `report.py` was tested against mocked data, not a live account.
5. The in-site **Progress** tab shows each learner's own progress; its site numbers are for the device you are on only.

## Keep it fresh
`recheck-content.yml` opens an Issue on the 1st and 15th: re-check model names, plan limits, skills format and Railway pricing. Edit lessons in `assets/content-1.js` and `assets/content-2.js`, then run `node tests/validate.js` (also runs on every push). It proves every exercise can be passed.

## The capstone starter
`capstone-starter/` is a small Flask app (BM25 retrieval, Claude answers with citations, rate limit, demo mode with no key). Learners run it in Module 9, push it to their own repo and deploy it on Railway.

## Launch posts
**LinkedIn:** I built a free, hands-on Claude course. Prompting, artifacts, skills, workflows, connectors, automation, then you deploy a real Q&A app. Practice exercises run in your browser, every capstone has a share card, and each module has a certificate. Start here: LINK. Tell me which lesson confused you and I will fix it.
**X:** Free hands-on Claude course: 9 modules, 37 lessons, 4 capstones, certificates. Practice in your browser, ship a real app at the end. LINK
**Reddit (read the sub's self-promotion rules first):** Title: "I made a free interactive course for learning Claude (prompting → skills → automation → a deployed app)". Body: why you built it, what is inside, one thing you want feedback on, link last.
**Four-week rhythm:** W1 soft launch to 10 people and fix the lesson with the lowest pass rate. W2 one post per module with a screenshot. W3 Reddit and Show HN after the fixes. W4 publish first numbers and feature learner capstones.

## Notes
- "Open in Claude" uses `https://claude.ai/new?q=` to prefill the prompt; long prompts are copied instead.
- The course says plainly that features and plans change. Check Anthropic's brand guidelines before promoting commercially.
- No learner data leaves the browser except anonymous GoatCounter events, if you enable it.
