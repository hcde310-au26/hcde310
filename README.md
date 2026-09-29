# HCDE 310: my course repo

This is your repo for the whole quarter. Every assignment gets its own folder. It starts with just `hw0/`, and you add a folder for each new assignment:

```
hcde310/
├── hw0/     setup + Day 1 snapshot
├── ex02/    added in Class 2
├── hw1/     added when HW1 is released
└── ...
```

## Getting a new assignment's starter files

1. Download the starter zip from the Canvas assignment (for example, `hw1.zip`).
2. Unzip it. You get a folder with the same name (`hw1`).
3. Drag that folder into this repo, next to `hw0`.
4. Check in VS Code: the files should be **directly** inside `hw1/` (for example, `hw1/part1.py`). If you see `hw1/hw1/`, move the inner files up one level.
5. Save a snapshot and push:
   ```
   git add .
   git commit -m "Add hw1 starter"
   git push
   ```

## Checking your work

Most assignments have a `check.py`. Run it from inside that folder:

```
cd hw1
python3 check.py
```

(🪟 Windows: `python` instead of `python3`.)

GitHub also runs it every time you push. Look for the ✓ or ✗ next to your commit, or open the **Actions** tab to see one check per folder.

## Submitting: send a commit link

On Canvas, you submit a **commit link**, not the repo URL. A commit link points to one exact saved version, so we grade exactly what you turned in, even if you keep working in the repo afterward.

1. Commit and push your finished work.
2. On GitHub, open your repo and click the **commits** link (the clock icon with a number, above the file list).
3. Click the message of the commit you want to submit.
4. Copy the URL from your browser. It looks like `https://github.com/you/hcde310/commit/3f9a2c1…`
5. Paste it into the Canvas assignment.

Changed something after submitting? Push again and resubmit the new commit link.
