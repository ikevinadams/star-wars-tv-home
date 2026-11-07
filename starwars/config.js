// Star Wars TV's settings: the apps in the cockpit and where the films and series open.
// On the TV, the Customise panel (Up in the cockpit, then OK) changes these and keeps its own copy; this file is the
// starting point for a new install, and the one to edit before you build. PROMPT.md fills it in for you.
window.STARWARS = {
  // Open the Customise panel by itself the first time Star Wars TV starts, so someone who only installed the APK can pick
  // their own apps and service on the TV. Set it to false when this file is already set up for the TV (PROMPT.md does):
  // the panel then waits until someone presses Up in the cockpit.
  askOnFirstRun: true,

  // Up to six, left to right. `pkg` is an app's package name, or "input:<name>" for an HDMI port: the port whose
  // HDMI-CEC device name contains <name> (or whose TV input id is exactly <name>). Anything not on the TV is skipped.
  dock: [
    { pkg: "com.netflix.ninja", label: "Netflix" },
    { pkg: "com.amazon.amazonvideo.livingroom", label: "Prime Video" },
    { pkg: "in.startv.hotstar", label: "JioHotstar" },
    { pkg: "input:playstation", label: "PlayStation" },
    { pkg: "com.google.android.youtube.tv", label: "YouTube" },
    { pkg: "com.apple.atve.androidtv.appletv", label: "Apple TV" },
  ],

  // Where OK on a lightsaber, a bounty puck or a place through the bridge's windows takes you:
  //   an app's package: straight to the title if `links` below has it for that app, else that app's own search
  //   "search":         the TV's own search, which shows where each title streams in your country
  // If the app isn't installed, the TV's search is used.
  films: "in.startv.hotstar",

  // Direct links to each title, per app, keyed by the title as Star Wars TV names it. Each is opened in that app with an
  // ordinary "view this link" request, so use the links the app's own website gives. A season opens at its first episode.
  // Add a block for your service and set `films` to its package.
  links: {
    "in.startv.hotstar": {                     // JioHotstar, India (from hotstar.com's own sitemap, checked 2026-11-07)
      "The Phantom Menace": "https://www.hotstar.com/in/movies/star-wars-the-phantom-menace/1660010584",
      "Attack of the Clones": "https://www.hotstar.com/in/movies/star-wars-attack-of-the-clones/1660010583",
      "Revenge of the Sith": "https://www.hotstar.com/in/movies/star-wars-revenge-of-the-sith/1660010579",
      "A New Hope": "https://www.hotstar.com/in/movies/star-wars-a-new-hope/1260016021",
      "The Empire Strikes Back": "https://www.hotstar.com/in/movies/star-wars-the-empire-strikes-back/1660010582",
      "Return of the Jedi": "https://www.hotstar.com/in/movies/star-wars-return-of-the-jedi/1660010578",
      "The Mandalorian, Season 1": "https://www.hotstar.com/in/shows/the-mandalorian/1260021071/chapter-1-the-mandalorian/1260021078/watch",
      "The Mandalorian, Season 2": "https://www.hotstar.com/in/shows/the-mandalorian/1260021071/chapter-9-the-marshal/1260045791/watch",
      "The Mandalorian, Season 3": "https://www.hotstar.com/in/shows/the-mandalorian/1260021071/chapter-17/1260112781/watch",
      "The Mandalorian and Grogu": "https://www.hotstar.com/in/movies/star-wars-the-mandalorian-and-grogu/1271500187",
      "Obi-Wan Kenobi": "https://www.hotstar.com/in/shows/obi-wan-kenobi/1260098452",
      "Andor, Season 1": "https://www.hotstar.com/in/shows/andor/1260103701/kassa/1260103764/watch",
      "Andor, Season 2": "https://www.hotstar.com/in/shows/andor/1260103701/one-year-later/1271339641/watch",
      "Rogue One: A Star Wars Story": "https://www.hotstar.com/in/movies/rogue-one-a-star-wars-story/1260018354",
    },
  },
};
