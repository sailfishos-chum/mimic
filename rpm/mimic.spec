Summary: Mycroft's TTS engine, based on CMU's Flite (Festival Lite)
Name: mimic
Version: 1.2.0.2
Release: 1%{?dist}
License: BSD-like
Group: System/TTS
URL: https://github.com/MycroftAI/mimic

Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++ python libtool
%define _unpackaged_files_terminate_build 0

%description
Mycroft's TTS engine, based on CMU's Flite (Festival Lite)

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

%changelog
* Wed Aug 10 2017 rinigus <rinigus.git@gmail.com> - 1.2.0.2-1
- packaging for SFOS
