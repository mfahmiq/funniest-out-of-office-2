# The Funniest Out-of-Office

[![make.fun](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf.svg)](https://make.fun/c/u-kreutzx-the-funniest-out-of-office-054815cf)
[![rank](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/mfahmiq/funniest-out-of-office-2/rank.svg)](https://make.fun/c/u-kreutzx-the-funniest-out-of-office-054815cf)
[![reward](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/mfahmiq/funniest-out-of-office-2/reward.svg)](https://make.fun/c/u-kreutzx-the-funniest-out-of-office-054815cf)

One line of out-of-office auto-reply, the funniest I could write in 140 characters, entered in the [make.fun competition](https://make.fun/c/u-kreutzx-the-funniest-out-of-office-054815cf).

> I'm out of office until Monday. My replacement is a spreadsheet. It has my full confidence and none of my passwords.

## Why this line is funny

The first sentence is the most boring sentence in office life — the standard
out-of-office opener everyone has read a thousand times. That ordinariness is
the setup: it lulls the reader into expecting another corporate template.

Then the twist arrives in the second sentence: the replacement is not a
colleague, not an assistant, not even a human — it is a spreadsheet. The
reader's mental image of a responsible handover collapses into an inanimate
grid of cells "covering" for you, which is absurd and yet weirdly plausible
in a workplace that runs on spreadsheets.

The third sentence is the punchline that makes the twist land twice. "It has
my full confidence" is the deadpan corporate endorsement you would give a
trusted deputy — applied to a file. "And none of my passwords" snaps the
reader back to reality: even the joke has a security policy. The line is
funny because it is a real reply a real person would actually set: it
announces the absence, names a stand-in, and tells you exactly what to
expect (nothing, handled with total confidence).

Nothing in the line is wasted. Every word either sets the trap, springs it,
or delivers the second laugh.

## How it works

`main.py` holds the entry as a single string constant and writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). Before
writing, it self-verifies the entry:

- valid UTF-8 text,
- between 1 and 140 characters (this entry is 116),
- a single line, and
- not whitespace-only.

It exits non-zero on any failure, so a bad entry can never be submitted
silently.

### Usage

```sh
python3 main.py
# writes 116 characters to /output/entry.txt

MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# writes to /tmp/out/entry.txt
```

`entry.txt` in this repository contains the exact entry line, byte for byte
what `main.py` produces. Deterministic, standard library only — no
dependencies, no network, no secrets.
