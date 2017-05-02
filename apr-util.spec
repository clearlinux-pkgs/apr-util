#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : apr-util
Version  : 1.5.4
Release  : 14
URL      : http://www.apache.org/dist/apr/apr-util-1.5.4.tar.gz
Source0  : http://www.apache.org/dist/apr/apr-util-1.5.4.tar.gz
Summary  : Apache Portable Runtime Utility library
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: apr-util-bin
Requires: apr-util-lib
BuildRequires : apr-dev
BuildRequires : cmake
BuildRequires : expat-dev
BuildRequires : openssl-dev
BuildRequires : sqlite-autoconf-dev
BuildRequires : util-linux-dev

%description
The mission of the Apache Portable Runtime (APR) is to provide a
free library of C data structures and routines.  This library
contains additional utility interfaces for APR; including support
for XML, LDAP, database interfaces, URI parsing and more.

%package bin
Summary: bin components for the apr-util package.
Group: Binaries

%description bin
bin components for the apr-util package.


%package dev
Summary: dev components for the apr-util package.
Group: Development
Requires: apr-util-lib
Requires: apr-util-bin

%description dev
dev components for the apr-util package.


%package lib
Summary: lib components for the apr-util package.
Group: Libraries

%description lib
lib components for the apr-util package.


%prep
%setup -q -n apr-util-1.5.4

%build
%configure --disable-static --with-apr=/usr/bin/apr-1-config
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
make check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/apr-util-1/apr_dbd_sqlite3-1.so
/usr/lib64/apr-util-1/apr_dbd_sqlite3.so
/usr/lib64/aprutil.exp

%files bin
%defattr(-,root,root,-)
/usr/bin/apu-1-config

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
