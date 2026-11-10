# sgawser on Android, phase 1: Cromite set up to be silent

Status: draft, not yet verified. sgawser, before it is a build, is a profile: a documented setup of Cromite for Android, plus a ten minute check anyone can run on their own phone. No binary.

The checklist is written from Cromite's documentation, not from a run, and Cromite's settings move between versions. Every row stays a claim until the emulator lab measurement of Cromite (first run, defaults, trackers, private tab, uninstall) confirms it; this page is updated with the measured results and the Cromite version they apply to.

## 1. Install without Google

1. Download the Cromite APK for your phone's architecture (arm64 on almost every phone since 2016) from Cromite's own releases page, or add Cromite's F-Droid repository to the F-Droid client. Never from Google Play: Cromite is not there, and the Play Store is itself a Google service.
2. Before installing, compare the APK's SHA-256 with the one printed on the releases page. On the phone, a file manager that shows hashes or the `sha256sum` of a terminal app does it; on a computer, `certutil -hashfile <file> SHA256` on Windows.
3. Install. Android asks to allow installs from that source once.

## 2. The checklist

| Default | Where in Cromite | Set to |
|---|---|---|
| Usage data, telemetry | none exists in Cromite (removed by patches) | nothing to do; the ten minute check below confirms it |
| Crash reports | none uploaded | nothing to do |
| Default search engine | Settings > Search engine | a community or non-profit engine that passes the selection rules: MetaGer (SUMA-EV, German non-profit), added as custom engine with `https://metager.org/meta/meta.ger3?eingabe=%s`. To confirm. |
| Search suggestions | Settings > Privacy and security > "Search and URL suggestions" (name to verify) | off |
| Safe Browsing | Settings > Privacy and security > Safe Browsing | No protection (Cromite's blocklists stay on) |
| DNS over HTTPS | Settings > Privacy and security > Use secure DNS | on, "With: custom provider", `https://dns.digitale-gesellschaft.ch/dns-query` (address taken from the operator's own page) |
| Third-party cookies | Settings > Site settings > Third-party cookies | Block |
| Tracking protection | Cromite's AdBlock (on by default) and the filter list | on; to be confirmed by the lab's tracker test |
| Do Not Track, GPC | Settings > Privacy and security | GPC on if offered; DNT off |
| Sponsored new tab | Cromite's new tab has no feed | nothing to do |
| AI feature | none in Cromite | nothing to do |
| Password and payment prompts | Settings > Passwords, Payment methods, Addresses | Save passwords off, Save and fill payment methods off, Save and fill addresses off |
| Sign-in, account prompts | none in Cromite | nothing to do |
| Auto-update | Settings > About Cromite > update check (if present) | off; update through F-Droid on your own schedule |
| Extras | Cromite flags page (`chrome://flags`) | leave Cromite's defaults; note every flag you change |

Rows marked "nothing to do" are claims from Cromite's documentation until the first run measurement proves them.

## 3. The ten minute check on your own phone

Tool: PCAPdroid (open source, community maintained from Italy, on F-Droid). It captures the phone's own traffic through Android's VPN interface, no root, nothing leaves the phone.

1. Install PCAPdroid from F-Droid. In its settings choose "Target app": Cromite, so only the browser's traffic is recorded.
2. Make sure Cromite is fully closed (Settings > Apps > Cromite > Force stop).
3. In PCAPdroid press Start. Accept the VPN prompt (this VPN is local to the phone, it is how the capture works).
4. Open Cromite. Do nothing: no tap, no typing, no page. Lock the screen if you like. Wait ten minutes.
5. Return to PCAPdroid and press Stop. Open the Connections tab.

Reading the result: zero connections is a pass. Every row shows the host, the bytes, and the app; PCAPdroid can export the list as CSV to share in a GitHub issue (it contains hostnames, never your identity). A row to a blocklist or update host after you switched updates off is a finding worth reporting, not something you did wrong.

Limit: this is the self-check of a single phone, not a lab measurement. The emulator lab repeats it on a clean emulator with the capture outside the phone, where nothing on the device can hide a connection.

## 4. What this profile cannot do (work for a later sgawser build)

- Remove the in-app update check if the installed build has one, or guarantee every default from the first start. A settings checklist is something a user does; a build is something a user receives.
- Show the browser's own network log inside the browser (PCAPdroid plays that role here).
- Offer a signed sgawser download: that needs the build first.
