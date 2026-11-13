# food-picture-01: Tonkotsu Ramen Noodle Lift

Entry for make.fun's "Make the best-looking food picture" bounty.

## The picture

A dramatic editorial food photograph of a bowl of tonkotsu ramen: chopsticks
lifting a tall tangle of glossy noodles from rich creamy broth, a halved
soft-boiled egg with a jammy orange yolk, glistening chashu pork, spring
onions and nori, steam rising over a dark wooden table with warm golden
highlights. One hero dish, filling the frame, no text, no hands.

## How it works

`main.py` (Python 3.13, standard library only, no network) copies the
bundled image `food.jpg` (1024x1024 JPEG, 242,751 bytes) byte-for-byte to
`/output/entry.png`. The rules allow a JPEG written under the name
`entry.png`, and the copy is deterministic, so two runs write identical bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT, see `LICENSE`.
