Name:           adns
%define lname	libadns
Version:        1.4
Release:        0
License:        GPL-2.0+
Summary:        Advanced Easy-to-Use Asynchronous-Capable DNS Utilities
Url:            http://www.chiark.greenend.org.uk/~ian/adns/
Group:          Productivity/Networking/DNS/Utilities
Source:         %{name}-%{version}.tar.bz2
Source1:        README.SUSE
Source2:        baselibs.conf
Patch0:         %{name}-%{version}-destdir.patch
Patch1:         %{name}-%{version}-configure.patch
Patch2:         %{name}-%{version}-ipv6.patch
Patch3:         adns-visibility.patch
Patch4:         adns-ocloexec.patch
BuildRequires:  autoconf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
adns includes a collection of useful DNS resolver utilities.

%package -n %lname
Summary:        Advanced DNS resolver client library
Group:          System/Libraries
Provides:       libadns = %{version}

%description -n %lname
Libadns is an advanced, easy to use, asynchronous-capable DNS resolver
client library for C (and C++) programs.

%package -n libadns-devel
Summary:        Libraries and header files to develop programs with libadns support
Group:          Development/Languages/C and C++
Requires:       %lname = %{version}
Requires:       glibc-devel

%description -n libadns-devel
Libadns-devel includes the header file and static library to develop
programs with libads support.

%prep
%setup -q
%patch0
%patch1
%patch2
%patch3
%patch4
cp %{SOURCE1} .

%build
autoreconf -fiv
%configure
make %{?_smp_mflags} all

%install
%make_install


%files
%defattr(-,root,root)
%doc COPYING GPL-vs-LGPL LICENCE.WAIVERS
%{_bindir}/adns*

%files -n %lname
%defattr(-,root,root)
%{_libdir}/libadns.so.1*

%files -n libadns-devel
%defattr(-,root,root)
%{_includedir}/adns.h
%{_libdir}/libadns.so

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%changelog
