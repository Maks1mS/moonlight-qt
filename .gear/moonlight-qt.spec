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

BuildRequires(pre): rpm-macros-qt6
BuildRequires: qt6-tools
BuildRequires: qt6-base-devel

%description
%summary

%prep
%setup

%build
%qmake_qt6
%make_build

%install
%makeinstall_std

%check
%make_build check

%files
%doc *.md
%_bindir/*
%_man1dir/*

%changelog
* Fri Oct 25 2024 Maxim Slipenko <no-reply@maxim.slipenko.com> 6.1.0-alt1
- Initial build for Sisyphus
