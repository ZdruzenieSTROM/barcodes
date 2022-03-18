#!/usr/bin/bash

set -o errexit
set -o nounset
set -o pipefail

error()
{
    local MESSAGE="${1}"
    local STATUS="${2}"

    echo "${MESSAGE}" >> "/dev/stderr"
    exit "${STATUS}"
}

setup()
{
    local BUILDDIR="${1}"
    local BUILDTYPE="${2}"
    local ARCHIVE="${3}"

    unzip -o -qq -d "${BUILDDIR}" "${ARCHIVE}"

    cp -t "${BUILDDIR}" "kody.tex" "makra-kody.tex"

    local PROBLEM_FILES

    case "${BUILDTYPE}" in
        "MAMUT")
            PROBLEM_FILES=(lahke.tex stredne.tex tazke.tex)
            ;;
        "LOMIHLAV")
            PROBLEM_FILES=(ulohy.tex)
            ;;
        *)
            error "Unknown build type" 1
            ;;
    esac

    ./partition.py -o "${BUILDDIR}/zadania" "${PROBLEM_FILES[@]/#/${BUILDDIR}/}"
}

build()
{
    local BUILDDIR="$1"

    pushd "${BUILDDIR}"

    latex -interaction=batchmode "kody.tex"

    # shellcheck source=/dev/null
    source kody+mp.sh

    latex -interaction=batchmode "kody.tex"

    dvips  -q "kody.dvi"
    ps2pdf    "kody.ps"

    popd
}

main()
{
    if [[ "${#}" -lt 2 ]]; then
        error "Usage: ${0} <MAMUT|LOMIHLAV> ARCHIVE" 1
    fi

    local BUILDTYPE="${1}"
    local ARCHIVE="${2}"

    local BUILDDIR
    BUILDDIR="$( mktemp -d )"

    setup "${BUILDDIR}" "${BUILDTYPE}" "${ARCHIVE}"
    build "${BUILDDIR}" > "/dev/null"

    cp -t "." "${BUILDDIR}/kody.pdf"
    rm -r -f  "${BUILDDIR}"
}

main "${@}"
