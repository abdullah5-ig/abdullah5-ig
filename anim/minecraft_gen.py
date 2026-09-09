"""Minecraft-style animated banner, data-themed.

Everything is drawn on a small canvas (300 x 84) and then scaled up with
nearest-neighbour, which is what gives it the authentic chunky-pixel look.
No fonts are loaded — the glyphs below are a hand-built 5x7 bitmap font, so
the output is identical everywhere and depends on nothing.

The animation: blocks drop in one at a time to build a bar chart, the last
bar lights up like diamond ore, and a line of text types itself underneath.
"""

from pathlib import Path

from PIL import Image, ImageDraw

# ── 5x7 bitmap font ─────────────────────────────────────────────────────
F = {
    "A": ["01110", "10001", "10001", "11111", "10001", "10001", "10001"],
    "B": ["11110", "10001", "10001", "11110", "10001", "10001", "11110"],
    "C": ["01110", "10001", "10000", "10000", "10000", "10001", "01110"],
    "D": ["11110", "10001", "10001", "10001", "10001", "10001", "11110"],
    "E": ["11111", "10000", "10000", "11110", "10000", "10000", "11111"],
    "F": ["11111", "10000", "10000", "11110", "10000", "10000", "10000"],
    "G": ["01110", "10001", "10000", "10111", "10001", "10001", "01110"],
    "H": ["10001", "10001", "10001", "11111", "10001", "10001", "10001"],
    "I": ["11111", "00100", "00100", "00100", "00100", "00100", "11111"],
    "J": ["00111", "00010", "00010", "00010", "00010", "10010", "01100"],
    "K": ["10001", "10010", "10100", "11000", "10100", "10010", "10001"],
    "L": ["10000", "10000", "10000", "10000", "10000", "10000", "11111"],
    "M": ["10001", "11011", "10101", "10101", "10001", "10001", "10001"],
    "N": ["10001", "11001", "10101", "10011", "10001", "10001", "10001"],
    "O": ["01110", "10001", "10001", "10001", "10001", "10001", "01110"],
    "P": ["11110", "10001", "10001", "11110", "10000", "10000", "10000"],
    "Q": ["01110", "10001", "10001", "10001", "10101", "10011", "01111"],
    "R": ["11110", "10001", "10001", "11110", "10100", "10010", "10001"],
    "S": ["01111", "10000", "10000", "01110", "00001", "00001", "11110"],
    "T": ["11111", "00100", "00100", "00100", "00100", "00100", "00100"],
    "U": ["10001", "10001", "10001", "10001", "10001", "10001", "01110"],
    "V": ["10001", "10001", "10001", "10001", "10001", "01010", "00100"],
    "W": ["10001", "10001", "10001", "10101", "10101", "11011", "10001"],
    "X": ["10001", "10001", "01010", "00100", "01010", "10001", "10001"],
    "Y": ["10001", "10001", "01010", "00100", "00100", "00100", "00100"],
    "Z": ["11111", "00001", "00010", "00100", "01000", "10000", "11111"],
    "0": ["01110", "10001", "10011", "10101", "11001", "10001", "01110"],
    "1": ["00100", "01100", "00100", "00100", "00100", "00100", "01110"],
    "2": ["01110", "10001", "00001", "00010", "00100", "01000", "11111"],
    "3": ["11110", "00001", "00001", "01110", "00001", "00001", "11110"],
    "4": ["00010", "00110", "01010", "10010", "11111", "00010", "00010"],
    "5": ["11111", "10000", "11110", "00001", "00001", "10001", "01110"],
    "6": ["00110", "01000", "10000", "11110", "10001", "10001", "01110"],
    "7": ["11111", "00001", "00010", "00100", "01000", "01000", "01000"],
    "8": ["01110", "10001", "10001", "01110", "10001", "10001", "01110"],
    "9": ["01110", "10001", "10001", "01111", "00001", "00010", "01100"],
    " ": ["00000"] * 7,
    ".": ["00000", "00000", "00000", "00000", "00000", "01100", "01100"],
    ",": ["00000", "00000", "00000", "00000", "01100", "01100", "00100"],
    ":": ["00000", "01100", "01100", "00000", "01100", "01100", "00000"],
    "-": ["00000", "00000", "00000", "11111", "00000", "00000", "00000"],
    "'": ["01100", "01100", "00100", "00000", "00000", "00000", "00000"],
    "&": ["01100", "10010", "10100", "01000", "10101", "10010", "01101"],
    "@": ["01110", "10001", "10111", "10101", "10111", "10000", "01110"],
    "/": ["00001", "00010", "00010", "00100", "01000", "01000", "10000"],
    "%": ["11001", "11010", "00010", "00100", "01000", "01011", "10011"],
    "+": ["00000", "00100", "00100", "11111", "00100", "00100", "00000"],
    "·": ["00000", "00000", "00000", "01100", "01100", "00000", "00000"],
    "_": ["00000", "00000", "00000", "00000", "00000", "00000", "11111"],
}


