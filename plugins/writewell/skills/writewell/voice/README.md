# Personal Voice

This folder used to hold the generated profile (`SKILL.md`).

New profiles are written outside the plugin, so a plugin update cannot wipe them and a local install cannot ship them. The destination is `WRITEWELL_VOICE_PATH` when that variable is set, otherwise `~/.config/writewell/voice.md` (`$XDG_CONFIG_HOME/writewell/voice.md` when `XDG_CONFIG_HOME` is set). The file is not named `SKILL.md`.

writewell still checks this directory for an old `SKILL.md`. If it finds one, it tells the user and offers to copy it to the new location. `.gitignore` still ignores that file.

This folder, this README, and `.gitkeep` are no longer required for a new profile. They are still here so an existing checkout keeps the old path. They can be removed once that is approved.

Generate a profile with the [onboard skill](../../onboard/SKILL.md).
