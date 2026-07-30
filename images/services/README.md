# Service photos

Drop the eight service photos in THIS folder, named exactly as listed below.
Names must match exactly (all lowercase, hyphens, `.jpg`) or the card will show
the pink gradient fallback instead of the photo.

    laser-hair-removal.jpg
    waxing-threading.jpg
    hydrafacial.jpg
    skincare-facials.jpg
    microneedling-peel.jpg
    massage.jpg
    eyes-brows.jpg
    makeup.jpg

## Export settings

| Setting | Value |
|---|---|
| Dimensions | **1000 x 1250 px** |
| Aspect ratio | **4:5 (portrait)** |
| Format | JPG |
| Quality | ~80% |
| Target file size | 150-250 KB each (keep under 400 KB) |

## Why 4:5

The homepage cards are locked to a 4:5 portrait ratio so all eight tiles stay
exactly the same height regardless of how long the description is. The photos are
placed with `object-fit: cover`, so they always fill the card without stretching
or distorting - anything not matching 4:5 simply gets centre-cropped.

On mobile the cards switch to a wider 4:3 crop, and the same image is reused as
the hero background on that service's own page (a wide crop). So:

**Keep the subject centred with a little breathing room around it** - the edges
get cropped at some screen sizes.

## Darkening

Do not pre-darken the photos. A dark veil is applied in CSS
(`.service-tile-veil`) so the white text stays legible, and it lightens slightly
on hover. Supply normal, well-lit images.
