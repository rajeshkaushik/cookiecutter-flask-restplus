#!/bin/bash
for s in $PWD/tools/git/hooks/*; do
  if [ -x $s ]; then
    ln -sf $s .git/hooks/`basename $s`
  fi
done
