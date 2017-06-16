%global debug_package %{nil}

Name: apm_planner
Version: 2.0.25
Release: 4%{?dist}.rc1
Summary: ArduPilot and PX4 compatible ground station application
License: GPLv3+
URL: https://github.com/ArduPilot/apm_planner
Source0: %{name}-%{version}.tar.gz

BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtscript-devel
BuildRequires: qt5-qtwebkit-devel
BuildRequires: qt5-qtserialport-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: pyserial
BuildRequires: python-pexpect
BuildRequires: SDL-devel
BuildRequires: libsndfile-devel
BuildRequires: openssl-devel
BuildRequires: libudev-devel
BuildRequires: SDL2-devel
BuildRequires: gcc-c++

Requires: pyserial
Requires: python-pexpect

%description
APM Planner is an open-source ground station application for MAVlink based
autopilots including ArduPilot and PX4/Pixhawk.

%prep
%autosetup
qmake-qt5 apm_planner.pro PREFIX=%{_prefix}

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"


%install
make install INSTALL_ROOT=$RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc README.md license.txt

%{_bindir}/apmplanner2
%attr(0755, root, root) %{_bindir}/sik_uploader.py
%{_datadir}/APMPlanner2
%{_datadir}/sik_uploader
%{_datadir}/applications/apm_planner.desktop

%changelog
* Fri Jun 16 2017 Lars Kellogg-Stedman <lars@oddbit.com> 2.0.25-3
- initial packaging for copr
