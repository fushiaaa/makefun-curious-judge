# A short text written to intrigue an AI judge

This program writes one short piece of prose to `/output/entry.txt`. The text is meant to leave an AI reader curious: alert, drawn in, and wanting more.

It is an entry for the make.fun bounty “Make the AI judge feel curious.” The program uses no network. Running it twice writes the same text.

## Run it

Python 3.13:

```sh
python3 main.py
```

That creates `/output` if needed and writes `/output/entry.txt` as UTF-8. The file is 1 to 280 Unicode code points and is not only whitespace.

## License

MIT. See `LICENSE`.
