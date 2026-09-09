# Updating your GitHub profile

This folder is your profile README — the special repo named `abdullah5-ig`,
which GitHub displays at the top of your profile page.

## Push it

**1. Make a token**

https://github.com/settings/tokens/new?scopes=repo&description=profile-readme

Expiration 7 days, check **repo** is ticked, click **Generate token**, copy it.

**2. Save it to a file**

Open Notepad, paste the token, then **File → Save As**:

- Navigate to this folder (the one with `README.md` in it)
- Set **Save as type** to **All Files**
- Filename: `token.txt`

**3. Run it**

Right-click inside this folder → **Open Git Bash here**, then type:

```
bash push_profile.sh
```

**4. Clean up**

Delete `token.txt`, and delete the token at github.com/settings/tokens.

## One thing to change first

The README links to your portfolio at:

```
https://portfolio-theta-liart-69.vercel.app
```

If you have since added a cleaner Vercel domain, open `README.md` in Notepad,
press **Ctrl+H**, and replace that address with your new one. It appears twice.

## What is in here

```
README.md              your profile page
assets/banner.png      the header image
assets/*.png           the three charts shown in the projects
push_profile.sh        creates/updates the repo and pushes
```

The charts are copies, kept here so the profile page never breaks if you rename
or move the project repos.
