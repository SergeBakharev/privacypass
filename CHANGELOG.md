# Change Log
Notable changes to this project will be documented in this file.

## [Unreleased]
### Added
### Changed
### Deprecated
### Removed
### Fixed
### Security

## [0.2.2]
### Security
- Updated cryptography library to 42.0.4

## [0.2.1]
### Fixed
- redemption_header() returns token with value

## [0.2.0]
### Added
- privacypass: redemption_header()
### Changed
- README example to use redemption_header instead of redemption_token
### Fixed
- Docstring for redemption_token
- Cleaned up double module import
## [0.1.0]
Bare minimum of [Privacy Pass protocol](https://privacypass.github.io/) to redeem tokens.
### Added
- voprf: derive_key() - Derives the shared key used for redemption MACs
- voprf: create_request_binding()
- privacypass: redemption_token()
- docs: Initial README
- docs: Firefox Token extraction steps in README
- docs: Usage example

[Unreleased]: https://github.com/sergebakharev/privacypass/compare/v0.2.2...HEAD
[0.2.2]: https://github.com/sergebakharev/privacypass/releases/tag/v0.2.2
[0.2.1]: https://github.com/sergebakharev/privacypass/releases/tag/v0.2.1
[0.2.0]: https://github.com/sergebakharev/privacypass/releases/tag/v0.2.0
[0.1.0]: https://github.com/sergebakharev/privacypass/releases/tag/v0.1.0
