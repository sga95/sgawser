# sgawser on Android, phase 1: Cromite set up to be as quiet as its settings allow

Status: draft, not yet verified. sgawser, before it is a build, is a profile: a documented setup of Cromite for Android, plus a ten minute check anyone can run on their own phone. No binary.

The checklist is written from Cromite's documentation, not from a run, and Cromite's settings move between versions. Every row stays a claim until the emulator lab measurement of Cromite (first run, defaults, trackers, private tab, uninstall) confirms it; this page is updated with the measured results and the Cromite version they apply to.

**Know this before installing (checked on 2026-11-10).** Cromite's latest release is v153.0.8010.37 of 15 September 2026; the stable release before it was 21 May 2026. Chrome, which is built from the same engine, was at version 157 on the day of the check, gets a new version every two weeks and security fixes every week. On 10 November 2026 this Cromite was eight weeks old, so the warning applies now: do not use it for banking or other sensitive things until a newer release is out. After about ten weeks without an update (around 24 November 2026 for this release) the engine is also expected to stop one of its certificate checks; this is not yet tested on Cromite. This page prints the gap every time it is updated.

## 1. Install without the Play Store

Limit: on most phones Google's Play Protect still checks every app you install, and may tell Google about it or warn you. Do not switch it off for this guide. Cromite's files are hosted on GitHub, which belongs to Microsoft.

1. Easiest: install the F-Droid app from f-droid.org and add Cromite's repository to it (the link is on Cromite's page). F-Droid then checks each download and offers updates. By hand: on Cromite's releases page download the file named `arm64_ChromePublic.apk` (for almost every phone since 2016). Do not take the `SystemWebView` files: they are a different thing. Never from Google Play: Cromite is not there.
2. If you installed through F-Droid, skip this step: F-Droid checks the download itself. If you downloaded the file by hand, the releases page shows a SHA-256 value next to each file: compare it on a computer (on Windows: `certutil -hashfile <file> SHA256`). This catches a damaged or swapped download; it proves nothing if the releases page itself was tampered with. This guide names no phone app for this step yet.
3. Install. Android asks to allow installs from that source once.

## 2. The checklist

| Default | Where in Cromite | Set to |
|---|---|---|
| Usage data, telemetry | none exists in Cromite (removed by patches) | nothing to do; the ten minute check below confirms it |
| Crash reports | none uploaded | nothing to do |
| Default search engine | Settings > Search engine | Cromite starts with a search engine of its own choice (which one is to be checked in the lab). No engine has yet been checked against the project's rules, so this guide recommends none: MetaGer, the first candidate, needs a paid key since September 2024. Whatever you use, switch suggestions off (next row). |
| Search suggestions | Settings > Privacy and security > "Search and URL suggestions" (name to verify) | off |
| Safe Browsing | Settings > Privacy and security > Safe Browsing | No protection (Cromite states it is already off; setting name to verify). Limit: after this the browser gives no warning about malware pages and almost none about fake login pages. Cromite's ad-block lists do not replace it. |
| DNS over HTTPS | Settings > Privacy and security > Use secure DNS | on, "With: custom provider", `https://dns.digitale-gesellschaft.ch/dns-query` (address taken from the operator's own page). Limits: this service sees the name of every site you open, and it is run by volunteers who promise no availability. If pages stop opening it may be down: switch this setting off for a while and on again later. |
| Third-party cookies | Settings > Site settings > Third-party cookies | Block |
| Tracking protection | Cromite's ad blocker (on by default). It is the engine of eyeo, the company behind Adblock Plus, and by default it downloads its filter lists every day from the Adblock Plus download server | on; the daily download is a known connection (section 3); the blocking itself is to be confirmed by the lab's tracker test. If its settings show a list called Acceptable Ads, switch it off (not yet checked whether Cromite has one) |
| Do Not Track, GPC | Settings > Privacy and security | GPC on if offered; DNT off |
| Sponsored new tab | Cromite's new tab has no feed | nothing to do |
| AI feature | none in Cromite | nothing to do |
| Password and payment prompts | Settings > Passwords, Payment methods, Addresses | Save passwords off, Save and fill payment methods off, Save and fill addresses off |
| Sign-in, account prompts | none in Cromite | nothing to do |
| Auto-update | Cromite's own update check. Its privacy policy says it is off by default and checks once a day when on (setting name to verify) | If you added Cromite's repository to F-Droid: leave it off and update through F-Droid. If you installed the file by hand: switch it on. It then contacts github.com once a day, which is a smaller risk than an old engine |
| Extras | Cromite flags page (`chrome://flags`) | leave Cromite's defaults; note every flag you change |

Rows marked "nothing to do" are claims from Cromite's documentation until the first run measurement proves them.

## 3. The ten minute check on your own phone

Tool: PCAPdroid (open source, written by one developer, in Italy according to his profile, on F-Droid). It sells optional extras, through Google Play or a licence code, and names a company sponsor; nothing this check uses is paid. It captures the phone's own traffic through Android's VPN interface, without root, and its author states that the data is processed on the phone.

1. Install PCAPdroid from F-Droid. In its settings choose "Target app": Cromite, so only the browser's traffic is recorded.
2. Make sure Cromite is fully closed (Settings > Apps > Cromite > Force stop).
3. In PCAPdroid press Start. Accept the VPN prompt (this VPN is local to the phone, it is how the capture works).
4. Open Cromite. Do nothing: no tap, no typing, no page. Lock the screen if you like. Wait ten minutes.
5. Return to PCAPdroid and press Stop. Open the Connections tab.

Reading the result. Zero connections is the goal, and stock Cromite is not expected to reach it. Its own privacy policy lists: a filter-list download from `easylist-downloads.adblockplus.org` once a day (on by default); a font archive from `www.cromite.org`, fetched once; and, only when the connection seems broken, a test request to `www.ripe.net` and `k.root-servers.net`. Because you set secure DNS in section 2, rows to `dns.digitale-gesellschaft.ch` are expected too, and rows to `github.com` if you switched the update check on. These rows are expected until the lab has measured which settings stop them. Any other row is a finding worth reporting, not something you did wrong.

Every row shows the host, the bytes and the app. PCAPdroid can export the list as CSV. The file holds the names of the sites the browser contacted, which is browsing history: read it before sharing it in a public issue.

Limit: this is the self-check of a single phone, not a lab measurement. The emulator lab repeats it on a clean emulator with the capture outside the phone, where nothing on the device can hide a connection.

## 4. What this profile cannot do (work for a later sgawser build)

- Remove the in-app update check if the installed build has one, or guarantee every default from the first start. A settings checklist is something a user does; a build is something a user receives.
- Show the browser's own network log inside the browser (PCAPdroid plays that role here).
- Offer a signed sgawser download: that needs the build first.
