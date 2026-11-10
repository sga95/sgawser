# sgawser

> **An independent browser that wants nothing from you.**
>
> In an era that always chases something new, the cloud, AI, nobody ever asked who controls the browser.
>
> Thanks to the people who built Chromium and left it open to everyone: it is the engine that opens today's web, and an independent one that does the same does not exist yet.
>
> sgawser is being built to take that engine, remove the services built into it, and hand the browser back to the person using it. Free of charge, no account, no data collected. Nothing to sell, because nothing is collected. It is meant to show, in plain words, everything it sends, and its code is open so that anyone can check.
>
> Thanks for the engine. sgawser takes care of the rest. Created in Italy.

sgawser is an independent browser in the making: one person's project, with no company, investor or advertiser behind it, published under the personal site [sga.os](https://sgalliani.com). Android comes first. Limit: independent describes who runs the project, not what it is built on. The engine is Chromium, which the project does not control.

## Status

Nothing is released and there is no code yet.

Phase 1 is sgawser as a profile: a documented setup of Cromite for Android with a ten minute self-check, no binary. The draft is in [docs/profile/android.md](docs/profile/android.md); it is not verified until the emulator lab measurement of Cromite is done. A build of its own comes only for what a settings checklist cannot reach. Limit: the author has no machine that can build the engine today, so a build has no date.

## Principles

Every sentence below carries its limit. If one does not, open an issue.

**Free of charge.** No price, no paid tier, no in-app purchase, and no request for money in the browser or anywhere else in the project. Limits: nothing is released yet. Free describes sgawser only: the sites and services reached with it set their own prices, and other projects named in the guides (Cromite, PCAPdroid) accept donations or sell extras, of which this project receives nothing.

**The project earns no money.** It is one person's project. It is not a company, and it is not a registered non-profit organisation. No ads, no sponsored content, no search deal, no affiliate link, no donations asked or accepted. The project collects no data about the people who use the browser, so it has nothing to sell or share. Limits: sgawser stands on other people's work, and part of that work belongs to companies, named in the [dependency list](docs/dependencies.md). One of them sells an advertising programme tied to the ad blocker inside Cromite; whether Cromite has it switched off is not yet checked.

**Reasons stated, nothing collected.** Why it exists: the author measured what mainstream browsers send on their own, and wants one that sends less. The rules used to choose third-party parts are in the dependency list. Limit: the author also applies criteria of his own that are not written there for now. The design has no telemetry, no account and no install identifier, and on its own the browser is meant to contact only the sites the user opens and the services named in its settings. None of this is built or measured yet: until then the guide uses Cromite as it comes, and Cromite makes a few connections of its own, listed in the guide. One service is planned to be on by default: secure DNS, which sends the names of the sites opened to a non-profit resolver. Limits: whoever is contacted always sees the network address, websites can still set their own cookies, and the hosts of the downloads keep their own access logs.

**Open to checking.** Code, build scripts, lists, test methods and test results will be public from the first commit that contains them. Today the repository holds only documents. Not public yet: the design document, the decision log and the notes of the dependency check, which stay private until the author decides to publish them. Private by necessity: the signing key, and vulnerability reports until they are fixed. Tests that fail will be published next to the ones that pass. The project is written with the help of an AI assistant (Claude, made by the company Anthropic). The commit history shows where: commits written with the assistant carry its name. The session links in those commits are private and cannot be opened by readers. The maintainer reviews and answers for every line.

**Created in Italy.** sgawser is designed and maintained by one person in Italy. Limit: this says where the author works; it is not an origin mark. Almost all of the browser is not Italian. The engine is Chromium, an open source project led by Google, taken through Cromite, a project kept by one maintainer, because no engine that fits the project's rules can yet display enough of today's web for daily use. Code and site are hosted by companies that are not Italian (GitHub, which belongs to Microsoft, and Vercel).

**As little borrowed as possible, all of it listed.** A browser built on Chromium cannot have few dependencies: it inherits everything that Chromium and Cromite contain. The rule applies to what sgawser adds inside the browser: no third-party library and no prebuilt program. Around the browser the project writes its small tools itself; the ready-made tools it still needs for testing and publishing are in the dependency list. Security standards are never home made: cryptography, signature formats, TLS, certificate checks and the update format come from Android, from the engine or from a named existing standard. Limit: two parts of the current design (an own signed release file and an own update check) break this rule; removing them is proposed and not decided yet. The [dependency list](docs/dependencies.md) aims to name everything not written here, with who is behind it and why it is used; a missing row is a fault to report.

**The simplest secure code.** This is the aim for sgawser's own layer on top of Cromite: small enough for one person to read in a weekend. It cannot be true of the whole browser, because Chromium is tens of millions of lines.

## License

GNU General Public License, version 3 only (GPL-3.0-only), the licence Cromite uses. The full text is in [LICENSE](LICENSE). Anyone may use, read, change and share what is in this repository; a changed version that is shared must stay under the same licence, with its source. There is no warranty. Limit: the licence covers what is written in this repository. The engine and Cromite are not in it and keep their own licences.

## Security

See [SECURITY.md](SECURITY.md).
