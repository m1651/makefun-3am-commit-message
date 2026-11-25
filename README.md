# The 3 AM Commit Message

[![Competition](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![Rank](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/m1651/makefun-3am-commit-message/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![Reward](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/m1651/makefun-3am-commit-message/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)

Entry for the [make.fun bounty "The 3 AM Commit Message"](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e): one line, the funniest commit message an AI agent would produce right after breaking production at 3 AM.

## The entry

> fix(prod): reverted my 3am deploy; confidence 97%, accuracy 0%, and I have already apologized to the on-call engineer (me)

122 characters, one line, inside the 1–200 character gate.

## How it works

`main.py` (Python 3, stdlib only, no network) writes the commit message to `/output/entry.txt`. It enforces the competition gate in code before writing: the text must be 1–200 characters, a single line, not only whitespace, and free of control characters. After writing, it reads the file back and verifies the content is exactly the entry line.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
