#!/bin/bash

set -e
tempDir=$(mktemp -d)
checkoutDir="$tempDir/cool-retro-term"
git clone --quiet https://github.com/Swordfish90/cool-retro-term "$checkoutDir"

pushd "$checkoutDir" >/dev/null
git submodule --quiet init
git submodule --quiet update
popd >/dev/null

tar -C "$tempDir" -cjf cool-retro-term.tar.bz2 cool-retro-term

lastTag=$(cd "$checkoutDir"; git describe --tags)
headCommit=$(cd "$checkoutDir"; git rev-list HEAD -n 1 | cut -c 1-7)

echo "%global gitdate $(date +%Y%m%d)"
echo "%global gitversion ${lastTag}"
echo "%global gitcommit ${headCommit}"

rm -rf "$tempDir"
