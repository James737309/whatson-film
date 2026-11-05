# WhatsOn Film

A UK guide to films on TV and streaming, this week and next week. Sister app to WhatsOn Sport. Owned by Definitive Projects Limited (DPL).

Test version: https://claude.ai/artifact/YNKrfXMJn95qrU9BwcPkBq

## What it does

- Opens on **today**: On now (with progress bar), New to stream today, Starting soon (next 2 hours), then the rest of the day. Finished films sit behind a "Show earlier films" button. Refreshes every minute.
- This week / Next week, with a day strip showing how many films each day.
- Filters (remembered on the device): Where (all, free TV, Sky Cinema, Netflix), Time (morning, afternoon, evening, late night), Age (BBFC U to 18; unconfirmed "TBC" films are hidden when an age is picked), Genre.
- Repeats are grouped: one card per film per day at its next showing, with "Also at …" times.
- "Which service?" sheet: counts films matching your filters on free TV, Sky Cinema / NOW and Netflix.
- Rolling ad banner, light and dark mode.

## Files

| File | What it is |
|---|---|
| `index.html` | The built app: one self-contained page. This is what gets hosted. |
| `src/app.html` | Page layout, styles and code. `/*DATA*/` marks where the data goes. |
| `src/data.js` | Listings: `TV` (showings), `STREAM` (new on Netflix / Sky Cinema) and `CH` (channel type and catch-up app). |
| `src/raw_tv.txt` | TV listings in a simple one-line-per-showing format (easiest to edit each week). |
| `src/build.py` | Turns `raw_tv.txt` into `data.js` and builds `index.html`. |

## Weekly update

1. Update `src/raw_tv.txt` with the new week's showings, and `STREAM` in `src/data.js` for new streaming films.
2. Update `UPDATED`, `WEEKS`, `TV_FROM` and `TV_UNTIL` near the top of the script in `src/app.html`.
3. Run `python3 src/build.py --tv`.
4. Commit and publish `index.html`.

## Notes

- Times are UK time. Film end times are estimated: until the next film on the same channel, capped at 2½ hours.
- Sources for the 5–11 Nov 2026 listings: tvradar.uk (free TV and Sky Cinema), What's on Netflix, Digital Spy (Sky Cinema premieres).

See `TODO.md` for the backlog.
