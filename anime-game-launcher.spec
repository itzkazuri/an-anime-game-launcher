Name:           anime-game-launcher
Version:        3.19.7
Release:        1%{?dist}
Summary:        Anime Game launcher

License:        GPL-3.0-or-later
URL:            https://github.com/an-anime-team/an-anime-game-launcher
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Packager:       itzkazuri
# Code developed by aagl team

BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  pkg-config
BuildRequires:  glib2-devel
BuildRequires:  gtk4-devel
BuildRequires:  libadwaita-devel
BuildRequires:  openssl-devel
BuildRequires:  protobuf-compiler

%description
An Anime Game launcher is an unofficial launcher for anime games that handles setting up Wine and installing the game on Linux.
Code by aagl team, maintained by itzkazuri.

%prep
%autosetup -n an-%{name}-%{version} -p1

%build
cargo build --release

%install
rm -rf %{buildroot}
install -Dm755 target/release/anime-game-launcher %{buildroot}%{_bindir}/anime-game-launcher
install -Dm644 assets/anime-game-launcher.desktop %{buildroot}%{_datadir}/applications/moe.launcher.an-anime-game-launcher.desktop
install -Dm644 assets/moe.launcher.an-anime-game-launcher.metainfo.xml %{buildroot}%{_metainfodir}/moe.launcher.an-anime-game-launcher.metainfo.xml

%files
%{_bindir}/anime-game-launcher
%{_datadir}/applications/moe.launcher.an-anime-game-launcher.desktop
%{_metainfodir}/moe.launcher.an-anime-game-launcher.metainfo.xml

%changelog
* Sun Sep 06 2026 itzkazuri <itzkazuri@local> - 3.19.7-1
- Maintainer: itzkazuri
- Code by aagl team
- RPM spec created for Fedora