def text_width(s, scale=1, tracking=1):
    return sum((len(F.get(c, F[" "])[0]) + tracking) * scale for c in s)


def draw_text(d, s, x, y, colour, scale=1, tracking=1):
    """Blit the bitmap font one rectangle per lit pixel."""
    cx = x
    for ch in s.upper():
        g = F.get(ch, F[" "])
        for ry, row in enumerate(g):
            for rx, bit in enumerate(row):
                if bit == "1":
                    d.rectangle(
                        [cx + rx * scale, y + ry * scale,
                         cx + rx * scale + scale - 1, y + ry * scale + scale - 1],
                        fill=colour)
        cx += (len(g[0]) + tracking) * scale
    return cx


# ── block drawing ───────────────────────────────────────────────────────
def shade(rgb, f):
    return tuple(max(0, min(255, int(c * f))) for c in rgb)


def block(d, x, y, size, base, noise=True):
    """A Minecraft-ish cube: lit top-left edge, dark bottom-right, speckled face."""
    d.rectangle([x, y, x + size - 1, y + size - 1], fill=base)
    d.line([x, y, x + size - 2, y], fill=shade(base, 1.34))          # top light
    d.line([x, y, x, y + size - 2], fill=shade(base, 1.22))          # left light
    d.line([x, y + size - 1, x + size - 1, y + size - 1],
           fill=shade(base, 0.62))                                   # bottom dark
    d.line([x + size - 1, y, x + size - 1, y + size - 1],
           fill=shade(base, 0.72))                                   # right dark
    if noise and size >= 5:
        for px, py in ((2, 2), (size - 3, 3), (3, size - 3)):
            d.point((x + px, y + py), fill=shade(base, 0.84))


# ── palette ─────────────────────────────────────────────────────────────
BG_TOP = (22, 28, 64)
BG_BOT = (14, 18, 44)
STONE = (96, 104, 132)
IRON = (124, 147, 255)
DIAMOND = (58, 214, 192)
GOLD = (224, 176, 72)
WHITE = (238, 242, 255)
DIM = (128, 141, 184)
LABEL = (143, 164, 255)

W, H, UP = 300, 84, 3          # low-res canvas, then x3 -> 900 x 252
                                # (near GitHub's content width, so pixels stay crisp)

BARS = [2, 3, 3, 4, 5, 5, 7, 9]        # blocks per bar
BS = 6                                  # block size in low-res pixels
CHART_X, CHART_BASE = 196, 74

# Max 28 characters — at 6px per char that keeps the text clear of the chart.
LINES = [
    "TURNING DATA INTO DECISIONS",
    "RISK & PORTFOLIO ANALYTICS",
    "CHURN & PRICING MODELS",
    "SQL · PYTHON · POWER BI",
]


