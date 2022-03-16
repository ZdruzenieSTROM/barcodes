#!/usr/bin/bash

set -o errexit
set -o nounset
set -o pipefail

build()
{
    latex -interaction=batchmode kody.tex

    # shellcheck source=/dev/null
    source kody+mp.sh

    latex -interaction=batchmode kody.tex

    dvips  kody.dvi
    ps2pdf kody.ps
}

main()
{
    local BUILDDIR="build"
    local ARCHIVE="Mamut 2020.zip"

    mkdir -p "$BUILDDIR"
    unzip -o -q -d "$BUILDDIR" "$ARCHIVE"  > /dev/null

    ./partition.py \
        -o "$BUILDDIR/zadania" \
        "$BUILDDIR/lahke.tex" \
        "$BUILDDIR/stredne.tex" \
        "$BUILDDIR/tazke.tex"

    cp "kody.tex"       "$BUILDDIR"
    cp "makra-kody.tex" "$BUILDDIR"

    pushd "$BUILDDIR" > /dev/null
    build > /dev/null
    popd > /dev/null

    cp -t . "$BUILDDIR/kody.pdf"
}

main "$@"
