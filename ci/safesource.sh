# Source a script with `set -e` disabled, but still returning the final status
# code.
#
# This is needed for a lot of the ATLAS setup scripts that don't work with
# `set -e` enabled.

if [ ${#} == 0 ]; then
    echo "usage: source ${0} command to run"
    exit 1
fi

set +e
"${@}"
CODE=${?}
set -e

if [ ${CODE} != 0 ]; then
    exit ${CODE}
fi