def frame(f, N):
    img = Image.new("RGB", (W, H), BG_TOP)
    d = ImageDraw.Draw(img)

    # vertical gradient in chunky 4px bands so it stays pixel-art
    for y in range(0, H, 4):
        t = y / H
        c = tuple(int(BG_TOP[i] + (BG_BOT[i] - BG_TOP[i]) * t) for i in range(3))
        d.rectangle([0, y, W, y + 3], fill=c)

    # sparse star/ore speckle
    for sx, sy in ((28, 8), (74, 15), (132, 6), (168, 20), (250, 11), (284, 26),
                   (46, 68), (108, 74), (162, 70)):
        d.point((sx, sy), fill=(58, 68, 116))

    # ── text block ──────────────────────────────────────────────────────
    draw_text(d, "ABDULLAH NAQVI", 14, 12, WHITE, scale=2, tracking=1)
    draw_text(d, "DATA & FINTECH ANALYST", 14, 34, LABEL, scale=1, tracking=1)

    # typing line
    per = N // len(LINES)
    idx = min(f // per, len(LINES) - 1)
    t = f - idx * per
    line = LINES[idx]
    type_f = int(per * 0.55)
    hold_f = int(per * 0.28)
    if t < type_f:
        n = round(len(line) * t / type_f)
    elif t < type_f + hold_f:
        n = len(line)
    else:
        n = round(len(line) * (1 - (t - type_f - hold_f) / max(1, per - type_f - hold_f)))
    shown = line[:max(0, n)]
    endx = draw_text(d, shown, 14, 48, DIAMOND, scale=1, tracking=1)
    if (f // 3) % 2 == 0:                      # blinking caret
        d.rectangle([endx, 48, endx + 1, 54], fill=DIAMOND)

    # ── hotbar: the four tools, as inventory slots ──────────────────────
    TOOLS = [("SQL", (110, 132, 214)), ("PY", (224, 176, 72)),
             ("BI", (232, 196, 66)), ("XL", (72, 168, 108))]
    hx, hy, slot = 14, 62, 13
    for i, (_, col) in enumerate(TOOLS):
        sx = hx + i * (slot + 2)
        # slot frame, drawn like a Minecraft inventory cell
        d.rectangle([sx, hy, sx + slot - 1, hy + slot - 1], fill=(64, 72, 110))
        d.rectangle([sx + 1, hy + 1, sx + slot - 2, hy + slot - 2], fill=(40, 47, 82))
        # the item sits inside, appearing as the bars build
        if f > 6 + i * 4:
            block(d, sx + 3, hy + 3, slot - 6, col, noise=False)

    # ── bar chart: blocks drop in, one per frame, then hold ─────────────
    total = sum(BARS)
    build_f = int(N * 0.42)
    placed = total if f >= build_f else round(total * f / build_f)

    n = 0
    for i, h in enumerate(BARS):
        bx = CHART_X + i * (BS + 2)
        for lvl in range(h):
            n += 1
            if n > placed:
                break
            by = CHART_BASE - (lvl + 1) * BS
            if i == len(BARS) - 1:
                col = DIAMOND
            elif lvl == h - 1:
                col = IRON
            else:
                col = STONE
            block(d, bx, by, BS, col)

    # the top block of the tallest bar sparkles once it is placed
    if placed >= total:
        tx = CHART_X + (len(BARS) - 1) * (BS + 2)
        ty = CHART_BASE - BARS[-1] * BS
        if (f // 4) % 2 == 0:
            d.point((tx + 2, ty + 2), fill=WHITE)
            d.point((tx + BS - 3, ty + BS - 3), fill=WHITE)

    # ground line under the chart
    d.line([CHART_X - 3, CHART_BASE, W - 6, CHART_BASE], fill=(70, 80, 124))

    return img.resize((W * UP, H * UP), Image.NEAREST)


if __name__ == "__main__":
    out = Path("/home/claude/mc/frames")
    out.mkdir(parents=True, exist_ok=True)
    N = 96
    for f in range(N):
        frame(f, N).save(out / f"{f:03d}.png")
    print(f"{N} frames at {W*UP}x{H*UP}")
