Summary: Mycroft's TTS engine, based on CMU's Flite (Festival Lite)
Name: mimic
Version: 1.2.0.2
Release: 1%{?dist}
License: BSD-like
Group: Applications/Multimedia
URL: https://github.com/MycroftAI/mimic

Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++ python libtool
BuildRequires: pkgconfig(icu-uc)
BuildRequires: pkgconfig(libpcre)
%define _unpackaged_files_terminate_build 0

%description
Mimic is a fast, lightweight Text-to-speech engine
developed by Mycroft A.I. and VocaliD, based on Carnegie Mellon
University Flite (Festival-Lite) software. Mimic takes in text and
reads it out loud to create a high quality voice.

Type: console-application
Categories:
  - Utility
  - Audio
  - Accessibility

%package devel
Summary: Mimic development headers and static library
Group: Development/Libraries

%description devel
Mimic TTS engine development headers and static
library

Categories:
- Library
- Audio
- Accessibility

%package tools
Summary: mimic tools
Group: Applications/Multimedia

%description tools
Mimic TTS engine tools

Type: console-application
Categories:
- Utility
- Audio
- Accessibility

%prep
%setup -q -n %{name}-%{version}/mimic

%build
%{__make} clean || true

./autogen.sh
%configure --with-audio=none

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%pre

%post

%files
%defattr(-, root, root, 0755)
%{_bindir}/mimic

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/ttsmimic
%{_libdir}/libttsmimic*
%{_libdir}/pkgconfig/mimic.pc

%files tools
%defattr(-, root, root, 0755)
%{_bindir}/compile_regexes
%{_bindir}/mimic_time
%{_bindir}/mimicvox_info
%{_bindir}/t2p

%changelog
* Wed Aug 10 2017 rinigus <rinigus.git@gmail.com> - 1.2.0.2-1
- packaging for SFOS
