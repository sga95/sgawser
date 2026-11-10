# sgawser

sgawser is a browser in the making: one person's project, published under the personal site [sga.os](https://sgalliani.com). Android comes first.

## Status

Nothing is released and there is no code yet.

Phase 1 is sgawser as a profile: a documented setup of Cromite for Android with a ten minute self-check, no binary. The draft is in [docs/profile/android.md](docs/profile/android.md); it is not verified until the emulator lab measurement of Cromite is done. A build of its own comes only for what a settings checklist cannot reach.

## Principles

Every sentence below carries its limit. If one does not, open an issue.

**Free of charge.** No price, no paid tier, no in-app purchase, and no request for money in the browser or anywhere else in the project. Limits: nothing is released yet. Free describes sgawser only: the sites and services reached with it set their own prices, and other projects named in the guides (Cromite, PCAPdroid) accept donations or sell extras, of which this project receives nothing.

**Nobody earns money from it.** It is one person's project. It is not a company, and it is not a registered non-profit organisation. No ads, no sponsored content, no search deal, no affiliate link, no donations asked or accepted. The project collects no data about the people who use the browser, so it has nothing to sell or share. Limit: sgawser stands on other people's work, and part of that work belongs to companies. They are named in the [dependency list](docs/dependencies.md).

**Reasons stated, nothing collected.** Why it exists: the author measured what mainstream browsers send on their own, and wants one that sends less. The rules used to choose every third-party part are published in the dependency list. No telemetry, no account, no install identifier created or sent by the browser. Design goal, not yet built or measured: on its own, the browser contacts only the sites the user opens and the services named in its settings. One of those is planned to be on by default: secure DNS, which sends the names of the sites opened to a non-profit resolver. Limits: whoever is contacted always sees the network address, websites can still set their own cookies, and the hosts of the downloads keep their own access logs.

**Open to checking.** Code, build scripts, lists, test methods and test results are public from the first commit that contains them. Two things stay private by necessity: the signing key, and vulnerability reports until they are fixed. Tests that fail are published next to the ones that pass. The project is written with the help of an AI assistant (Claude, made by Anthropic, a United States company): the commit history shows where, and the maintainer reviews and answers for every line.

**Created in Italy.** sgawser is designed and maintained by one person in Italy. Limit: this says where the author works; it is not an origin mark. Almost all of the browser is not Italian. The engine is Chromium, an open source project led by Google, taken through the community project Cromite, because no engine that fits the project's rules can yet display enough of today's web for daily use. Code and site are hosted in the United States.

**As little borrowed as possible, all of it listed.** A browser built on Chromium cannot have few dependencies: it inherits everything that Chromium and Cromite contain. The rule applies to what sgawser adds: no third-party library, no prebuilt program, and where a small tool is needed the project writes it. Security standards are never home made: cryptography, signature formats, TLS, certificate checks and the update format come from the platform. Everything not written here is named in the [dependency list](docs/dependencies.md), with who is behind it and why it is used.

**The simplest secure code.** This is the aim for sgawser's own layer on top of Cromite: small enough for one person to read in a weekend. It cannot be true of the whole browser, because Chromium is tens of millions of lines.

## License

Not chosen yet. It will be an open source licence compatible with Cromite's GPL version 3. Until it is chosen, nobody has the legal right to reuse what is in this repository.

## Security

See [SECURITY.md](SECURITY.md).
