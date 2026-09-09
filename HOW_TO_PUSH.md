# Updating your GitHub profile

## What's at the top

A **Minecraft-style animated banner**, data-themed:

- Blocks drop in one at a time to build a bar chart
- The tallest bar is diamond, and it sparkles once placed
- Four inventory slots fill with your tools
- A line of text types itself out and cycles through four messages

It's 900 x 252, 96 frames, **40 KB**. Everything is drawn from scratch — the
letters are a hand-built pixel font, so it loads no fonts and depends on no
outside service. The image lives in your own repo.

## Push it

**1. Make a token**

https://github.com/settings/tokens/new?scopes=repo&description=profile-readme

Expiration 7 days, tick **repo**, **Generate token**, copy it.

**2. Save it to a file**

Notepad → paste the token → **File → Save As** → this folder →
set **Save as type** to **All Files** → filename `token.txt`

**3. Run it**

Right-click inside this folder → **Open Git Bash here** → type:

```
bash push_profile.sh
```

**4. Clean up**

Delete `token.txt`, then delete the token at github.com/settings/tokens.

---

## Changing the animation

Everything lives in `anim/minecraft_gen.py`.

**The four typing lines** — the `LINES` list near the top.
Keep each one **28 characters or fewer**, or the text runs into the chart.

**The bar heights** — `BARS = [2, 3, 3, 4, 5, 5, 7, 9]` (blocks per bar).

**The colours** — the palette block: `DIAMOND`, `IRON`, `STONE`, `GOLD`.

**The tools in the inventory slots** — the `TOOLS` list inside `frame()`.

To rebuild after editing:

```bash
cd anim
python3 minecraft_gen.py
ffmpeg -framerate 12 -i frames/%03d.png -vf "palettegen=max_colors=64:stats_mode=full" -y pal.png
ffmpeg -framerate 12 -i frames/%03d.png -i pal.png -lavfi "paletteuse=dither=none" -loop 0 -y ../assets/minecraft-banner.gif
```

Needs `pillow` and `ffmpeg`. Two notes on why those flags matter:
`max_colors=64` and `dither=none` are what keep the pixel edges hard — the
defaults blur pixel art into mush.

---

## Swapping the banner

Three other headers are in this folder. Change line 1 of `README.md`:

| Want | Use |
|---|---|
| Minecraft, animated (current) | `assets/minecraft-banner.gif` |
| Your site's style, animated | `assets/banner.gif` |
| Your site's style, still image | `assets/banner-static.png` |

`urls.txt` also has the two third-party service URLs (capsule-render and
readme-typing-svg) if you'd rather go back to those.

## Files

```
README.md                     your profile page
assets/minecraft-banner.gif   the pixel banner (current header)
assets/banner.gif             alternative: your site's style, animated
assets/banner-static.png      alternative: your site's style, still
assets/*.png                  the four project charts
anim/minecraft_gen.py         source for the pixel banner
anim/frame.html               source for the other animated banner
push_profile.sh               creates/updates the repo and pushes
urls.txt                      third-party header URLs, if you want them
```
