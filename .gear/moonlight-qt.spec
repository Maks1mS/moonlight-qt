Name:    moonlight-qt
Version: 6.1.0
Release: alt1

Summary: GameStream client for PCs (Windows, Mac, Linux, and Steam Link)
License: GPL-3.0
Group:   Other
Url:     https://moonlight-stream.org/

Packager: Maxim Slipenko <no-reply@maxim.slipenko.com>

# Source-url: https://github.com/moonlight-stream/%name/releases/download/v%version/MoonlightSrc-%version.tar.gz
Source: %name-%version.tar
Source1: com.moonlight_stream.Moonlight.mobile.desktop

Patch0: 001-Support-Phosh.patch

BuildRequires(pre): rpm-macros-qt6
BuildRequires: qt6-tools
BuildRequires: qt6-base-devel
BuildRequires: libSDL2_ttf-devel
BuildRequires: libopus-devel
BuildRequires: qt6-declarative-devel
BuildRequires: qt6-svg-devel
BuildRequires: ffmpeg
BuildRequires: libEGL-devel
BuildRequires: libva-devel
BuildRequires: libvdpau-devel
BuildRequires: libswscale-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libavcodec-devel

Requires: libqt6-qmlworkerscript
Requires: libqt6-quickcontrols2material
Requires: libqt6-quickcontrols2basic
Requires: libqt6-quicklayouts

%description
%summary

%prep
%setup

%patch0 -p1

%build
%qmake_qt6 moonlight-qt.pro PREFIX=%prefix
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot

install -Dpm0644 %SOURCE1 %buildroot%_desktopdir/com.moonlight_stream.Moonlight.mobile.desktop

%files
%doc *.md
%_bindir/*
%_desktopdir/*
%_iconsdir/*
%_datadir/metainfo/*

%changelog
* Fri Oct 25 2024 Maxim Slipenko <no-reply@maxim.slipenko.com> 6.1.0-alt1
- Initial build for Sisyphus
