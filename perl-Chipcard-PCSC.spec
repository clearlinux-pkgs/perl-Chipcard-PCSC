#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v3
# autospec commit: c1050fe
#
Name     : perl-Chipcard-PCSC
Version  : 1.4.16
Release  : 9
URL      : https://cpan.metacpan.org/authors/id/W/WH/WHOM/Chipcard-PCSC-v1.4.16.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/W/WH/WHOM/Chipcard-PCSC-v1.4.16.tar.gz
Summary  : 'Communicate with a smart card using PC/SC from a Perl script'
Group    : Development/Tools
License  : GPL-2.0
Requires: perl-Chipcard-PCSC-license = %{version}-%{release}
Requires: perl-Chipcard-PCSC-perl = %{version}-%{release}
Requires: pcsc-lite-lib
BuildRequires : buildreq-cpan
BuildRequires : perl(Getopt::Long)
BuildRequires : pkgconfig(libpcsclite)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Perl interface to the PC/SC smart card library
==============================================

%package dev
Summary: dev components for the perl-Chipcard-PCSC package.
Group: Development
Provides: perl-Chipcard-PCSC-devel = %{version}-%{release}
Requires: perl-Chipcard-PCSC = %{version}-%{release}

%description dev
dev components for the perl-Chipcard-PCSC package.


%package license
Summary: license components for the perl-Chipcard-PCSC package.
Group: Default

%description license
license components for the perl-Chipcard-PCSC package.


%package perl
Summary: perl components for the perl-Chipcard-PCSC package.
Group: Default
Requires: perl-Chipcard-PCSC = %{version}-%{release}

%description perl
perl components for the perl-Chipcard-PCSC package.


%prep
%setup -q -n Chipcard-PCSC-v1.4.16
cd %{_builddir}/Chipcard-PCSC-v1.4.16

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Chipcard-PCSC
cp %{_builddir}/Chipcard-PCSC-v%{version}/LICENCE %{buildroot}/usr/share/package-licenses/perl-Chipcard-PCSC/4cc77b90af91e615a64ae04893fdffa7939db84c || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Chipcard::PCSC.3
/usr/share/man/man3/Chipcard::PCSC::Card.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Chipcard-PCSC/4cc77b90af91e615a64ae04893fdffa7939db84c

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
