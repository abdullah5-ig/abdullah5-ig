# Fixing the broken banner

The images were referenced with a relative path (`assets/banner.png`). That works
in a normal repo README, but GitHub's **profile page** does not resolve it, so
the images showed as broken links.

This README now uses full URLs instead, which always work.

## Easiest fix — edit it in the browser (1 minute, no terminal)

1. Go to **github.com/abdullah5-ig/abdullah5-ig**
2. Click **README.md**
3. Click the **pencil** icon (top right)
4. Select everything (**Ctrl+A**) and delete it
5. Open the new `README.md` from this folder in Notepad, select all, copy
6. Paste it into the GitHub editor
7. Scroll down, click **Commit changes**, then **Commit changes** again

Refresh your profile page. The banner and charts will be there.

## Or push it from the terminal

Same as before — token in `token.txt`, then:

```
bash push_profile.sh
```
