#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "$0" )" && pwd )"

rm -R "$SCRIPT_DIR/../custom_components/hacs"
cp -R "$SCRIPT_DIR/../submods/hacs__integration/custom_components/hacs" "$SCRIPT_DIR/../custom_components"
