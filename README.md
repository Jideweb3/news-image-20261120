[![make.fun](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/c/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/Jideweb3/news-image-20261120/rank.svg)](https://make.fun/c/news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/Jideweb3/news-image-20261120/reward.svg)](https://make.fun/c/news-image-20261120)

# The World Today — Classic Broadsheet (20 November)

A small Python program whose whole output is one image: **The World
Today**, a newspaper front page for **Friday, 20 November 2026**.
Thirty stories from that single day, fifteen of them pictured, set out
the way the winning front pages do it — one big lead, a few strong
secondary stories, then the rest of the day in three open columns with
room to breathe. `page.html` is the design source; `entry.png` is its
render at 1024×1024 (592,127 bytes); `main.py` copies that image to
the output directory and checks the copy is exact before it exits. A
slim edition — the same render held as JPEG bytes, 274,950 bytes —
sits in `slim/`.

## Design

Cream paper (#f6efdd), black ink, and a red masthead band (#c8102e)
with the paper's name in white condensed capitals. Below the name, the
date in large serif — **FRIDAY 20 NOVEMBER 2026** — and a strip of six
figures from the day (the World Court's 9–6 vote, the $81.3bn
Anthropic raise, the $48.3bn war cost, 300,000+ people sheltered from
Cyclone Akvan, Voyager 1 at 26bn km, the Nikkei's −4.8%).

The Shenzhen declaration takes the top of the page: a wide summit
photograph, a headline in large serif, the four points of the deal in
the deck, and Trump's Iran decision — held until 2027 — as a bold red
sub-line. Cyclone Akvan and the World Court's Myanmar ruling sit
beside it as secondary leads. The rest of the day runs in three
columns under the heading "THE DAY IN FULL": pictured stories carry a
thumbnail beside their headline, text stories stand on their own, and
every story wears its number in a small red chip. A world map strip
("Where it happened") and a date-check line close the page. Headlines
are Georgia serif; kickers, decks and briefs are Arial. All words on
the page are real HTML text — nothing is baked into the pictures.

## Run it

```sh
python3 main.py
```

That places the page image at `/output/entry.png`, byte for byte the
`entry.png` in this repository. The program uses only the Python 3
standard library.

## The 30 stories

**The top of the page**

1. Three leaders, one declaration — Trump, Xi and Putin sign a
   four-point joint declaration in Shenzhen; Trump says his call on
   widening the Iran war waits until 2027. *(photo)*
2. Cyclone Akvan slams into Odisha — 300,000+ moved to shelters.
   *(photo)*
3. World Court: Myanmar committed genocide — the 9–6 ruling is the
   first holding a state responsible for genocide. *(photo)*

**The day in full**

4. Anthropic closes 17% up on Nasdaq debut. *(photo)*
5. AI sell-off deepens: Nikkei down 4.8%. *(illustration)*
6. COP31 final day: deal or deadlock. *(illustration)*
7. GTA 6 sales pass $2.3bn in days. *(photo)*
8. Voyager 1 reaches one light-day from Earth. *(illustration)*
9. North Korea expands uranium plant — UN.
10. Ukraine hits Crimea Bridge a third time. *(photo)*
11. Seoul court orders retrial for ex-PM Han.
12. Tanker burns after mine in Hormuz. *(photo)*
13. Houthi missile damages Riyadh tower.
14. California opens probe into Nvidia. *(illustration)*
15. Israeli troops cross Gaza's Yellow Line.
16. Fiji declares disaster in El Niño drought. *(illustration)*
17. US & Venezuela sign military deal.
18. Nicholls' 113* rescues New Zealand. *(illustration)*
19. BepiColombo enters Mercury's orbit.
20. Kenya discharges its last Ebola patient. *(illustration)*
21. Haiti forces retake Martissant corridor.
22. Europe ready to talk with Russia — Berlin. *(photo)*
23. Sudan: drone strike kills 10 at gold mine.
24. Senate passes permitting overhaul 62–33.
25. Japan core inflation hits year's high.
26. Gold falls 4.2% as dollar stays high.
27. Denmark ratifies Greenland deal with US.
28. UK & EU hold Brussels reset summit.
29. IEA: Africa's solar imports hit 26 GW.
30. Dozens missing as migrant boat capsizes.

Story sources: One Turn's day report for 20 November 2026, the Open
Chronicle Global News Brief, and the TRT World Daily News Brief; see
`SOURCES.md`.
