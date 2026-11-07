# Star Wars TV: the full guide

Full prompt and guide. A home screen for Android TV built around the Millennium Falcon's cockpit: your apps are destinations out in space beyond the canopy, moving between them is a short burst of speed, and opening one is a jump to hyperspace. Scroll down to a hall in the Jedi Temple where Episodes I to VI are lightsabers on a ledge, down again to a campfire with Din Djarin and Grogu where bounty pucks project The Mandalorian as holograms, and down once more to Vader's bridge, where each story has its own place through the windows. This guide has the steps to install the finished APK and make it yours (your apps in the cockpit, your streaming service for the films and series), every prompt used to make the pictures, and the prompts to build it yourself with a coding assistant, starting from cleaning up the TV. If you'd rather have a coding assistant set it all up for you, use [`PROMPT.md`](PROMPT.md).

A fan-made project for personal use. Not affiliated with or endorsed by Lucasfilm or Disney. The holograms are The Mandalorian's posters from TMDB (themoviedb.org), the lightsaber hilts are Lucasfilm's own renders (via Wookieepedia and the StarWars.com Databank), and the app logos belong to Netflix, Amazon, JioHotstar, Sony, Google and Apple. The cockpit, the hall, the camp and the bridge with its views were generated with AI (Nano Banana 2.1, through Higgsfield). Don't sell it or publish the APK on an app store.

## 1. What you get

- **The cockpit (home):** the Millennium Falcon's cockpit, seen from the back, its canopy open onto space. Stars drift past, a nebula hangs far off, and a planet sits low on the right. The cockpit sways gently, as a ship does.

- **Your apps, out in space:** up to six of your apps and HDMI inputs float beyond the canopy as destinations. The one you pick sits in the round centre pane under an amber targeting reticle, with its name below; the others wait a step apart on a shallow arc, each in a pane of its own. It starts with Netflix, Prime Video, JioHotstar, PlayStation, YouTube and Apple TV (whichever your TV has); those six show their logos, and any other app shows its name.

- **Moving:** each move along the apps is a short burst of speed: the stars stretch into streaks, the ship banks toward the new destination and the cockpit lurches.

- **Opening:** OK spools up the hyperdrive, the stars stretch into the hyperspace tunnel, a flash, and the app opens. When you come back, the ship drops out of hyperspace in front of a different planet (a desert world, an ice world and a forest world, in turn).

- **The clock:** the time and date are on the square monitor in the cockpit's right-hand wall, drawn onto it in perspective.

- **The Jedi Temple (one step down):** a quiet stone hall with a long ledge, and on it six lightsabers, one from each film of Episodes I to VI in order: Darth Maul's, Yoda's, Mace Windu's, Obi-Wan Kenobi's, Darth Vader's and Luke Skywalker's. The one you pick rises off the ledge and ignites, the hall takes on its colour, and the film's episode, title and whose saber it is appear below. OK opens the film.

- **The camp (two steps down):** night on a grassy world, Din Djarin by a campfire, Grogu in his floating pram, the Razor Crest landed behind them. On a stone in front lie four bounty pucks: The Mandalorian's three seasons and the film, The Mandalorian and Grogu. The one you pick lights up and projects its poster as a flickering blue hologram. OK opens it.

- **The dark side (three steps down):** Vader stands at the windows of a Star Destroyer's bridge. Four stories, in story order: Obi-Wan Kenobi, Andor seasons 1 and 2, and Rogue One. Each has its own place outside: Mustafar, Coruscant at night, the Death Star being built, and Scarif. Moving to the next is a hop through hyperspace seen through the glass, the bridge trembling and the room's light changing with the place. OK jumps all the way and opens it.

- **Customise:** press Up in the cockpit and **Customise** lights up at the top; OK opens a panel to pick the apps and where the films and series open. It also opens by itself the first time.

- **Smoothness:** on an ordinary 1080p TV (tested on a MediaTek TV with 1.8 GB of memory), about 60 frames per second in the Jedi Temple, at the camp and on the bridge, and about 36 in the cockpit, whose moving starfield that TV draws on its processor.

## 2. What's in this repository

| File or folder | What it is |
|---|---|
| `README.md` | The short version: what it is, install, the remote. |
| `GUIDE.md` | This guide. Also as a PDF in `docs/`. |
| `PROMPT.md` | A prompt for a coding assistant that asks what you watch and where, sets Star Wars TV up for you, builds it and installs it on your TV. |
| `starwars/` | The home screen: one web page (`index.html`), its settings (`config.js`), the pictures (the two cockpits, the hall, the camp, the bridge and its four views), the hilts, the holograms and the logos. |
| `starwars/tools/` | The scripts that made the pictures the page uses from the generated originals, and the one that makes the TV copy (section 9). |
| `starwars-tv/` | The Android TV app: a full-screen WebView around the page, with a small bridge to the TV. |
| `build.sh` | Builds the APK (and installs it with `./build.sh install`). |
| `docs/` | Screenshots and the PDF guide. |

On the [Releases](../../releases/latest) page: **Star-Wars-TV.apk** (ready to install) and **Star-Wars-TV-assets.zip**: every picture the page uses at full resolution, the 4K generated originals they were made from, the hilt renders and the posters.

## 3. Install the APK

Works on: Android TV and Google TV, Android 7 or newer, with Android System WebView kept up to date from the Play Store. Built and tested on a 1080p Android 10 TV. The file is **Star-Wars-TV.apk**.

