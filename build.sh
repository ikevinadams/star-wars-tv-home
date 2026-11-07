#!/bin/bash
# Build Star Wars TV: copy a TV-sized copy of the page into the app (starwars/tools/tv_assets.py), then build the APK.
#   ./build.sh            the release APK (signed with your key in starwars-tv/release/, or else your debug key)
#   ./build.sh install    and install it on the TV adb is connected to
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
python3 "$HERE/starwars/tools/tv_assets.py"
(cd "$HERE/starwars-tv" && ./gradlew assembleRelease --console=plain -q)
APK="$HERE/starwars-tv/app/build/outputs/apk/release/app-release.apk"
echo "$APK"
if [ "$1" = "install" ]; then adb install -r "$APK"; fi
