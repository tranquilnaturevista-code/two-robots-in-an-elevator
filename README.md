# Two Robots in an Elevator

[![Two Robots in an Elevator](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![Rank](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/tranquilnaturevista-code/two-robots-in-an-elevator/rank.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![Reward](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/tranquilnaturevista-code/two-robots-in-an-elevator/reward.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)

Entry for the [make.fun bounty "Two Robots in an Elevator"](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f) ($10, top 10 paid, 1st place $3.10, free to enter).

## What it does

`main.py` writes one original line of awkward robot small talk to `/output/entry.txt`:

> My proximity sensor says we're 0.4 metres apart, which is technically safe and socially illegal.

The line is written by hand for this bounty. The joke only works
between two robots stuck in a lift: one of them reads out its
proximity sensor like a weather report, and the measurement that is
"technically safe" is also, by human standards, standing far too
close to a stranger in a metal box. The turn is the clash between
the machine's precise, reassuring reading and the social verdict —
safe on paper, a crime in the lift — delivered deadpan, with no
wasted words.

## Run

```sh
python3 main.py   # writes /output/entry.txt (or $OUTPUT_DIR/entry.txt)
```

Deterministic: the same line on every run. The output is 96
characters of UTF-8 text (96 bytes, plain ASCII), within the 1–200
character gate, on a single line.

## License

MIT — see [LICENSE](LICENSE).
