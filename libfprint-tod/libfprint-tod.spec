Name:           libfprint-tod

Version:        1.94.6+tod1
Release:        1
Summary:        Toolkit for fingerprint scanner (TOD version)

License:        LGPLv2+
URL:            http://www.freedesktop.org/wiki/Software/fprint/libfprint
Source0:        https://gitlab.freedesktop.org/3v1n0/libfprint/-/archive/v%{version}/libfprint-v%{version}.tar.gz
ExcludeArch:    s390 s390x

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildRequires:  pkgconfig(gio-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gusb) >= 0.3.0
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  gtk-doc
# For the udev.pc to install the rules
BuildRequires:  systemd
BuildRequires:  gobject-introspection-devel
# For internal CI tests; umockdev 0.13.2 has an important locking fix
BuildRequires:  python3-cairo python3-gobject cairo-devel
BuildRequires:  umockdev >= 0.13.2
BuildRequires:  libgudev-devel

%description
libfprint-tod offers support for consumer fingerprint reader devices.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -S git -n libfprint-v%{version}

%build
# Include the virtual image driver for integration tests
%meson -Dintrospection=false
%meson_build

%install
%meson_install
mkdir -vp %{buildroot}/usr/lib64/libfprint-2/tod-1

%ldconfig_scriptlets

%files
%license COPYING
%doc NEWS THANKS AUTHORS
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/*.typelib
/usr/lib/udev/hwdb.d/60-autosuspend-libfprint-2.hwdb
%dir /usr/lib64/libfprint-2/tod-1
%{_udevrulesdir}/70-libfprint-2.rules

%files devel
%doc HACKING.md
%{_includedir}/*
%{_libdir}/*.so
%{_datadir}/gir-1.0/*.gir
%{_datadir}/gtk-doc/html/libfprint-2/
%{_libdir}/pkgconfig/libfprint-2-tod-1.pc
%{_libdir}/pkgconfig/libfprint-2.pc


%changelog
* Mon Sep 04 2023 Piotr Rogowski <piotr.rogowski@creativestyle.pl> - 1.94.6+tod1-1
- new version

* Sat Nov 5 2022 Piotr Rogowski <piotr.rogowski@creativestyle.pl> - 1.94.5+tod1-1
- new version

* Mon Dec 20 2021 Piotr Rogowski <piotr.rogowski@creativestyle.pl> - 1.94.2+tod1-1
- new version

* Mon Dec 20 2021 Piotr Rogowski <piotr.rogowski@creativestyle.pl> - 1.94.1+tod1-1
- new version

* Tue Mar 30 2021 Kevin Anderson <andersonkw2@gmail.com> - 1.90.7+git20210222+tod1-2
- Add directory for tod drivers

* Tue Mar 30 2021 Kevin Anderson <andersonkw2@gmail.com> - 1.90.7+git20210222+tod1
- Initial Release
