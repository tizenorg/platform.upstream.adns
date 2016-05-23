Name:           adns
%define lname   libadns
Version:        1.4
Release:        0
License:        GPL-2.0+
Summary:        Advanced Easy-to-Use Asynchronous-Capable DNS Utilities
Url:            http://www.chiark.greenend.org.uk/~ian/adns/
Group:          System/Utilities
Source:         %{name}-%{version}.tar.bz2
Source2:        baselibs.conf
Source1001:     adns.manifest
BuildRequires:  autoconf

%description
adns includes a collection of useful DNS resolver utilities.

%package -n %lname
Summary:        Advanced DNS resolver client library
Group:          System/Libraries

%description -n %lname
Libadns is an advanced, easy to use, asynchronous-capable DNS resolver
client library for C (and C++) programs.

%package -n libadns-devel
Summary:        Libraries and header files to develop programs with libadns support
Group:          System/Libraries
Requires:       %lname = %{version}
Requires:       glibc-devel

%description -n libadns-devel
Libadns-devel includes the header file and static library to develop
programs with libads support.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%restore_fcommon

%reconfigure
%__make %{?_smp_mflags} all

%install
%make_install

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%license COPYING GPL-vs-LGPL LICENCE.WAIVERS
%{_bindir}/adns*

%files -n %lname
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/libadns.so.1*

%files -n libadns-devel
%manifest %{name}.manifest
%defattr(-,root,root)
%{_includedir}/adns.h
%{_libdir}/libadns.so
