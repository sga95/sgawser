# sgawser on Android, phase 1: Cromite set up to be as quiet as its settings allow

Status: draft, not yet verified. sgawser, before it is a build, is a profile: a documented setup of Cromite for Android, plus a ten minute check anyone can run on their own phone. No binary.

The checklist is written from Cromite's documentation, not from a run, and Cromite's settings move between versions. Every row stays a claim until the emulator lab measurement of Cromite (first run, defaults, trackers, private tab, uninstall) confirms it; this page is updated with the measured results and the Cromite version they apply to.

**Know this before installing (checked on 2026-11-10).** Cromite's latest release is v153.0.8010.37 of 15 September 2026. Chrome, which is built from the same engine, was at version 157 on the day of the check and gets a new version every two weeks. This Cromite therefore lacks about two months of the engine's security fixes. Look at the date of the latest release on Cromite's releases page first: while it is weeks behind, do not use it for banking or other sensitive things. This page prints the gap every time it is updated.

## 1. Install without Google

1. Download the Cromite APK for your phone's architecture (arm64 on almost every phone since 2016) from Cromite's own releases page, or add Cromite's F-Droid repository to the F-Droid client. Never from Google Play: Cromite is not there, and the Play Store is itself a Google service.
2. Before installing, compare the APK's SHA-256 with the one shown on the releases page. This catches a damaged or swapped download; it proves nothing if the releases page itself was tampered with. On the phone, a file manager that shows hashes or the `sha256sum` of a terminal app does it; on a computer, `certutil -hashfile <file> SHA256` on Windows.
3. Install. Android asks to allow installs from that source once.

## 2. The checklist

| Default | Where in Cromite | Set to |
|---|---|---|
| Usage data, telemetry | none exists in Cromite (removed by patches) | nothing to do; the ten minute check below confirms it |
| Crash reports | none uploaded | nothing to do |
| Default search engine | Settings > Search engine | not chosen yet. MetaGer, the first candidate, needs a paid key since September 2024. Until an engine has been checked against the project's rules, keep the one you trust and switch suggestions off (next row). |
| Search suggestions | Settings > Privacy and security > "Search and URL suggestions" (name to verify) | off |
| Safe Browsing | Settings > Privacy and security > Safe Browsing | No protection (Cromite's blocklists stay on) |
| DNS over HTTPS | Settings > Privacy and security > Use secure DNS | on, "With: custom provider", `https://dns.digitale-gesellschaft.ch/dns-query` (address taken from the operator's own page) |
| Third-party cookies | Settings > Site settings > Third-party cookies | Block |
| Tracking protection | Cromite's ad blocker (on by default). It is the engine of eyeo, the company behind Adblock Plus, and by default it downloads its filter lists every day from that company's server | on; the daily download is a known connection (section 3); the blocking itself is to be confirmed by the lab's tracker test |
| Do Not Track, GPC | Settings > Privacy and security | GPC on if offered; DNT off |
| Sponsored new tab | Cromite's new tab has no feed | nothing to do |
| AI feature | none in Cromite | nothing to do |
| Password and payment prompts | Settings > Passwords, Payment methods, Addresses | Save passwords off, Save and fill payment methods off, Save and fill addresses off |
| Sign-in, account prompts | none in Cromite | nothing to do |
| Auto-update | Cromite's own update check. It may ask at the first start; Cromite's documents disagree on the default | off; update through F-Droid on your own schedule, and do update: an old engine is the larger risk |
| Extras | Cromite flags page (`chrome://flags`) | leave Cromite's defaults; note every flag you change |

Rows marked "nothing to do" are claims from Cromite's documentation until the first run measurement proves them.

## 3. The ten minute check on your own phone

Tool: PCAPdroid (open source, written by one developer in Italy, on F-Droid). It sells optional extras; nothing this check uses is paid. It captures the phone's own traffic through Android's VPN interface, without root, and its author states that the data is processed on the phone.

1. Install PCAPdroid from F-Droid. In its settings choose "Target app": Cromite, so only the browser's traffic is recorded.
2. Make sure Cromite is fully closed (Settings > Apps > Cromite > Force stop).
3. In PCAPdroid press Start. Accept the VPN prompt (this VPN is local to the phone, it is how the capture works).
4. Open Cromite. Do nothing: no tap, no typing, no page. Lock the screen if you like. Wait ten minutes.
5. Return to PCAPdroid and press Stop. Open the Connections tab.

Reading the result. Zero connections is the goal, and stock Cromite is not expected to reach it. Its own privacy policy lists a daily filter-list download from `easylist-downloads.adblockplus.org` (on by default), a font archive from `www.cromite.org`, and connectivity probes to `www.ripe.net` and `k.root-servers.net`. Rows to those hosts are expected until the lab has measured which settings stop them. Any other row is a finding worth reporting, not something you did wrong.

Every row shows the host, the bytes and the app. PCAPdroid can export the list as CSV. The file holds the names of the sites the browser contacted, which is browsing history: read it before sharing it in a public issue.

Limit: this is the self-check of a single phone, not a lab measurement. The emulator lab repeats it on a clean emulator with the capture outside the phone, where nothing on the device can hide a connection.

## 4. What this profile cannot do (work for a later sgawser build)

- Remove the in-app update check if the installed build has one, or guarantee every default from the first start. A settings checklist is something a user does; a build is something a user receives.
- Show the browser's own network log inside the browser (PCAPdroid plays that role here).
- Offer a signed sgawser download: that needs the build first.