### Option A: with a USB stick or the "Send files to TV" app (no computer commands)

1. Copy **Star-Wars-TV.apk** to a USB stick, or send it to the TV with the **Send files to TV** app (phone and TV both need it).

1. On the TV, open a file manager, for example File Commander or X-plore from the Play Store.

1. Select the APK. When the TV asks, allow that file manager to **Install unknown apps**, then go back and select the APK again.

1. If Play Protect warns that the app isn't from the Play Store, choose **Install anyway**.

1. **Star Wars TV** now appears in your apps. Open it from there anytime.

### Option B: with adb from a computer

1. On the TV, enable Developer options: Settings → Device Preferences → About, then press **Build** 7 times.

1. In Settings → Device Preferences → Developer options, turn on **USB debugging** (on some TVs, Network debugging).

1. On the computer, install Android platform-tools (it includes adb), then run:

```bash
adb connect YOUR-TV-IP:5555
adb install "Star-Wars-TV.apk"
```

Accept the "Allow USB debugging?" prompt on the TV the first time.

## 4. Make it your home screen (optional)

You can simply open Star Wars TV from your apps. To make the remote's Home button go to it:

- If the TV asks which home app to use after you press Home, pick **Star Wars TV**, then **Always**.

- Most Android TV and Google TV models never ask. Use adb (see Option B), as follows.

First note your current launcher, so you can switch back later:

```bash
adb shell cmd package resolve-activity --brief -a android.intent.action.MAIN -c android.intent.category.HOME
```

Switch to Star Wars TV on Android 10 or newer:

```bash
adb shell cmd role add-role-holder android.app.role.HOME app.tvhome.starwars 0
```

Switch to Star Wars TV on Android 7 to 9:

```bash
adb shell cmd package set-home-activity app.tvhome.starwars/.HomeAlias
```

To switch back, run the same command with your old launcher's package name (from the first command), or simply uninstall Star Wars TV:

```bash
adb uninstall app.tvhome.starwars
```

When you're done with adb, turn USB / Network debugging off again.

## 5. Using it with the remote

- **Left / Right:** fly to the next app, pick the next lightsaber or bounty puck, or hop to the next place from the bridge.

- **Down / Up:** cockpit → Jedi Temple → camp → bridge, and back. In the cockpit, **Up** lights up **Customise** at the top; OK there opens it.

- **OK:** jump to hyperspace and open the selected app, or open the selected film or series. An HDMI input in the cockpit (a PlayStation, say) switches the TV to it.

- **Back:** up one section, or out of the Customise panel. In the cockpit it closes the app (if Star Wars TV is your home screen, it does nothing).

- **Home:** back to the cockpit, from anywhere.

When it starts, the screen fades in from black over a second or two while it prepares all four sections.

## 6. Make it yours

**On the TV.** In the cockpit, press **Up**, then **OK** on **Customise**. The panel opens (it also opens by itself the first time):

- **The apps:** every app on your TV and every HDMI input, as tiles. OK adds one to the cockpit (it gets a number: its place from the left) or takes it off. Six at most.
- **The films and series open in:**
  - **JioHotstar, each title directly** (India): straight into each film, or each season's first episode. Shown when JioHotstar is installed.
  - **Your TV's search, any country:** the TV's own search for the title. On Google TV it lists where the title streams where you live; on older Android TV sets it shows the title's results (trailers, related titles) from the apps that take part in search. The safe choice outside India.
  - **Any app you picked, its search:** opens that app's search for the title (or the app itself, if it doesn't take searches).
- **Done** (or Back) keeps it; **Start again** goes back to the starting apps.

The choices are kept by the app on the TV, so they survive restarts and updates.

**In the files.** `starwars/config.js` is the starting point for every new install: the apps (`dock`), where the titles open (`films`), direct links per app (`links`), and whether the panel opens by itself the first time (`askOnFirstRun`; set it to `false` once the file is already set up for your TV). To send the titles straight into your service, add a block of links for it, keyed by the titles exactly as the JioHotstar block names them ("The Phantom Menace" … "Rogue One: A Star Wars Story", seasons as "The Mandalorian, Season 1"), with the links that service's website gives, set `films` to its package, and rebuild (section 9). [`PROMPT.md`](PROMPT.md) has a coding assistant find those links for your country and do the rest.

## 7. Troubleshooting

- **A title opens on "Who's watching?":** JioHotstar asks for a profile when it wasn't already running. Pick one and the title starts.

- **A title doesn't open, or opens the wrong page:** the JioHotstar links are for India (hotstar.com/in) and were checked on 7 November 2026. If a title moves, update its address in `starwars/config.js` (`links`) and rebuild (section 9). Outside India, choose **Your TV's search** in Customise.

- **An HDMI input does nothing:** pick it again in Customise, from the list of your TV's own inputs. The starting apps look for a port whose HDMI-CEC device name has "PlayStation" in it; if your console doesn't report its name, it won't be found and is left off.

- **"That app isn't on this TV":** it was uninstalled; take it off in Customise.

- **"This TV has no search to open":** the TV's search app is switched off (some cleanups do that). Choose an app's search in Customise instead.

- **Not smooth:** update Android System WebView from the Play Store, and restart the TV once. The cockpit runs slower than the other sections on TVs that draw its starfield on their processor (about 36 fps on the TV it was built on); TVs with less than 1.5 GB of memory may be slower everywhere.

