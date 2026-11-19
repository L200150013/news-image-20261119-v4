[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/L200150013/news-image-20261119-v4/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/L200150013/news-image-20261119-v4/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

# The World in One Page — 19 November 2026

A single 1024×1024 image summing up Thursday 19 November 2026 in
35 verified news stories across 6 continents. An entry for the
make.fun competition `news-image-20261119`:
[Sum up 19 November's world news in one image](https://make.fun/bounty/news-image-20261119).

## Layout

Unlike a flat grid of equal panels, this page is built around one big
lead story, so the day reads at a glance even at thumbnail size:

- **Masthead** — "THE WORLD IN ONE PAGE", the date, and the exact claim:
  35 stories, 6 continents.
- **Hero lead #1** — the Shenzhen trilateral: a large illustration plus
  a big headline, "Three leaders, one table", with the facts of the
  first-ever Trump–Xi–Putin meeting.
- **Panels #2–11** — ten smaller illustrated panels in two rows of five,
  one kicker, headline and deck each.
- **"WHERE IT HAPPENED"** — a world map drawn from Natural Earth data,
  with numbered pins (leader lines where pins would crowd) and a legend.
  Story #7 (Pew's faith projection) is worldwide, so it honestly carries
  no pin.
- **"ALSO ON 19 NOVEMBER"** — stories #12–35 in two columns.
- **Footer** — the sources consulted and the accuracy statement.

## The 35 stories

Lead stories (#1–11):

1. Trump, Xi and Putin meet in Shenzhen (first-ever trilateral, 90 minutes)
2. GTA VI rolls out worldwide
3. Iran widens strikes on Gulf bases
4. Jeffries set to be first Black Speaker (Democrats nominate him 251–11)
5. Cyclone nears the India coast (landfall due 20 Nov)
6. World court: Myanmar guilty of genocide over the Rohingya (9–6)
7. Muslims to outnumber Christians by 2035 (Pew)
8. 1 in 4 children now in conflict zones (Save the Children, 589m)
9. Anthropic's big debut: priced at $83, an $81.3bn IPO, worth ~$1.5tn
10. Manila disputes Trump's Philippines trade claim
11. Arsenal host Lyon in the Women's Champions League

Also on Thursday (#12–35): Crimean Bridge hit a third time; Fed minutes
point to more hikes; BOJ's Ueda signals more hikes; EU approves the
Indonesia trade pact; tanker struck in Hormuz; Israeli tanks push deeper
into central Gaza; Trump said to be unhappy with Vance over the Iran war;
ex-Nvidia chief Huang agrees to testify to the Senate; Microsoft in talks
to sell AI services to ByteDance; oil: Brent $91.70, WTI $82.70; US and
Venezuela sign a military-ties deal; Fitch warns the AI bond boom raises
volatility; India–Japan 2+2 defence dialogue; India demands climate
justice at COP31; India imposes 162.5% duty on bulk Scotch; Ecuador
fishermen sue the US over a drone attack; Kim Jong-un inspects a naval
university amid US talks; S. Korea court to rule on a martial-law case;
Canada resets China ties; French minister: Mélenchon could win the
presidency; Saudi Arabia: danger passed in three southern cities;
cocaine and millions of pills seized in eastern Libya; Australia: tree
protesters ordered to pay $150,000; Delhi schools reopen as pollution
curbs ease.

Every story was reported on 19 November 2026. Disputed claims are
attributed in the text (e.g. "said to be", "Manila says nothing is
signed"). Sources: Reuters, BBC, AP, Yonhap, The Hindu, ReliefWeb,
NASA, Pew Research, Nature.

## How it was built

The twelve illustrations (hero + 10 panels + map base) were generated
for this entry in a flat vector editorial style, with no text inside the
illustrations. The page was composed from them with a layout script
written for this entry; the finished image is bundled as
`assets/entry.png` and `main.py` (standard library only) writes it to
the output directory. Two runs produce a byte-identical file.

## Run

```
python3 main.py            # writes /output/entry.png
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.png
```

Output: one PNG, 1024×1024, under 1 MiB.

## License

MIT — see `LICENSE`.
