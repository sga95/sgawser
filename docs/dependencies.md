# Dependencies

Everything sgawser relies on that the project did not write: code, data, services, hosting, tools, and the apps the guides ask people to install. Nothing is built yet, so the list has two parts: what is in use today, and what the design plans to use.

Facts were read on each project's own pages on 2026-11-10. "Unverified" marks what could not be confirmed that day. A final completeness pass over this list is still owed, so a missing row is possible: open an issue if you find one.

## The rules

**Order of preference for every need.**

1. Drop the need.
2. Use what the platform and the engine already contain.
3. Write it in the project, in plain code, when it is small and is not a security standard.
4. Take a third-party part only as a written exception in this list.

**Never home made.** The engine, cryptography and hashing, signature formats, TLS and certificate checks, the update path and the repository format, the parsing of addresses. For these the project uses the platform's or the engine's implementation, or a named existing standard.

**What a third-party part should be.** Open source; run by a community or a non-profit, not by a company that sells it or makes money from it; transparent about who runs it and how it is paid for. The author also applies criteria of his own that are not written here for now. Many rows below do not meet these rules. Each of those is marked "exception" with the reason, or "undecided" where the choice is still open.

## In use today

| What | Used for | Who is behind it | Fits the rules | Status and reason |
|---|---|---|---|---|
| Cromite | The browser the phase 1 guide sets up; the planned base of a build | One maintainer (GitHub account uazo; the project's pages do not say who that is). GPL version 3, funded by donations | Yes | Kept. Limit: its latest release is v153.0.8010.37 of 15 September 2026, about two months behind the engine's security fixes on the check date. Privacy Guides removed it from its recommendations on 18 May 2026 for lack of updates |
| Chromium, inside Cromite | Renders every page, makes every connection, holds TLS, certificate checks and the sandbox | Google, with other companies contributing. BSD-style licence | No | Exception: no engine that fits the rules can yet display enough of today's web for daily use. Every Google service is removed, and the removal is to be measured |
| Ad-blocking engine inside Cromite, and its default filter lists | Blocks trackers and ads in the phase 1 setup | eyeo, the company behind Adblock Plus and its paid Acceptable Ads programme. The lists are downloaded daily from its server by default | No | Undecided. Comes with Cromite. A build would either use an own host-list check or carry a written exception |
| Android | The platform | Google | No | Exception: the only mobile platform that allows a browser with its own engine. Note: Google's developer verification is announced for all certified devices in 2027; apps from developers not registered with Google will then install only through a computer or a one-time advanced flow |
| F-Droid client | Installs and updates Cromite and PCAPdroid without Google Play | The F-Droid project, under The Commons Conservancy, a foundation in the Netherlands | Yes | Kept |
| PCAPdroid | The ten minute self-check of the guide | Emanuele Faranda, an individual (Italy, per his profile). GPL version 3 or later. Sells optional extras and names a company sponsor | Unclear | Kept. The proof must come from software other than the browser, and the capture the guide uses is free |
| Digitale Gesellschaft resolver | Secure DNS in the guide; planned default of a build | Digitale Gesellschaft, a Swiss association of non-profit character | Yes | Kept. Limits: the resolver sees every site name looked up, its no-logging policy is its own statement, and it is volunteer run with no availability promise. It has not yet been asked whether it accepts a browser's default traffic |
| GitHub | Hosts this repository, its pull requests and issues | GitHub, a subsidiary of Microsoft | No | Exception, undecided for the long run: the project's tooling works here today. A non-profit forge (Codeberg, Berlin) is the candidate if the project moves |
| Vercel | Serves sgalliani.com, where guides and releases would be published | Vercel, a company; free plan for non-commercial personal use | No | Exception for the site. Its free plan cannot serve a browser package (limit of 100 MB per file), so releases need another home |
| The sgalliani.com domain | The address of the site | Registrar and DNS provider not yet recorded here | Unverified | To be listed |
| Proton mailbox | Private vulnerability reports ([SECURITY.md](../SECURITY.md)) | Proton, a Swiss company (not re-checked on the check date) | No | Exception: a private mailbox cannot be home made safely |
| Git | Version history, patches | Legal home is a charity | No | Exception: the standard tool, nothing to replace it with |
| Python 3 | The project's scripts (lab, checks, generators) | Python Software Foundation (not checked on the check date) | Unverified | Kept as the single script language; no package beyond its standard library |
| Android Emulator and the open source system image | The measurement lab | Google | No | Exception, lab only: the image without Google apps is used. Limit: the lab measures an emulator build, so a pass on a real phone is a required second witness |
| Cloudflare Workers | Serve the controlled test pages of the lab and keep their request log | Cloudflare, a company | No | Exception, lab only, to shrink: most test pages can move to a small local server kept in this repository |
| AI assistant | Drafts documents and code, which the maintainer reviews | Claude, made by the company Anthropic | No | Exception: stated in the README; the commit history shows where it was used |

## Planned for a build, not in use yet

| What | Used for | Who is behind it | Fits the rules | Status and reason |
|---|---|---|---|---|
| Chromium build toolchain | Compiling the engine | Google; the build downloads prebuilt compilers | No | Exception with the engine. Limit: the maintainer has no machine that can build it. The build needs Linux, more than 16 GB of memory is recommended, and 100 GB of disk |
| Android APK signing and its signer | Signing each release; Android refuses an update signed by another key | Google (part of Android) | No | Exception: signature formats are never home made |
| F-Droid repository format and its server tool | Publishing releases so that a repository client updates the browser | The F-Droid project | Yes | Kept: it removes the need for any update code inside the browser |
| Signature copy and comparison tool (apksigcopier) | Letting other people check that a published package matches the public source | Fay Stegerman, an individual. GPL version 3 or later | Unverified | Kept: comparing signed packages is signature handling, never an own script |
| Applied Privacy resolver | Second choice for secure DNS | Foundation for Applied Privacy, an Austrian association; calls the service experimental and best effort | Yes | Kept as the second entry |
| Phishing.Database | List of known phishing addresses for the address check | Volunteers; MIT licence | Yes | Kept on condition: the source looked five weeks old on the check date; if it is not updated again the feature is cut |
| Tracker and ad lists | Blocking by list | Not chosen. Candidates to check: EasyList and EasyPrivacy, by the EasyList authors | Unverified | Undecided |
| Search engine | The default search | None chosen | n/a | Undecided. No free search engine with its own index fits the rules; the options are a volunteer-run relay, with its operator's consent, or a written exception |
| Typefaces | The interface | Space Grotesk (Florian Karsten, Czech Republic) and Space Mono (designed for Google Design, owned by Google); both under the SIL Open Font License | No for Space Mono | Undecided: the system typeface is the alternative with no added part |
| Servo | Measured once a year as the possible future engine | A project of Linux Foundation Europe, Brussels | Unclear | Kept as a measurement only; nothing of it ships |
| Independent builders | Rebuilding each release from the public source | People who are not the maintainer; none yet | n/a | Until two exist, releases say "published by the maintainer only" |

## Written in the project (planned)

The network gate and the local network log. The simple and expert modes and the routine that checks the protections. The address check rules and its small lists (brands, link shorteners, pressure words). The help texts. Theme colours. The scripts that count lines, check patches, run the tests and draft each release record. A local server for most test pages. The test that reads a capture and counts connections.

## Withdrawn or left out

| What | Why |
|---|---|
| MetaGer as default search | It needs a paid key since September 2024 |
| Google Play, Google Safe Browsing, Google's DRM module download | Google services; the browser is designed to contact none of them |
| An update check inside the browser | Proposed to be left out, not decided yet: updates would come through the repository client, and an own update protocol would be home-made security |
| Any library added by sgawser's own code | The own layer adds none |