- **Play Protect warning:** expected for any app installed from outside the Play Store.

## 8. The full prompts (build it yourself with a coding assistant)

Three steps: clean up the TV, make the pictures, then build the home screen. (To install this one and set it up for you instead, use [`PROMPT.md`](PROMPT.md).) Paste each prompt into Claude Code with your TV connected over adb (Network debugging on, TV and computer on the same Wi-Fi). Copy everything between the two lines.

### Step 1: Clean up (debloat) the TV

The easiest way is [cleanyourtv](https://github.com/Gathin23/cleanyourtv): paste its [`PROMPT.md`](https://github.com/Gathin23/cleanyourtv/blob/main/PROMPT.md) into a coding assistant and it does this safely for most Android TV and Google TV brands. Star Wars TV was built on a TV cleaned that way. The prompt below is the one used on that TV, if you'd rather do it by hand.

Optional, and fully reversible: nothing is uninstalled, only switched off. The list at the end is what was disabled on the TV this was built on (a OnePlus TV); other brands have different packages, so the assistant will look at yours first.

━━━━━━━━━━ PROMPT START ━━━━━━━━━━

```text
My Android TV is cluttered and slow. It's connected over adb (I'll run adb pair / adb connect myself; don't ever type my pairing codes). Clean it up safely, and keep everything reversible.

BEFORE ANYTHING
- Take a full backup into backup/<date>/ and point backup/latest at it: package lists (all, enabled, disabled, third-party), getprop, every setting (global, secure, system), the current HOME configuration and the TV's inputs.
- Write tools/tv (adb pointed at the TV, finding it on the network by itself) and tools/disable (disables packages for user 0, one pm call per package, and logs each one with time and batch in debloat-log.txt).

RULES
- Only ever disable for user 0 (pm disable-user --user 0). Never uninstall anything.
- Work in batches, and after each batch check that Home, the inputs/HDMI, Live TV, the remote (including its Netflix key), Wi-Fi, Bluetooth and the Play Store still work.
- Never touch: Live TV and the HDMI/TV input services, the Input/Source menu and channel scan, the TV API and picture-quality services, the remote-control services and the Netflix-key observer, Bluetooth, the keyboard, the Play Store and Play Services, setup/OOBE and the factory menu.

BATCHES
1. Telemetry: the manufacturer's push/analytics services, remote diagnostics, Google feedback and bug-report senders.
2. Content and ads: Play Auto Installs (pushes promoted apps), the manufacturer's content feed, partner rows for the stock launcher, the recommendations service.
3. Background nags: "TV manager" cleaners and smart-home services I don't use.
4. Log upload services.
5. The stock launcher, only after another home screen is installed and set as Home (on some firmware Home keeps going to the stock launcher while it's enabled).

AFTERWARDS
- restore.sh: re-enables every package disabled since the backup (or one package: ./restore.sh com.package.name; --dry-run to preview) and gives Home back to the stock launcher.
- A README listing what was disabled, why, and what was deliberately kept.

For reference, on a OnePlus TV (Android TV 10) these were disabled: com.heytap.mcs, com.heytap.tv.remotediagnosing, com.google.android.feedback, com.google.android.tv.bugreportsender, android.autoinstalls.config.OnePlus, com.oneplus.tv.launcher, com.mediatek.android.leanbacklauncher.partnercustomizer, com.google.android.tvrecommendations, com.heytap.tv.assistant.oneplus, oneplus.smarthome, com.heytap.rom.service and (last) com.google.android.tvlauncher.
```

━━━━━━━━━━ PROMPT END ━━━━━━━━━━

### Step 2: Make the pictures

All of these are in the assets zip already: the generated originals in `src/gen/`, next to the pictures the page uses in `img/`. Use these prompts to make your own versions. Every picture was made with **Nano Banana 2.1** on Higgsfield, 16:9 at 4K (3 credits a picture); the ones the page uses cost 111 credits in all (section 10). "Reference" means the image was attached to the prompt.

**Two things that saved a lot of tries:**
- The image filter refuses Star Wars characters by name, and pictures of Vader as a reference. Describe them instead ("the armoured traveller from the second reference image", "a tall commander in a long black cape and a rounded black helmet") and call them "figures".
- Make the empty scene first, then add the figures to it in a second prompt that keeps everything else exactly as it is. For the bridge, every view through the windows is an edit of the same empty bridge, so they all line up.

**The cockpit** (reference: a still of the Falcon's cockpit from Wookieepedia, [File:MF_Cockpit_TFA.png](https://starwars.fandom.com/wiki/File:MF_Cockpit_TFA.png), from The Force Awakens; the prompt asks for the cockpit as it looked in the original films). The windows come out pure black so `cockpit.py` can cut them out:

```text
Ultra-realistic cinematic photograph of the inside of the Millennium Falcon's cockpit, exactly as in the reference image and as it looked in the original Star Wars films (1977 to 1983): the round canopy at the front, its thick window frames radiating out from a small round centre pane in concentric rings, the worn grey-beige panels and metal struts, the low curved console across the front with rows of small toggle switches, square push buttons and tiny glowing indicator lights in red, amber, green and white, two small old monochrome screens, and the throttle levers between the two pilot positions. Camera at the back of the cockpit, centred, at seated eye height, looking straight ahead and level: the canopy fills the upper two thirds of the frame and is symmetrical, the console runs across the bottom third. No seats or people in view. Through every window pane there is only empty, pure, flat black: no stars, no planets, no nebula, no light and no reflections on the glass. The cockpit is dark and moody, lit only by the soft glow of the console lights and a faint cool rim light on the frames, with worn, scratched, used surfaces, fine film grain, crisp detail, high dynamic range. No text, no logos, no people.
```

**The second cockpit, from the pilots' seats** (`img/cockpit2.png`, more canopy; the page shows it with `#cockpit2`, or C on a keyboard). References: the cockpit above, then the Wookieepedia still:

```text
The same Millennium Falcon cockpit as in the first reference image, with exactly the same window frames, metal struts, colours, wear and console, but the camera has moved much further forward: it is now at the very front, between the pilot and co-pilot positions, at seated eye height, looking straight ahead and very slightly up through the canopy. The canopy now fills most of the frame: the window panes take up about 60 percent of the image, with the thick frames radiating out from the small round centre pane, which sits in the middle of the frame. Only the top edge of the front console, with its rows of small toggle switches and tiny glowing lights in red, amber, green and white, is visible along the bottom fifth of the frame. Perfectly symmetrical and level. Through every window pane there is only empty, pure, flat black: no stars, no planets, no light and no reflections on the glass. Dark and moody, lit only by the soft glow of the console lights and a faint cool rim light on the frames, worn and scratched surfaces, fine film grain, crisp detail. No seats, no people, no text, no logos.
```

**The Jedi Temple hall** (no reference). The ledge is left empty for the lightsabers:

```text
Ultra-realistic cinematic wide shot of a dark, quiet hall inside the Jedi Temple on Coruscant, as seen in the Star Wars prequel films: smooth warm-grey stone walls with tall, slender recessed columns and a high ceiling lost in shadow, very dim and moody, lit only by faint cool light falling from high above. Across the lower third of the frame runs one long, low, horizontal display ledge of dark polished stone with a thin dull-bronze edge, perfectly level and straight, starting at about 10% and ending at about 90% of the width, its top surface at about 72% of the image height. The ledge is completely empty. The space above the ledge is open dark air with nothing in it. Below the ledge, a dark polished stone floor with faint reflections. Perfectly symmetrical, centred, eye level, the camera facing the ledge straight on. Deep shadows, low contrast in the background, rich cinematic colour grading, fine film grain, crisp detail. No people, no lightsabers, no objects on the ledge, no statues, no text, no logos.
```

**The camp, in two steps.** First the empty valley (reference: the Razor Crest, Wookieepedia [File:RazorCrest-DB.png](https://starwars.fandom.com/wiki/File:RazorCrest-DB.png)):

```text
Ultra-realistic cinematic wide shot, eye level, of a wide grassy valley on a remote world at night. Knee-high wild grass, silvery green in the moonlight, covers the ground, with scattered dark boulders and low rocky outcrops; a line of distant jagged mountains along the horizon under a deep blue night sky full of stars, with two moons, one large and one smaller, low in the sky on the right. In the middle distance on the right, the gunship from the reference image (a weathered, battle-worn silver ship with two large cylindrical engine nacelles) sits landed on the grass, seen from the side and slightly behind, its boarding ramp down with a dim warm light spilling from inside. Slightly right of centre, nearer the camera, a small campfire in a ring of stones throws a warm amber pool of light on the grass. Two clear, empty spots wait beside the fire: a low flat rock just to the right of the fire, for a seated figure, and a patch of flattened grass just to the left of the fire, for a small floating pod. These spots are empty. In the foreground on the lower left, a large flat stone slab, and on it four identical small round dark metal discs, about the size of a hockey puck, laid in an even row with space between them. The top-left quarter of the image is open night sky with nothing important in it, and the area above the stone slab is open (distant grass and mountains only). The bottom tenth is dark grass. Night-time, moody, deep blue and teal shadows with warm amber firelight accents, rich cinematic colour grading, shot on an ARRI Alexa with an anamorphic 35mm lens, light haze, fine film grain, high dynamic range, crisp detail. No people, no characters, no creatures, no text, no logos.
```

Then the two of them, added in place (references: the valley above, then Wookieepedia's [File:DinDjarin-CGSWG.png](https://starwars.fandom.com/wiki/File:DinDjarin-CGSWG.png) and [File:GroguNewPram-TMtAoDD.png](https://starwars.fandom.com/wiki/File:GroguNewPram-TMtAoDD.png)):

```text
Keep the first image exactly as it is: same camera, framing, lighting, colour grade, and every blade of grass, rock, the ship, the campfire, the stone slab and the four discs on it in exactly the same place. Only add two figures, photorealistic, lit by the warm amber light of the campfire and the cool blue moonlight, each casting a soft contact shadow, at a natural scale for their distance from the camera. (1) Sitting on the low flat rock just to the right of the campfire: the armoured traveller from the second reference image, with the same polished silver armour plates, the same helmet with its T-shaped dark visor, a dark grey flight suit and a dark grey-brown cape; he sits calmly with his forearms resting on his knees, body turned three-quarters toward the camera, helmet turned slightly toward the small figure by the fire. (2) On the flattened grass just to the left of the campfire: the small figure from the third reference image, the little green child with large pointed ears, big dark eyes and a beige-brown robe, sitting up in his round silver hovering pod, which floats about knee height above the grass; he looks toward the camera. The firelight warms the sides of both figures facing the fire. Same quiet night atmosphere. No other figures, no text, no logos.
```

**The bridge, in three steps.** First the empty bridge (no reference). Through its windows here: the second Death Star over Endor's moon, which every view below replaces:

```text
Ultra-realistic cinematic wide shot inside the command bridge of an enormous wedge-shaped warship, in the style of the original Star Wars films (1980 to 1983): dark grey metal walls and floor, a raised central walkway leading to a wall of huge angled viewports at the front, two sunken crew pits on either side with rows of small glowing green and red console screens, very dark and cold. The end of the walkway, right of centre, in front of the window, is empty and clear, a spot where a tall figure will stand. Through the viewports, in deep space: a colossal half-built spherical battle station, the exposed skeletal framework of its unfinished side visible, a large circular concave dish set into its completed upper half, hanging above the curved edge of a forested green moon; a few distant wedge-shaped warships. The lower left quarter of the image is dark floor and shadow with nothing important in it. Cold blue-grey light from the viewports, rich cinematic colour grading, high contrast, fine film grain, crisp detail. No people, no text, no logos.
```

Then Vader at the window (reference: the empty bridge only):

```text
Keep this image exactly as it is: same camera, framing, lighting, colour grade, and everything in exactly the same place. Only add one person, small in the frame, standing at the far end of the central walkway in front of the window, seen from behind as a dark silhouette against the window: a tall commander in a long black cape that reaches the floor and a rounded black helmet, hands clasped behind his back, looking out of the window. Thin cold rim light on his shoulders. Natural scale for his distance. No other people, no text.
```

Then the glass made flat green, so `dark.py` can cut it out cleanly (reference: the bridge with Vader):

```text
Keep this image exactly as it is: the same bridge interior, window frames, consoles, crew pits, walkway, lighting, the tall figure in black armour and cape standing on the walkway, and the camera, every pixel in exactly the same place. Change only what is seen through the window glass: replace the space, stars, planet and station outside with a flat, perfectly uniform pure chroma-key green (#00FF00), no stars, no gradient, no reflections, no glare on the glass. The figure and the frames stay in front of the green exactly as before. No text.
```

**The four places through the windows.** Each is an edit of the empty bridge (reference: the empty bridge), so its windows line up with the cut-out:

Mustafar, for Obi-Wan Kenobi:

```text
Keep this image exactly as it is: the same bridge interior, window frames, consoles, crew pits, walkway, lighting and camera, everything in exactly the same place. Change only what is seen through the windows: the ship is now in orbit above a dark volcanic planet of black rock, its surface cracked with glowing orange rivers and lakes of lava, a thin red-orange haze along its edge, stars beyond. No battle station, no green moon, no other planet. No people, no text.
```

Coruscant at night, for Andor, Season 1:

```text
Keep this image exactly as it is: the same bridge interior, window frames, consoles, crew pits, walkway, lighting and camera, everything in exactly the same place. Change only what is seen through the windows: the ship is now in orbit above the night side of a planet entirely covered by one endless city, glittering with countless warm golden lights in dense grid patterns, a thin blue line of atmosphere at the horizon, streams of tiny moving lights of traffic, a few distant wedge-shaped warships. No battle station, no green moon. No people, no text.
```

The Death Star being built, for Andor, Season 2, then a second pass to clear reflections off the glass (reference: the first pass):

```text
Keep this image exactly as it is: the same bridge interior, window frames, consoles, crew pits, walkway, lighting and camera, everything in exactly the same place. Change only what is seen through the windows: the ship is now in deep space, close to a colossal spherical battle station still under construction, much of its grey surface plated and part of it an open skeletal framework, a large circular concave dish set into its upper half being fitted, construction platforms and small work ships around it, faint stars. No planet, no moon. No people, no text.
```

```text
Keep this image exactly as it is: the same bridge interior, window frames, consoles, walkway, lighting and camera, and outside the half-built grey spherical battle station with its exposed framework, the large circular dish being fitted, and the small construction ships, all in exactly the same place. Change only the window glass: remove every reflection on the glass, especially the ghostly reflections of the room in the three windows on the left, so the glass is perfectly clear and those windows show only deep black space with small stars, the half-built station and a few distant construction ships. No new objects, no text.
```

Scarif, for Rogue One, in three passes: the planet (the first take also drew a ring-shaped gate and the Death Star), then the gate removed, then the Death Star removed, since at that size it read as smaller than the planet (each pass references the one before):

```text
Keep this image exactly as it is: the same bridge interior, window frames, consoles, crew pits, walkway, lighting and camera, everything in exactly the same place. Change only what is seen through the windows: the ship is now in orbit above a bright tropical ocean planet of turquoise seas, white sand and small green islands with palm forests, a huge ring-shaped gate structure in orbit around it, and above the planet the completed grey spherical battle station with a large circular concave dish in its upper half. No green forest moon. No people, no text.
```

```text
Keep this image exactly as it is: the same bridge interior, window frames, consoles, walkway, lighting and camera, the tropical ocean planet with turquoise seas and green islands, and the grey spherical battle station with its circular dish, all in exactly the same place. Remove only the spoked wheel-shaped ring structure on the left; where it was, continue the planet, ocean, clouds and black space naturally. No new objects, no text.
```

```text
Keep this image exactly as it is: the same bridge interior, window frames, consoles, walkway, lighting and camera. Change only the view through the windows: remove the large grey spherical battle station completely. Where it was, continue the tropical ocean planet exactly as it looks around it: turquoise shallows, deep blue water, white sandbars and small green palm islands below, the planet's curved horizon with its thin glowing blue atmosphere, and black space with small stars above. Nothing else in the sky. No new objects, no text.
```

**Not generated:**

- **The lightsaber hilts:** Lucasfilm's own renders, from their Wookieepedia file pages: Episode I [Darth_Maul_Lightsaber_DB](https://starwars.fandom.com/wiki/File:Darth_Maul_Lightsaber_DB.png), II [YodasLightsaber-Databank](https://starwars.fandom.com/wiki/File:YodasLightsaber-Databank.png), III [Windu_Lightsaber_DB](https://starwars.fandom.com/wiki/File:Windu_Lightsaber_DB.png), IV [KenobiThirdLightsaber-DB](https://starwars.fandom.com/wiki/File:KenobiThirdLightsaber-DB.png), V [VadersLightsaber-DB](https://starwars.fandom.com/wiki/File:VadersLightsaber-DB.png), VI [LukeSkywalkerLightsaber-SWE](https://starwars.fandom.com/wiki/File:LukeSkywalkerLightsaber-SWE.png). Each is the saber of that era: Luke's is the green one he built for Return of the Jedi, not the rebuilt Skywalker saber of the sequels, and Episode V's is Vader's. `hilts.py` stands them upright and sizes them alike.
- **The holograms:** The Mandalorian's posters from TMDB, w780 size: Season 1 `K45A0qGcnGsxNKEvaOItvfVrZx.jpg`, Season 2 `pQ33MqEUEQGChyknPtvWODUza1q.jpg`, Season 3 `mYmFUlheJrXCLoZdS94kezG8Nuw.jpg`, The Mandalorian and Grogu `uwMKWjcNID0D9jjplsjkQS2OrB4.jpg` (each at `https://image.tmdb.org/t/p/w780/` plus the name). `mando.py` turns each into a blue hologram: light where the poster is light, see-through where it's dark, with scan lines.
- **The app logos:** white versions of the six apps' logos, the same files as in Hogwarts TV.

### Step 3: Build Star Wars TV

Put the pictures in a folder first: the two cockpits, the hall, the camp, the bridge with Vader on green, the empty bridge's four views, the six hilt renders and the four posters. This is the complete brief, including every refinement and everything learned getting it smooth on a TV. It's the brief for the first version, with its fixed apps and JioHotstar links; this repository has since moved those into settings (the Customise panel and `config.js`, section 6), so to make your own variation, start from this repository rather than from scratch.

━━━━━━━━━━ PROMPT START ━━━━━━━━━━

```text
Build me a home screen for my Android TV themed on Star Wars, called Star Wars TV. Build it first as an HTML prototype I can preview in Chrome, then package that same page as its own Android TV app (a full-screen WebView loading the page from the APK), so my current launcher is never touched. Design everything on a 1920×1080 stage and scale it to the screen. Only the six films of the prequels and the original trilogy, The Mandalorian, and the stories of the Empire; nothing from the sequel trilogy. Everything on screen must be accurate to the films (the right prop for the right era), and only real information as text: no invented readouts, no filler lines.

THE PICTURES (in my folder): cockpit1.png (the Falcon's cockpit with black windows), pilot1.png (the same from the pilots' seats), hall1.png (a Jedi Temple hall with an empty ledge), camp2.png (Din Djarin and Grogu by a campfire with the Razor Crest and four bounty pucks on a stone), vader_green.png (Vader on a Star Destroyer's bridge with the glass flat green), the empty bridge's four views (Mustafar, Coruscant at night, the Death Star being built, Scarif), six hilt renders and four posters. Crop each to 16:9, prepare 2560 px copies for the browser and screen-sized ones for the TV, and keep the originals.

SECTION 1, THE COCKPIT (home)
- The cockpit picture over everything, with its windows cut out: the large, near-black areas in the top of the picture become transparent, so what's drawn behind shows through the canopy. A second version from the pilots' seats (more canopy), switchable with #cockpit2.
- Behind the canopy, on a canvas: a soft nebula and far stars (one picture, drifting very slowly with the ship), a lit planet low on the right (three, rendered once each from noise: desert, ice and forest), and 900 near stars flying past in 3D, each drawn as a line from where it was a moment ago to where it is now, so speed draws them out into streaks.
- The apps are destinations out in space: Netflix, Prime Video, JioHotstar, PlayStation (an HDMI input), YouTube and Apple TV, white logos only, with a faint blue glow. The picked one sits in the round centre pane under an amber targeting reticle (four corner brackets) that slides over and settles on it, its name below in small tracked capitals; the others wait a step apart on a shallow arc, each in a pane of its own, dimmer and smaller. The stars stream from where the picked one is.
- Moving: a short burst of speed (about 0.8 s): the stars streak, the far sky turns with the ship, the cockpit lurches (springs on its position, tilt and zoom), and the canopy brightens a little.
- Opening: 0 to 0.8 s the hyperdrive spools up (the stars stretch, the cockpit rattles), 0.8 to 1.75 s the tunnel (the stars turn blue-white, a glow down the middle), then a flash and the app opens behind a black curtain with its name. Coming back: the ship drops out of hyperspace in front of the next planet, which grows in.
- The cockpit sways gently all the time (a few pixels and a fraction of a degree).
- The time and date on the square monitor in the cockpit's right-hand wall: measure its four corners and put a box onto it in perspective (a matrix3d homography), moving with the cockpit. The time large, "SUN 8 NOV" below, glowing screen-blue, clipped clear of the bezel.

SECTION 2, THE JEDI TEMPLE (one step down)
- The hall picture. On its ledge, six hilts standing upright, evenly spaced, one per film, each the saber of that film: I Darth Maul's double-bladed saber, II Yoda's, III Mace Windu's, IV Obi-Wan Kenobi's, V Darth Vader's, VI Luke Skywalker's green one. Turn each render upright (emitter on top), trim it, and size them alike.
- The picked one rises off the ledge on a spring and hovers, drifting a little, held by the Force; once clear of the ledge its blade ignites (a white core with a coloured glow in the film's colour, a slight hum), and the others shut off at once. The whole hall takes on the blade's colour, and a line of that colour glows along the ledge's edge.
- Below: "EPISODE V" small, the title large, "Darth Vader's lightsaber" small. The Roman numerals stay on the ledge under each hilt.

SECTION 3, THE MANDALORIAN (two steps down)
- The camp picture, breathing slowly. The fire's glow flickers, and sparks rise from it.
- The four bounty pucks on the stone are The Mandalorian's seasons 1 to 3 and the film The Mandalorian and Grogu. The picked one lights up: a lens on top, a pool of light on the stone, a soft beam, and above it its poster as a hologram: blue, light where the poster is light and see-through where it's dark, with scan lines, faded at the edges. It unfolds upward, flickers, and now and then slips sideways like a bad signal. Keep it clear of Grogu.
- At the top left: "THE MANDALORIAN" small, "Season 2" large.

SECTION 4, THE DARK SIDE (three steps down)
- Vader's bridge, fixed, with its glass cut out from the green (a soft edge from the green itself, and the green taken back out of the frames and the cape). Behind the glass, a place for each story in story order: Obi-Wan Kenobi (Mustafar), Andor Season 1 (Coruscant at night), Andor Season 2 (the Death Star being built), Rogue One (Scarif). Line each view up with the bridge and spread it past the window frames, so no frame of its own shows at the edge of the glass.
- The place outside drifts slowly as the ship holds station. Each place's light falls into the room (a soft spill in its colour).
- Left/Right: a hyperspace hop seen only through the glass: streaks rush in, the place changes at their peak, then they fall away (about 1.35 s); the bridge trembles a little and the light changes with the place. If I press again mid-hop, it goes to the new place instead.
- At the bottom left: the year or the series small, the title large, and a row of four short marks with the current one lit red.
- OK: the full jump through the windows, and the title opens.

NAVIGATION
- Left/Right within a section. Down/Up: cockpit → Jedi Temple → camp → bridge and back, sliding on a spring. OK opens. Back goes up one section; in the cockpit it closes the app, unless the app is the home screen (then nothing). Home always returns to the cockpit. No hints or cues on screen.

OPENING THINGS (the TV app's bridge to the page: TV.launch(package or "input:<name>") and TV.openFilm(url, package, title))
- Apps by package: Netflix com.netflix.ninja, Prime Video com.amazon.amazonvideo.livingroom, JioHotstar in.startv.hotstar, YouTube com.google.android.youtube.tv, Apple TV com.apple.atve.androidtv.appletv (the TV launch intent, or the normal one). PlayStation: switch to its HDMI input (TvContract.buildChannelUriForPassthroughInput with my TV's input id).
- Films and series: an ACTION_VIEW intent for the title's JioHotstar page (https://www.hotstar.com/in/movies/<slug>/<id>; for a season, its first episode's /watch page) sent to in.startv.hotstar. Look up each title's current address in hotstar.com's sitemap. Without a link, JioHotstar's own search for the title.
- The app tells the page when it goes to the background and comes back (tvPause / tvResume), so it drops out of hyperspace when I return; if nothing opened, it comes back by itself after a few seconds.

THE TV APP
- A separate package (app.tvhome.starwars), Java, no extra libraries, a full-screen black-background WebView with JavaScript, and the page's console going to logcat.
- Serve the page and its pictures from the APK's assets under https://appassets.androidplatform.net (shouldInterceptRequest), not file://: a page loaded from a file has no origin, so the browser won't let it use a picture as a CSS mask or a WebGL texture.
- In the TV's app list. A home-screen entry (an activity alias) that's off in debug builds, so it never competes with my launcher until I switch it on from adb, and on in the signed release build. Debug builds are testOnly so adb can switch that entry on and off.
- A build script that copies the page into the app with TV-sized pictures (refusing to build if the page's script doesn't parse), builds it, waits until I haven't touched the physical remote for 45 seconds, installs it and opens it. Never send keys or install while I'm using the remote. A script to switch the home screen to it and back.
- Log a frame-time report every 5 seconds so you can measure smoothness on the TV.

MAKE IT SMOOTH ON THE TV (a 1.8 GB MediaTek TV, where the WebView's 2D canvas is drawn by the processor)
- Fit the stage with CSS zoom on the TV, not transform: scale(); under a transform the TV renders every moving layer at four times the pixels and runs out of graphics memory.
- No CSS animations: move everything from one requestAnimationFrame loop. Move things with transforms and opacity only; a scale that changes every frame makes the TV redraw that picture from scratch.
- Draw anything that animates over a large area with WebGL, not the 2D canvas: on this TV a few full-screen 2D drawImage calls cost about 22 ms a frame, and a few hundred stroked lines about 300 ms. The bridge's glass (the place outside, the hyperspace streaks and their glow) is one WebGL canvas the size of the glass, and the room's light is a half-resolution WebGL canvas masked by the bridge picture, redrawn only when it changes. Keep the 2D canvas as a fallback.
- Full-screen layers cost even when mostly transparent: crop every layer to what it covers, and draw soft light at half resolution. No blend modes on the TV.
- At start-up, behind a nearly black curtain, decode every picture and show each section for a few frames (Jedi Temple, camp, bridge, cockpit), drawing each WebGL program once, so nothing stalls on the first visit.
- The page handles every arrow key itself (preventDefault, even unused ones) and has no click handlers on the TV, otherwise the web view moves its own focus and draws a gold box.
- Skip style writes that haven't changed.

Preview everything in Chrome first (screenshots of each section), then put it on my TV and measure.
```

━━━━━━━━━━ PROMPT END ━━━━━━━━━━

### Follow-up prompts, in the order the look was refined

1. "I like the cockpit idea. When we toggle between the apps on the home screen, there should be a slight jump into hyperspace: not a complete hyperspace, but a speed-up in how fast the ship is moving. Do it in HTML first."

1. "We don't need to follow the same format as the other home screens. Try something very different, something that is more apt for the fandom."

1. "I really want to do something with lightsabers. Only the six films: the prequels and the originals. I don't want to touch the sequels at all. And a section dedicated to the Mandalorian, like the Harry Potter greenhouse, with the Mandalorian and Grogu."

1. "Are those lightsabers accurate, and how do they relate to those films? I want this to be absolutely perfect, with no AI-looking elements."

1. "Generate an image of the cockpit. I want something accurate to the actual Star Wars ship. Upload any reference image you need."

1. "I also want another version of the cockpit: the glass is very little. It should be 50/50, or the viewport 40% or so."

1. "We should not leave out the dark side: something with the Death Star, Darth Vader or the Sith."

1. "The only animation in the dark side is the light beam from the Death Star; it needs more life." Then, after ships were added outside: "The ships look choppy, they need to be outside the window. Go for a completely different approach." The approach chosen: Vader's bridge stays, and each title gets its own place through the windows.

1. "Remove the cues (scroll up for this, scroll down for that). Take them all off."

1. "Move the date and time to one of the displays inside the cockpit instead of the glass, even if the format has to change to fit."

1. "Get rid of the Death Star in the Rogue One view: it would be far bigger than the planet. Just the island planet."

1. "The dark side is laggy when I toggle between the categories" (on the TV). Fixed by moving the glass and the room's light to WebGL.

## 9. Rebuilding from the source

| Path | What it is |
|---|---|
| `starwars/index.html` | The whole home screen (one page). Preview it with `python3 -m http.server 8780 --directory starwars` and open `http://localhost:8780/`; add `?tv` to see the TV version. Jump around with `#saga`, `#mando`, `#dark`, `#app=0..5`, `#f=0..5`, `#m=0..3`, `#d=0..3`, and `#cockpit2` for the second cockpit. In a browser the Customise panel shows a sample list of apps. |
| `starwars/config.js` | The starting apps, where the titles open, and the direct links (section 6). |
| `starwars/tools/` | The picture tools: `cockpit.py 1` and `cockpit.py 2` (the cockpits, windows cut out), `hall.py`, `mando.py` (the camp and the holograms), `hilts.py`, `dark.py` (the bridge cut out from the green, and the four views lined up with it). They read the originals from `starwars/src/`: unzip the assets zip's `src/` there first. `tv_assets.py` (the TV copy) is run by `build.sh`. |
| `starwars-tv/` | The Android TV app (Java, no libraries): `MainActivity.java` is the WebView, the asset server and the bridge (`TV.launch`, `TV.openFilm`, `TV.search`, `TV.apps`, `TV.inputs`, `TV.icon`). |
| `build.sh` | `./build.sh` builds the APK; `./build.sh install` also installs it on the TV adb is connected to. |

**You need:** JDK 17 and the Android SDK (platform 35; Android Studio has both), Python 3 with Pillow and NumPy, and Node.js (it checks the page's script before a build).

```bash
echo "sdk.dir=$HOME/Library/Android/sdk" > starwars-tv/local.properties     # where your Android SDK is
./build.sh
```

Without a key, the release build is signed with your debug key, which is fine for your own TV. To sign it with your own release key:

```bash
mkdir -p starwars-tv/release
keytool -genkeypair -keystore starwars-tv/release/starwars-release.jks -alias starwars -keyalg RSA -keysize 2048 -validity 10000
```

and create `starwars-tv/release/keystore.properties` with `storeFile=release/starwars-release.jks`, `storePassword=…`, `keyAlias=starwars` and `keyPassword=…`. Keep that key private (`.gitignore` keeps `starwars-tv/release/` out of git). The APK on the Releases page is signed with the author's own key, so a build signed with yours can't update it in place: uninstall it first.

## 10. Credits used

111 Higgsfield credits for the pictures the page uses, at 3 credits a picture (Nano Banana 2.1, 4K), counting every take of each prompt; refused takes cost nothing. The cockpit 12, the second cockpit 12, the hall 12, the camp 18 (the valley 12, the two of them 6), the bridge 18 (the empty bridge 12, Vader 3, the green glass 3), and the four views 39 (Mustafar 6, Coruscant 6, the Death Star being built 12, Scarif 15). The hilts, the holograms and the logos cost nothing.
