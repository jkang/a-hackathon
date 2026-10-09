---
name: agent-reach
description: Give your AI agent eyes on the internet — search and read the sources that reach from mainland China (Exa web search, any web page, GitHub, Bilibili, XiaoHongShu, Douyin, WeChat Articles, Xiaoyuzhou Podcast, V2EX, RSS). GFW-blocked channels (Twitter/X, Reddit, YouTube, LinkedIn, Instagram) are intentionally left out so research runs fast without dead links. Use whenever you need to search, read, or research. Triggers: "search", "research", "web search", "read this link", "bilibili", "wechat article", "v2ex".
metadata:
  openclaw:
    homepage: https://github.com/Panniantong/Agent-Reach
---

# Agent Reach — Usage Guide

Upstream tools for 10 platforms that are reachable from mainland China. Call them directly. Run `agent-reach doctor` to see which channels are available.

> **Reachability note.** Twitter/X, Reddit, YouTube, LinkedIn, and Instagram are blocked by the GFW and are intentionally excluded from this toolkit — do not attempt them, as retries only add latency. Use the channels below, or reach a blocked source indirectly through Exa web search / Jina Reader when a report cites it.

## Workspace rules

- **Never create files in the agent workspace.** Use `/tmp/` for temporary output and `~/.agent-reach/` for persistent data.

## Web — any URL

```bash
curl -s "https://r.jina.ai/URL"
```

## Web search (Exa)

```bash
mcporter call 'exa.web_search_exa(query: "query", numResults: 5)'
mcporter call 'exa.get_code_context_exa(query: "code question", tokensNum: 3000)'
```

> Free shared Exa endpoint may be rate-limited. For heavy use add your own key:
> `mcporter config add exa "https://mcp.exa.ai/mcp?exaApiKey=YOUR_KEY" --scope home`

## GitHub (gh CLI)

```bash
gh search repos "query" --sort stars --limit 10
gh repo view owner/repo
gh search code "query" --language python
gh issue list -R owner/repo --state open
gh issue view 123 -R owner/repo
```

## Bilibili (yt-dlp)

```bash
yt-dlp --dump-json "https://www.bilibili.com/video/BVxxx"
yt-dlp --write-sub --write-auto-sub --sub-lang "zh-Hans,zh,en" --convert-subs vtt --skip-download -o "/tmp/%(id)s" "URL"
```

> Server IPs may get 412. Use `--cookies-from-browser chrome` or configure a proxy.

## XiaoHongShu (mcporter)

```bash
mcporter call 'xiaohongshu.search_feeds(keyword: "query")'
mcporter call 'xiaohongshu.get_feed_detail(feed_id: "xxx", xsec_token: "yyy")'
mcporter call 'xiaohongshu.get_feed_detail(feed_id: "xxx", xsec_token: "yyy", load_all_comments: true)'
```

> Requires login. Import cookies with Cookie-Editor.

## Douyin (mcporter)

```bash
mcporter call 'douyin.parse_douyin_video_info(share_link: "https://v.douyin.com/xxx/")'
mcporter call 'douyin.get_douyin_download_link(share_link: "https://v.douyin.com/xxx/")'
```

> No login needed.

## WeChat Articles

**Search** (miku_ai):
```python
python3 -c "
import asyncio
from miku_ai import get_wexin_article
async def s():
    for a in await get_wexin_article('query', 5):
        print(f'{a[\"title\"]} | {a[\"url\"]}')
asyncio.run(s())
"
```

**Read** (Camoufox — bypasses WeChat anti-bot):
```bash
cd ~/.agent-reach/tools/wechat-article-for-ai && python3 main.py "https://mp.weixin.qq.com/s/ARTICLE_ID"
```

> WeChat articles cannot be read with Jina Reader or curl. Use Camoufox.

## Xiaoyuzhou Podcast (groq-whisper + ffmpeg)

```bash
~/.agent-reach/tools/xiaoyuzhou/transcribe.sh "https://www.xiaoyuzhoufm.com/episode/EPISODE_ID"
```

> Needs ffmpeg + a free Groq API key (`agent-reach configure groq-key YOUR_KEY`). Output markdown goes to `/tmp/`.

## V2EX (public API)

```bash
curl -s "https://www.v2ex.com/api/topics/hot.json" -H "User-Agent: agent-reach/1.0"
curl -s "https://www.v2ex.com/api/topics/show.json?node_name=python&page=1" -H "User-Agent: agent-reach/1.0"
curl -s "https://www.v2ex.com/api/topics/show.json?id=TOPIC_ID" -H "User-Agent: agent-reach/1.0"
```

> No auth required. Public JSON.

## RSS (feedparser)

```python
python3 -c "
import feedparser
for e in feedparser.parse('FEED_URL').entries[:5]:
    print(f'{e.title} — {e.link}')
"
```

## Troubleshooting

- **Retry cap (important).** If a source fails, retry **at most 2–3 times**, then stop. Mark it **unreachable**, move to another channel/source, and don't loop on one dead link.
- **Channel not working?** Run `agent-reach doctor` — shows status and fix instructions.
- **Blocked source cited in a report?** Read it indirectly via Exa web search or `curl -s "https://r.jina.ai/URL"` instead of hitting the platform directly.

## Setting up a channel

If a channel needs setup (cookies, Docker, etc.), fetch the install guide:
https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
The user only provides cookies; everything else is your job.
