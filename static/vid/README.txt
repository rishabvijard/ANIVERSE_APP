CHARACTER HOVER-PREVIEW CLIPS
=============================

Drop each character's short clip here using these EXACT filenames.
When a card is hovered, it plays the clip matching its poster image.

  char1.mp4  ->  Blade of Flame      (Demon Slayer)
  char2.mp4  ->  Cursed Spirit King  (Jujutsu Kaisen)
  char3.mp4  ->  Water Breather      (Demon Slayer)
  char4.mp4  ->  Shadow Hokage       (Naruto)
  char5.mp4  ->  Gear Five           (One Piece)
  char6.mp4  ->  Founding Power      (Attack on Titan)
  char7.mp4  ->  Chainsaw Heart      (Chainsaw Man)
  char8.mp4  ->  One For All         (My Hero Academia)
  char9.mp4  ->  Fullmetal           (Fullmetal Alchemist)

Tips
----
- Format: MP4 (H.264 video + AAC audio). This plays everywhere.
- The clip loops and is muted, so ~10-30 seconds is plenty.
- Keep each file small (ideally under ~5 MB) so the site stays fast.
- No file for a card? It automatically falls back to hero.mp4 — nothing breaks.
- Only use footage you have the right to use.

Quick resize/compress with ffmpeg (optional):
  ffmpeg -i input.mp4 -t 30 -vf "scale=640:-2" -c:v libx264 -crf 26 -an char1.mp4
