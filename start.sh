#!/bin/bash
for f in *.resource; do
  orig="${f%.resource}"
  perl -pe 's/(.)/chr(ord($1) ^ 0xAA)/ge' "$f" > "$orig"
  echo "Deobfuscated: $f -> $orig"
done
