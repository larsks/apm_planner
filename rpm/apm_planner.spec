%global debug_package %{nil}

Name: apm_planner
Version: 2.0.25
Release: 3%{?dist}
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
BuildRequires: flite-devel
BuildRequires: openssl-devel
BuildRequires: libudev-devel
BuildRequires: SDL2-devel
BuildRequires: gcc-c++

Requires: pyserial
Requires: python-pexpect
Requires: flite

%description
APM Planner is an open-source ground station application for MAVlink based
autopilots including ArduPilot and PX4/Pixhawk.

%prep
%autosetup

sed -i '/FLITE_AUDIO_ENABLED/ d' apm_planner.pro

%build
mkdir -p $RPM_BUILD_ROOT/etc

qmake-qt5 apm_planner.pro
make %{?_smp_mflags} CFLAGS="%{optflags}"


%install
env > $RPM_BUILD_ROOT/etc/buildenv-%{name}
make install INSTALL_ROOT=$RPM_BUILD_ROOT/usr

mkdir -p $RPM_BUILD_ROOT%{_datadir}
mv $RPM_BUILD_ROOT/usr/bin/sik_uploader \
	$RPM_BUILD_ROOT%{_datadir}/sik_uploader

mv $RPM_BUILD_ROOT%{_datadir}/sik_uploader/sik_uploader.py \
	$RPM_BUILD_ROOT/usr/bin/sik_uploader

%files
%defattr(-, root, root)
%doc README.md license.txt

/etc/buildenv-%{name}
%{_bindir}/apmplanner2
%attr(0755, root, root) %{_bindir}/sik_uploader
%{_datadir}/APMPlanner2
%{_datadir}/sik_uploader
%{_datadir}/applications/apmplanner2.desktop
%{_datadir}/menu/apmplanner2

%changelog
* Fri Jun 16 2017 Lars Kellogg-Stedman <lars@redhat.com> 2.0.25-3
- new package built with tito

* Thu Feb 04 2016 Lars Kellogg-Stedman <lars@redhat.com> - 0.21
- updated to 0.21-1fcbf09
