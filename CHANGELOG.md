# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [0.1.1] - 2023-11-20
### Added
- Copy Waveshare V4 files to the ui/hw/libs/waveshare v4 directory from the waveshare e-Paper repo 
    - git clone https://github.com/waveshare/e-Paper.git
- Copy/Paste ui/hw waveshare3.py from pwnagotchi to waveshare4.py and change all the V3 to V4 and pwnagotchi to stenogotchi. Copy over the stenogotchi positions from V2.
- is_waveshare_v4 in ui.display.py
- waveshare4 in utils.py
- is_waveshare_v4 in memtemp.py
### Changed
- ui/hw/__init__.py change to waveshare4.
- defaults.toml waveshare_2 to waveshare_4
### Fixed

## [Unreleased]
### Added
### Changed
### Fixed
### Removed

## [0.1.0] - 2022-01-02
### Added
- Modifier, function and navigation-key support, both individually and in combination (unsupported inputs logged in plover.log).
- Reactions to new records in WPM-tracking mode.
- Plover dictionary lookup with eINK display and STENO input support. The plugin (dict_lookup) utilizes native Plover lookup functionality for full compatibility with supported dictionary formats.
- Buttonshim actions, both built-in and custom, accessible through web UI.
- Hardware build guide.

### Changed
- Plover v4.0.0.dev10 or higher required.
- Stenogotchi_link v0.3.0 required. Plugin now logs to plover.log.
- Character and personality adjustments.
- Simplified installation process.
- Added documentation for aligning text output with target device expected input language and layout.
- Web UI default port changed from 8080 to 80.
- Bluetooth connection established only once Plover has started.

### Fixed
- Significantly reduced input latency in STENO mode.
- Improved Bluetooth pairing and connection management.
- Web UI now starts only once a wifi connection has been established.

## [Unreleased]
### Added
### Changed
### Fixed
### Removed

## [0.0.5] - 2021-03-24
### Added
- DS3231 real time clock module wiring and positioning reference picture to README.
- Four new faces, producing processing animation when combined.
- WPM stats now track and display top result for session.

### Changed
- Led plugin and default patterns to better indicate noteworthy events.

### Fixed
- QWERTY-mode breaking bug introduced in v0.0.4.
- Letter capitalization, symbol characters and return key in STENO-mode.

## [0.0.4] - 2021-03-21
### Added
- This CHANGELOG file.
- User configurable bluetooth device name using main.plugins.plover_link.bt_device_name.
- User configurable list of bluetooth mac addresses, in order of priority, to auto-connect to using main.plugins.plover_link.bt_autoconnect_mac.
- User configurable option to clear eINK display at shutdown using ui.display.clear_at_shutdown.
- User configurable wpm calculation method using main.plugins.plover_link.wpm_method.
- User configurable wpm update frequency and calculation window in seconds using main.plugins.plover_link.wpm_timeout.
- More variety in mood indicators on common events.
- Requirements file.

### Changed
- Improved installation guide and documentation in README.
- All functionality in buttonshim plugin reworked into class for better integration with the project.
- More consistent logging messages.
- Stenogotchi_link version upgrade to v0.0.4.

### Fixed
- Reboot after initial setup or hostname change not working.
- Wifi status not showing as [OFF] if wifi is disabled at boot.
- Mode not changing to STENO when Plover becomes operational.
- All button press events not producing logging messages.
- Dependencies for stenogotchi_link Plover plugin corrected in setup.cfg.

## [0.0.3] - 2021-03-18
### Added
- First public pre-release version on GitHub.
- Stenogotchi, portable stenography using Plover and bluetooth keyboard emulation on a Raspberry Pi Zero W. With support for Waveshare 2.13 v2, ButtonSHIM and UPS-Lite v1.2 modules.
- Plover plugin stenogotchi_link for communicating between Plover and Stenogotchi.
- README now includes tested installation guide no longer requiring building PyQt5 from source.
- README now includes basic configuration and usage documentation.
- LICENSE file.

[Unreleased]: https://github.com/prgskidmark/stenogotchi/compare/v0.1.1...dev
[Unreleased]: https://github.com/Anodynous/stenogotchi/compare/v0.1.0...dev
[0.1.0]: https://github.com/Anodynous/stenogotchi/compare/v0.0.5...v0.1.0
[0.0.5]: https://github.com/Anodynous/stenogotchi/compare/v0.0.4...v0.0.5
[0.0.4]: https://github.com/Anodynous/stenogotchi/compare/v0.0.3...v0.0.4
[0.0.3]: https://github.com/Anodynous/stenogotchi/releases/tag/v0.0.3