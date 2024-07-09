if [ ${#} != 0 ] && [ ${#} != 1 ]; then
    echo "usage: ${0} [build]"
    return 1
fi

#
# Check for build directory
MYBUILD=build
if [ ${#} == 1 ]; then
    MYBUILD=${1}
fi

if [ ! -d ${MYBUILD} ]; then
    echo "Build directory ${MYBUILD} does not exist!"
    return 1
fi

# Convert to absolute path
export MYWORKSPACE=$(realpath $(dirname ${BASH_SOURCE[0]}))
export MYBUILD=$(realpath ${MYBUILD})

#
# Main software
source /opt/setup_mucoll.sh

#
# Add exts
if [ -d ${MYBUILD}/exts ]; then
    export LD_LIBRARY_PATH="$(find ${MYBUILD}/exts/* -name lib64 -type d | tr '\n' ':')$(find ${MYBUILD}/exts/* -name lib -type d | tr '\n' ':')${LD_LIBRARY_PATH}"
    export PATH="$(find ${MYBUILD}/exts/*/bin -type d | tr '\n' ':')${PATH}"
fi

#
# Add new modules
for pkglib in $(find ${MYBUILD}/packages -name '*.so' -type l -o -name '*.so' -type f)
do
    pkgname=$(basename ${pkglib})
    if [[ "${MARLIN_DLL}" == *"${pkgname}"* ]]; then
        MARLIN_DLL=$(echo ${MARLIN_DLL} | sed -e 's|[^:]\+'${pkgname}'|'${pkglib}'|')
    else
        MARLIN_DLL=${pkglib}:${MARLIN_DLL}
    fi
done
export MARLIN_DLL
