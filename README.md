[![make.fun](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/c/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/Jideweb3/news-image-20261120/rank.svg)](https://make.fun/c/news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/Jideweb3/news-image-20261120/reward.svg)](https://make.fun/c/news-image-20261120)

# The World Today — Classic Broadsheet (20 November)

This entry is a small Python program whose output is a single image:
**The World Today**, a classic newspaper front page summing up the world
news of **Friday, 20 November 2026** — 52 stories, 24 of them in
pictures, every continent, all from this one day. The design source is
`page.html`; its rendered form is `entry.png` (1024×1024), and `main.py`
simply delivers that image to the output directory, byte for byte. A
slim edition of the same page, encoded as a JPEG of 305,834 bytes, sits
in `slim/` with its own copy of `main.py`.

## Design

A dense classic broadsheet in the old front-page manner: cream paper
(#f6efdd), black ink, and a big red masthead band (#c8102e) carrying the
name in white condensed type. Under it, the date — **FRIDAY 20 NOVEMBER
2026** — in large serif, then a numbers strip of six figures from the
day. One huge lead (the Shenzhen declaration) with a big picture and a
bold sub-line on Trump's Iran decision; two secondary leads (Cyclone
Akvan, the World Court ruling) beside it; a strip of four more pictured
stories (Anthropic's trading day, the AI sell-off, the Riyadh tower,
COP31's final day); then the day in full: three dense columns where
pictured stories sit scattered among numbered text stories, every story
carrying its number in a red chip. A world map ("Where it happened")
and a date-check line close the page. Georgia serif for headlines,
Arial for kickers, decks and briefs — all text is real HTML text, never
baked into the pictures. Pictures are a mix of real photographs and
editorial illustrations, credited in `SOURCES.md`.

`entry.png` is rendered from `page.html` with headless Chrome at
1024×1024 and is 620,691 bytes — under the 1 MiB limit.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

That writes `out/entry.png`. Without `MAKEFUN_OUTPUT_DIR` the program
writes to `/output/entry.png`. It uses only the Python 3 standard
library and checks that the copied bytes match the source before
exiting.

## The 52 stories

**Leads and pictured strip**

1. Three leaders, one declaration — Trump, Xi and Putin sign a
   four-point joint declaration in Shenzhen; Trump says his call on
   widening the Iran war waits until 2027. *(photo)*
2. Cyclone Akvan slams into Odisha — 300,000+ moved to shelters.
   *(photo)*
3. World Court: Myanmar committed genocide — the 9–6 ruling is the
   first holding a state responsible for genocide. *(photo)*
4. Anthropic closes 17% up on Nasdaq debut — $81.3bn raised, a record
   IPO, value near $1.5tn. *(photo)*
5. AI sell-off deepens: Nikkei down 4.8% — S&P 500 falls 2%, SoftBank
   −16%, AMD −7%, Korea halts sell orders. *(illustration)*
6. Houthi missile damages Riyadh tower — the PIF tower hit, no
   injuries. *(illustration)*
7. COP31 final day: deal or deadlock — the draft drops any fossil-fuel
   phase-out. *(illustration)*

**The day in full — pictured**

8. GTA 6 sales pass $2.3bn in days. *(photo)*
9. Voyager 1 reaches one light-day from Earth. *(illustration)*
10. Ukraine hits Crimea Bridge a third time. *(photo)*
11. Tanker burns after mine in Hormuz. *(photo)*
12. North Korea expands uranium plant — UN. *(illustration)*
13. Fiji declares disaster in El Niño drought. *(illustration)*
14. Seoul court orders retrial for ex-PM Han. *(illustration)*
15. California opens probe into Nvidia. *(illustration)*
16. Kenya discharges its last Ebola patient. *(illustration)*
17. Nicholls' 113* rescues New Zealand. *(illustration)*
18. Europe ready to talk with Russia — Berlin. *(photo)*
19. Israeli troops cross Gaza's Yellow Line. *(illustration)*
20. US & Venezuela sign military deal. *(illustration)*
21. Dozens missing as migrant boat capsizes. *(illustration)*
22. BepiColombo enters Mercury's orbit. *(illustration)*
23. El Niño storm threatens Los Angeles. *(illustration)*
24. Haiti forces retake Martissant corridor. *(illustration)*

**The day in full — text stories**

25. Sudan: drone strike kills 10 at gold mine.
26. Bukele registers for a third term.
27. Senate passes permitting overhaul 62–33.
28. IEA: Iran war crushes Hormuz confidence.
29. Japan core inflation hits year's high.
30. Brazil sells $1bn to curb the dollar.
31. US firm wins Kenya minerals deal.
32. White House fires cyber director.
33. Race to succeed Guterres stalls.
34. Arson & protests spread in Bangladesh.
35. Mosque set on fire in northern Israel.
36. Iraq gives Kataib Hezbollah a deadline.
37. Denmark ratifies Greenland deal with US.
38. Strikes reported near Badme.
39. Gold falls 4.2% as dollar stays high.
40. IMF: public debt nears 100% of world GDP.
41. Thousands march in Colombia.
42. Pakistan raids kill 22 militants.
43. Mongolia's president resigns.
44. Somalia expels UAE ambassador.
45. Philippines & Chile sign trade deal.
46. World Children's Day marked worldwide.
47. UK & EU hold Brussels reset summit.
48. Takaichi gets cool APEC reception.
49. Sánchez admits mistakes in TV debate.
50. Europe's youth plan strikes in 25+ countries.
51. IEA: Africa's solar imports hit 26 GW.
52. UN: no state OK needed to form a group.

Story sources: One Turn's day report for 20 November 2026, the Open
Chronicle Global News Brief, and the TRT World Daily News Brief; see
`SOURCES.md`.
